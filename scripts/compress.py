import os
n_splits=10 # this is the number of file the original file is split into
def get_tags(run):
    name=os.popen(f'module load SACLA_tool; ShowRunInfo -b 3 -r {run}')
    ourstring=name.read()
    ourstring=ourstring.partition('trigger ')[2]
    ourstring=ourstring.partition('\nComment')[0]
    startTag=int(ourstring.partition('-')[0])
    endTag=int(ourstring.partition('-')[2])
    return(startTag,endTag)

tot_tags=endTag-startTag

for i in range(n_splits):
    os.system(f'cd /home/girelli/scripts; qsub -v run={sys.argv[1]},darks={sys.argv[2]},startTag={int(tagStart+tot_tags/n_splits*i)},endTag={int(tagStart+tot_tags/n_splits*i+tot_tags/n_splits)} job_all.sh')
