import random

total = 500
SCT = 0.1
SCD = 0.0

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


for _ in range(0,int(total*SCT)):
    a = Person(True,False)
    set.append(a)

for _ in range(0,int(total*SCD)):
    a = Person(True,True)
    set.append(a)

for _ in range(0,int(total - total*SCD - total*SCT)):
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

    print(generation, len(set), SCT, SCD, sep="\t")