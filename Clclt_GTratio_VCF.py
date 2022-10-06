
import string
file = open("Y://Dmitry/original_VCF_FILES/control.aa.snps.snp.vcf",'r')#VCF_tst.txt
newfile = open("//cmh/user/Folders2/dgrigoryev/Genetics/control.aa.snps.snp_prcssd.vcf",'w')

line = file.readline()

while line != "":
      rec = string.split(line,"\t")
      
      if rec[0][1] == "#":
            line = file.readline()
            continue
      else:          
            if rec[0][0] == "#": # Title line
                  newfile.write("SNP ID") #write SNP ID instead of just ID, which will convert output to SYLK format
                  for i in range(9,len(rec),2):
                        Smpl_ID = string.split(rec[i],".")
                        newfile.write("\t"+ Smpl_ID[0])
                  newfile.write("\n")
            else:
                  newfile.write(rec[2]) #write SNP ID
                  REF = rec[3]
                  ALT = rec[4]
                  for i in range(9,len(rec),2):
                        print "GTA", GT_a
                        if len(rec[i]) > 5:
                              GT_a = rec[i][1]
                              GT_b = rec[i][3]   
                        elif len(rec[i+1]) > 5:                              
                              GT_a = rec[i+1][1]
                              GT_b = rec[i+1][3]           
                        else:
                              newfile.write("\tN/N") # No call
                              if i+1 == len(rec):
                                   newfile.write("\n")  
                              continue
                        print "REC", rec, GT_a 
                        if int(GT_a) == 0:
                              GT_a = REF
                        else: GT_a = ALT

                        if int(GT_b) == 0:
                              GT_b = REF
                        else: GT_b = ALT
                        newfile.write("\t"+ GT_a +"/"+ GT_b)                   
                  newfile.write("\n")
      line = file.readline()

newfile.close()
file.close()
print "END"
