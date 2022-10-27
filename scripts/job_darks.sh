# Script to convert the data of a dark run to h5 file
# Argument: "run" number of the dark run
# run the job with: $ qsub -v run=690006 job_dark.sh

#!/bin/bash

#PBS -l walltime=1:00:00
#PBS -l select=ncpus=1:mem=4gb
#PBS -M maddalena.bin@fysik.su.se
#PBS -q serial
#PBS -N proc-dark
#PBS -v run

module load SACLA_tool

cd $PBS_O_WORKDIR
echo "JOB_ID           $PBS_JOBID"
echo dark run $run
echo Job started: `date "+%Y %m %d - %H:%M:%S"`

chmod +X ./process_darks.sh
sh process_darks.sh $run

echo Job ended: `date "+%Y %m %d - %H:%M:%S"`