# Script to convert the data of a run to h5 file
# Argument: "run" run number, "dark" dark run number
# run the job with: $ qsub -v run=690006,dark=690007 job_run.sh

#!/bin/bash

#PBS -l walltime=1:00:00
#PBS -l select=ncpus=1:mem=4gb
#PBS -M maddalena.bin@fysik.su.se
#PBS -q serial
#PBS -N proc-run
#PBS -v run,dark

module load SACLA_tool

cd $PBS_O_WORKDIR
echo "JOB_ID           $PBS_JOBID"
echo run $run, with dark $dark
echo Job started: `date "+%Y %m %d - %H:%M:%S"`

chmod +X ./process_run.sh
sh process_run.sh $run $dark

echo Job ended: `date "+%Y %m %d - %H:%M:%S"`
