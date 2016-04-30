#! /usr/bin/env python

#######################################################
# Project: EISA
#
# Obtain the ontology for the movielens 311 example used in paper.
# Ontology contains 311 concepts.
# (Partial ontology - no user information)
#######################################################

######################
# IMPORT FILES
######################
from includes import *

BASE_PATH = "../data/"
MOVIELENS_DATA_PATH = "ml-100k/"
FULL_PATH = BASE_PATH + MOVIELENS_DATA_PATH

ITEMS_NAME = "u.item"
DATA_NAME = "u.data"
USERS_NAME = "u.user"

ITEMS = FULL_PATH + ITEMS_NAME
DATA = FULL_PATH + DATA_NAME
USERS = FULL_PATH + USERS_NAME

OUT_PATH = BASE_PATH

# WARNING:
#The author notes the movieX used in this example is banned 
# in several countries, but is not banned in the US. 
# The title is not revealed in the paper associated with this code, 
# but can be derived when comparing the list of movies banned in 
# Canada maintained on Wikipedia and the movies rated by Canadian 
# users in the 100K dataset. The title is also necessarily revealed 
# in the source code. The author does not recommend or endorse 
# this film. Seriously, it's horrible.
movieX = "In the Realm of the Senses (Ai no corrida) (1976)"
movieY = "Star Trek: First Contact (1996)"

######################
#      COUNTRY
######################
def getCountry( country ) :
  dict_country = {}
  
  newKey = country
  newValue = []

  newValue.append( newKey )

  zips = getZips( country )
  for z in zips :
    v = zips.get( z )
    newValue.extend( v )

  # remove duplicates
  unique = []
  [unique.append(item) for item in newValue if item not in unique]
  newValue = unique
 
  dict_country[ newKey ] = newValue
 
  return dict_country

######################
#      getZips
######################
# zips subsume themselves and movie titles for users in the location.
# Returns a dict containing all zips for the region + subsumed movieTitles.
def getZips( region ) :
  dict_zips = {}
  
  zipList = []
  if os.path.isfile( USERS ) and os.access( USERS, os.R_OK ) :
    infile = open( USERS, "r")
    for line in infile :
      b = line.split("|")
      zipcode = b[4].replace("\n", "")
      if movieSeenAtZip( zipcode, movieX, movieY ) : # only include zip if users saw movieY or movieX
        if region == "canada" :
          if any(c.isalpha() for c in zipcode) :
            zipList.append( zipcode )
        else :
          if any(c.isalpha() for c in zipcode) :
            pass
          else :
            zipList.append( zipcode )
      else:
        pass

  for z in zipList :
    print "currZip = " + z
    newKey = z
    newValue = []

    movieTitles = []
    userIDs = getUsersAtZip( z )
    for u in userIDs :
      titles = getTitlesGivenUser( u )
      for t in titles :
        if not t in movieTitles :
          if t == movieY or t == movieX : # comment out this line to include all movies per zip code
            movieTitles.append( t )
    
    newValue.append( newKey )
    newValue.extend( movieTitles )

    # remove duplicates
    unique = []
    [unique.append(item) for item in newValue if item not in unique]
    newValue = unique

    dict_zips[ newKey ] = newValue

  print "number of zips in " + region + " = " + str(len(dict_zips))

  return dict_zips

def movieSeenAtZip( zipcode, movieX, movieY ) :
  usersAtZip = getUsersAtZip( zipcode )
  for u in usersAtZip :
    uTitles = getTitlesGivenUser( u )
    if (movieY in uTitles) or (movieX in uTitles) :
      return True
    else :
      return False

def getUsersAtZip( z ) :
  uidList = []
  if os.path.isfile( USERS ) and os.access( USERS, os.R_OK ) :
    infile = open( USERS, "r")
    for line in infile :
      b = line.split("|")
      uid = b[0]
      zipcode = b[4].replace("\n", "")
      if zipcode == z :
        uidList.append( uid )

  return uidList

def getTitlesGivenUser( user ) :
  titles = []
  ids = []
  if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
    infile = open( DATA, "r")
    for line in infile :
      b = line.split()
      if b[0] == user :
        tid = b[1]
        if not tid in ids :
          ids.append( tid )

  for i in ids :
    t = getTitle( i )
    if not t in titles : 
      titles.append( t ) 

  return titles 

def getTitle( tid ) :
  title = ""
  if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
    infile = open( ITEMS, "r")
    for line in infile :
      b = line.split("|")
      t = b[0]
      if t == tid :
        title = b[1]

  return title

######################
#     getMovie
######################
def getMovie() :
  dict_movie = {}
  
  key1 = "movie"
  value1 = []
  value1.append( key1 )

  titles = getIndivMovies()

  for t in titles :
    value1.extend( titles.get(t) )

  dict_movie[ key1 ] = value1

  return dict_movie

######################
#   getIndivMovies
######################
def getIndivMovies() :
  dict_indivmovies = {}

  key1 = movieY
  value1 = []
  value1.append( movieY )

  key2 = movieX
  value2 = []
  value2.append( movieX )

  dict_indivmovies[ key1 ] = value1
  dict_indivmovies[ key2 ] = value2

  return dict_indivmovies

######################
#      DRIVER
######################
# canada -> canada, zips_ca, toy story, movieX
# us -> us, zips_us, toy story, movieX
# movie -> movie, movieX, toy story
# zips_ca -> zips_ca, toy story or movieX
# zips_us -> zips_us, toy story and movieX
# toy story -> toy story
# movieX -> movieX

# initialize ontology
onto = {}

# canada
canada = getCountry( "canada" )

# us
us = getCountry( "us" )

# zips
zips_ca = getZips( "canada" )
zips_us = getZips( "us" )

# movie
movie = getMovie()

# individual movies
indivMovies = getIndivMovies()
#print str(indivMovies)


onto.update( canada )
onto.update( us )
onto.update( movie )
onto.update( zips_ca )
onto.update( zips_us )
onto.update( indivMovies )

print "onto = " + str(onto)

# save ontology
outFile = open( OUT_PATH + "movielens_small.out", "w" )
outFile.write( str(onto) )
outFile.close()

# clean directory
#os.system("find . -name \*.pyc -delete")
