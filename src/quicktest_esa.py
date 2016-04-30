#!/usr/bin/env python

#######################################################
# Project: EISA
# quick sanity test.
#######################################################

######################
# IMPORT FILES
######################
from includes import *

import esa

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
#abar = ["p", "x", "a"]
abar = ["p", "y", "a"]
#ans = []
ans = [ ["c", "y", "a"], ["c", "x", "a"], ["q", "p", "a"]]
onto = { "con5":["con1", "x"], "con1":["a", "b", "c"], "con2":["x", "y", "z"], "a":["a"], "b":["b"], "c":["c"], "x":["x"], "y":["y"], "z":["z"], "con3":["p", "q"], "p":["p"], "q":["q"] }

finalx = esa.esa( abar, ans, onto )

print "abar = " + str(abar)
print "ans = " + str(ans)
print "onto = " + str(onto)
print "finalx = " + str( finalx )

print ""
print "---------------------------------------------"
print "---------------------------------------------"
print ""

# clean directory
#os.system("find . -name \*.pyc -delete")
