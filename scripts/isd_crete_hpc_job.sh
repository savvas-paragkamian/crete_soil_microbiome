#!/bin/bash -l

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --mem=40G
#SBATCH --job-name="isd-2016-test-pema"
#SBATCH --mail-user=s.paragkamian@hcmr.gr
#SBATCH --output=my_pema_job.output
#SBATCH --requeue

module purge # unloads all previous loads

module load singularity/3.7.1 #loads singularity

singularity run -B /home1/s.paragkamian/isd-crete/:/mnt/analysis /mnt/big/containers/singularity/pema_v.2.1.4.sif

module unload singularity/3.7.1 #unloads singularity
