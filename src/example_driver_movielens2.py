#! /usr/bin/env python

#######################################################
# Project: EISA
# Driver for movielens2 example.
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
EXAMPLE_DIR_PATH = "../examples/movielens2/"

abar = ""
ans = ""
onto = ""

# get abar string
ABAR_FILE = "abar.txt"
PATH = EXAMPLE_DIR_PATH + ABAR_FILE
if os.path.isfile( PATH ) and os.access( PATH, os.R_OK ) :
  infile = open( PATH, "r")
  for line in infile :
      abar = line.replace("\n","")
  infile.close()
else :
  print "(1) In example_driver_movielens.py : Either file is missing or is not readable"

# get ans string
ANS_FILE = "ans.txt"
PATH = EXAMPLE_DIR_PATH + ANS_FILE
if os.path.isfile( PATH ) and os.access( PATH, os.R_OK ) :
  infile = open( PATH, "r")
  for line in infile :
      ans = line.replace("\n","")
  infile.close()
else :  
  print "(2) In example_driver_movielens.py : Either file is missing or is not readable"

# get onto string
ONTO_FILE = "onto.txt"
PATH = EXAMPLE_DIR_PATH + ONTO_FILE
if os.path.isfile( PATH ) and os.access( PATH, os.R_OK ) :
  infile = open( PATH, "r")
  for line in infile :
      onto = line.replace("\n","")
  infile.close()
else :  
  print "(3) In example_driver_movielens.py : Either file is missing or is not readable"

abar = ast.literal_eval( abar )
ans = ast.literal_eval( ans )
onto = ast.literal_eval( onto )

print "abar = " + str(abar)
print "ans = " + str(ans)
#print "onto = " + str(onto)

finalx = esa.esa( abar, ans, onto )
print "finalx = " + str( finalx )

print ""
print "---------------------------------------------"
print "---------------------------------------------"
print ""

# clean directory
#os.system("find . -name \*.pyc -delete")
