import astropy.coordinates as coord
from astropy.time import Time
import datetime

loc = coord.EarthLocation.from_geodetic(21,38,24.78)

now = Time.now()

then = datetime.datetime(2016, 1, 1, 0, 0)
th = Time(then, format = 'datetime', scale = 'utc')


def sun_angles(utime):
    print(utime)
    altaz = coord.AltAz(location=loc, obstime=utime)
    sun = coord.get_sun(utime)
#    altitude = sun.transform_to(altaz).alt.degrees
    azimuth = sun.transform_to(altaz).az.degree
    zenith = sun.transform_to(altaz).zen.degree
    return [zenith, azimuth]


zenaz_now = sun_angles(now)
zenaz_th = sun_angles(th)

