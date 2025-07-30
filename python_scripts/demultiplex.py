#!/usr/bin/env python

import argparse, gzip

def get_args():
    parser = argparse.ArgumentParser(description="A program to take library preps, and determine the number of index-pairs, index-swaps, and unknown indexes after quality filtering of index reads")
    parser.add_argument("-r1", "--read1file", help="FASTQ file for insert")
    parser.add_argument("-r2", "--read2file", help="FASTQ file for i7 indexes")
    parser.add_argument("-r3", "--read3file", help="FASTQ file for i5 indexes")
    parser.add_argument("-r4", "--read4file", help="FASTQ file for insert reverse complement")
    parser.add_argument("-t", "--threshold", help="The average quality score threshold that you want your indexes to be higher than",type=float)
    return parser.parse_args()

args = get_args()

# Counters
mismatched_indexes = 0
unknown_indexes = 0
matched_indexes = 0
index_match_ct: dict[str, int] = {}

# barcode_dict = {
#     "GTAGCGTA": True,
#     "CGATCGAT": True,
#     "GATCAAGG": True,
#     "AACAGCGA": True,
#     "TAGCCATG": True,
#     "CGGTAATC": True,
#     "CTCTGGAT": True,
#     "TACCGGAT": True,
#     "CTAGCTCA": True,
#     "CACTTCAC": True,
#     "GCTACTCT": True,
#     "ACGATCAG": True,
#     "TATGGCAC": True,
#     "TGTTCCGT": True,
#     "GTCCTAAG": True,
#     "TCGACAAG": True,
#     "TCTTCGAC": True,
#     "ATCATGCG": True,
#     "ATCGTGGT": True,
#     "TCGAGAGT": True,
#     "TCGGATTC": True,
#     "GATCTTGC": True,
#     "AGAGTCCA": True,
#     "AGGATAGC": True
# }

barcode_dict = {"ATA": True, "GCC": True}

# Take the barcode, and get the list of R1 and R2 files it corresponds to
barcode_file_dict = {}

