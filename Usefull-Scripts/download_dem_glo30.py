"""
Downloads Copernicus DEM GLO-30 tiles covering the KSA AOI from the
Copernicus Data Space Ecosystem (CDSE) S3-compatible object store.

Credentials: create an S3 access key/secret in the CDSE dashboard
(https://dataspace.copernicus.eu -> account -> S3 credentials), then set:
    export CDSE_S3_ACCESS_KEY=...
    export CDSE_S3_SECRET_KEY=...

Usage:
    python download_dem_glo30.py discover              # list top-level bucket folders
    python download_dem_glo30.py discover --prefix X    # list folders under X
    python download_dem_glo30.py download --prefix X    # download AOI tiles under X
"""

import argparse
import os
import re

import boto3
from botocore.config import Config

ENDPOINT_URL = "https://eodata.dataspace.copernicus.eu"
BUCKET = "eodata"

# Saudi Arabia bounds (from data/raw/shapefiles/KSA, total_bounds), +1 deg margin
AOI_LON_MIN = 33
AOI_LON_MAX = 57
AOI_LAT_MIN = 15
AOI_LAT_MAX = 33

OUTPUT_DIR = "../data/raw/Digital-elevation-model-30m"

TILE_NAME_RE = re.compile(
    r"Copernicus_DSM_COG_10_([NS])(\d{2})_00_([EW])(\d{3})_00_DEM"
)


def make_client():
    access_key = os.environ["CDSE_S3_ACCESS_KEY"]
    secret_key = os.environ["CDSE_S3_SECRET_KEY"]
    client = boto3.client(
        "s3",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
    )
    return client


def list_common_prefixes(client, prefix):
    paginator = client.get_paginator("list_objects_v2")
    prefixes = []
    for page in paginator.paginate(Bucket=BUCKET, Prefix=prefix, Delimiter="/"):
        for entry in page.get("CommonPrefixes", []):
            prefixes.append(entry["Prefix"])
    return prefixes


def list_all_keys(client, prefix):
    paginator = client.get_paginator("list_objects_v2")
    keys = []
    for page in paginator.paginate(Bucket=BUCKET, Prefix=prefix):
        for obj in page.get("Contents", []):
            keys.append(obj["Key"])
    return keys


def parse_tile_lat_lon(key):
    match = TILE_NAME_RE.search(key)
    if match is None:
        return None
    ns, lat_str, ew, lon_str = match.groups()
    lat = int(lat_str)
    if ns == "S":
        lat = -lat
    lon = int(lon_str)
    if ew == "W":
        lon = -lon
    return lat, lon


def tile_in_aoi(lat, lon):
    in_lat = AOI_LAT_MIN <= lat < AOI_LAT_MAX
    in_lon = AOI_LON_MIN <= lon < AOI_LON_MAX
    return in_lat and in_lon


def find_aoi_tile_folders(client, prefix):
    aoi_folders = []
    for folder_prefix in list_common_prefixes(client, prefix):
        parsed = parse_tile_lat_lon(folder_prefix)
        if parsed is None:
            continue
        lat, lon = parsed
        if tile_in_aoi(lat, lon):
            aoi_folders.append(folder_prefix)
    return aoi_folders


def find_tif_keys_in_folder(client, folder_prefix):
    tif_keys = []
    for key in list_all_keys(client, folder_prefix):
        if key.lower().endswith(".tif"):
            tif_keys.append(key)
    return tif_keys


def find_aoi_tif_keys(client, prefix):
    aoi_folders = find_aoi_tile_folders(client, prefix)
    print(
        f"{len(aoi_folders)} tile folders intersect the AOI (lon {AOI_LON_MIN}-{AOI_LON_MAX}, "
        f"lat {AOI_LAT_MIN}-{AOI_LAT_MAX})"
    )
    aoi_keys = []
    for folder_prefix in aoi_folders:
        tif_keys = find_tif_keys_in_folder(client, folder_prefix)
        if not tif_keys:
            print(f"Warning: no .tif found under {folder_prefix}")
        if len(tif_keys) > 1:
            print(
                f"Warning: {len(tif_keys)} .tif files under {folder_prefix}, downloading all"
            )
        aoi_keys.extend(tif_keys)
    return aoi_keys


def download_keys(client, keys, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for key in keys:
        local_path = os.path.join(output_dir, os.path.basename(key))
        if os.path.exists(local_path):
            print(f"Skipping {local_path} (already downloaded)")
            continue
        print(f"Downloading {key} -> {local_path}")
        client.download_file(BUCKET, key, local_path)


def run_discover(client, prefix):
    prefixes = list_common_prefixes(client, prefix)
    if not prefixes:
        print(f"No folders found under prefix '{prefix}'")
        return
    print(f"Folders under '{prefix}':")
    for found_prefix in prefixes:
        print(f"  {found_prefix}")


def run_download(client, prefix):
    aoi_keys = find_aoi_tif_keys(client, prefix)
    print(f"{len(aoi_keys)} DEM files to download")
    download_keys(client, aoi_keys, OUTPUT_DIR)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["discover", "download"])
    parser.add_argument(
        "--prefix", default="", help="S3 key prefix to list/search under"
    )
    args = parser.parse_args()

    client = make_client()
    if args.command == "discover":
        run_discover(client, args.prefix)
    elif args.command == "download":
        run_download(client, args.prefix)


if __name__ == "__main__":
    main()
