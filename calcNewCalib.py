#!/bin/env python

''' this file will get the amplitude at the given frequency for a given station '''

import os
from obspy import UTCDateTime
from getStageGain import getStageGain
from calcSinAmp import calcSinAmp

station='SFJD'
network='IU'
location='10'
channel='BHZ'
calfreq=1

# get the current resp stage gains
date=UTCDateTime("2018,01,18,00,33,00")
stage=1
stage1 = getStageGain(station,network,location,channel,date,stage,calfreq)
stage=2
stage2 = getStageGain(station,network,location,channel,date,stage,calfreq)
stage=3
stage3 = getStageGain(station,network,location,channel,date,stage,calfreq)

print(stage1)
print(stage2)
print(stage3)

# now get the amps from the sine calibrations
# first the current year:
fileName = ('/msd/'+network+'_'+station+'/'+str(date.year)+'/'+
              str(date.julday).zfill(3)+'/'+location+'_'+channel+'.512.seed')
currentAmpOut = calcSinAmp(fileName,date)
print(currentAmpOut)
try:
# since we have 2 different naming conventions, try the new way
   fileName = ('/msd/'+network+'_'+station+'/'+str(date.year)+'/'+
              str(date.julday).zfill(3)+'/BC1.512.seed')
   calAmpOut = calcSinAmp(fileName,date)
  
except:
# if it doesn't work, try the old way.
   fileName = ('/msd/'+network+'_'+station+'/'+str(date.year)+'/'+
              str(date.julday).zfill(3)+'/_BC1.512.seed')
   calAmpOut = calcSinAmp(fileName,date)
# naming convention from Ringler paper ... add a ref in comments so that people can look it up
Ft2=currentAmpOut/calAmpOut

# now a different year:
date2=UTCDateTime("2015,01,29,05,20,00")
fileName = ('/msd/'+network+'_'+station+'/'+str(date2.year)+'/'+
              str(date2.julday).zfill(3)+'/'+location+'_'+channel+'.512.seed')
oldAmpOut = calcSinAmp(fileName,date2)
print(oldAmpOut)
try:
# since we have 2 different naming conventions, try the new way
   fileName = ('/msd/'+network+'_'+station+'/'+str(date2.year)+'/'+
              str(date2.julday).zfill(3)+'/BC1.512.seed')
   oldCalAmpOut = calcSinAmp(fileName,date2)
  
except:
# if it doesn't work, try the old way.
   fileName = ('/msd/'+network+'_'+station+'/'+str(date2.year)+'/'+
              str(date2.julday).zfill(3)+'/_BC1.512.seed')
   oldCalAmpOut = calcSinAmp(fileName,date2)

Ft1=oldAmpOut/oldCalAmpOut
