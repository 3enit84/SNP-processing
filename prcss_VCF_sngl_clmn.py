
import string
file = open("G:/KFU/VCF/\
\
R026.vcf",'r')#VCF_tst.txt
            
newfile = open("G:/KFU/VCF/\
\
R026_prcssd.txt",'w')

line = file.readline()

while line != "":
      rec = string.split(line,"\t")
      
      if rec[0][1] == "#":
            line = file.readline()
            continue
      else:          
            if rec[0][0] == "#": # Title line
                  newfile.write("SNP ID") #write SNP ID instead of just ID, which will convert output to SYLK format
                  for i in range(9,len(rec)):
                        newfile.write("\t"+ string.strip(rec[i]))
                  newfile.write("\n")
            else:
                  newfile.write(rec[2]) #write SNP ID
                  REF = rec[3]
                  ALT = rec[4]
                  for i in range(9,len(rec)):
                        if len(rec[i]) > 5:
                              GT_a = rec[i][1]
                              GT_b = rec[i][3]   
                        else:
                              newfile.write("\tN/N") # No call
                              if i == len(rec):
                                   newfile.write("\n")  
                              continue
                              
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
