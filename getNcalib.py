#!/bin/env python

def getNcalib(station,channel):
   f=open('IDC_calibs','r')
   for line in f:
      print(line)
      if "station" in line:
         print(line)
         if "channel" in line:
            
            return(line.split(",")[2])
   
