#!/bin/env python

''' check if calib is w/in 5% of ncalib '''

########################################################################
#
# inputs:
#   calib  - sensitivity value calculated from sine wave calibration
#   ncalib - expected value provided by the CTBTO
#
# outputs:
#   yes = If the percent difference is less than 5% it is in spec
#   no  = If the percent difference is greater than 5%
#
# Kimberly Schramm
########################################################################

def checkSpec(calib,ncalib):
   spec='yes'
   percdiff = ((calib-ncalib)/ncalib)*100
   if percdiff >= 5.0:
      spec='no'
      print('NOT IN SPEC!')
   return(spec)
