#!/bin/env python

''' given a start time and filename this script will read in a waveform 
and return the amplitude'''

# the start time should be the beginning of the actual sine wave, not 
# the beginning of the cal input. I will investigate how the time in 
#the seed blockette matches up for this.

from obspy import read, UTCDateTime

#fileName = '/tr1/telemetry_days/IU_SFJD/2018/2018_018/10_BH2.512.seed'
fileName = '/msd/IU_FURI/2015/281/_BC1.512.seed'
#calStart=UTCDateTime("2018,018,00,33,00")
calStart=UTCDateTime("2015,281,09,37,00")
print(calStart)

st = read(fileName,starttime=calStart, endtime=calStart+600)
st.plot()
sinAmp=st[0].std()

print(sinAmp)
