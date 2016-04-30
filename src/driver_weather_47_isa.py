#! /usr/bin/env python

#######################################################
# Project: EISA
# Drive ISA for weather tests.
#
# Filename: driver_weather_47_isa.py
#
#######################################################

######################
# IMPORT FILES
######################
from includes import *

import isa

############################
# MAIN THREAD OF EXECUTION
############################
print ""
print "---------------------------------------------"
print "---------------------------------------------"
print ""
EXAMPLE_DIR_PATH = "../examples/weather_47/"
OUT_PATH = "../data/"

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
  print "(1) In driver_weather_47_isa.py : ABAR missing or is not readable"

# get ans string
ANS_FILE = "ans.txt"
PATH = EXAMPLE_DIR_PATH + ANS_FILE
if os.path.isfile( PATH ) and os.access( PATH, os.R_OK ) :
  infile = open( PATH, "r")
  for line in infile :
      ans = line.replace("\n","")
  infile.close()
else :  
  print "(2) In driver_weather_47_isa.py : ANS missing or is not readable"

# get onto string
ONTO_FILE = "onto.txt"
PATH = EXAMPLE_DIR_PATH + ONTO_FILE
if os.path.isfile( PATH ) and os.access( PATH, os.R_OK ) :
  infile = open( PATH, "r")
  for line in infile :
      onto = line.replace("\n","")
  infile.close()
else :  
  print "(3) In driver_weather_47_isa.py : ONTO missing or is not readable"

abar = ast.literal_eval( abar )
ans = ast.literal_eval( ans )
onto = ast.literal_eval( onto )

#print "abar = " + str(abar)
#print "ans = " + str(ans)
#print "onto = " + str(onto)

# get instance (hack)
inst = []
for key in onto :
  inst.append(key)

# remove duplicates
unique = []
[unique.append(item) for item in inst if item not in unique]
inst = unique

print len(inst)

finale = isa.isa( abar, ans, inst, onto )
print "finale = " + str( finale )

# save result
outFile = open( OUT_PATH + "weather_47_isa_result.data", "w" )
outFile.write( str(finale) + "\n"  )
outFile.close()

print ""
print "---------------------------------------------"
print "---------------------------------------------"
print ""

# clean directory
#os.system("find . -name \*.pyc -delete")
