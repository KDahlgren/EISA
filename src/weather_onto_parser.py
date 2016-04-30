#! /usr/bin/env python

#######################################################
# Project: EISA
# Generate ontology for the weather example used in the paper.
# 47 concepts.
#######################################################

######################
#    IMPORT FILES
######################
from includes import *

######################
#      MACROS
######################
BASE_PATH = "../data/"
WEATHER_DATA_PATH = "../examples/weather_47/weather_data_60.csv"
OUT_PATH = BASE_PATH

######################
#      getState
######################
def getState( state ) :
  dict_state = {}

  newKey = state
  newValue = []

  newValue.append(state)

  dict_city = {}

  if state == "ca" :
    dict_city = getCity( "SanFrancisco" )
  elif state == "ar" :
    dict_city = getCity( "Phoenix" )
  elif state == "il" :
    dict_city = getCity( "Chicago" )
  elif state == "ny" :
    dict_city = getCity( "NewYork" )

  for c in dict_city :
    m = dict_city.get( c )
    newValue.extend( m )

  dict_state[ newKey ] = newValue

  return dict_state

######################
#      getCity
######################
def getCity( city ) :
  p = {}
  l = []
  newKey = city
  l.append(city)
  if os.path.isfile( WEATHER_DATA_PATH ) and os.access( WEATHER_DATA_PATH, os.R_OK ) :
    infile = open( WEATHER_DATA_PATH, "r")
    for line in infile :
      b = line.split(",")
      if b[0] == city :
        l.append( b[1].replace("\n","").replace("\r","") )
    infile.close()
  else :
    print "In getPrecips : Either file is missing or is not readable"

  p[ newKey ] = l
  return p

######################
#      getPrec
######################
def getPrec() :
  dict_prec = {}
  
  newKey = "Precipitation"
  newValue = []
  newValue.append( newKey )

  if os.path.isfile( WEATHER_DATA_PATH ) and os.access( WEATHER_DATA_PATH, os.R_OK ) :
    infile = open( WEATHER_DATA_PATH, "r")
    for line in infile :
      b = line.split(",")
      currPrecip = b[1].replace("\n","").replace("\r","")
      if not currPrecip in newValue :
        newValue.append( currPrecip )
    infile.close()
  else :
    print "In getPrec : Either file is missing or is not readable"

  dict_prec[ newKey ] = newValue

  return dict_prec

######################
#     getPrecips
######################
def getPrecips() :
  dict_precips = {}
  if os.path.isfile( WEATHER_DATA_PATH ) and os.access( WEATHER_DATA_PATH, os.R_OK ) :
    infile = open( WEATHER_DATA_PATH, "r")
    for line in infile :
      p = {}
      b = line.split(",")
      currPrecip = b[1].replace("\n","").replace("\r","")
      if not currPrecip in p :
        tmp = []
        tmp.append(currPrecip)
        p[ currPrecip ] = tmp
      dict_precips.update(p)
    infile.close()
  else :
    print "In getPrecips : Either file is missing or is not readable"
  return dict_precips

######################
#      DRIVER
######################
# ca -> ca, SanFrancisco, sf_precips
# ar -> ar, Phoenix, ph_precips
# il -> il, Chicago, ch_precips
# ny -> ny, NewYork, ny_precips
# SanFrancisco -> SanFrancisco, sf_precips
# Phoenix -> Phoenix, ph_precips
# Chicago -> Chicago, ch_precips
# NewYork -> NewYork, ny_precips
# prec -> the concept of precipitation and all precips
# precips -> all precips in dataset

# initialize ontology
onto = {}

ca = getState( "ca" )
ar = getState( "ar" )
il = getState( "il" )
ny = getState( "ny" )

sf = getCity( "SanFrancisco" )
ph = getCity( "Phoenix" )
ch = getCity( "Chicago" )
nyc = getCity( "NewYork" )

prec = getPrec()
precips = getPrecips()

onto.update( ca )
onto.update( ar )
onto.update( il )
onto.update( ny )
onto.update( sf )
onto.update( ph )
onto.update( ch )
onto.update( nyc )
onto.update( prec )
onto.update( precips )

print "onto = " + str(onto)

# save ontology
outFile = open( OUT_PATH + "weather_onto.out", "w" )
outFile.write( str(onto) )
outFile.close()

# clean directory
#os.system("find . -name \*.pyc -delete")
