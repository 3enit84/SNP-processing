#This script converts .vcf allele calls into alleles itself 
##########################################################################

LOCATION_INPUT = "U:/Exome_Seq/InDel/"
INPUT = "pneumonia.aa.snps.indel.filt.vcf"


LOCATION_OUTPUT = "U:/Exome_Seq/InDel/"

OUTPUT = "pneumonia.aa.snps.indel.alleles.txt"

import string

file = open(LOCATION_INPUT + INPUT,'r')
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')

line = file.readline()
L_in = L_out = 0
ACGT_lst = ['A','C','G','T']
print "START"
while line != "":
      rec = string.split(line,"\t")
      
      if rec[0][1] == "#":
            line = file.readline()
            continue
      else:          
            if rec[0][0] == "#": # Title line
                  L_out = L_out +1
                  newfile.write("SNP_location" + "\tSNP ID" + "\tQC" + "\tREF/ALT") #write SNP ID instead ofjust ID, 
                                                      #which will convert output to SYLK format
                  for i in range(9,len(rec)):
                        Smpl_ID = string.split(rec[i],".")
                        newfile.write("\t"+ string.strip(Smpl_ID[0]))
                  newfile.write("\tRef/Ref" + "\tRef/Alt" +"\tAlt/Alt\t"\
                                + "REF count\t" + "ALT count\n")
            else:
                  newfile.write(rec[0]+"_"+rec[1] +"\t"+ rec[2]+"\t"+rec[6]+ "\t" + rec[3]+"/"+rec[4]) #write SNP ID
                  REF = rec[3]
                  ALT = rec[4]
                  REFcnt = ALTcnt = RR = RA = AA = 0
                  for i in range(9,len(rec)):
                        GT_a = rec[i][0]
                        if GT_a == ".":
                              GT_a = "N"
                        elif GT_a == "0":
                              GT_a = REF
                              REFcnt = REFcnt + 1
                        else:
                              GT_a = ALT
                              ALTcnt = ALTcnt +1
                        GT_b = rec[i][2]
                        if GT_b == ".":
                              GT_b = "N"
                        elif GT_b == "0":
                              GT_b = REF
                              REFcnt = REFcnt + 1
                        else:
                              GT_b = ALT
                              ALTcnt = ALTcnt +1
                        newfile.write("\t"+ GT_a +"/"+ GT_b)
                        if GT_a == REF and GT_b == REF:
                              RR = RR + 1
                        elif (GT_a == REF and GT_b == ALT) or (GT_a == REF and GT_b == ALT):
                              RA = RA + 1
                        elif GT_a == ALT and GT_b == ALT:
                              AA = AA + 1                 
                  newfile.write("\t" + `RR` + "\t" + `RA` + "\t" + `AA` + "\t"\
                                + `REFcnt` + "\t" + `ALTcnt` + "\n")

      line = file.readline()
newfile.close()
file.close()
print "END"

