#! /usr/bin/env python

#######################################################
# Project: EISA
#
# Obtain the ontology for the movielens example.
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

# ONTOLOGY:
# canada subsumes all canadian zipcodes + 
#                 all canadian users    +
#                 all movies reviewed by canadian users.
# us subsumes     all us zipcodes + 
#                 all us users    +
#                 all movies reviewed by us users. 
# movie subsumes all movie titles.
# each zipcode subsumes all users associated with the zipcode +
#                       all movies reviewed by those users.
# each user subsumes all movies she reviews.

# ALG:
# Get canada info and add to onto.
# Get us info and add to onto.
# Get info for each zipcode and add to onto.
# Get movie info and add to onto.
# Get info for each user and add to onto.

# declare onto as a dict
onto = {}

# -------------------------------
#           CANADA
# -------------------------------
key_canada = "canada"
value_canada = []

# all concepts subsume themselves
value_canada.append(key_canada)

# ALG:
# get canadian zipcodes. (u.user)
# get all canadian user ids. (u.data)
# get all movies reviewed by canadian users. (u.item)

# get canadian zipcodes and user ids
zipcodes_ca = []
users_ca = []

if os.path.isfile( USERS ) and os.access( USERS, os.R_OK ) :
  infile = open( USERS, "r")
  for line in infile :
    b = line.split("|")
    if any(c.isalpha() for c in b[4]) :
      zipcodes_ca.append( b[4].replace("\n","") )
      users_ca.append( b[0] )
  infile.close()
else :
  print "In movielens_onto_parser.py : Either file is missing or is not readable"

#print "zipcodes_ca = " + str(zipcodes_ca) 
#print "users_ca = " + str(users_ca)

# get all movie titles for movies rated by canadian users
movieTitles_ca = []
movieIDs_ca = []

# get list of movieIDs for movies rated by canadian users
if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
  infile = open( DATA, "r")
  for line in infile :
    b = line.split()
    if b[0] in users_ca :
      movieIDs_ca.append( b[1] )
  infile.close()
else :
  print "In movielens_onto_parser.py : Either file is missing or is not readable"

#print "movieIDs_ca = " + str(movieIDs_ca)

# get list of movie titles for movies rated by canadian users
if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
  infile = open( ITEMS, "r")
  for line in infile :
    b = line.split("|")
    if b[0] in movieIDs_ca :
      movieTitles_ca.append( b[1] )
  infile.close()
else :
  print "In movielens_onto_parser.py : Either file is missing or is not readable"

#print "movieTitles_ca = " + str(movieTitles_ca)

value_canada.extend( zipcodes_ca )
value_canada.extend( users_ca )
value_canada.extend( movieTitles_ca )

onto[ key_canada ] = value_canada
#print "onto = " + str( onto )

#print len(movieTitles_ca)
#print len(users_ca)

# -------------------------------
#              US
# -------------------------------
key_us = "us"
value_us = []

# all concepts subsume themselves
value_us.append(key_us)

# ALG:
# get us zipcodes. (u.user)
# get all us user ids. (u.data)
# get all movies reviewed by us users. (u.item)

# get us zipcodes and user ids
zipcodes_us = []
users_us = []

if os.path.isfile( USERS ) and os.access( USERS, os.R_OK ) :
  infile = open( USERS, "r")
  for line in infile :
    b = line.split("|")
    if any(c.isalpha() for c in b[4]) :
      pass
    else :
      zipcodes_us.append( b[4].replace("\n","") )
      users_us.append( b[0] )
  infile.close()
else :
  print "In movielens_onto_parser.py : Either file is missing or is not readable"

#print "zipcodes_us = " + str(zipcodes_us) 
#print "zipcodes_ca = " + str(zipcodes_ca)
#print len(zipcodes_us)
#print len(zipcodes_ca)
#print "users_us = " + str(users_us)

# get all movie titles for movies rated by canadian users
movieTitles_us = []
movieIDs_us = []

# get list of movieIDs for movies rated by canadian users
if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
  infile = open( DATA, "r")
  for line in infile :
    b = line.split()
    if b[0] in users_us :
      movieIDs_us.append( b[1] )
  infile.close()
