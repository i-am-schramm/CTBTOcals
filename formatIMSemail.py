#!/bin/env python

''' when given a station and date it will produce the cal result email '''
from obspy import UTCDateTime
from getStageGain import getStageGain
from formatPAZ import formatPAZ
from formatFIR import formatFIR
from formatDIG import formatDIG
########################################################################
# inputs:
#   station=station name
#   calDate=UTCDateTime object with the start time of the calibration
#   calib=sensitivity value calculated from sine wave calibration
#   calper=period of sine wave used in calib calculation
#
# outputs: 
#   creates a file, CALIBRATE_RESULT_$station_$year that can be 
#   copied into an email and sent to the CTBTO.
# Kimberly Schramm
########################################################################

def formatIMSemail(station,network,channel,location,calDate,calib,calper,yORn):

   calOutFile="CALIBRATE_RESULT_"+station+'_'+str(calDate.year)
   f=open(calOutFile,"a")

   ### get some gains so I don't keep passing sncl all the time
   freq=1.0
   stage=1
   pazGain=getStageGain(station,network,channel,location,calDate,stage,freq)
   stage=2
   digGain=getStageGain(station,network,channel,location,calDate,stage,freq)
   stage=3
   firGain=getStageGain(station,network,channel,location,calDate,stage,freq)
   
   ### this is the header info
   to="calibration@ctbto.org"
   subject ="Subject: CALIBRATE_RESULT_{}\n \n"
   msg_id="MSG_ID cal_{}_1_{}_cr\n" 
   ref_id="REF_ID cal_{}_1_{}_cs\n"
   timeStamp="TIME_STAMP {}\n"
   
   f.write(subject.format(station))
   f.write("BEGIN IMS2.0\n")
   f.write("MSG_TYPE COMMAND_RESPONSE\n")
   f.write(msg_id.format(calDate.year,station))
   f.write(ref_id.format(calDate.year,station))
   f.write(timeStamp.format(UTCDateTime.now().strftime("%Y/%m/%d %H:%M:%S")))
   f.write("\n")
   
   ### this needs to be repeated for all 3 channels
   chanList=["BHZ", "BHE", "BHN"]
   instType='STS-2.5'
   digType='Q330HR'
   print(chanList)
   for chan in chanList:
      staList="STA_LIST {}\n"
      chaList="CHAN_LIST {}\n"
      spec="IN_SPEC {}\n"
      val="CALIB {}\n"
      per="CALPER {}\n"
   
      f.write(staList.format(station))
      f.write(chaList.format(chan))
      f.write("CALIBRATE_RESULT\n")
      f.write(spec.format(yORn))
      f.write(val.format(calib))
      f.write(per.format(calper))
      f.write("DATA_TYPE RESPONSE IMS2.0\n")
      # need to call the PAZ, dig2, fir2 here
      f.close()
      formatPAZ(calOutFile,instType,digType,pazGain)
      formatDIG(calOutFile,digType,digGain)
      formatFIR(calOutFile,calDate,digType,firGain)
      f=open(calOutFile,"a")
      f.write("\n")
   
   f.write("STOP")
   
   
