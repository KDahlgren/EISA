#######################################################
# Project: EISA
#
# Filename: utils.py
#
# All ESA functionality.
#######################################################

######################
#    IMPORT FILES
######################
from includes import *

########################################
#               GETSETS
########################################
# Get the list of concepts subsuming
# each component of the abar instance.
def getSets( abar, onto ) :
  #print ""
  #print "... entering getSets ..."
  #print ""

  conSetList = {}

  for concept_abar in abar :
    #print "In esa, getSets: concept_abar = " + concept_abar
    for key_concept_onto in onto :
      #print "In esa, getSets: key_concept_onto = " + str(key_concept_onto)
      for value_concept_onto in onto[key_concept_onto] :
        #print "In esa, getSets: value_concept_onto = " + str(value_concept_onto)
        if value_concept_onto == concept_abar :
          #print concept_abar + " is subsumed by " + str(key_concept_onto)
          conSetList.setdefault(concept_abar,[]).append(key_concept_onto)
          # remove duplicates
          unique = []
          [unique.append(item) for item in conSetList[concept_abar] if item not in unique]
          conSetList[concept_abar] = unique

  #print ""
  #print "... exiting getSets ..."
  #print ""
  return conSetList

########################################
#               GETALLSUBS
########################################
# Get the list of concepts subsuming
# each component of the abar instance.
def getAllSubs( expl, onto ) :
  allSubsDict = {}
  for con in expl :
    subList = getSubs(con, onto)
    allSubsDict[con] = subList
  return allSubsDict

########################################
#               GETSUBS
########################################
# Get the list of concepts subsuming
# each component of the abar instance.
def getSubs( concept, onto ) :
  return onto[concept]

########################################
#               GETX
########################################
# Get the list of all possible
# explanations for abar.
def getX( abar, ans, onto, conSetList ) :
  #print ""
  #print "... entering getX ..."
  #print ""

  #print "IN GETX : "
  #print "abar = "
  #print abar
  #print "ans = "
  #print ""
  #print ans
  #print "onto = "
  #print onto
  #print "conSetList = "
  #print conSetList

  newDir = "../data/results_" + str(abar).translate(None, string.whitespace).replace("[", "").replace("]", "").replace(",", ".").replace("'","").replace("(","_").replace(")","_") + "/"
  if not os.path.isdir(newDir) :
    os.system("mkdir " + newDir)
  else : #clear dir if exists
    os.system("rm " + newDir + "*.txt")

  x = []
  combosFilePath = getValidExpls( conSetList, abar, ans, onto, newDir )

  # populate the set x
  # combos of concepts in x represent explanations
  # and do not intersect the answer set
  PATH = combosFilePath
  if os.path.isfile(PATH) and os.access(PATH, os.R_OK) :
    #print "In getX: File exists and is readable"
    combosFile_open = open( PATH, "r")
    for line in combosFile_open :
      line = line.translate(None, string.whitespace)
      b = line.split(",")
      x.append(b)
    combosFile_open.close()
  else :
    print "In getX: Either file is missing or is not readable"

  #print "validExpls stored in " + combosFilePath
 
  #print ""
  #print "... exiting getX ..."
  #print ""
  return x

