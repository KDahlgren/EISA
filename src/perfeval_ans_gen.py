#! /usr/bin/env python

#######################################################
# Project: EISA
# Get the answer set for the performance examples used 
# in the paper.
#######################################################

######################
#    IMPORT FILES
######################
from includes import *

######################
#      MACROS
######################
BASE_PATH = "../data/"
OUT_PATH = BASE_PATH

######################
#      DRIVER
######################

# test info
num = 1024

# initialize ans
ans = []

# populate ans
for i in range(1,num+1) :
  currList = []
  currA = "a" + str(i)
  currB = "b" + str(i)
  currList.append( currA )
  currList.append( currB )
  ans.append( currList )

print "ans = " + str(ans)

# save ans
testNum = num
testName = str( testNum )
outFile = open( OUT_PATH + "ans" + testName + ".txt", "w" )
outFile.write( str( ans ) )
outFile.close()

# clean directory
#os.system("find . -name \*.pyc -delete")
