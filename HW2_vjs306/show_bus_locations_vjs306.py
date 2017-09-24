from __future__ import division, print_function
__author__ = 'vjs306'

import os
import numpy as np
import pylab as pl
import json
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Please enter 3 arguments")
    sys.exit()

mta_key = sys.argv[1]
bus_line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + mta_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


print ("Bus Line : " + bus_line)
busdata = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
#type(busdata)

numbus = str(len(busdata))

print ("Number of Active Buses : " + numbus)

buscount = 0
for i in busdata:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

    print ("Bus " + str(buscount) + " is at latitude " + str(latitude) + " and longitude " + str(longitude))
    buscount += 1
