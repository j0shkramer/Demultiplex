#!/usr/bin/env python

import argparse
import numpy as np
import matplotlib.pyplot as plt
import gzip

def get_args():
    parser = argparse.ArgumentParser(description="A program to analyze the quality scores of a FASTQ file at each position")
    parser.add_argument("-f", "--file", help="FASTQ file")
    parser.add_argument("-k", "--read_size", help="Size of the reads", type=int)
    return parser.parse_args()

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score for phred+33 encoding'''
    return ord(letter) - 33

args = get_args()

qc_score_per_pos_total = np.zeros(args.read_size, dtype=float) # np array to hold the total quality score of every base at that position
qc_score_per_pos_avg = np.zeros(args.read_size, dtype=float) # np array to hold the avg quality score of every base at that position

# take the FQ file, iterate over each quality score line, summate each converted value of each quality score at each position
with gzip.open(args.file, "rt") as fq:
    num_lines: int = 0
    for line in fq:
        num_lines += 1
        if num_lines % 4 == 0:
            curr_base = 0
            curr_qc_scores = line.strip()
            for ascii_score in curr_qc_scores:
                qc_score_per_pos_total[curr_base] += convert_phred(ascii_score)
                curr_base += 1

# the number of records in the FASTQ file
total_records = num_lines / 4

# find the average qc at each position
for idx in range(0, args.read_size):
    qc_score_per_pos_avg[idx] = qc_score_per_pos_total[idx] / total_records

# plot
plt.bar(range(args.read_size), qc_score_per_pos_avg, color='skyblue', edgecolor='black')
plt.xlim(0,args.read_size - 1)
plt.xlabel("Base Position (0 indexed)")
plt.ylabel("Average Quality Score")
plt.title(f'Avg Quality Score Per Base Position in {args.file}')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(f'{args.file}.png')