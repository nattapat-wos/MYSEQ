import re

def countBase(seq, base):
    return seq.count(base)

def gcContent(seq):
    return (countBase(seq, 'G') + countBase(seq, 'C')) / (countBase(seq, 'A') + countBase(seq, 'T') + countBase(seq, 'G') + countBase(seq, 'C'))

def atContent(seq):
    return (countBase(seq, 'A') + countBase(seq, 'T')) / (countBase(seq, 'A') + countBase(seq, 'T') + countBase(seq, 'G') + countBase(seq, 'C'))

def countBasesDict(seq):
    basesM = {}
    for base in seq:
        basesM[base] = basesM.setdefault(base, 0) + 1
    return basesM
