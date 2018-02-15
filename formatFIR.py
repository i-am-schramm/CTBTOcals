#!/bin/env python

''' this will format the fir filter info '''
from obspy import UTCDateTime
from getStageGain import getStageGain
from getFIRinfo import getFIRinfo

#station='SFJD'
#network='IU'
#channel='BHZ'
#location='10'
#calDate=UTCDateTime("2018,01,17,00,00,00")

def formatFIR(calOutFile,calDate,digType,firGain):
   f=open(calOutFile,"a")
   
   #fir2="FIR2 3  1.0067E+00 1    0.430    A 39"
   fir2=("FIR2 3  %10.2e 1    0.430    A 39\n" % firGain)
   f.write(fir2)
   
   firCoefs=getFIRinfo(digType)
   
   for i in range(0,len(firCoefs),5):
      f.write(" %15.8e" % firCoefs[i])
      f.write(" %15.8e" % firCoefs[i+1])
      f.write(" %15.8e" % firCoefs[i+2])
      f.write(" %15.8e" % firCoefs[i+3])
      print(i+4,len(firCoefs))
      if (i+4 < len(firCoefs)):
         f.write(" %15.8e\n" % firCoefs[i+4])
      else:
         f.write("\n")
