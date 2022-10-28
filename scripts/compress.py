# to run this:
#$ python compress.py -r run -d dark -n 10

import os
import sys
import argparse

# - parsers
parser = argparse.ArgumentParser(description='Compress the run and analyse')
parser.add_argument('-r', '--run', type=str, required=True, help='run number to process')
parser.add_argument('-d', '--dark', type=str, required=True, help='dark run number for the run')
parser.add_argument('-n', '--nsplits', type=int, required=False, default=10, help='number of jobs to submit')

args = parser.parse_args()
run = args.run
dark = args.dark
n_splits = args.nsplits
# n_splits = 10

def get_tags(run):
    name = os.popen(f'module load SACLA_tool; ShowRunInfo -b 3 -r {run}')
    ourstring = name.read()
    ourstring = ourstring.partition('trigger ')[2]
    ourstring = ourstring.partition('\nComment')[0]
    startTag = int(ourstring.partition('-')[0])
    endTag = int(ourstring.partition('-')[2])
    return (startTag, endTag)

startTag, endTag = get_tags(run)
tot_tags = endTag - startTag
print("End tag: ", endTag)
print("Run: ", run)
print("Dark", dark)

for i in range(n_splits):
    os.system(f'qsub -v run={run},dark={dark},tagStart={int(startTag+tot_tags/n_splits*i)},tagEnd={int(startTag+tot_tags/n_splits*i+tot_tags/n_splits)} job_all.sh')