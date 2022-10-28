# Script to submit a job to calculate the Iq of all the shots of a run
# Argument: "run" run number, "dark" dark run number
# run the job with: $ qsub -v run=690006,dark=690007,tagStart=2312123,tagEnd=13243123 job_all.sh

#!/bin/bash

#PBS -l walltime=10:00:00
#PBS -l select=ncpus=1:mem=32gb
#PBS -q serial
#PBS -N proc-run
#PBS -v run,dark,tagStart,tagEnd

module load SACLA_tool
source /home/maddalena/drop/bin/activate

cd $PBS_O_WORKDIR
echo "JOB_ID           $PBS_JOBID"
echo run $run, with dark $dark
echo from tag $tagStart to tag $tagEnd
echo Job started: `date "+%Y %m %d - %H:%M:%S"`

chmod +X ./process_run.sh
sh process_run.sh $run $dark $tagStart $tagEnd

echo Data reduction ended: `date "+%Y %m %d - %H:%M:%S"`

chmod +X ./IqPhi.py
python IqPhi.py -r $run -s $tagStart -e $tagEnd

echo Job and analysis ended: `date "+%Y %m %d - %H:%M:%S"`