# Helper functions

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score for phred+33 encoding'''
    return ord(letter) - 33

def qual_score(qc_scores: str) -> float:
    """Input: Phred scores as a string
    Function: Iterates over the string and converts each ASCII character into its quality score
    Output: Average phred score of the entire string"""
    score_sum = 0
    for char in qc_scores:
        score_sum += convert_phred(char)
    return score_sum / len(qc_scores)

def DNA_reverse_complement(DNA_seq: str) -> str:
    """Takes the reverse complement of the inputed DNA sequence"""
    reverse_complement = ""
    DNA_upper = DNA_seq.upper()
    DNA_upper = DNA_upper[::-1]
    for base in DNA_upper:
        if base == "A":
            reverse_complement += "T"
        elif base == "T":
            reverse_complement += "A"
        elif base == "G":
            reverse_complement += "C"
        elif base == "C":
            reverse_complement += "G"
        elif base == "N":
            reverse_complement += "N"
    return reverse_complement

def write_to_file(file_name, header_append, header, seq, plus, qcs):
    file_name.write(f'{header}:{header_append}\n')
    file_name.write(f'{seq}\n')
    file_name.write(f'{plus}\n')
    file_name.write(f'{qcs}\n')


# Create the output files

for barcode in barcode_dict.keys():
    R1_file = open(f'{barcode}_R1.fastq', "w")
    R2_file = open(f'{barcode}_R2.fastq', "w")
    barcode_file_dict[barcode] = (R1_file, R2_file)

barcode_file_dict["unknown"] = (open("unknown_R1.fastq", "w"), open("unknown_R2.fastq", "w"))
barcode_file_dict["hopped"] = (open("hopped_R1.fastq", "w"), open("hopped_R2.fastq", "w"))

print(barcode_file_dict)

# Parse through the input files and send the FASTQ records to the correct output file
# with gzip.open(args.read1file, "r") as fq1, gzip.open(args.read2file, "r") as fq2, gzip.open(args.read3file, "r") as fq3, gzip.open(args.read4file, "r") as fq4:
with open(args.read1file, "r") as fq1, open(args.read2file, "r") as fq2, open(args.read3file, "r") as fq3, open(args.read4file, "r") as fq4:
    num_line: int = 0
    curr_fq1_record = []
    curr_fq2_record = []
    curr_fq3_record = []
    curr_fq4_record = []
    while True:
        num_line += 1
        curr_fq1_line = fq1.readline().strip()
        curr_fq2_line = fq2.readline().strip()
        curr_fq3_line = fq3.readline().strip()
        curr_fq4_line = fq4.readline().strip()
        if curr_fq1_line == "" and curr_fq2_line == "" and curr_fq3_line == "" and curr_fq4_line == "":
            break
        else:
            curr_fq1_record.append(curr_fq1_line)
            curr_fq2_record.append(curr_fq2_line)
            curr_fq3_record.append(curr_fq3_line)
            curr_fq4_record.append(curr_fq4_line)
        # you have a complete record
        if num_line % 4 == 0:  
            r1_header, r1_seq, r1_plus, r1_qc = curr_fq1_record
            r2_header, r2_seq, r2_plus, r2_qc = curr_fq2_record
            r3_header, r3_seq, r3_plus, r3_qc = curr_fq3_record
            r4_header, r4_seq, r4_plus, r4_qc = curr_fq4_record
            # Need to find the reverse complement of the 2nd index to compare to the 1st index
            r3_seq_rv_com = DNA_reverse_complement(r3_seq)
            # Need to find the average quality scores of the indexes to see if it below the threshold
            r2_avg_qc = qual_score(r2_qc)
            r3_avg_qc = qual_score(r3_qc)
            append_to_header = f'{r2_seq}-{r3_seq_rv_com}'
            # unknown indexes or one of the average quality scores of the index is below the set threshold
            if r2_seq not in barcode_dict.keys() or r3_seq_rv_com not in barcode_dict.keys() or r2_avg_qc < args.threshold or r3_avg_qc < args.threshold:
                unknown_indexes += 1
                R1_file, R2_file = barcode_file_dict["unknown"]
                write_to_file(R1_file, append_to_header, r1_header, r1_seq, r1_plus, r1_qc)
                write_to_file(R2_file, append_to_header, r4_header, r4_seq, r4_plus, r4_qc)
            # known indexes that are mismatched
            elif r2_seq != r3_seq_rv_com:
                mismatched_indexes += 1
                if append_to_header in index_match_ct.keys():
                    index_match_ct[append_to_header] += 1
                else:
                    index_match_ct[append_to_header] = 1
                R1_file, R2_file = barcode_file_dict["hopped"]
                write_to_file(R1_file, append_to_header, r1_header, r1_seq, r1_plus, r1_qc)
                write_to_file(R2_file, append_to_header, r4_header, r4_seq, r4_plus, r4_qc)
            # known indexes that are matched
            elif r2_seq == r3_seq_rv_com:
                matched_indexes += 1
                if append_to_header in index_match_ct.keys():
                    index_match_ct[append_to_header] += 1
                else:
                    index_match_ct[append_to_header] = 1
                write_to_file(R1_file, append_to_header, r1_header, r1_seq, r1_plus, r1_qc)
                write_to_file(R2_file, append_to_header, r4_header, r4_seq, r4_plus, r4_qc)
            curr_fq1_record.clear()
            curr_fq2_record.clear()
            curr_fq3_record.clear()
            curr_fq4_record.clear()


# Close the output files

for barcode in barcode_file_dict.keys():
    r1, r2 = barcode_file_dict[barcode]
    r1.close()
    r2.close()


print(f'Matched Index Count: {matched_indexes}')
print(f'Mismatched Index Count: {mismatched_indexes}')
print(f'Unknown Index Count: {unknown_indexes}')

print(index_match_ct)