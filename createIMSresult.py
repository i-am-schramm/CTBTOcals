#!/bin/env python
''' this will cal the calib calculation and then write it to an output file'''

from obspy import UTCDateTime
from calcNewCalib import calcNewCalib

debug=False
# all of this should become command line input.
station='SFJD'
network='IU'
location='10'
channel='BHZ'
calper=1.0
date=UTCDateTime("2018,01,18,00,33,00")
date2=UTCDateTime("2015,01,29,05,20,00")

calib = calcNewCalib(station,network,channel,location,calper,date,date2)

print(calib)