########################################
#           GETVALIDEXPLS
########################################
# Get the list of concepts subsuming
# each component of the abar instance.
# Save all combos to a file.
# Saved explanations do not intersect
# answer set.
def getValidExpls( conSetList, abar, ans, onto, saveDir ) :
  #print ""
  #print "... entering getValidCombos ..."
  #print ""

  completePath = ""
  basepath = saveDir
  filename = "validcombos_" + str(abar).replace(" ", "").replace("'", "").replace("[", "").replace(",", ".").replace("]", "").replace("(","_").replace(")","_") + ".txt"
  completePath = basepath + filename
  outFile_open = open( completePath, "w")

  # get all representations of abar
  # for each representation, check if
  #   the representation intersects ans.
  #   if intersection is true, skip
  #   else, save.

  # get all representations of abar
  abarCombosFile = getAllCombos( 0, abar, conSetList, "", saveDir )

  # import all representations
  # allReps contains the compete set of representations for abar as arrays of strs
  allReps = []
  PATH = abarCombosFile
  if os.path.isfile(PATH) and os.access(PATH, os.R_OK) :
    #print "In getValidExpls: File exists and is readable"
    repsFile_open = open( PATH, "r")
    for line in repsFile_open :
      #line = line.translate(None, string.whitespace)
      b = line.split(",")
      allReps.append(b)
    repsFile_open.close()
  else :
    print "In getValidExpls: Either file is missing or is not readable"

  # iterate over all representations
  for rep in allReps :
    #print "^^^^ rep = " + str(rep)
    rep[ len(rep) - 1 ] = rep[ len(rep) - 1 ].replace("\n", "")
    #print "^^^^ rep = " + str(rep)
    if checkAnsIntersection( rep, ans, onto, saveDir ) : # Call returns true if rep intersects ans
      pass
    else :
      finalExpl = str(rep).translate(None, string.whitespace).replace("'", "").replace("[", "").replace("]","") + "\n"
      outFile_open.write( finalExpl )

  outFile_open.close()

  #print "completePath = " + completePath

  #print ""
  #print "... exiting getValidCombos ..."
  #print ""
  return completePath

########################################
#         CHECKANSINTERSECTION
########################################
def checkAnsIntersection( savedExpl, ans, onto, saveDir ) :
  for answerTup in ans :
    #print "answerTup = " + str(answerTup)
    #print "savedExpl = " + str(savedExpl)
    #print "ans = " + str(ans)
    result = checkSub( savedExpl, answerTup, onto ) #check if savedExpl subsumes answerTup
    #print "result = " + str(result)
    if result == True : #savedExpl subsumes some answer tuple
      return True
  else :
    return False

########################################
#              CHECKSUB
########################################
# check if savedExpl subsumes a
# Returns True if savedExpl subsumes a
# Returns False if savedExpl does not subsume a
def checkSub( savedExpl, a, onto ) :
  if len(savedExpl) != len(a) :
    print "ERROR! Proposed explanation and answer tuple are different lengths!"
    print "savedExpl = " + str(savedExpl)
    print "a = " + str(a)
    sys.exit()
  else :
    flag = checkSub_trim(savedExpl, a, onto)
    return flag

########################################
#           CHECKSUB_HELPER
########################################
# Assumes every concept subsumes a data 
# concept at some point
def checkSub_helper(concept, answer, pos, onto) :
  countSubs = 0
  #print "... entered checkSub_helper ..."
  subCons = getSubs(concept, onto)
  if len(subCons) == 1 :
    if concept == answer[pos] :
      countSubs = countSubs + 1
  else :
    for con in subCons :
      checkSub_helper(con, answer, pos, onto)
  return countSubs

