import io
import urllib.request
from ftplib import FTP

IP = ""
USER = ""
PASSWORD = ""

IP_FILE = "dataloggers/IP-addresses/test.txt"


def get_external_ip():
    external_ip = (
        urllib.request.urlopen("https://ifconfig.me/ip").read().decode("utf-8")
    )
    print(f"External IP: {external_ip}")
    return external_ip


def str_to_bytes_io(text):
    bio = io.BytesIO()
    bio.write(text.encode())
    bio.seek(0)  # move to beginning of file
    return bio


def upload_file_from_memory(remote_fname, bytes_io_object):
    with FTP(IP, USER, PASSWORD) as ftp:
        ftp.storbinary(f"STOR {remote_fname}", bytes_io_object)
    print(f"Created file {remote_fname} at FTP")


def upload_ip_file():
    external_ip = get_external_ip()
    ip_bytes_io = str_to_bytes_io(external_ip)
    upload_file_from_memory(IP_FILE, ip_bytes_io)


upload_ip_file()