dna_seq=open('data/data.fa.fna','r')
output=open('results/output.txt','w')
metiral=""
Length=0

output.write("heder\tLength\tGC_amont\tCG_precent\n")
cont=0
def rearol (metiral,heder):
    GC_cont=0
    part=heder.split("[")
    output.write(str(part[0])+"\t")
    Length=len(metiral)
    output.write(str(Length)+"\t")
    for letter in metiral:
        if letter=="C" or letter=="G":
            GC_cont=GC_cont+1
    output.write(str(GC_cont)+"\t")
    GC_precent=GC_cont*100/Length
    output.write(("%.2f %%" % ((GC_precent)))+"\n")




for line in dna_seq:
    if cont==0:
        curr_hedder=line
        cont=cont+1
    elif line[0] !=">":
        metiral=metiral+line.rstrip("\n\r")
    else:
        rearol(metiral,curr_hedder)
        metiral=""
        curr_hedder=line
rearol(metiral,curr_hedder)