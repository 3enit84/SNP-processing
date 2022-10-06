

LOCATION_INPUT = "Y://Dmitry/original_VCF_FILES/"
INPUT = "control.aa.snps.snp.vcf"


LOCATION_OUTPUT = "//cmh/user/Folders2/dgrigoryev/Genetics/"

OUTPUT = "control.aa.snps.snp_Alleles.txt"



###################################################################

import string

file = open(LOCATION_INPUT + INPUT,'r')#VCF_tst.txt
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')

line = file.readline()
L_in = L_out = 0
ACGT_lst = ['A','C','G','T']
while line != "":
      rec = string.split(line,"\t")
      
      if rec[0][1] == "#":
            line = file.readline()
            continue
      else:          
            if rec[0][0] == "#": # Title line
                  L_out = L_out +1
                  newfile.write("SNP_location" + "\t" + "SNP ID" + "\t" + "QC") #write SNP ID instead ofjust ID, 
                                                      #which will convert output to SYLK format
                  for i in range(9,len(rec)):
                        Smpl_ID = string.split(rec[i],".")
                        newfile.write("\t"+ string.strip(Smpl_ID[0]))
                  newfile.write("\tAA" + "\tCC" +"\tGG" + "\tTT"\
                                "\tA" +"\tC" + "\tG" + "\tT\n")
            else:
                  REF = rec[3]
                  ALT = rec[4]
                  G_lst = []
                  No_call_REF = No_call_ALT = 0
                  for i in range(9,len(rec)):
                        GT_a = rec[i][0]
                        if GT_a == ".":
                              GT_a = "N"
                              No_call_REF = No_call_REF + 1
                        elif GT_a == "0":
                              GT_a = REF
                        else: GT_a = ALT
                        GT_b = rec[i][2]
                        if GT_b == ".":
                              GT_b = "N"
                              No_call_ALT = No_call_ALT + 1
                        elif GT_b == "0":
                              GT_b = REF
                        else: GT_b = ALT
                        lst = []
                        G_lst = G_lst + [GT_a,GT_b]
                  
                  if float(No_call_REF)/(len(G_lst)/2) < 0.2:#greater than 80% of SNPs are called
                        newfile.write(rec[0]+"_"+rec[1] +"\t"+ rec[2]+"\t"+rec[6]) #write SNP ID
                        for i in range(0,len(G_lst),2):
                              newfile.write("\t" + G_lst[i] + "/" + G_lst[i+1])
                        Nuc_lst = [0,0,0,0]
                        for i in range(len(G_lst)): #count allels
                              for j in range(len(Nuc_lst)):
                                    if G_lst[i] == ACGT_lst[j]:#check for nucleotide
                                          Nuc_lst[j] = Nuc_lst[j] + 1
                                          break
                                    
                        Hyp_lst = [0,0,0,0]
                        for i in range(0,len(G_lst),2): #count genotype, every two entries
                              if G_lst[i] == G_lst[i+1]:#check for homozygosity
                                    for j in range(len(Hyp_lst)):
                                          if G_lst[i] == ACGT_lst[j]:#check for nucleotide
                                                Hyp_lst[j] = Hyp_lst[j] + 1
                                                break                
                        for i in range(4):                 
                              newfile.write("\t" + `Hyp_lst[i]`)
                        for i in range(4):                 
                              newfile.write("\t" + `Nuc_lst[i]`)
                        newfile.write("\n")
                  

            
      line = file.readline()
newfile.close()
file.close()
print "END"

