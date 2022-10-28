import os
import sys
n_splits=10 # this is the number of file the original file is split into
def get_tags(run):
    name=os.popen(f'module load SACLA_tool; ShowRunInfo -b 3 -r {run}')
    ourstring=name.read()
    ourstring=ourstring.partition('trigger ')[2]
    ourstring=ourstring.partition('\nComment')[0]
    startTag=int(ourstring.partition('-')[0])
    endTag=int(ourstring.partition('-')[2])
    return(startTag,endTag)
startTag,endTag=get_tags(sys.argv[1])
tot_tags=endTag-startTag
print(endTag)
print(sys.argv[1])
print(sys.argv[2])

for i in range(n_splits):
    os.system(f'cd /home/girelli/SACLA_2022B8033/scripts/; qsub -v run={sys.argv[1]},dark={sys.argv[2]},tagStart={int(startTag+tot_tags/n_splits*i)},tagEnd={int(startTag+tot_tags/n_splits*i+tot_tags/n_splits)} job_all.sh')
    #print(f'cd /home/girelli/SACLA_2022B8033/scripts/; qsub -v run={sys.argv[1]},dark={sys.argv[2]},tagStart={int(startTag+tot_tags/n_splits*i)},tagEnd={int(startTag+tot_tags/n_splits*i+tot_tags/n_splits)} job_all.sh')
    