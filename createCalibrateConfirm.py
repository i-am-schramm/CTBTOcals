#!/bin/env python
''' given a station channel list and start time will create the calibration confirm email for the CTBTO'''

from obspy import UTCDateTime

station='GNI'
channels=['BHN','BHE','BHZ']
#channels=['BH1','BH2','BHZ']
calDate=UTCDateTime("2018,02,19,15,00,00")

calConf_file="CALIBRATE_CONFIRM_"+station+"_"+str(calDate.year)
f=open(calConf_file,'w')

f.write("To        : calibration@ctbto.org\n")
f.write("Subject : CALIBRATE_CONFIRM_TSUM\n")
f.write("\n")
f.write("\n")

msg_id="MSG_ID cal_{}_1_{}_cc\n"
ref_id="REF_ID cal_{}_1_{}_cs\n"
timeStamp="TIME_STAMP {}\n"
startTime="START_TIME {}\n"
staList="STA_LIST {}\n"

f.write("BEGIN IMS2.0\n")
f.write("MSG_TYPE COMMAND_RESPONSE\n")
f.write(msg_id.format(calDate.year,station))
f.write(ref_id.format(calDate.year,station))
f.write(timeStamp.format(UTCDateTime.now().strftime("%Y/%m/%d %H:%M:%S")))
f.write("\n")

for chan in channels:
   chaList="CHAN_LIST {}\n"
   f.write(staList.format(station))
   f.write(chaList.format(chan))
   f.write(startTime.format(calDate.strftime("%Y/%m/%d %H:%M:%S")))
   f.write("CALIBRATE_CONFIRM\n")
   f.write("\n")

f.write("STOP\n")
