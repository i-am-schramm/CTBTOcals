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

date= UTCDateTime("2018,01,01,00,00,00")
stage=1
stage1 = getStageGain(,'10','BHZ',date,stage,'1')
stage=2
stage2 = getStageGain('SFJD','IU','10','BHZ',date,stage,'1')
stage=3
stage3 = getStageGain('SFJD','IU','10','BHZ',date,stage,'1')

print(stage1)
print(stage2)
print(stage3)

calStart=UTCDateTime("2018,01,18,00,33,00")
fileName = ('/msd/'+network+'_'+station+'/'+str(start.year)+'/'+
              str(start.julday).zfill(3)+'/'+channel+'_'+location+'.512.seed')
currentAmpOut = calcSinAmp(fileName,calStart)
print(currentAmpOut)