########################################
#             GETALLCOMBOS
########################################
def getAllCombos( depth, abar, conceptList, currCombo, saveDir ) :
  #print ""
  #print "... entering getAllCombos ..."
  #print ""

  #print "conceptList: "
  #print conceptList
  #print "abar = " + str(abar)
  #print "depth = " + str(depth)

  completePath = ""
  basepath = saveDir
  #currTime = strftime("%d-%b-%Y_%H.%M.%S")
  myNum = random.randint(0,999)
  #filename = "allcombos_" + currTime + "_" + str(myNum) + ".txt"
  filename = "allcombos_" + str(abar).replace(" ", "").replace("'", "").replace("[", "").replace(",", ".").replace("]", "").replace("(","_").replace(")","_") + ".txt"
  completePath = basepath + filename

  currCombo_orig = copy.copy(currCombo)
  conceptList_orig = copy.copy(conceptList)
  conceptList_new = copy.copy(conceptList_orig)

  #print "1** conceptList_orig = " + str(conceptList_orig)

  #print "*****************************"
  #print "            -----"
  con = abar[depth]
  value_list = conceptList_orig[con]

  #print "depth = " + str(depth)
  #print "con = abar[depth] = " + con
  #print "value_list = " + str(value_list)

  flag = False
  for i in range(depth+1, len(abar)-1) :
    if abar[i] == con :
      #print "con = " + con + " is in abar = " + str(abar)
      flag = True

  # con appears in abar more than once
  if flag == False :
    status = conceptList_new.pop(con)
  #print "            -----"
  #print "*****************************"

  #print "2** conceptList_orig = " + str(conceptList_orig)

  for item in value_list :

    #print "con = " + con
    #print "value_list = " + str(value_list)
    #print "item = " + item

    #print "3** conceptList_orig = " + str(conceptList_orig)

    if bool(conceptList_new) == False :
      currCombo_new = currCombo_orig + item
      saveFile_open = open( completePath, "a") #overwrites file with same name
      saveFile_open.write( currCombo_new + "\n" ) #currCombo is a comma-delimited string
      saveFile_open.close()
      #print "** conceptList_orig = " + str(conceptList_orig)
      #print "currCombo_new = " + currCombo_new
      currCombo_new = currCombo_orig
    else :
      currCombo_new = currCombo_orig + item + ","
      #print "** conceptList_orig = " + str(conceptList_orig)
      getAllCombos( depth+1, abar, conceptList_new, currCombo_new, saveDir )

  #print ""
  #print "... exiting getAllCombos ..."
  #print ""
  return completePath

############################
#          TRIM
############################
def trim( x, onto ) :
  #print ""
  #print "... entering trim ..."
  #print ""

  newX = copy.copy(x)
  for e1 in x :
    for e2 in x :
      if e1 != e2 :
        if checkSub_trim(e1, e2, onto) == True :
          if e2 in newX :
            newX.remove(e2)

  #print ""
  #print "... exiting trim ..."
  #print ""
  return newX

############################
#      CHECKSUB_TRIM
############################
# check if e1 subsumes e2
def checkSub_trim( e1, e2, onto ) :
  #print ""
  #print "... entering checkSub_trim ..."
  #print ""

  flag = True
  for i in range(0, len(e1)) :
    e1_allConsPerCon = getAllConsPerCon(e1[i], onto, [])
    currCon_e2 = e2[i]

    #print "e1_allConsPerCon = " + str(e1_allConsPerCon)
    #print "currCon_e2 = " + currCon_e2

    if not currCon_e2 in e1_allConsPerCon :
      flag = False

  #print ""
  #print "... exiting checkSub_trim ..."
  #print ""
  return flag

############################
#      GETALLCONSPERCON
############################
def getAllConsPerCon( expl, onto, allConsPerCon ) :
  if not isList(expl) :
    #print "not list"
    temp = []
    temp.append(expl)
    expl = temp
    #print "new expl = " + str(expl)

  for con in expl :
    #print "con = " + str(con)
    subCons = onto[con]
    temp = []
    temp.append(con)
    #print "subCons = " + str(subCons)
    #print "temp = " + str(temp)
    if len(temp) == len(subCons) and con == subCons[0] :
      allConsPerCon.append( con )
    else :
      allConsPerCon.append(con)
      #print "allConsPerCon = " + str(allConsPerCon)
      for newCon in subCons :
        #print "**subCons = " + str(subCons)
        #print "**newCon = " + str(newCon)
        if newCon != con :
          getAllConsPerCon(newCon, onto, allConsPerCon)
  # remove duplicates
  unique = []
  [unique.append(item) for item in allConsPerCon if item not in unique]
  allConsPerCon = unique
  return allConsPerCon

############################
#          ISLIST
############################
def isList(a) :
  if "[" in str(a) and "]" in str(a) :
    return True
  else :
    return False
