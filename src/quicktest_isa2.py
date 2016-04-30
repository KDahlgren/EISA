#!/usr/bin/env python

#######################################################
# Project: EISA
# another sanity check.
#######################################################

######################
# IMPORT FILES
######################
from includes import *

import isa
import utils_isa

############################
# MAIN THREAD OF EXECUTION
############################
print ""
print "---------------------------------------------"
print "---------------------------------------------"
print ""

###########
#   ISA   #
###########
#abar = ["a2", "c2"] #no concept in ans tup, e = ['b2', 'b2']
#abar = ["a3", "c2"] #a concept in ans tup, e = ['b3', 'b2']
abar = ["a1", "c1"]  #abar is in ans, e = ['a1', 'c1']
ans = [ ["a1", "c1"], ["a3", "c3"] ]
inst = [ ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"] ]
ontoI = { "a1":["a1"], "a2":["a2"], "a3":["a3"], "b1":["b1", "a1"], "b2":["b2", "a2", "c2"], "b3":["b3", "a3", "c3"], "c1":["c1"], "c2":["c2"], "c3":["c3"] }

isa.isa( abar, ans, inst, ontoI )

print ""
print "---------------------------------------------"
print "---------------------------------------------"
print ""

# clean directory
#os.system("find . -name \*.pyc -delete")
