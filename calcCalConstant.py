#!/bin/env python
''' This will calculate the calibration constant '''

#######################################################################
# For more details on the calibration constant calculation, 
# see Ringler et al, 2014, "Obtaining Changes in Calibration-Coil to
# Seismometer Output Constants using Sine Waves"
# 
# outputs the ratio of the output sine wave (calAmpOut) to the 
# input sine wave (calAmpIn)
#
# uses calcSinAmp.py
#
# needs the path to the seed file, the channel (may need to BH1,2,Z for
# an STS-1.  
#
# currently assumes that this is only for 10 as that is where the 
# CTBTO sensors are located.
#######################################################################

from calcSinAmp import calcSinAmp

def calcCalConstant(filePath,channel,date):

   fileName=(filePath+'10_'+channel+'.512.seed')
   calAmpOut = calcSinAmp(fileName,date)
   
   try:
   # since we have 2 different naming conventions, try the new way
      fileName = (filePath+'BC1.512.seed')
      calAmpIn = calcSinAmp(fileName,date)
   
   except:
   # if it doesn't work, try the old way.
      fileName = (filePath+'_BC1.512.seed')
      calAmpIn = calcSinAmp(fileName,date)

   calConst=calAmpOut/calAmpIn
 
   return(calConst)
