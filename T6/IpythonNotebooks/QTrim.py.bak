import os, sys, glob, subprocess, gzip
sys.path.append(os.path.abspath('../code/python/cutadapt-1.1/cutadapt/scripts/'))
import cutadapt
sys.path.append('../code/python/')
import PhredTools

# DEBUG
import time

"""
RawDataDir is the path to the folders containing the raw read files. If run from the shell
it will prompt for the path; if run in ipython notebook the path has to be changed accordingly
in the variable assignment below.
"""
#try:
#    RawDataDir = raw_input('Type in path to raw data. Path must end in directory named RawData!:\n\n')
#except Exception:
RawDataDir = ('/home/bastodian/Dropbox/github/Dimensions/T6/test/RawData/')

"""
Create a sorted list of files to process
"""
#Iterate though the reference data files
#RawReads = [file for file in glob.glob('%s%s' % (RawDataDir, 'D[CN][1-8]0*/*'))]

# Iterate through all read-sets
RawReads = [file for file in glob.glob('%s%s' % (RawDataDir, 'D[CN][1-8]*/*'))]
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
        print Fwd, '\n', Rev
        # Create the directory to write trimmed read files into
        OutDir = '/'.join(Fwd.split('/')[:-1]).replace("RawData", "TrimmedData")
        try:
            os.makedirs(OutDir)
        except Exception:
            pass
        # Start cutadapt as two separate subprocesses for Fwd and Rev
        cmd1 = '%s%s%s' % (str0, Fwd, str1)
        print cmd1
        process0 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
        cmd2 = '%s%s%s' % (str2, Rev, str3)
        print cmd2
        process1 = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
    else:
        sys.exit('Files paired incorrectly... Quitting')
    
    # Open a gzipped file for storing the trimmed reads
    OutFile0 = '%s%s' % (Fwd.rstrip("fq.gz").replace("RawData", "TrimmedData"), '.trimmed.fq.gz')
    OutFile1 = '%s%s' % (Rev.rstrip("fq.gz").replace("RawData", "TrimmedData"), '.trimmed.fq.gz')
    print OutFile0, '\n', OutFile1
    with gzip.open(OutFile0, 'wb') as TrimOut0:
        with gzip.open(OutFile1, 'wb') as TrimOut1:
            #Read through each file line by line as passed by cutadapt to stdout
            while True:
                # Retrieve output from cutadapt
                Header0 = process0.stdout.readline().strip()
                if len(Header0) == 0:
                    break
                else:
                    Seq0 = process0.stdout.readline().strip()
                    Spacer0 = process0.stdout.readline().strip()
                    Qual0 = process0.stdout.readline().strip()
                    NewQual0 = '%s' % Convert.Convert(Qual0)
                    sys.stderr.write('Fwd: ' + Header0 + '\n')

                    Header1 = process1.stdout.readline().strip()
                    Seq1 = process1.stdout.readline().strip()
                    Spacer1 = process1.stdout.readline().strip()
                    Qual1 = process1.stdout.readline().strip()
                    NewQual1 = '%s' % Convert.Convert(Qual1)
                    sys.stderr.write('Rev: ' + Header1 + '\n')

                    # Trim the fwd reads using PhreadTools
                    Trim0 = PhredTools.EndTrim(Seq0, NewQual0, 20)
                    Trim0.FivePrime(15)
                    Trim0.ThreePrime(15)
                    Trim0.IntraTrim(5)
                    Trim0.MinLength(45)
                    
                    # Verify that we received a sequence; if yes move on to reverse reads
                    if None in Trim0.Retrieve():
                        sys.stderr.write('Empty Sequence 1' + '\n')
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
                            sys.stderr.write('Out0: %s\n' % (Header0))
                            sys.stderr.write('Out1: %s\n\n' % (Header1))
                        else:
                            sys.stderr.write("Empty Sequence 2" + "\n")
                            continue
