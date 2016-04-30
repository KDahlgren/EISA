#!/usr/bin/env python

#######################################################
# Project: EISA
# Test driver.
#######################################################

######################
# IMPORT FILES
######################
from includes import *

import esa
import utils
#import isa

############################
# MAIN THREAD OF EXECUTION
############################
print ""
print "---------------------------------------------"
print "---------------------------------------------"
print ""

###########
#   ESA   #
###########
abar = ["c", "x", "a"]
onto = { "con5":["con1", "a", "b", "c", "con2", "x", "y", "z"], "con1":["con1", "a", "b", "c"], "con2":["con2", "x", "y", "z"], "con3":["con3", "x","a"], "con4":["con4", "p", "q"], "x":["x"], "y":["y"], "z":["z"], "a":["a"], "b":["b"], "c":["c"], "p":["p"], "q":["q"]  }
#esa.esa( abar, ans, onto )

ans = [ ["c", "y", "a"], ["c", "x", "a"], ["p", "x", "a"] ]
saveDir = "../data/test/"
test = ["p", "y", "a"]
#test = ["c", "y", "a"]
#test = ["con1", "y", "a"]
#test = ["con4", "y", "a"]
conSetList1 = utils.getSets( test, onto )

x = utils.getX( test, ans, onto, conSetList1 )
newx = utils.trim(copy.copy(x), onto)
print "x = " + str(x)
print "trimmed x = " + str(newx)

print ""
print "---------------------------------------------"
print "---------------------------------------------"
print ""

# clean directory
os.system("find . -name \*.pyc -delete")
