

LOCATION_INPUT = "Y://Dmitry/original_VCF_FILES/"
INPUT = "sepsis.aa.snps.snp.vcf"


LOCATION_OUTPUT = "//cmh/user/Folders2/dgrigoryev/Genetics/"

OUTPUT = "sepsis.aa.snps.snp_prcssd.txt"



###################################################################

import string

file = open(LOCATION_INPUT + INPUT,'r')#VCF_tst.txt
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')

line = file.readline()
L_in = L_out = 0
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
                  newfile.write("\t% called" + "\tHomo_0" +"\tHetero" + "\tHomo2"\
                                "\t% Homo_0" +"\t% Hetero" + "\t%Homo2\n")
            else:
                  newfile.write(rec[0]+"_"+rec[1] +"\t"+ rec[2]+"\t"+rec[6]) #write SNP ID
                  REF = rec[3]
                  ALT = rec[4]
                  G_lst = []
                  for i in range(9,len(rec)):
                        GT_a = rec[i][0]
                        if GT_a == ".":
                              GT_a = "N"
                        elif GT_a == "0":
                              GT_a = REF
                        else: GT_a = ALT
                        GT_b = rec[i][2]
                        if GT_b == ".":
                              GT_b = "N"
                        elif GT_b == "0":
                              GT_b = REF
                        else: GT_b = ALT
                        lst = []
                        newfile.write("\t"+ GT_a +"/"+ GT_b)
                        if GT_a != "N":
                              lst = [GT_a,GT_b]
                              G_lst = G_lst + [sorted(lst)]

                  REF_ALT_lst =[rec[3],rec[4]]#original bases for a SNP
                  REF_ALT_lst = sorted(REF_ALT_lst)
                  H1 = H12 = H2 = 0
                  for i in range(len(G_lst)):
                        if REF_ALT_lst[0] == G_lst[i][0] and REF_ALT_lst[0] == G_lst[i][1]:#homo of allele 1
                                    H1 = H1 + 1
                        if REF_ALT_lst[0] == G_lst[i][0] and REF_ALT_lst[1] == G_lst[i][1]:#hetero
                                    H12 = H12 + 1
                        if REF_ALT_lst[1] == G_lst[i][0] and REF_ALT_lst[1] == G_lst[i][1]:#homo of allele 2
                                    H2 = H2 + 1

                  L_out = L_out +1                   
                  newfile.write("\t"+ "%.1f" % float((len(G_lst)*100.0)/(len(rec)-9)) +"\t" +\
                                `H1` +"\t"+ `H12` + "\t"+ `H2` +"\t"+\
                                "%.1f" % float((H1*100.0)/len(G_lst)) +"\t" +\
                                "%.1f" % float((H12*100.0)/len(G_lst)) +"\t" +\
                             "%.1f" % float((H2*100.0)/len(G_lst)) + "\n")
      L_in = L_in + 1          
      line = file.readline()

newfile.close()
file.close()
print "END", L_in, L_out

