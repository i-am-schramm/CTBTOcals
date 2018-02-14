#!/bin/env python

''' formats poles and zeros for IMS 2.0'''

from obspy import UTCDateTime
from getPAZinfo import getPAZinfo

station='SFJD'
network='IU'
channel='BHZ'
location='10'
calDate=UTCDateTime("2017,01,17,00,00,00")

resp=getPAZinfo(station,network,channel,location,calDate)
#print(dir(resp))
poles=(resp.poles)
zeros=(resp.zeros)
# add extra zero to convert units
zeros.append(0.0+0.0j)
print(poles,zeros)

for pol in poles:
   print(" %15.8e %15.8e" % (pol.real,pol.imag))

for zer in zeros:
   print(" %15.8e %15.8e" % (zer.real,zer.imag))

