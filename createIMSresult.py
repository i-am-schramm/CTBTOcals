#!/bin/env python
''' this will cal the calib calculation and then write it to an output file'''
########################################################################
# script to create the calibrate result in IMS 2.0 for CTBTO stations
#
#inputs needed:
#   station,network,location,channel
#   calper - the period at which to calculate the sine wave amplitude
#   date   - date and start time of the sine wave calibration at the 
#            period of interest
#   date2  - date and start time of a sine wave calibration from a 
#            previously verified calibration.  
# 
#outputs: 
#   calib value, and calibrate result in IMS 2.0 format. the result
#   should be sent to the calibration@CTBTO.org with the subject 
#   CALIBRATE_RESULT_$station, where $station is the station of interest
########################################################################
from obspy import UTCDateTime
from calcNewCalib import calcNewCalib
from formatIMSemail import formatIMSemail

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

formatIMSemail(station,date,calib,calper)

