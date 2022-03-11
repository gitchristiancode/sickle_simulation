import random

class Person:
    def __init__(self, a, b):
        self.chrom = [a, b]
    
    def combine(self, a):
        a = random.choice(self.chrom)
        b = random.choice(self.chrom)

        return Person(a, b)

affected = 0
carrier = 0
total = 10000

for i in range(0,total):
    a = Person(True, False)
    b = Person(True, False)
    res = a.combine(b)

    if(res.chrom.count(True) == 2):
        affected += 1

    if(res.chrom.count(True) == 1):
        carrier += 1

print("aff\tcarrier")
print(affected,"\t",carrier)