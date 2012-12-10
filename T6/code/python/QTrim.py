#!/usr/bin/env python

'''
    Provide QScore in ASCII
'''


class EndTrim(object):
    """ Two functions that trim sequences from the 5 and 3 prime ends. """

    def __init__(self, Sequence, Quality, QScore):
        """ Instantiation of the class requires 3 arguments:
        Sequence, Quality line, and Phred score to be clipped. """
        self.Sequence = Sequence
        self.Quality = Quality
        self.QScore = QScore

    def FivePrime(self):
        """ Trim from the 5 prime end of a sequence. """
        for i in range(len(self.Quality)):
            if self.Quality[i] > self.QScore:
                break
        return self.Sequence[(i-1):], self.Quality[(i-1):]


    def ThreePrime(self):
        """ Trim from the 3 prime end of a sequence. """
        Loc = -1
        for i in range(len(self.Quality)-1,-1,-1):
            if self.Quality[i] > self.QScore:
                Loc = i+1
            break

        return self.Sequence[0:Loc], self.Quality[0:Loc]
