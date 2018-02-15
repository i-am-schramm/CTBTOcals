#!/bin/env python
''' fetch the fir filter info for full frequency resp'''

from obspy import UTCDateTime

#station='SFJD'
#network='IU'
#channel='BHZ'
#location='10'
#calDate=UTCDateTime("2018,01,17,00,00,00")

def getFIRinfo(digType):

#respFile='/APPS/metadata/RESPS/RESP.'+network+'.'+station+'.'+location+'.'+channel

# at the moment just going to hard code this as they should be the same for all Q330HR
# per a conversation with Dave Wilson on 02/15/2018.  I have verified that these values 
# are the same for SFJD, ANMO, TSUM

   FIR=[4.189520E-13,
     3.303180E-04,
     1.029210E-03,
    -3.141230E-03,
     2.057090E-04,
     1.525210E-03,
    -6.231930E-03,
     1.048010E-02,
    -1.312020E-02,
     1.078210E-02,
    -1.444550E-03,
    -1.587290E-02,
     3.950740E-02,
    -6.510360E-02,
     8.537160E-02,
    -8.919130E-02,
     5.006190E-02,
     8.372330E-01,
     2.667230E-01,
    -1.666930E-01,
     9.528400E-02,
    -5.092180E-02,
     1.614580E-02,
     7.063620E-03,
    -1.838770E-02,
     1.994140E-02,
    -1.548950E-02,
     8.527350E-03,
    -2.557890E-03,
    -1.811030E-03,
     2.426490E-03,
    -3.757690E-03,
     4.672930E-04,
     6.330720E-04,
    -1.568740E-06,
    -1.254800E-05,
     3.210410E-07,
    -2.633240E-08,
    -5.099970E-08]

   return(FIR)
