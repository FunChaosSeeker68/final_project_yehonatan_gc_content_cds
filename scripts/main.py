dna_seq_ecoli=open('data/ecoli.fna','r')
output_ecoli=open('results/output_ecoli.txt','w')
dna_seq_yeast=open('data/data_yeast.fna','r')
output_yeast=open('results/output_yeast.txt','w')
dna_seq_homosapions=open('data/homosapians.fa','r')
output_homosapions=open('results/output_homosapions.txt','w')
metiral=""
Length=0

output_ecoli.write("heder\tLength\tGC_amont\tCG_precent\n")
output_yeast.write("heder\tLength\tGC_amont\tCG_precent\n")
output_homosapions.write("heder\tLength\tGC_amont\tCG_precent\n")

cont=0
def rearol_ecoli (metiral,heder):
    GC_cont=0
    Length=len(metiral)
    if Length >300:
        part=heder.split("[")
        output_ecoli.write(str(part[0])+"\t")
        output_ecoli.write(str(Length)+"\t")
        for letter in metiral:
            if letter=="C" or letter=="G":
                GC_cont=GC_cont+1
        output_ecoli.write(str(GC_cont)+"\t")
        GC_precent=GC_cont*100/Length
        output_ecoli.write(("%.2f %%" % ((GC_precent)))+"\n")

def rearol_yeast (metiral,heder):
    GC_cont=0
    Length=len(metiral)
    if Length >300:
        part=heder.split("[")
        output_yeast.write(str(part[0])+"\t")
        output_yeast.write(str(Length)+"\t")
        for letter in metiral:
            if letter=="C" or letter=="G":
                GC_cont=GC_cont+1
        output_yeast.write(str(GC_cont)+"\t")
        GC_precent=GC_cont*100/Length
        output_yeast.write(("%.2f %%" % ((GC_precent)))+"\n")

def rearol_homosapions (metiral,heder):
    GC_cont=0
    Length=len(metiral)
    if Length >300:
        part=heder.split(":")
        output_homosapions.write(str(part[0])+"\t")
        output_homosapions.write(str(Length)+"\t")
        for letter in metiral:
            if letter=="C" or letter=="G":
                GC_cont=GC_cont+1
        output_homosapions.write(str(GC_cont)+"\t")
        GC_precent=GC_cont*100/Length
        output_homosapions.write(("%.2f %%" % ((GC_precent)))+"\n")


for line in dna_seq_ecoli:
    if cont==0:
        curr_hedder=line
        cont=cont+1
    elif line[0] !=">":
        metiral=metiral+line.rstrip("\n\r")
    else:
        rearol_ecoli(metiral,curr_hedder)
        metiral=""
        curr_hedder=line
rearol_ecoli(metiral,curr_hedder)
cont=0

for line in dna_seq_yeast:
    if cont==0:
        curr_hedder=line
        cont=cont+1
    elif line[0] !=">":
        metiral=metiral+line.rstrip("\n\r")
    else:
        rearol_yeast(metiral,curr_hedder)
        metiral=""
        curr_hedder=line
rearol_yeast(metiral,curr_hedder)
cont=0

for line in dna_seq_homosapions:
    if cont==0:
        curr_hedder=line
        cont=cont+1
    elif line[0] !=">":
        metiral=metiral+line.rstrip("\n\r")
    else:
        rearol_homosapions(metiral,curr_hedder)
        metiral=""
        curr_hedder=line
rearol_homosapions(metiral,curr_hedder)
cont=0