#! /usr/bin/env python

#######################################################
# Project: EISA
# Drive ESA algorithm for performance tests.
#
# Run with ./driver_perfeval_esa.py <absolutePathToAns> <absolutePathToOnto> <testNum> <testCategory = ans | onto > <trial Number>
#
#######################################################

######################
# IMPORT FILES
######################
from includes import *

import esa

############################
# MAIN THREAD OF EXECUTION
############################
#print ""
#print "---------------------------------------------"
#print "---------------------------------------------"
#print ""
EXAMPLE_DIR_PATH = "../examples/perfeval/"
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
  print "(1) In driver_perfeval_esa.py : ABAR missing or is not readable"

# get ans string
ANS_FILE = str( sys.argv[1] )
PATH = ANS_FILE
if os.path.isfile( PATH ) and os.access( PATH, os.R_OK ) :
  infile = open( PATH, "r")
  for line in infile :
      ans = line.replace("\n","")
  infile.close()
else :  
  print "(2) In driver_perfeval_esa.py : ANS missing or is not readable"

# get onto string
ONTO_FILE = str( sys.argv[2] )
PATH = ONTO_FILE
if os.path.isfile( PATH ) and os.access( PATH, os.R_OK ) :
  infile = open( PATH, "r")
  for line in infile :
      onto = line.replace("\n","")
  infile.close()
else :  
  print "(3) In driver_perfeval_esa.py : ONTO missing or is not readable"

abar = ast.literal_eval( abar )
ans = ast.literal_eval( ans )
onto = ast.literal_eval( onto )

#print "abar = " + str(abar)
#print "ans = " + str(ans)
#print "onto = " + str(onto)

time1 = datetime.datetime.now()
finalx = esa.esa( abar, ans, onto )
time2 = datetime.datetime.now()
print "finalx = " + str( finalx )

myTime = (time2 - time1).seconds
print "myTime = " + str(myTime)

# save result
testNum = sys.argv[3]
testType = sys.argv[4]
trialNum = sys.argv[5]
testName = testType + str(testNum) + "trial_" + str(trialNum)
outFile = open( OUT_PATH + "perfeval_esa_" + testName + "_result.data", "w" )
outFile.write( str(finalx) + "\n"  )
outFile.close()

# save time
testNum = sys.argv[3]
testType = sys.argv[4]
trialNum = sys.argv[5]
testName = testType + str(testNum) + "_trial" + str(trialNum)
outFile = open( OUT_PATH + "time_perfeval_esa_" + testName + "_result.data", "w" )
outFile.write( str( myTime ) + "\n"  )
outFile.close()

#print ""
#print "---------------------------------------------"
#print "---------------------------------------------"
#print ""

# clean directory
#os.system("find . -name \*.pyc -delete")
