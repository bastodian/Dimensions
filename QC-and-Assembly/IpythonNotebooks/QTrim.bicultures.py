# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Removal of artefacts and low quality nucleotides from Reference Assembly reads
# ------------------------------------------------------------------------------
# 
# * Read sets are searched for contamination by Illumina adapters and primers using cutadapt ver. 1.1
# * Following removal of artefactual sequences, low quality basepairs are removed. (Here, nucleotides with a phred score less than 20 are below the quality threshold.)
# * Both 5 and 3 prime ends of the read are searched for low quality nucleotides and trimmed. After 1st low quality nucleotide is found, the sequence string of 15 nucleotides down-/upstream from that position is evaluated and trimmed if below phred threshold
# * Reads that contain more than 5 nucleotides below phred threshold after 5 and 3 prime trimming are removed
# * Only reads that exceed or are equal to 45 basepairs in length are retained.  # Convert old Illumina quality encoding to Sanger
# * Trimming and pairing of paired reads is performed in one pass. Input and output are compressed (gzip) fastq files to keep storage space needed small
# * To run QTrim change the RawDataDir variable to the directory in which the raw data are stored; trimmed data will be written to TrimmedData in the same directory as RawData
#         
#     ```
#         """ Important parts of the trimming process """
#         Convert.Convert(Qual)
#         # Initialize trimming tools
#         Trim = PhredTools.EndTrim(Seq, NewQual, 20)
#         # Trim 5-3 prime
#         Trim.FivePrime(15)
#         # Trim 3-5 prime
#         Trim.ThreePrime(15)
#         # Remove reads with > 5 poor quality nucleotides
#         Trim.IntraTrim(5)
#         # Remove reads that are < 45 bp long
#         Trim.MinLength(45)
#     ```

# <codecell>

import os, sys, glob, subprocess, gzip
sys.path.append(os.path.abspath('../code/python/cutadapt-1.1/cutadapt/scripts/'))
import cutadapt
sys.path.append(os.path.abspath('../code/python/'))
import PhredTools

"""
RawDataDir is the path to the folders containing the raw read files. If run from the shell
it will prompt for the path; if run in ipython notebook the path has to be changed accordingly
in the variable assignment below.
"""
# EDIT RawData dir to the directory containingthe raw data: dir must be named RawData!
RawDataDir = ('/mnt/pond/BGI/T6/RawData/')

"""
Create a sorted list of files to process
"""
# Iterate though the reference data files
#RawReads = [file for file in glob.glob('%s%s' % (RawDataDir, 'D[CN][1-8]0*/*gz'))]
# Iterate through all read-sets
RawReads = [file for file in glob.glob('%s%s' % (RawDataDir, 'D[CN][1-8][1-8]*/*'))]
RawReads.sort()


"""
Use cutadapt in a sub-process to remove artefactual sequences; low quality nucleotides
are removed using PhredTools
"""
# Create and instance of the Phredscore converter
Convert = PhredTools.Convert()

# Define strings to call cutadapt as a subprocess for fwd reads
str0 = """python -c 'import sys
sys.path.append("/home/bastodian/Dropbox/github/Dimensions/T6/code/python/cutadapt-1.1/cutadapt/scripts/")
import cutadapt
cutadapt.main(["-g", "AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT", "-b", "GATCGGAAGAGCACACGTCTGAACTCCAGTCAC", "-b", "ATCTCGTATGCCGTCTTCTGCTTG", \""""
str1 = """\"])\nsys.stdout.flush()'"""
# Define strings to call cutadapt as a subprocess for rev reads
str2 = """python -c 'import sys
sys.path.append("/home/bastodian/Dropbox/github/Dimensions/T6/code/python/cutadapt-1.1/cutadapt/scripts/")
import cutadapt
cutadapt.main(["-g", "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT", "-b", "CAAGCAGAAGACGGCATACGAGAT", "-b", "GTGACTGGAGTTCAGACGTGTGCTCTTCCGAT", \""""
str3 = """\"])\nsys.stdout.flush()'"""