else :
  print "In movielens_onto_parser.py : Either file is missing or is not readable"

#print "movieIDs_us = " + str(movieIDs_us)

# get list of movie titles for movies rated by us users
if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
  infile = open( ITEMS, "r")
  for line in infile :
    b = line.split("|")
    if b[0] in movieIDs_us :
      movieTitles_us.append( b[1] )
  infile.close()
else :
  print "In movielens_onto_parser.py : Either file is missing or is not readable"

#print "movieTitles_us = " + str(movieTitles_us)

value_us.extend( zipcodes_us )
value_us.extend( users_us )
value_us.extend( movieTitles_us )

onto[ key_us ] = value_us
#print "onto = " + str( onto )

# -------------------------------
#            MOVIE
# -------------------------------
key_movie = "movie"
value_movie = []

# all concepts subsume themselves
value_movie.append(key_movie)

# ALG:
# get us zipcodes. (u.user)
# get all us user ids. (u.data)
# get all movies reviewed by us users. (u.item)

# get all movie titles
movieTitles_movie = []

# get list of movie titles for movies rated by us users
if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
  infile = open( ITEMS, "r")
  for line in infile :
    b = line.split("|")
    movieTitles_movie.append( b[1] )
  infile.close()
else :
  print "In movielens_onto_parser.py : Either file is missing or is not readable"

#print "movieTitles_us = " + str(movieTitles_us)

value_movie.extend( movieTitles_movie )

#onto[ key_movie ] = value_movie
#print "onto = " + str( onto )

