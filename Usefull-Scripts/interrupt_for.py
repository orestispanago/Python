#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:55:47 2018

@author: orestis
"""

import time
try:
    for i in range(0,10):
        print('hey %d'%i)
        time.sleep(2)
except KeyboardInterrupt:
    print('Interrupted')
print('Done')
