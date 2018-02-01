#!/bin/env python

''' this file will get the amplitude at the given frequency for a given station '''

import os
from obspy import UTCDateTime

# this is from Dave Wilson - showing off his mad awk skillz
# evalresp SFJD BHZ 2018 1 1 1 1 -stage 1 2 -u dis -f /APPS/metadata/RESPS/RESP.IU.SFJD.10.BHZ
# cat AMP.IU.SFJD.10.BHZ | awk '{print $2 * 10^-9 }' | awk '{print 1 / $1 }'
# 0.0632679

#Here is NCALIB using the full response (including the FIR filters).  The FIR filter response is not flat, so it is slightly different at different frequencies.
# cat AMP.IU.SFJD.10.BHZ | awk '{print $2 * 10^-9 }' | awk '{print 1 / $1 }'
# 0.0628484

# now obspy has some evalresp utitility but it doesn't look like it gives me what I want.  There is a def in the source and it gives me an error when I try to use it... grrr...  https://docs.obspy.org/_modules/obspy/signal/invsim.html#evalresp - see also the evalresp_for_frequencies
# invsim.evalresp(40,1024,'/APPS/metadata/SEED/IU.dataless','2018,01,01,00,00,00',station='SFJD',channel='BHZ',network='IU',locid='10',units='dis',debug=True)
# invsim.evalresp_for_frequencies(40,1.0,'/APPS/metadata/RESPS/RESP.IU.SFJD.10.BHZ','2018,01,01,00,00,00',station='SFJD',channel='BHZ',network='IU',locid='10',units='dis',debug=True)
# need version 1.1.0 of obspy for this functionality.

#so we call from the command line...

def getStageGain(station,network,channel,component,date,stage,freq):
   gain=[]
   string=('evalresp '+ station + ' ' + component +' '+str(date.year)+
           ' '+str(date.month)+' '+str(date.day)+' '+str(freq)+' 1 -stage '+
           str(stage)+' 2 -u dis -f /APPS/metadata/RESPS/RESP.'+network+'.'+
           station+'.'+channel+'.'+component)
   os.system(string)
   filename='AMP.'+network+'.'+station+'.'+channel+'.'+component
   print(filename)
   with open(filename) as f:
      gain=f.read().split(' ')
   return(float(gain[1])*1e-9)

