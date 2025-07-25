#  July 24th, 2025

### 24 indexed (dual matched) libraries for sequencing. The indexes are:

    -B1	GTAGCGTA    
    -A5	CGATCGAT    
    -C1	GATCAAGG
    -B9	AACAGCGA    
    -C9	TAGCCATG    
    -C3	CGGTAATC
    -B3	CTCTGGAT    
    -C4	TACCGGAT    
    -A11 CTAGCTCA
    -C7	CACTTCAC    
    -B2	GCTACTCT    
    -A1	ACGATCAG
    -B7	TATGGCAC    
    -A3	TGTTCCGT    
    -B4	GTCCTAAG
    -A12 TCGACAAG    
    -C10 TCTTCGAC    
    -A2	ATCATGCG
    -C2	ATCGTGGT    
    -A10 TCGAGAGT    
    -B8	TCGGATTC
    -A7	GATCTTGC    
    -B10 AGAGTCCA    
    -A8	AGGATAGC

### 4 FASTQ files are on Talapas:

/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz
/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz
/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz
/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz

### To find the read length of each FASTQ file:

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz | head -2 | tail -1 | wc
    
    1       1     102

Read length of 101 bases because of new line character 

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz | head -2 | tail -1 | 
wc
    
    1       1     102

Read length of 101 bases because of new line character 

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | head -2 | tail -1 | 
wc
    
    1       1       9

Read length of 8 bases because of new line character 

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz | head -2 | tail -1 | 
wc
    
    1       1       9

Read length of 8 bases because of new line character 

### To determine whether it is Phred-33 or Phred-64 Encoding

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz | grep -A 1 "^+" | grep -v "^-" | grep -v "^+" | grep "<" | head

    #AA<FJ7A
    #A--<AAF
    #AA<<-AA
    #-AAFA-<
    #A<--A<F
    #<AAFFJJ
    #AA<FJJJ
    #AAAFJ<J
    #AAA<FFA
    #AA-<FJJ    

    Phred-66 encoding would not have "<"

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz | grep -A 1 "^+" | gre
p -v "^-" | grep -v "^+" | grep "<" | head

    A#A-<FJJJ<JJJJJJJJJJJJJJJJJFJJJJFFJJFJJJAJJJJ-AJJJJJJJFFJJJJJJFFA-7<AJJJFFAJJJJJF<F--JJJJJJF-A-F7JJJJ
    A#AFFFJFJJFJJJJFJJJJJJJJAJJFJJJJJFJFJ7<FAFJJFJFJJFJFJJJFJAAJJJFJJJJJJJJJJJJJJJAJJJFAJJJJJFFJJJAJJJ<F-
    A#<AAFJFJJJJFJJFJJ7JFJJJFJFAJJ<FF<<JJ<JJ<F<JJFAJJFFFJJJJJJA--77FJ--<<-AA<<AFJJJJJJFJJJFFFJ-<7--7-FFFA
    A#A-FJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFJJFJFJFJJJJJJJJJJFFJJJJJJFJJJJJJJJJJJJJJJJJJFJ<FJJAFJJJF<J7FJJJF
    A#AFF<FJJJJJJJJJJJJJJJJJJFJJJJJJJJJJJJ<JAJJJJJJJJJJJJJJJJJJJFJJJJJJJJJJJJJJJJJJFJJJJJJ-AJJJAJJFJJJFJF
    A#AF<FFJJJFFJJJJJJJJJJJJJJJFJJJJJJJJJFFJJJJJJJJJJJJJJJJJAJAJJJJJFJJFJJJJJJJJJJJJJJ<JFJJJFJJFJFJJJJAJJ
    A#AAFFJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJAJJJJJJJJJJJFJJJ<JJJJJJJJJJJ<JJJJJJJFJ
    A#AAAJJJJJJJJFJJJJFJJJJJFFJJJJJJJJJJJFFJ<JJFJJJJJJJFJJJJJJJJJJFJJJJJJJJJJJJJJJFJJ-AAJJFJJJJJJJJJJJJ7J
    A#AAFJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFJJJJJJJJJJJJJJJJJJJJJJJAJJJJJJJJJJFAAJJJJFJJFJJJJJJJJJJ<JJJFJ
    A#AAAAFJJJJJJJJJJJ<FFJAJJJJJJJJJJJJJJJJJJAJJJJJJJJJJJJJJJJJJJFJJFJFJJJJJJJJJAJJJJFJJJJJJJFJFJJJAJJJJF

    Phred-66 encoding would not have "<"

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | grep -A 1 "^+" | gre
p -v "^-" | grep -v "^+" | grep "<" | head

    #AA<FJJJ
    #AAAFJJ<
    #A<-AAFJ
    #AAAFJJ<
    #AAA<JFF
    #<AAFJFJ
    #<AFFFJF
    #AA--A<-
    #AAA<FAF
    #A-<--A-

    Phred-66 encoding would not have "<"

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz | grep -A 1 "^+" | gre
p -v "^-" | grep -v "^+" | grep "<" | head

    #AAFAFJJ-----F---7-<FA-F<AFFA-JJJ77<FJFJFJJJJJJJJJJAFJFFAJJJJJJJJFJF7-AFFJJ7F7JFJJFJ7FFF--A<A7<-A-7--
    #A-AFFJJFJJJJJJJJJJJJJJJJ<JAJFJJJJF<JFJJJAJJJJJJJJJJJJJJJJJJJFJJJAJJFJJJFJJJF<JJA-JJJ-<AFAF--FF<JAFJF
    #AAFFJJJJJJJJJJJJJJJJJJJJJJJJFJJJJJJJJFJJJJJJJJJJJFJJFJJJFJFJAJAF<7AJF<J--7AA7<FJ----7A-F-77-77------
    #A-7AF----<7---77--7<<<F-7---77F--77-<--7--<-----77<--<-<<<<<-7-7-7-F<<A-7-F-A-7-7------7-----7--77-7
    #AAF-<JFJFF-FJF-FF7<-FA<7AJJJJFJJJFFAAAJFA-A<FFJJJFFJFJJAFF<JJJJJJJJJJJAFJJJ<AJJ7--77A-AAAFAF-J7FJ<F-
    #AAAFJ<JAJAJJJJJJJJJJJAJAJFJJJJJJ-7A7FJJJJFFJJJJ<7FJJJJAJJJ<-FJJJFFJ7FAA<AJAFJJFFFJJJFJFJJ7AFJFJJFA7F
    #AAFF7AJJJJJJJJJJJJJJJJJJJJJJJJJJJJJF<JJJJFJJAJJJJJFJJF7AJFJ77FFJJJJF<FAFJJAAAJJJJJJ<J7F7FJJJJFJAJJFJ
    #AAAFJJJJJJFJJJFJJJJJJJJJJJJJJJJJFJJ<AJJJJJJJJJJJJJJJJJJJJJJFJJFJJJJJJJJJJJJJJJJJJJJJJJJJJJJJFFJJJJJJ
    #AAFFJJJJJJJJJJJJJFJFJFJFJFJJFJAAJJFJ<-FF-77FFFFJJJJFJJJ-F<-A7AJ-FJJJJJJJA-FAAFF7JA7F7AFFAFJJJFA<FJF-
    #AA-AFFJJJJJJJJFJAJ7FJFFJJAJJF<FFFJJFFFJJJFA-AFJJJFJJJJJJJFJJFJJ<FAJJJJJJJJ<JFF-FJAAFFFJ<AJ-FFAJ-FFF-

    Phred-66 encoding would not have "<"


