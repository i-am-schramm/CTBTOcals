#!/bin/env python

''' this file will get the amplitude at the given frequency for a given station '''

import os
from obspy import UTCDateTime
from getStageGain import getStageGain
from calcSinAmp import calcSinAmp
from calcCalConstant import calcCalConstant
import numpy as np

#station='SFJD'
#network='IU'
#location='10'
#channel='BHZ'
#calper=1.0
#date=UTCDateTime("2018,01,18,00,33,00")
#date2=UTCDateTime("2015,01,29,05,20,00")

def calcNewCalib(station,network,channel,location,calper,date,date2):
   idebug=False
   # get the current resp stage gains
   stageGains=[]
   calfreq=1.0/calper
   for stage in range(1,4):
      stageGains.append(getStageGain(station,network,channel,location,date,stage,calfreq))
   
   if(idebug):
      print("STAGE 1 gain: "+str(stageGains[0]))
      print("STAGE 2 gain: "+str(stageGains[1]))
      print("STAGE 3 gain: "+str(stageGains[2]))
   
   # now get the calibration constants
   # first the current year:
   filePath = ('/msd/'+network+'_'+station+'/'+str(date.year)+'/'+
                 str(date.julday).zfill(3)+'/')
   Ft2=calcCalConstant(filePath,channel,date)
   
   # now a different year:
   filePath2 = ('/msd/'+network+'_'+station+'/'+str(date2.year)+'/'+
                 str(date2.julday).zfill(3)+'/')
   Ft1=calcCalConstant(filePath2,channel,date2)
   
   #Ft1 and Ft2 should be fairly close in value; the ratio should be ~1.
   # need to check these numbers against the spreadsheet values... something isn't correct.
   S2=(Ft1/Ft2)*stageGains[0]
   
   if(idebug): print("This should be close to stage 1: "+str(S2))
   
   #now to get this into CTBTO calib formula.  This comes from a pdf presentation that is on the N-drive:
   # in Calibrations/CTBTO\ Requirements/Calibration_Procedures\ for\ communication\ with\ PTS.pdf
   # the formula is on slide 38/39.
   ### something isn't coming out correctly here....
   Calib=calper/(S2*stageGains[1]*stageGains[2]*2.0*np.pi*1e-9)
   return(Calib)
