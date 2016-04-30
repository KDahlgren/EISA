#! /usr/bin/env python

#######################################################
# Project: EISA
# Generates a simple ontology for the performance examples.
# Not used in paper. 1 explanation.
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
#      getLetters
######################
def getLetters( numA, numB, numC ) :
  dict_letters = {}

  newKey = "letters"
  newValue = []

  a = getA( numA )
  b = getB( numB )
  c = getC( numC )

  newValue.append( newKey )
  for key in a :
    newValue.append( key )
  for key in b :
    newValue.append( key )
  for key in c :
    newValue.append( key )

  dict_letters[ newKey ] = newValue

  return dict_letters

######################
#      getA
######################
def getA( num ) :
  dict_a = {}

  newKey = "a"
  newValue = []
  dataList = []

  newValue.append( newKey )

  # a and subsumptions
  for i in range(1,num+1) :
    datum = "a" + str(i)
    newValue.append( datum )
    dataList.append( datum )
  dict_a[ newKey ] = newValue

  # individual As and subsumptions
  for d in dataList :
    dict_temp = {}
    list_temp = []
    list_temp.append( d )    

    dict_temp[ d ] = list_temp 
    dict_a.update( dict_temp )

  return dict_a

######################
#      getBs
######################
def getB( num ) :
  dict_b = {}

  newKey = "b"
  newValue = []
  dataList = []

  newValue.append( newKey )

  # b and subsumptions
  for i in range(1,num+1) :
    datum = "b" + str(i)
    newValue.append( datum )
    dataList.append( datum )
  dict_b[ newKey ] = newValue

  # individual Bs and subsumptions
  for d in dataList :
    dict_temp = {}
    list_temp = []
    list_temp.append( d )

    dict_temp[ d ] = list_temp
    dict_b.update( dict_temp )

  return dict_b

######################
#      getCs
######################
def getC( num ) :
  dict_c = {}

  newKey = "c"
  newValue = []
  dataList = []

  newValue.append( newKey )

  # b and subsumptions
  for i in range(1,num+1) :
    datum = "c" + str(i)
    newValue.append( datum )
    dataList.append( datum )
  dict_c[ newKey ] = newValue

  # individual Cs and subsumptions
  for d in dataList :
    dict_temp = {}
    list_temp = []
    list_temp.append( d )

    dict_temp[ d ] = list_temp
    dict_c.update( dict_temp )

  return dict_c

######################
#      DRIVER
######################
# letters -> a, b, c
# a -> a1, a2, ...., aN
# b -> b1, b2, ...., bN
# c -> c1
# all data subsumes themselves

# test info
numA = 512
numB = 511
numC = 1

# initialize ontology
onto = {}
letters = getLetters( numA, numB, numC )
a = getA( numA )
b = getB( numB )
c = getC( numC )

print "letters = " + str(letters)
print "a = " + str(a)
print "b = " + str(b)
print "c = " + str(c)

onto.update( letters )
onto.update( a )
onto.update( b )
onto.update( c )

print "onto = " + str(onto)

# save ontology
testNum = numA + numB + numC
testName = str( testNum )
outFile = open( OUT_PATH + "onto" + testName + ".txt", "w" )
outFile.write( str(onto) )
outFile.close()

# clean directory
#os.system("find . -name \*.pyc -delete")
