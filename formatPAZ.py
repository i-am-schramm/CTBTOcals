#!/bin/env python

''' formats poles and zeros for IMS 2.0'''

from obspy import UTCDateTime
from getPAZinfo import getPAZinfo

station='SFJD'
network='IU'
channel='BHZ'
location='10'
calDate=UTCDateTime("2018,01,17,00,00,00")

calOutFile="CALIBRATE_RESULT_"+station+'_'+str(calDate.year)
f=open(calOutFile,"a")
instType='STS-2.5'
#for the cal2 line, the intsrument can only have 5 chars

cal2="CAL2 SFJD  BHE      {}  0.0628497       1.000   40.0000     {}\n"

sens=0.683000000
PAZout=("PAZ2 01 V %15.8e  0    0.000    7   7   {} + Q330\n" % sens)

f.write(cal2.format(instType[0:5],calDate.strftime("%Y/%m/%d %H:%M")))
f.write(PAZout.format(instType))
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

