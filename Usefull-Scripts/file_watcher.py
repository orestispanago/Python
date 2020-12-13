#!/usr/bin/python

import os
from time import sleep


filename = "test.txt"
timestamp = os.stat(filename).st_mtime


try:
   while True:
        stamp = os.stat(filename).st_mtime
        if stamp != timestamp:
            timestamp = stamp
            print("file changed!")
        else:
            print("not changed")
        sleep(10)
except KeyboardInterrupt:
   print('\nExiting nicely...')
