import geopy.distance 

lapup_coords = (38.291969, 21.788156) # lapup
coords_2 = (38.289458000000010, 21.783286800000003)

dist = geopy.distance.geodesic(lapup_coords, coords_2).m
