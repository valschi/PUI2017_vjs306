
# coding: utf-8

# In[32]:

from __future__ import division, print_function
__author__ = 'vjs306'

import os
import numpy as np
import pylab as pl
import json
import sys
import pandas as pd

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Please enter 4 arguments")
    sys.exit()

mta_key = sys.argv[1]
bus_line = sys.argv[2]
bus_line_csv = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + mta_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busdata = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

datalist = []

for i in busdata:
    dict = {}
    dict['Longitude'] = str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    dict['Latitude'] = str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    try:
        dict['Stop Name'] = str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
    except BaseException:
        dict['Stop Name'] = 'NA'
    try:
        dict['Stop Status'] = str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    except BaseException:
        dict['Stop Status'] = 'NA'
    datalist.append(dict)

df = pd.DataFrame(datalist)

df.to_csv(str(bus_line_csv))
