#!/bin/bash

#######################################################
# Project: EISA
#
# Filename:run_perfeval.sh 
#
# For _2 tests, run with: ./run_perfeval.sh "_2"
# Version "_2" tests have 2 explanations. Leave the field
# blank for a test with only 1 explanation.
# 
#######################################################

##################################
#         testCall
##################################
# 1 = ans path
# 2 = onto path
# 3 = testNum
# 4 = test category = ans | onto
# 5 = trial number
function testCall
{
  aPath=$1
  oPath=$2
  testnum=$3
  tcat=$4
  trial=$5

  #echo "aPath = $aPath"
  #echo "oPath = $oPath"
  #echo "testnum = $testnum"
  #echo "tcat = $tcat"
  #echo "trial = $trial"

  filename_esa="${OUTPATH}time_perfeval_esa_${tcat}${testnum}_trial${trial}_2.txt"
  filename_isa="${OUTPATH}time_perfeval_isa_${tcat}${testnum}_trial${trial}_2.txt"

  #echo ${filename_esa}
  #echo ${filename_isa}
  #echo ${aPath}
  #echo ${oPath}

  cd "${SRCPATH}" ;
  ##########
  #  ESA
  ##########
  curr_time1=$(date)
  (time -p ./driver_perfeval_esa.py $aPath $oPath $testnum $tcat $trial) > ${filename_esa} 2>&1 ;
  curr_time2=$(date)
  echo $curr_time1 >> ${filename_esa}
  echo $curr_time2 >> ${filename_esa}

  ##########
  #  ISA
  ##########
  curr_time3=$(date)
  (time -p ./driver_perfeval_isa.py $aPath $oPath $testnum $tcat $trial) > ${filename_isa} 2>&1 ;
  curr_time4=$(date)
  echo $curr_time3 >> ${filename_isa}
  echo $curr_time4 >> ${filename_isa}
}

##################################
#         testSuite
##################################
# 1 = ans path
# 2 = onto path
# 3 = testNum
# 4 = test category = ans | onto
function testSuite
{
  aPath=$1
  oPath=$2
  testnum=$3
  tcat=$4
  
  #echo "aPath = $aPath"
  #echo "oPath = $oPath"
  #echo "testnum = $testnum"
  #echo "tcat = $tcat"
  #echo "trial = $trial"
 
  for i in `seq 1 32`;
  do
    echo "trial = $i"
    testCall $aPath $oPath $testnum $tcat $i
  done
}

##############################
#   MAIN THREAD OF EXECUTION
##############################
echo ""
echo "--------------------------------------------"
echo "... Running $0 ..."
echo "--------------------------------------------"
echo ""

EXAMPLEDIR=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "${EXAMPLEDIR}" ;
ANSPATH="${EXAMPLEDIR}/"
ONTOPATH="${EXAMPLEDIR}/"
OUTPATH="${EXAMPLEDIR}/data/"
cd "../.." ;
SRCPATH="$( cd "$(dirname ".")" ; pwd -P )/src/"
cd "${EXAMPLEDIR}" ;

testList=(4)
#testList=(8 16 32 64 128 256)
#testList=(512)
#testList=(1024)

#################
#   onto tests
#################
for i in "${testList[@]}"; do
  echo "onto size: $i"
  testnum=$i
  tcat="onto"

  ansName="ans_base"
  ontoName="onto$testnum"
  version=${1}
  ext=".txt"
  aPath="${ANSPATH}${ansName}${testNum}${ext}"
  oPath="${ONTOPATH}${ontoName}${testNum}${version}${ext}"

  testSuite $aPath $oPath $testnum $tcat
done

#################
#   ans tests
#################
for i in "${testList[@]}"; do
  echo "ans size: $i"
  testnum=$i
  tcat="ans"

  ansName="ans$testnum"
  ontoName="onto_base"
  version=${1}
  ext=".txt"
  aPath="${ANSPATH}${ansName}${testNum}${ext}"
  oPath="${ONTOPATH}${ontoName}${testNum}${version}${ext}"

  testSuite $aPath $oPath $testnum $tcat
done

echo ""
echo "--------------------------------------------"
echo "... Exiting $0 ..."
echo "--------------------------------------------"
echo ""
