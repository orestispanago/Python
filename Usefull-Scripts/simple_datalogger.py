import datetime
import time

import numpy as np
import schedule

# pip install schedule

measurements = []


def measure():
    measurement = np.random.random_sample()
    measurements.append(measurement)
    time.sleep(1)


def log(fname):
    time_stamp = datetime.datetime.now(datetime.timezone.utc)
    count = len(measurements)
    mean = np.mean(measurements)
    stdev = np.std(measurements)
    measurements.clear()
    with open(fname, 'a') as f:
        f.write(f"{time_stamp}, {count}, {mean}, {stdev}\n")


def create_file(fname):
    with open(fname, 'w') as f:
        f.write(f"time, count, mean, stdev\n")


file_name = "logs.csv"
create_file(file_name)

schedule.every().minute.at(":00").do(log, file_name)
schedule.every(3).seconds.do(measure)
while True:
    schedule.run_pending()
    time.sleep(0.2)  # Added to avoid CPU overheating
