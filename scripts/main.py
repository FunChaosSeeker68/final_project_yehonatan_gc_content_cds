dna_seq=open('data/data.fa.fna','r')
metiral=""
langh=0
GC_cont=0
for line in dna_seq:
    if line[0] !=">":
        metiral=metiral+line.rstrip()
    else:
        langh=len(metiral)
        for letter in metiral:
            if letter=="C" or letter=="G":
                GC_cont=GC_cont+1