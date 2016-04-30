# script for retrieing execution time in seconds per test.
# run command:
# bash getData.sh esa onto 4 i["_2"]

EXAMPLEDIR=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
DATAPATH="${EXAMPLEDIR}/data"

for i in `seq 1 32`; do
  f="${DATAPATH}/time_perfeval_${1}_${2}${3}_trial${i}${4}.txt"
  tail -4 $f | head -1 | cut -d" " -f2
done
