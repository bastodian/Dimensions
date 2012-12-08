Analysis of final time point of experiment (T6)
===============================================

Overview
--------

We received libraries from 200 samples for the analysis of the final timepoint
of the experiment. Scripts, programs, and modules used during the analysis can be 
found in the code folder, while log files are in the logs folder and linked to 
in this documentation.

Initial QC
----------

The quality of all libraries was assessed using FASTQC. IMPORTANT: the libraries follow
the old Illumina encoding with a Phred ASCII +64 offset rather than standard Sanger +33 
encoding; I will address this by converting the qual lines in the fastq files.

Number of sequences in all libraries were counted using the following command:

```bash
for file in /mnt/pond/BGI/T6/RawData/D[CN]*/*fq.gz
do 
    echo $file | sed 's/\/mnt\/pond\/BGIhdd\/F12FPCUSAT0183_ALGjhnT\/Data\///g'
    gunzip -c $file |  grep -c 'FC'
done >> NumSeqs.raw 
```

Min, Max, and Average of library sizes was calculated. 

```bash
perl -pe 's/gz\n/gz\t/g' NumSeqs.raw |\
awk 'NR == 1 { max=$2; min=$1; sum=0 }\
{ if ($2>max) max=$2; if ($2<min) min=$2; sum+=$2;}\
END {printf "Min: %d\tMax: %d\tAverage: %f\n", min, max, sum/NR}'
```
These stats can be found [here](https://github.com/bastodian/Dimensions/blob/master/T6/logs/NumSeqs.txt)



I was interested to see where the adapters/primers in the libraries are located
in each read. I did a simple grep search for this purpose.

```bash
: <<'!'
    This script looks for the first part of the indexed Illumina adapter and
    and counts the number of its occurrence in the reads file.

    In addition the number of occurrences of the adapter at the beginning or
    the end of a read are counted.

    This assumes exact matches.
!

for file in /mnt/pond/BGIhdd/F12FPCUSAT0183_ALGjhnT/Data/D[CN]*/*1.fq.gz
do 
    echo $file | sed 's/\/mnt\/pond\/BGIhdd\/F12FPCUSAT0183_ALGjhnT\/Data\///g'
    gunzip -c $file | grep -c 'GATCGGAAGAGCACACGTCTGAACTCCAGTCAC'
    gunzip -c $file | grep -c '^GATCGGAAGAGCACACGTCTGAACTCCAGTCAC'
    gunzip -c $file | grep -c 'GATCGGAAGAGCACACGTCTGAACTCCAGTCAC$'
done
```

The following sequences were searched for:
    
    In Paired End member 1 (in our data files ending in 1.fq.gz):
    tag5prime = 'GATCGGAAGAGCACACGTCTGAACTCCAGTCAC - INDEX - ATCTCGTATGCCGTCTTCTGCTTG'  
    tag3prime = 'AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT'

    In Paired End member 2 (in our data files ending in 2.fq.gz):
    tag5prime = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'  
    tag3prime = 'CAAGCAGAAGACGGCATACGAGAT - INDEX - GTGACTGGAGTTCAGACGTGTGCTCTTCCGATC'

The results of this were somewhat surprising in that I could find the adapter sequences in
the data we received in batch 1 (the test batch), but not in most (all?) of the remaining
libraries. My assumption is that BGI removed the adapters in a first pass QC step for
batch 2. Nonetheless, the orientation of the adapters/primers I found corresponds to my
expetation above. This should allow me to use cutadapt with these target sequences.

In addition, I was interested in figuring out what the sequence of the index used by
BGI for multiplexing was, so that I could include that sequence in downstream clean ups
of the data. From previous work with BGI data I knew to expect an 8-mer rather than the 
standard Illumina 6-mer. I could only find adapter and primer sequences in the test batch 
of 8 samples we sequenced prior to the remainder of the batch for T6.

The following code was used to retrieve the adapter sequence:

```bash
: <<'!'
    This script searches for the 5 prime part of the Truseq index adapter and then 
    cuts the 8 characters following it out of the seqeunce. I keep the most abundant
    8-mer. Not pretty but seems to work...

    FindIndex.sh PATH/TO/DATA
!

INPATH=$1

for file in ${INPATH}D[CN]*/*1.fq.gz
do
    echo $file
    gunzip -c $file |\
    awk '{for(i=1;i<=NF;i++){if($i~/^GATCGGAAGAGCACACGTCTGAACTCCAGTCAC/){print $i}}}' |\
    cut -c34-41 |\
    sort |\
    uniq -c |\
    sort -r |\
    head -n 1
done
```

This yields the following 8 index sequences:

* ACAGTGAT
* ATCACGAT
* GCCAATAT
* GTCCGCAC
* GTGAAACG
* GTGGCCTT
* GTTTCGGA
* TGACCAAT

QC: removal of poor quality bases and contaminants
--------------------------------------------------

Notebook:
* [IpythonNotebooks/FastQ_Filtering.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/bastodian/Dimensions/master/T6/IpythonNotebooks/FastQ_Filtering.ipynb)
