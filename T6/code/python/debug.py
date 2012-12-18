#!/us/bin/env python

from PhredTools import EndTrim

a = 'NGGACAAACCCGGGGGTTGTTACCCCGGCTATGTCGCCTGGCCGACCGAGGAATGAAGGGCGCTCTCTGAGTCCTCCGGGAACTGCGTCC'
#b = """!"#$!!!$%&'$"""
b = """#1:ADDDDFFFDFFIFF<F;;FFFFI>EEDD>A6@@??>;?B(';@BBBB59?@B3@@BB7@B-8?AABAB(:A(:>>BBB-8:>@####"""
c = 20

trim = EndTrim(a,b,c)
#trim.FivePrime(5)
trim.ThreePrime(5)
#trim.IntraTrim(30)
#trim.MinLength(2)

if None in trim.Retrieve():
    print trim.Retrieve()
else:
    print '\n'.join(trim.Retrieve())
