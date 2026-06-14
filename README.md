# final_project_yehonatan_gc_content_cds
the way to use the code is vary simple all you need to do is to press the play key but if you want to add more data all you need to do is to add the data to the data folder then go to main.py after that copy the first two lines: 
dna_seq_ecoli=open('data/ecoli.fna','r')
output_ecoli=open('results/output_ecoli.txt','w')
then you need to change the name of data/ecoli.fna to the name of the new data aded but don't get rid of data/ also cange the start to the name of the specese for exsample:
dna_seq_ecoli=open('data/ecoli.fna','r') turns in to dna_seq_flu=open('data/flu.fna','r')
and output_flu=open('results/output_flu.txt','w')
the edited lines will be put above metiral=""

after that you can copy one of the def and rename it for your specese let's use the flu exsample renme it from rearol_ecoli to rearol_flu but rember you also need to change all the output_ecoli.write to the one you set up erlier output_flu.write

after that copy th last for loop and repupuse it 

for line in dna_seq_flu:
    if cont==0:
        curr_hedder=line
        cont=cont+1
    elif line[0] !=">":
        metiral=metiral+line.rstrip("\n\r")
    else:
        rearol_flu(metiral,curr_hedder)
        metiral=""
        curr_hedder=line
rearol_flu(metiral,curr_hedder)
cont=0
remember alwys swap the original rearol to the rearol you use