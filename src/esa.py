#######################################################
# Project: EISA
#
# Filename: esa.py
#
#######################################################

######################
# IMPORT FILES
######################
from includes import *

import utils

############################
#          ESA
############################
def esa( abar, ans, onto ) :
  #print ""
  #print "... entering esa ..."
  #print ""

  conExtList = utils.getSets( abar, onto )
  #print "getSets: " + str(conExtList)
  x = utils.getX( abar, ans, onto, conExtList)
  #print "getX: " + str(x)
  x = utils.trim( x, onto)

  #print ""
  #print "... exiting esa ..."
  #print ""
  return x
