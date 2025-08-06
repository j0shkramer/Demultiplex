### Define the problem

We are given a lane of paired sequencing generated from the 2017 BGMP cohort’s library preps. The goal is to create FASTQ files for the indvidual indexes, indexes that have been swapped, and unknown index pairs. This is so we can figure out the amount of index swapping and undetermined index-pairs, before and after quality filtering of index reads.

### Describe output

The output will be 52 FASTQ files. Each index (24) will have a FASTQ file that matches with its first and second biological read. 
There will also be FASTQ files that store the first and read biological reads for mismatched indexes and indexes that are unknown.

### Steps

- Open all of the Read files at once
- Create a variable that stores the amount of lines you have seen: num_lines
- Create a variable that stores the number of reads that have unknown indexes: unknown_ct
- Create a dict: index_matches_and_swaps[i1-rev_i2] = count
- Create a two lists to store the header, sequence, plus line, and quality scores of the Read1,2,3,4 files: read1_list, read2_list, read3_list, read4_list
- Append the stripped lines to their respective lists
- When num_lines % 4 == 0, you have completed a full record
    - Collect all the headers, sequences, plus lines, quality scores from read2_list, read3_list: header1, seq1, plus1, qc1, header2, seq2, plus2, header2
    - Collect the sequence, and qc scores from read2_list, read3_list: i1, i1_qc, i2, i2_qc
    - Find the average quality scores of the indexes, and see if it falls below the threshold we've set in a bool: threshold
    - Create new variable: header_append = f'{i1}-{rev_i2}'
    - Check if i1, rev_i2 are known indexes or if threshold == True
        - If they are not known or if threshold == False, add open unknown_R1.fastq and increment unknown_ct
            - f'{header1}:{header_append}'
            - f'{seq1}'  
            - f'{plus1}'
            - f'{qc1}'
            - Close file
            - Repeat for unknown_R2.fastq
    - Check if i1, rev_i2 are the same
        - if they are the same, open a their specific file using "f'{i1}_R1.fastq'" and index_matches_and_swaps[header_append] += 1
            - f'{header1}:{header_append}'
            - f'{seq1}'  
            - f'{plus1}'
            - f'{qc1}'
            - Close file
            - Repeat for "f'{rev_i2}_R2.fastq'"
        - if they are mismatching, open the mismatch_R1.fastq and index_matches_and_swaps[header_append] += 1
            - f'{header1}:{header_append}'
            - f'{seq1}'  
            - f'{plus1}'
            - f'{qc1}'
            - Close file
            - Repeat for mismatch_R2.fastq   
    - Clear read1_list, read2_list, read3_list, read4_list
- Print out to terminal how many times each indexes had matches or swaps or were unknown. Perhaps create a graph?


### Pseudocode

    def get_args():
        """Input in the command line that will take the four read files and your quality score threshold"""
        return parser

    def reverse_complement(i2: str) -> str
        """Input the index taken from R3, create its reverse complement so it can be compared to index from R2"""
        return rev_i2
        Input: ATATGGC
        Output: GCCATAT

    def avg_qc_score(qc_scrores: str, len(qc_scores): int) -> float
        """Input the quality scores from the indexes and the length of the index. Convert each and summate ASCII character from its PHRED-33 score, then divide by the length to find the average score"""
        return qc_score_avg
        Input: ABCDE
        Output: 34
    