# -------------------------------
#         ZIPCODES_CA
# -------------------------------
for zipcode in zipcodes_ca :
  key_zipcode_ca = zipcode
  value_zipcode_ca = []

  # all concepts subsume themselves
  value_zipcode_ca.append(key_zipcode_ca)

  #print "key_zipcode_ca = " + key_zipcode_ca
  #print "value_zipcode_ca = " + str(value_zipcode_ca)

  # ALG:
  # get us zipcodes. (u.user)
  # get all us user ids. (u.data)
  # get all movies reviewed by us users. (u.item)

  # get user ids for this zipcode
  users_zipcode_ca = []

  if os.path.isfile( USERS ) and os.access( USERS, os.R_OK ) :
    infile = open( USERS, "r")
    for line in infile :
      b = line.split("|")
      if b[4].replace("\n","") == key_zipcode_ca :
        users_zipcode_ca.append( b[0] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  #print "users_zipcode_ca = " + str(users_zipcode_ca)

  # get all movie titles for movies rated by canadian users in this zipcode
  movieTitles_zipcode_ca = []
  movieIDs_zipcode_ca = []

  # get list of movieIDs for movies rated by canadian users in this zipcode
  if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
    infile = open( DATA, "r")
    for line in infile :
      b = line.split()
      if b[0] in users_zipcode_ca :
        movieIDs_zipcode_ca.append( b[1] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  # get list of movie titles for movies rated by us users
  if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
    infile = open( ITEMS, "r")
    for line in infile :
      b = line.split("|")
      if b[0] in movieIDs_zipcode_ca :
        movieTitles_zipcode_ca.append( b[1] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  #print "movieTitles_us = " + str(movieTitles_us)

  value_zipcode_ca.extend( users_zipcode_ca )
  value_zipcode_ca.extend( movieTitles_zipcode_ca )

  #print "value_zipcode_ca = " + str(value_zipcode_ca)

  onto[ key_zipcode_ca ] = value_zipcode_ca

#print "onto[E2E3R] = " + str(onto['E2E3R'])


# -------------------------------
#         ZIPCODES_US
# -------------------------------
for zipcode in zipcodes_us :
  key_zipcode_us = zipcode
  value_zipcode_us = []

  # all concepts subsume themselves
  value_zipcode_us.append(key_zipcode_us)

  #print "key_zipcode_us = " + key_zipcode_us
  #print "value_zipcode_us = " + str(value_zipcode_us)

  # ALG:
  # get us zipcodes. (u.user)
  # get all us user ids. (u.data)
  # get all movies reviewed by us users. (u.item)

  # get user ids for this zipcode
  users_zipcode_us = []

  if os.path.isfile( USERS ) and os.access( USERS, os.R_OK ) :
    infile = open( USERS, "r")
    for line in infile :
      b = line.split("|")
      if b[4].replace("\n","") == key_zipcode_us :
        users_zipcode_us.append( b[0] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  #print "users_zipcode_us = " + str(users_zipcode_us)

  # get all movie titles for movies rated by canadian users in this zipcode
  movieTitles_zipcode_us = []
  movieIDs_zipcode_us = []

  # get list of movieIDs for movies rated by canadian users in this zipcode
  if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
    infile = open( DATA, "r")
    for line in infile :
      b = line.split()
      if b[0] in users_zipcode_us :
        movieIDs_zipcode_us.append( b[1] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  # get list of movie titles for movies rated by us users
  if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
    infile = open( ITEMS, "r")
    for line in infile :
      b = line.split("|")
      if b[0] in movieIDs_zipcode_us :
        movieTitles_zipcode_us.append( b[1] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  #print "movieTitles_us = " + str(movieTitles_us)

  value_zipcode_us.extend( users_zipcode_us )
  value_zipcode_us.extend( movieTitles_zipcode_us )

  #print "value_zipcode_us = " + str(value_zipcode_us)

  onto[ key_zipcode_us ] = value_zipcode_us

#print "onto[E2E3R] = " + str(onto['E2E3R'])

# -------------------------------
#          USERS_CA
# -------------------------------
for user in users_ca :
  key_users_ca = user
  value_users_ca = []

  # all concepts subsume themselves
  value_users_ca.append(key_users_ca)

  # get all movie titles for movies rated by canadian users in this zipcode
  movieTitles_users_ca = []
  movieIDs_users_ca = []

  # get list of movieIDs for movies rated by canadian users in this zipcode
  if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
    infile = open( DATA, "r")
    for line in infile :
      b = line.split()
      if b[0] == key_users_ca :
        movieIDs_users_ca.append( b[1] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  # get list of movie titles for movies rated by us users
  if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
    infile = open( ITEMS, "r")
    for line in infile :
      b = line.split("|")
      if b[0] in movieIDs_users_ca :
        movieTitles_users_ca.append( b[1] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  value_users_ca.extend( movieTitles_users_ca )

  #print "key_users_ca = " + key_users_ca
  #print "value_users_ca = " + str(value_users_ca)
  onto[ key_users_ca ] = value_users_ca

#print "onto['74'] = " + str(onto['74'])

# -------------------------------
#          USERS_US
# -------------------------------
for user in users_us :
  key_users_us = user
  value_users_us = []

  # all concepts subsume themselves
  value_users_us.append(key_users_us)

  # get all movie titles for movies rated by us users in this zipcode
  movieTitles_users_us = []
  movieIDs_users_us = []

  # get list of movieIDs for movies rated by us users in this zipcode
  if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
    infile = open( DATA, "r")
    for line in infile :
      b = line.split()
      if b[0] == key_users_us :
        movieIDs_users_us.append( b[1] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  # get list of movie titles for movies rated by us users
  if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
    infile = open( ITEMS, "r")
    for line in infile :
      b = line.split("|")
      if b[0] in movieIDs_users_us :
        movieTitles_users_us.append( b[1] )
    infile.close()
  else :
    print "In movielens_onto_parser.py : Either file is missing or is not readable"

  value_users_us.extend( movieTitles_users_us )
  
  #print "key_users_us = " + key_users_us
  #print "value_users_us = " + str(value_users_us)
  onto[ key_users_us ] = value_users_us

#print "onto['780'] = " + str(onto['780'])


# -------------------------------
#         MOVIE_TITLES
# -------------------------------
for movie in movieTitles_movie :
  key_movie_titles = movie
  value_movie_titles = []

  # all concepts subsume themselves
  value_movie_titles.append(key_movie_titles)

  print "key_movie_titles = " + key_movie_titles
  print "value_movie_titles = " + str(value_movie_titles)
  onto[ key_movie_titles ] = value_movie_titles

#print "onto['Toy Story'] = " + str(onto['Toy Story (1995)'])

outFile = open( BASE_PATH + "onto.out", "w")
outFile.write( str(onto) )
outFile.close()

# clean directory
os.system("find . -name \*.pyc -delete")
