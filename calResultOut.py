#!/bin/env python

''' when given a station and date it will produce the cal result email '''
from obspy import UTCDateTime

station='SFJD'
calDate=UTCDateTime("2018,01,18,00,33,00")
calib=6.284974E-02
calper=1.0

calOutFile="CALIBRATE_RESULT_"+station+'_'+str(calDate.year)
f=open(calOutFile,"w")

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
   f.write(spec.format("yes"))
   f.write(val.format(calib))
   f.write(per.format(calper))
   f.write("\n")

f.write("STOP")


