#!/usr/bin/env python

import cutadapt

def PhredConvert(phredscore)
    




fwd:

# 5 prime universal Truseq adaptor
Universal = 'AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT'
# 3 prime indexed adapter
Index = 'GATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG'

# Reverse Complement of universal Truseq Adaptor
UniversalRevComp = 'AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT'
# Reverse Complement of Universal Truseq Adaptor
IndexRevComp = 'CAAGCAGAAGACGGCATACGAGATNNNNNNGTGACTGGAGTTCAGACGTGTGCTCTTCCGATC'

Phred64 = ['@','A','B','C','D','E','F','G','H','I','J','K','L','M','N',\
            'O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']',\
            '^','_','`','a','b','c','d','e','f','g','h']

# Maps Phred 64 offset to Phred 33
Phred64toPhred33 = {'@':'!','A':'"','B':'#','C':'$','D':'%','E':'&','F':"'",'G':'(','H':')','I':'*','J':'+','K':',','L':'-','M':'.','N':'/','O':'0','P':'1','Q':'2','R':'3','S':'4','T':'5','U':'6','V':'7','W':'8','X':'9','Y':':','Z':';','[':'<',"\\":'=',']':'>','^':'?','_':'@','`':'A','a':'B','b':'C','c':'D','d':'E','e':'F','f':'G','g':'H','h':'I'}
# Map to associate raw Phred score to ASCII+33
PhredToPhred33Map = {0:'!',1:'"',2:'#',3:'$',4:'%',5:'&',6:"'",7:'(',8:')',9:'*',10:'+',11:',',12:'-',13:'.',14:'/',15:'0',16:'1',17:'2',18:'3',19:'4',20:'5',21:'6',22:'7',23:'8',24:'9',25:':',26:';',27:'<',28:'=',29:'>',30:'?',31:'@',32:'A',33:'B',34:'C',35:'D',36:'E',37:'F',38:'G',39:'H',40:'I'}
