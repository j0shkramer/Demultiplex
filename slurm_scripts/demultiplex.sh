#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --nodes=1
#SBATCH --time=24:00:00
#SBATCH --output=output_%j.log
#SBATCH --error=error_%j.log

fastqR1="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
fastqR2="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz"
fastqR3="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz"
fastqR4="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"

cd ../python_scripts

/usr/bin/time -v ./demultiplex.py -r1 $fastqR1 -r2 $fastqR2 -r3 $fastqR3 -r4 $fastqR4 -t 5