#######################################################
# Project: EISA
#
# Filename: utils_isa.py
#
# All isa functionality.
#######################################################

######################
# IMPORT FILES
######################
from includes import *

############################
#          LUB
############################
# the most specific concept subsuming
# all concepts in the conSet
def lub( conSet, ontoI ) :
  #print "... entering lub ..."

  saveList = []

  #print "conSet = " + str(conSet)

  for con in ontoI :
    #print "con = " + str(con)
    a = set(conSet)
    b = ontoI[con]
    c = set(b)

    #print "set(conSet) = " + str(a)
    #print "set(ontoI[con]) = " + str(c)

    if a.issubset(c) :
      #print "*** TRUE ***"
      saveList.append(con)

  # get the most specific concept
  if len(saveList) > 0 :
    #print "saveList = " + str(saveList)
    #print "ontoI[saveList[0]] = " + str(ontoI[saveList[0]])
    currMinConPos = 0
    currMinConCount = len( ontoI[saveList[0]] )
    for i in range(1, len(saveList)) :
      #print "i = " + str(i)
      if currMinConCount > len( ontoI[saveList[i]] ) :
        currMinConPos = i
        currMinConCount = len( ontoI[saveList[i]] )

    #print "currMinConPos = " + str(currMinConPos)
    #print "currMinConCount = " + str(currMinConCount)

  #print "... exiting lub ..."

  if len(saveList) > 0 :
    return saveList[currMinConPos]
  else :
    return ""

############################
#          getAdom
############################
def getAdom( inst ) :
  temp = []
  for list in inst :
    temp.extend(list)
  # remove duplicates
  unique = []
  [unique.append(item) for item in temp if item not in unique]
  temp = unique
  return temp

############################
#          getX
############################
def getX( abar ) :
  x = []
  for con in abar :
    temp = []
    temp.append(con)
    x.append(temp)
  return x

############################
#          getE
############################
def getE( x, ontoI ) :
  e = []
  for component in x :
    e.append( lub( component, ontoI ) )
  return e

############################
#        getCompExt
############################
# returns list of data concepts subsumed by conset 
def getCompExt( conSet, ontoI, adom ) :
  #print "conSet = " + str(conSet)
  #print "ontoI = " + str(ontoI)

  if not isList( conSet ) :
    temp = []
    temp.append(conSet)
    conSet = temp

  saveList = []
  for concept in conSet :
    #print concept
    if isData( concept, ontoI ) == True :
      saveList.append(concept)
    else :
      for con in ontoI[concept] :
        #print "con = " + con
        if concept != con :
          saveList.extend( getCompExt(con, ontoI, adom) )
          # remove duplicates
          unique = []
          [unique.append(item) for item in saveList if item not in unique]
          saveList = unique
        elif concept in adom : # the extension of a concept into the instance includes itself if it is also appears in the instance
          saveList.append(concept)
  return saveList

############################
#          isData
############################
def isData( con, ontoI ) :
  subs = ontoI[con]
  if len(subs) == 1 and con == subs[0] :
    return True
  else :
    return False

############################
#          ISLIST
############################
def isList(a) :
  if "[" in str(a) and "]" in str(a) :
    return True
  else :
    return False

############################
#   checkAnsIntersection
############################
def checkAnsIntersection( newE, ans, ontoI, adom ) :
  for a in ans :
    if checkSub( newE, a, ontoI, adom ) == True : #newE subsumes some ans tup
      return True
  return False

############################
#       checkSub
############################
# check if t1 subsumes t2
def checkSub( t1, t2, ontoI, adom ) : 
  #print "t1 = " + str(t1)
  #print "t2 = " + str(t2)
  if len(t1) == len(t2) :
    for i in range(0, len(t1)) :
      completeExt_t1i = getCompExt( t1[i], ontoI, adom )
      if not t2[i] in completeExt_t1i :
        #print "t2[i] = " + t2[i] + " not in " + str(completeExt_t1i)
        return False
  else :
    print "MAJOR ERROR : cardinality of abar != cardinality of ans tups"
    sys.exit()

  return True
