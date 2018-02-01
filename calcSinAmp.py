#!/bin/env python

''' given a start time and filename this script will read in a waveform 
and return the amplitude'''

# the start time should be the beginning of the actual sine wave, not 
# the beginning of the cal input. I will investigate how the time in 
#the seed blockette matches up for this.

from obspy import read, UTCDateTime

def calcSinAmp(fileName,start):
   st = read(fileName,starttime=start, endtime=start+600)
   st.plot()
   sinAmp=st[0].std()

   return(sinAmp)
