import random
import numpy as np

total = 500

set = []
pairs = []

def pairSet():
    random.shuffle(set)
    global pairs
    pairs = []

    for i in range(0,len(set),2):
        if i+1 < len(set):
            pairs.append([set[i], set[i+1]])



class Person:
    def __init__(self, a, b):
        self.chrom = [a, b]
        self.a = 0

    def combine(self, other):
        self.a += 1
        other.a += 1

        a = random.choice(self.chrom)
        b = random.choice(other.chrom)

        return Person(a, b)


for SC in np.arange(0,1.05,0.05):
    set=[]
    pairs=[]

    for _ in range(0,int(total*SC)):
        a = Person(True,False) # One True for SCT block, Two True for SCD block
        set.append(a)

    for _ in range(0,int(total - total*SC)):
        a = Person(False,False)
        set.append(a)

    for generation in range(0,100):
        newSet = []
        pairSet()
        for pair in pairs:
            for i in range(0,random.randint(1,3)):
                newSet.append(pair[0].combine(pair[1]))
        
        set = newSet

    SCT = len([person for person in set if person.chrom.count(True) == 1])
    SCD = len([person for person in set if person.chrom.count(True) == 2])

    print(len(set), round(SCT/len(set),3), round(SCD/len(set),3), sep="\t")