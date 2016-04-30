#! /usr/bin/env python

#######################################################
# Project: EISA
# Get the get movielens answer set.
#
#######################################################

######################
# IMPORT FILES
######################
from includes import *

BASE_PATH = "../data/"
MOVIELENS_DATA_PATH = "ml-100k/"
FULL_PATH = BASE_PATH + MOVIELENS_DATA_PATH

# QUERY:
# get all zipcodes of users who reviewed movieX
# movie titles are in u.item
# u.data connects user ids with movie ids
# zipcodes are in u.user

ITEMS_NAME = "u.item"
DATA_NAME = "u.data"
USERS_NAME = "u.user"

ITEMS = FULL_PATH + ITEMS_NAME
DATA = FULL_PATH + DATA_NAME
USERS = FULL_PATH + USERS_NAME

OUT_PATH = BASE_PATH

# ALG:
# Get movie id for movieX from u.item
# Get list of user ids associated with the movie id.
# Get the zipcodes for all users on id.
# Save zipcodes in ["<zipcode>", "<movieX>"] pairs
# in an output file called ans.txt saved in data/

# movie id
# DISCLAIMER: The author warns readers that the movie examined 
# in the example was banned in several Canadian provinces until recently.
# The movie is still banned in Nova Scotia.
# The movie is/was banned for good reason.
movieX = "In the Realm of the Senses (Ai no corrida) (1976)"
movie_id = ""

if os.path.isfile( ITEMS ) and os.access( ITEMS, os.R_OK ) :
  infile = open( ITEMS, "r")
  for line in infile :
    b = line.split("|")
    if b[1] == movieX :
      movie_id = b[0]
  infile.close()
else :
  print "In movielens_data_parser.py : Either file is missing or is not readable"

print "movie_id = " + movie_id

# users
user_ids = []

if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
  infile = open( DATA, "r")
  for line in infile :
    b = line.split()
    if b[1] == movie_id :
      user_ids.append( b[0] )
  infile.close()
else : 
  print "In movielens_data_parser.py : Either file is missing or is not readable"

print "user_ids = " + str(user_ids)

# zipcodes
zipcodes = []
pairs = ""

pairs = pairs + "[ "

if os.path.isfile( USERS ) and os.access( USERS, os.R_OK ) :
  infile = open( USERS, "r")
  for line in infile :
    b = line.split("|")
    if b[0] in user_ids :
      zipcodes.append( b[4].replace("\n","") )
      pairs = pairs + "[\"" + b[4].replace("\n","") + "\", \"" + movieX + "\"], " # "["<zipcode>", "<movieX>"], "
  infile.close()
else : 
  print "In movielens_data_parser.py : Either file is missing or is not readable"

# edit hack to remove last ", "
s = list( pairs )
s[ len(s)-2 ] = " "
s[ len(s)-1 ] = "]"
pairs = "".join(s)

#outFile = open( BASE_PATH + "pairs.out", "w")
#outFile.write( pairs )
#outFile.close()

print "zipcodes = " + str(zipcodes)

# list all canadian zip codes
print "Canadian zip codes: "
if os.path.isfile( USERS ) and os.access( USERS, os.R_OK ) :
  infile = open( USERS, "r")
  for line in infile :
    b = line.split("|")
    a = b[4].replace("\n", "")
    if any(c.isalpha() for c in a) :
      print b[4].replace("\n","") + ", "
      id = b[0]
      if os.path.isfile( DATA ) and os.access( DATA, os.R_OK ) :
        infile1 = open( DATA, "r")
        for line in infile1 :
          a = line.split()
          if b[0] == a[0] :
            print a[3] #print timestamp
        infile1.close()
      else :
        print "In movielens_data_parser.py : Either file is missing or is not readable"
  infile.close()
else :
  print "In movielens_data_parser.py : Either file is missing or is not readable"

# clean directory
#os.system("find . -name \*.pyc -delete")
