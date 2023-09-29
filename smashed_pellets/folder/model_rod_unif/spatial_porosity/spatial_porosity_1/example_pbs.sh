#!/bin/bash
#PBS -N test_saw
#PBS -P moose
#PBS -l select=1:ncpus=48:mpiprocs=48
#PBS -l walltime=4:00:00
#PBS -j oe
#PBS -k oe
#PBS -m ae
#PBS -M chiara.genoni@inl.gov

# Example PBS script

date

module load use.moose moose-dev PETSc

#Change to directory with the input file
# This should be the directory that the script was run from
echo $PBS_O_WORKDIR
cd $PBS_O_WORKDIR
#Count number of processors
myprocs=`cat $PBS_NODEFILE | wc -l`
echo $myprocs

#Link log with job log
JOB_NUM=${PBS_JOBID%\.*}
if [ $PBS_O_WORKDIR != $HOME ]
then
ln -s $HOME/$PBS_JOBNAME.o$JOB_NUM $PBS_JOBNAME.o$JOB_NUM
fi

# Run Bison or MOOSE
time mpiexec -n $myprocs ~/projects/moose/modules/combined/combined-opt -i stochastic_tools.i

#End of script
echo "Finishing..."
date

#Remove the link and move the job file
if [ $PBS_O_WORKDIR != $HOME ]
then
rm $PBS_JOBNAME.o$JOB_NUM
mv $HOME/$PBS_JOBNAME.o$JOB_NUM $PBS_JOBNAME.o$JOB_NUM
fi