https://support.illumina.com/content/dam/illumina-support/documents/documentation/system_documentation/miseq/indexed-sequencing-overview-guide-15057455-08.pdf 

Dual-Indexing Workflows

    The control software performs Read 1, any index reads, and then Read 2 based on the parameters
    provided for the run in the sample sheet or during run setup.
    For all indexing workflows, the Index 1Read directly follows Read 1. However, for dual-indexing on a
    paired-end flow cell, the rest of the workflow differs:
    • Forward strand—The Index 2 Read occurs before Read 2 resynthesis, so the Index 2 (i5) adapter is
    sequenced on the forward strand.
    • Reverse complement—The Index 2 Read occurs after Read 2 resynthesis, which creates the
    reverse complement of the Index 2 (i5) index adapter sequence.

If the average quality score of the one of the indexes fall below the selected threshold, place it into the unknown file

### Generate a per position distribution of quality scores per FASTQ file

Job ID: 36455367

    zcat "$fastqR1" > R1.fastq

    /usr/bin/time -v ./base-nt-distribution.py -f R1.fastq -k 101

    rm R1.fastq

    Command being timed: "./base-nt-distribution.py -f R1.fastq -k 101"
	User time (seconds): 10034.63
	System time (seconds): 49.96
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 2:48:31
	Maximum resident set size (kbytes): 66828
	Exit status: 0

Job ID: 36455368

    zcat "$fastqR2" > R2.fastq

    /usr/bin/time -v ./base-nt-distribution.py -f R2.fastq -k 8

    rm R2.fastq

    Command being timed: "./base-nt-distribution.py -f R2.fastq -k 8"
	User time (seconds): 1038.67
	System time (seconds): 15.68
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 17:38.08
	Maximum resident set size (kbytes): 69568
	Page size (bytes): 4096
	Exit status: 0

Job ID: 36455369

    zcat "$fastqR3" > R3.fastq

    /usr/bin/time -v ./base-nt-distribution.py -f R3.fastq -k 8

    rm R3.fastq

    Command being timed: "./base-nt-distribution.py -f R3.fastq -k 8"
	User time (seconds): 1027.07
	System time (seconds): 22.54
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 17:33.04
	Maximum resident set size (kbytes): 67528
	Exit status: 0

Job ID: 36455370

    zcat "$fastqR4" > R4.fastq

    /usr/bin/time -v ./base-nt-distribution.py -f R4.fastq -k 101

    rm temp_R4.fastq

    Command being timed: "./base-nt-distribution.py -f R4.fastq -k 101"
	User time (seconds): 10206.63
	System time (seconds): 77.93
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 2:52:01
	Maximum resident set size (kbytes): 66680
	Exit status: 0

# July 25th, 2025

### How many indexes have undetermined (N) base calls? 

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | grep "^@" -A 1 | grep -v "^@" | grep "N" | 
wc -l

    3976613 indexes

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz | grep "^@" -A 1 | grep -v "^@" | grep "N" | 
wc -l

    3328051 indexes