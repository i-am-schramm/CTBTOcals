#!/bin/env python

''' given a station and start time this will create the outage report email '''

from obspy import UTCDateTime

station="GNI"
calDate=UTCDateTime("2018,02,19,00,00,00")
calEndDate=calDate+(2*24*60*60)

OR_file="Outage_Request_"+station
f=open(OR_file,"w")

subject="Subject : Report - OR - {}\n"
stat="{}\n"
time="{}\n"
heading=("Scheduled Calibration Activities {}\n")

f.write("To      : support@ctbto.org\n")
f.write(subject.format(station))
f.write("\n")
f.write("\n")

f.write("#Report type\n")
f.write("Outage request\n")
f.write("\n")

f.write("#Station code\n")
f.write(stat.format(station))
f.write("\n")

#f.write("#Source\n")
#f.write("Station - New Report\n")
#f.write("\n")

#f.write("#Site (optional for array stations)\n")
#f.write("\n")

f.write("#Submitted by\n")
f.write("Kimberly Schramm\n")
f.write("\n")

f.write("#email (optional)\n")
f.write("kschramm@usgs.gov\n")
f.write("\n")

f.write("#Heading\n")
f.write(heading.format(calDate.strftime("%Y")))
f.write("\n")

f.write("#Start date of requested outage (UTC)\n")
f.write(time.format(calDate.strftime("%Y/%m/%d")))
f.write("\n")

f.write("#End date of requested outage (UTC) (optional)\n")
f.write(time.format(calEndDate.strftime("%Y/%m/%d")))
f.write("\n")

f.write("#Mission capable\n")
f.write("yes\n")
f.write("\n")

f.write("#Data quality\n")
f.write("Calibration signal\n")
f.write("\n")

f.write("#Equipment affected (including serial/version number)(optional)\n")
f.write("\n")

f.write("#Description: reason for outage\n")
f.write("Scheduled Calibration activity\n")
f.write("\n")

f.write("#End")
