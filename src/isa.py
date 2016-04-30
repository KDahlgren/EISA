#######################################################
# Project: EISA
#
# Filename: isa.py
#
#######################################################

######################
# IMPORT FILES
######################
from includes import *

import utils_isa

############################
#          ISA
############################
def isa( abar, ans, inst, ontoI ) :
  #print ""
  #print "... entering isa ..."
  #print ""

  # get adom
  # get x
  # get e
  # iterate over e
  #   iterate over contents of adom st contents not in ext of e component

  #adom = utils_isa.getAdom( inst ) #actual line
  adom = inst #hack for movielens example
  #print adom
  x = utils_isa.getX( abar )
  #print x
  e = utils_isa.getE( x, ontoI )
  #print e
  for j in range(0, len(e)) :
    for b in adom :
      #print "j = " + str(j) + "; " + "b in adom: " + b
      #print "e[j] = " + str(e[j])
      #print "utils_isa.getCompExt(e[j], ontoI) = " + str(utils_isa.getCompExt(e[j], ontoI))
      if not b in utils_isa.getCompExt(e[j], ontoI, adom) :
        #print "Comleted getCompExt"
        #print "b = " + b
        #print "x[" + str(j) + "] = " + str(x[j] )
        newX_j = copy.copy(x[j])
        newX_j.append(b)
        #print "newX_j = " + str(newX_j)
        newC_j = utils_isa.lub(newX_j, ontoI)
        #print "Completed lub"
        #print "newC_j = " + str(newC_j)
        if newC_j != "" :
          newE = copy.copy(e)
          newE[j] = newC_j
          #print "newE = " + str(newE)
          if utils_isa.checkAnsIntersection(newE, ans, ontoI, adom ) == False :
            #print "newE = " + str(newE)
            #print "checkAnsIntersection: NO INTERSECTION"
            e = newE
            x[j] = newX_j
          #else :
            #print "checkAnsIntersection: YES INTERSECTION"
  #print ""
  #print "... exiting isa ..."
  #print ""

  #print "e = " + str(e)
  return e
