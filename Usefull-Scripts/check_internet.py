# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:41:20 2018

@author: orestispanago
"""
import requests
import time

def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

while connected_to_internet() != True:
    time.sleep(10)
else:
    print('Connected')
print('Done checking...exiting')
