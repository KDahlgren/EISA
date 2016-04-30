#! /usr/bin/env python

#######################################################
# Project: EISA
# Generate a more complex ontology for the performance
# examples. 2 explanations. Used in paper.
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
#      getSpecial1
######################
def getSpecial1( numC ) :
  dict_special1 = {}

  newKey = "special1"
  newValue = []

  c = getC( numC )

  newValue.append( newKey )
  for key in c :
    newValue.append( key )

  dict_special1[ newKey ] = newValue

  return dict_special1

######################
#      getSpecial2
######################
def getSpecial2( numC ) :
  dict_special2 = {}

  newKey = "special2"
  newValue = []

  c = getC( numC )

  newValue.append( newKey )
  for key in c :
    newValue.append( key )

  dict_special2[ newKey ] = newValue

  return dict_special2

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
special1 = getSpecial1( numC )
special2 = getSpecial2( numC )
a = getA( numA )
b = getB( numB )
c = getC( numC )

print "letters = " + str(letters)
print "special1 = " + str(special1)
print "special2 = " + str(special2)
print "a = " + str(a)
print "b = " + str(b)
print "c = " + str(c)

onto.update( letters )
onto.update( special1 )
onto.update( special2 )
onto.update( a )
onto.update( b )
onto.update( c )

print "onto = " + str(onto)

# save ontology
testNum = numA + numB + numC
testName = str( testNum )
outFile = open( OUT_PATH + "onto" + testName + "_2.txt", "w" )
outFile.write( str(onto) )
outFile.close()

# clean directory
#os.system("find . -name \*.pyc -delete")
