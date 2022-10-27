# Script to submit a job to calculate the Iq of all the shots of a run
# Argument: "run" run number
# run the job with: $ qsub -v run=690006 job_analysis.sh

#!/bin/bash

#PBS -l walltime=1:00:00
#PBS -l select=ncpus=1
#PBS -M maddalena.bin@fysik.su.se
#PBS -q serial
#PBS -N proc-analysis
#PBS -v run

module load SACLA_tool

source /home/maddalena/drop/bin/activate

cd $PBS_O_WORKDIR
echo "JOB_ID_ANALYSIS           $PBS_JOBID"
echo run $run, with dark $dark
echo Job started: `date "+%Y %m %d - %H:%M:%S"`

chmod +X ./Iq_test.py
python Iq_test.py $run

echo Job ended: `date "+%Y %m %d - %H:%M:%S"`