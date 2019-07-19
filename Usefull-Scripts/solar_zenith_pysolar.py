from pysolar import solar
import datetime


lat = 38.291969
lon = 21.788156

date = datetime.datetime(2019, 7, 19, 20, 40, 25, 0, tzinfo=datetime.timezone.utc)

print(solar.get_altitude(38.291969,21.788156, date))