# Step though the files containing fwd reads
for index in range(0,len(RawReads[:]),2):
    # Pair fwd and reverse read files
    Fwd = RawReads[index]
    Rev = RawReads[index + 1]
    assert '1.fq.gz' in Fwd
    assert '2.fq.gz' in Rev
    
    if Fwd.rstrip('1.fq.gz') == Rev.rstrip('2.fq.gz'):
        sys.stdout.write('Paired...\n\t%s\n\t%s\n' % (Fwd,Rev))
        # Create the directory to write trimmed read files into
        OutDir = '/'.join(Fwd.split('/')[:-1]).replace("RawData", "TrimmedData")
        try:
            os.makedirs(OutDir)
        except Exception:
            pass
        # Start cutadapt as two separate subprocesses for Fwd and Rev
        cmd1 = '%s%s%s' % (str0, Fwd, str1)
        process0 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
        cmd2 = '%s%s%s' % (str2, Rev, str3)
        process1 = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
    else:
        sys.exit('Files paired incorrectly... Quitting')
    
    # Open a gzipped file for storing the trimmed reads
    OutFile0 = '%s%s' % (Fwd.rstrip("fq.gz").replace("RawData", "TrimmedData"), '.trimmed.fq.gz')
    OutFile1 = '%s%s' % (Rev.rstrip("fq.gz").replace("RawData", "TrimmedData"), '.trimmed.fq.gz')
    with gzip.open(OutFile0, 'wb') as TrimOut0:
        with gzip.open(OutFile1, 'wb') as TrimOut1:
            sys.stdout.write('Writing outfiles...\n\t%s\n\t%s\n\n' % (OutFile0,OutFile1))
            # Read through each file line by line as passed by cutadapt to stdout
            while True:
                # Retrieve fwd header from cutadapt; if header empty the file is at its end
                Header0 = process0.stdout.readline().strip()
                if len(Header0) == 0:
                    break
                else:
                    # Retrieve output from cutadapt: fwd
                    Seq0 = process0.stdout.readline().strip()
                    Spacer0 = process0.stdout.readline().strip()
                    Qual0 = process0.stdout.readline().strip()
                    NewQual0 = '%s' % Convert.Convert(Qual0)

                    # Retrieve output from cutadapt: rev
                    Header1 = process1.stdout.readline().strip()
                    Seq1 = process1.stdout.readline().strip()
                    Spacer1 = process1.stdout.readline().strip()
                    Qual1 = process1.stdout.readline().strip()
                    NewQual1 = '%s' % Convert.Convert(Qual1)

                    # Trim the fwd reads using PhreadTools
                    Trim0 = PhredTools.EndTrim(Seq0, NewQual0, 20)
                    Trim0.FivePrime(15)
                    Trim0.ThreePrime(15)
                    Trim0.IntraTrim(5)
                    Trim0.MinLength(45)
                    
                    # Verify that we received a sequence; if yes move on to reverse reads
                    if None in Trim0.Retrieve():
                        continue
                    else:
                        # Trim the fwd reads using PhreadTools
                        Trim1 = PhredTools.EndTrim(Seq1, NewQual1, 20)
                        Trim1.FivePrime(15)
                        Trim1.ThreePrime(15)
                        Trim1.IntraTrim(5)
                        Trim1.MinLength(45)
                        
                        # Make sure that we have a reverse read; if no, move on to net read pair
                        if not None in Trim1.Retrieve():
                            TrimOut0.write('%s\n%s\n%s\n%s\n' % (Header0, Trim0.Retrieve()[0], Spacer0, Trim0.Retrieve()[1]))
                            TrimOut1.write('%s\n%s\n%s\n%s\n' % (Header1, Trim1.Retrieve()[0], Spacer1, Trim1.Retrieve()[1]))
                        else:
                            continue
