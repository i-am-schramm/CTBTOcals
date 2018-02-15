#!/bin/env python
''' fetch digitizer information for full frequency response.'''

def formatDIG(calOutFile,digType,digGain):
   dig2=("DIG2 2  %15.8e    40          {}\n" % digGain)
   f=open(calOutFile,'a')
   f.write(dig2.format(digType))
