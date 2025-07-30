# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here:

[Base-nt-distribution](/python_scripts/base-nt-distribution.py)

[Base-nt-distribution-SLURM](/slurm_scripts/base-nt-plot-slurm.sh)

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | Forward Read | 101 | Phred-33 |
| 1294_S1_L008_R2_001.fastq.gz | Index 1 (i7) | 8 | Phred-33 |
| 1294_S1_L008_R3_001.fastq.gz | Index 2 (i5) | 8 | Phred-33 |
| 1294_S1_L008_R4_001.fastq.gz | Reverse Read | 101 | Phred-33 |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.

![graph1](/plots/R1.fastq.png)

![graph2](/plots/R2.fastq.png)

![graph3](/plots/R3.fastq.png)

![graph4](/plots/R4.fastq.png)

    2. We are using this mRNA-seq data to measure the relative expression of genes across different samples. To ensure accuracy, I chose an average quality score threshold of Q30 for the barcode sequences, which aligns with common industry and academic standards. A base with a quality score of 30 has only a 1 in 1,000 chance of being called incorrectly, making it a reliable cutoff. Since accurate demultiplexing is critical when comparing gene expression between treatment conditions, if you use a lower threshold, it could result in reads being misassigned to the wrong samples. This would obscure biologically meaningful differences between the samples and compromise the interpretation of treatment effects. By using an average Q30 threshold, it minimizes misassignment risk while retaining a sufficient number of high-confidence reads for future analysis.

    3. 7304664 indexes have at least one undetermined (N) base call

        zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | grep "^@" -A 1 | grep -v "^@" | grep "N" | wc -l

        3976613

        zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz | grep "^@" -A 1 | grep -v "^@" | grep "N" | wc -l

        3328051
    
## Part 2
1. Define the problem
2. Describe output
3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement

[Psuedocode](/psuedocode.md)