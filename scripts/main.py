dna_seq=open('data/data.fa.fna','r')
output=open('results/output.txt','w')
metiral=""
Length=0
GC_cont=0
output.write("heder\tLength\tGC_amont\tCG_precent\n")

def rearol (metiral,heder):
    part=heder.split("[")
    output.write(part[0]+"\t")
    Length=len(metiral)
    output.write(Length+"\t")
    for letter in metiral:
        if letter=="C" or letter=="G":
            GC_cont=GC_cont+1
    output.write(GC_cont+"\t")
    GC_precent=GC_cont*100/Length
    output.write(GC_precent+"\t")




for line in dna_seq:
    if line[0] !=">":
        metiral=metiral+line.rstrip("\n\r")
    else:
        rearol(metiral,line)
        metiral=""