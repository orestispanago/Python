import time

def check_timezone_utc():
    print(f"System timezone: {time.tzname}")
    if ("Coordinated Universal Time" in time.tzname) or ("UTC" in time.tzname):
        print(f"System timezone: {time.tzname} OK")
    else:
        raise ValueError("System timezone not UTC")
