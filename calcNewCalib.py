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

#date= UTCDateTime("2018,01,01,00,00,00")
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

fileName = ('/msd/'+network+'_'+station+'/'+str(date.year)+'/'+
              str(date.julday).zfill(3)+'/'+location+'_'+channel+'.512.seed')
currentAmpOut = calcSinAmp(fileName,date)
print(currentAmpOut)
