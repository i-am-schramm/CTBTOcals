#!/bin/env python

''' fetch the resp paz for full-frequency response email '''

from obspy.core.inventory import read_inventory
from obspy import UTCDateTime

def timeInRange(start,end,time):
   if start <= end:
      return(start <= time <= end)
   else:
      return(start <= time or time <= end)


def getPAZinfo(station,network,channel,location,calDate):
   
   # must have 1.1.0 of obspy for this to work
   respFile='/APPS/metadata/RESPS/RESP.'+network+'.'+station+'.'+location+'.'+channel
   
   # read in the resp file
   respInfo=read_inventory(respFile,'RESP')
   net=respInfo[0]
   
   for i in range(0,len(net.stations)):
      sta=respInfo[0][i][0]
      if(timeInRange(sta.start_date,sta.end_date,calDate)):
        PAZ=sta.response.get_paz()

   return(PAZ)
       
########################################################################   


station='SFJD'
network='IU'
channel='BHZ'
location='10'
calDate=UTCDateTime("2017,01,17,00,00,00")

resp=getPAZinfo(station,network,channel,location,calDate)
#print(dir(resp))
poles=(resp.poles)
zeros=(resp.zeros)
print(poles,zeros)
