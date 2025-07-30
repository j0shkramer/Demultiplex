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

# zcat and rm is no longer needed becuse changed python script to gzip.open()

# zcat "$fastqR1" > R1.fastq

# /usr/bin/time -v ./base-nt-distribution.py -f R1.fastq -k 101

# rm R1.fastq

# zcat "$fastqR2" > R2.fastq

# /usr/bin/time -v ./base-nt-distribution.py -f R2.fastq -k 8

# rm R2.fastq

# zcat "$fastqR3" > R3.fastq

# /usr/bin/time -v ./base-nt-distribution.py -f R3.fastq -k 8

# rm R3.fastq

zcat "$fastqR4" > R4.fastq

/usr/bin/time -v ./base-nt-distribution.py -f R4.fastq -k 101

rm R4.fastq