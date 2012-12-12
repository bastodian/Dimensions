#!/usr/bin/env python

import sys

class Convert(object):
    """
        The class Covert provides functions for converting between different 
        Phred quality score encodings and allows retrieving ASCII characters
        corresponding to integer Phred scores.
    """
    def __init__(self):
        # Map to associate raw Phred score to ASCII+33
        self.Phred33 = {
                0:'!',
                1:'"',
                2:'#',
                3:'$',
                4:'%',
                5:'&',
                6:"'",
                7:'(',
                8:')',
                9:'*',
                10:'+',
                11:',',
                12:'-',
                13:'.',
                14:'/',
                15:'0',
                16:'1',
                17:'2',
                18:'3',
                19:'4',
                20:'5',
                21:'6',
                22:'7',
                23:'8',
                24:'9',
                25:':',
                26:';',
                27:'<',
                28:'=',
                29:'>',
                30:'?',
                31:'@',
                32:'A',
                33:'B',
                34:'C',
                35:'D',
                36:'E',
                37:'F',
                38:'G',
                39:'H',
                40:'I',
                41:'J',
                42:'K',
                43:'L',
                44:'M',
                45:'N',
                46:'O',
                47:'P',
                48:'Q',
                49:'R',
                50:'S',
                51:'T',
                52:'U',
                53:'V',
                54:'W',
                55:'X',
                56:'Y',
                57:'Z',
                58:'[',
                59:'\\',
                60:']',
                61:'^',
                62:'_',
                63:'`',
                64:'a',
                65:'b',
                66:'c',
                67:'d',
                68:'e',
                69:'f',
                70:'g',
                71:'h',
                72:'i',
                73:'j',
                74:'k',
                75:'l',
                76:'m',
                77:'n',
                78:'o',
                79:'p',
                80:'q',
                81:'r',
                82:'s',
                83:'t',
                84:'u',
                85:'v',
                86:'w',
                87:'x',
                88:'y',
                89:'z',
                90:'{',
                91:'|',
                92:'}',
                93:'~'
        }

        # Map to associate raw Phred score to ASCII+64
        self.Phred64 = {
                '@':0,
                'A':1,
                'B':2,
                'C':3,
                'D':4,
                'E':5,
                'F':6,
                'G':7,
                'H':8,
                'I':9,
                'J':10,
                'K':11,
                'L':12,
                'M':13,
                'N':14,
                'O':15,
                'P':16,
                'Q':17,
                'R':18,
                'S':19,
                'T':20,
                'U':21,
                'V':22,
                'W':23,
                'X':24,
                'Y':25,
                'Z':26,
                '[':27,
                '\\':28,
                ']':29,
                '^':30,
                '_':31,
                '`':32,
                'a':33,
                'b':34,
                'c':35,
                'd':36,
                'e':37,
                'f':38,
                'g':39,
                'h':40,
                'i':41,
                'j':42,
                'k':43,
                'l':44,
                'm':45,
                'n':46,
                'o':47,
                'p':48,
                'q':49,
                'r':50,
                's':51,
                't':52,
                'u':53,
                'v':54,
                'w':55,
                'x':56,
                'y':57,
                'z':58,
                '{':59,
                '|':60,
                '}':61,
                '~':62
        }

    def Convert(self, QualLine):
        """ Converts Illumina >1.3<1.8 phred encoding to Sanger format. """
        NewQualLine = []
        for Value in QualLine:
            try:
                Key = self.Phred64[Value]
                NewQualLine.append(self.Phred33[Key])
            except KeyError:
                return 'Invalid Format. Are you sure you are trying to convert between the right formats?'
                sys.exit(1)
        return ''.join(NewQualLine)
    
    def PhredToASCII(self, PhredScore):
        """ Takes phred score as argument and returns corresponding ASCII character (Sanger encoding). """
        try:
            return self.Phred33[PhredScore]
        except KeyError:
            return 'Cannot retrieve ASCII character. Valid integers range from 0 to 93!'
            sys.exit(1)

class EndTrim(Convert):
    """ 
        Methods for trimming fastq sequences and corresponding quality scores from 5 and 3 
        prime ends. To instantiate, provide 3 arguments, Nucleotide sequence and correspondig
        quality string in Sanger Phred encoding, and minimum Phred score to accept. 
    """
    def __init__(self, Sequence, Quality, QScore):
        """ Instantiation of the class requires 3 arguments:
        Sequence, Quality line, and minimum Phred score to accept. """
        try:
            assert type(Sequence) == str
            self.Sequence = Sequence
        except KeyError:
            print 'Sequence not a string!'
            sys.exit(1)
        try:
            assert type(Quality) == str
            self.Quality = Quality
        except KeyError:
            print 'Quality line not a string!'
            sys.exit(1)
        try:
            assert 0 <= QScore <= 93 and type(QScore) == int
#            self.Convert = Convert() THIS Works as an alternative to the 2 lines below
#            self.QScore = self.Convert.PhredToASCII(QScore)
            super(EndTrim, self).__init__()
            self.QScore = super(EndTrim, self).PhredToASCII(QScore)
        except KeyError:
            self.QScore = QScore
            print 'Quality score not an integer!'
            sys.exit(1)
        print self.QScore, self.Sequence, self.Quality

    def FivePrime(self):
        """ Trim from the 5 prime end of a sequence. """
        for i in range(len(self.Quality)):
            if self.Quality[i] >= self.QScore:
                break
        self.Sequence = self.Sequence[i:]
        self.Quality = self.Quality[i:]

    def ThreePrime(self):
        """ Trim from the 3 prime end of a sequence. """
        for i in range(len(self.Quality)-1,-1,-1):
            if self.Quality[i] >= self.QScore:
                break
        self.Sequence = self.Sequence[0:i]
        self.Quality = self.Quality[0:i]

    def Retrieve(self):
        """ Retrieve the sequence and quality line. """
        return self.Sequence, self.Quality
    
# TODO implement intercrap and length trim -- what about pairing?

#       Make 5 and 3 prime trimmers check up to 5 base pairs into sequence
