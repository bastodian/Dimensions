#!/usr/bin/env python

'''
    Methods for trimming fastq sequences and corresponding quality scores as 
    provided in the string of phred scores.
'''
 
class EndTrim(object):
    """ Two functions that trim sequences from the 5 and 3 prime ends. """

    def __init__(self, Sequence, Quality, QScore):
        """ Instantiation of the class requires 3 arguments:
        Sequence, Quality line, and minimum Phred score to accept. """
        from PhredTools import Convert
        PhredConvert = Convert()
        assert type(Sequence) == str
        self.Sequence = Sequence
        assert type(Quality) == str
        self.Quality = Quality
        assert 0 <= QScore <= 93 and type(QScore) == int
        self.QScore = PhredConvert.ReturnASCII(QScore)

    def FivePrime(self):
        """ Trim from the 5 prime end of a sequence. """
        for i in range(len(self.Quality)):
            if self.Quality[i] >= self.QScore:
                break
        self.Sequence = self.Sequence[(i-1):]
        self.Quality = self.Quality[(i-1):]

    def ThreePrime(self):
        """ Trim from the 3 prime end of a sequence. """
        Loc = -1
        for i in range(len(self.Quality)-1,-1,-1):
            if self.Quality[i] >= self.QScore:
                Loc = i+1
            break
        self.Sequence = self.Sequence[0:Loc]
        self.Quality = self.Quality[0:Loc]

    def Retrieve(self):
        """ Retrieve the sequence and quality line. """
        return self.Sequence, self.Quality
    
# TODO implement intercrap and length trim -- what about pairing?

#    def IntraTrim(self, IntraCrap, MinLength):
#        """ Trims 5-3 prime if the number of bases below Qscore exceeds
#        a user-specified threshold (IntraCrap). """
#        Count = 0
#        Trim = -1
#        for i in range(len(self.Quality)):
#            if self.Quality[i] <= self.QScore:
#                Count += 1
#                if Trim == -1:
#                    Trim = i
#        if Count >= IntraCrap:
#            NewSeq = self.Sequence[:Trim]
#            NewQual = self.Quality[:Trim]
#
#        if len(NewSeq) >= MinLength:
#            return NewSeq, NewQual
