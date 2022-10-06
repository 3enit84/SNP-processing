#This script converts .vcf allele calls into alleles itself 
##########################################################################

LOCATION_INPUT = "U:/Exome_Seq/InDel/"
INPUT = "Indel_cmmn_all.txt"


LOCATION_OUTPUT = "U:/Exome_Seq/InDel/"

OUTPUT_1 = "Indel_cmmn_Maj_Min_unidir.txt"
OUTPUT_2 = "Indel_cmmn_MisMatch_multidir.txt"

import string

file = open(LOCATION_INPUT + INPUT,'r')
newfile = open(LOCATION_OUTPUT + OUTPUT_1,'w')
MMfile = open(LOCATION_OUTPUT + OUTPUT_2,'w')

line = file.readline()
newfile.write(line)#title
line = file.readline()
print "START"
while line != "":
      rec = string.split(line,"\t")
      newfile.write(rec[0]+ "\t" + rec[1])
      A = string.split(rec[2],"/")
      if int(rec[3]) >= int(rec[4]):
            M = A[0]#Major allele
            m = A[1]#minor allele
            newfile.write("\t" + rec[2]+ "\t" + rec[3] + "\t" + rec[4])#white control
            for i in range(5,len(rec),3): #work with every 3 records
                  A = string.split(rec[i],"/")
                  if A[0] == M and A[1] == m:
                        newfile.write("\t" + rec[i]+ "\t" + rec[i+1] + "\t" + string.strip(rec[i+2]))#sample
                  else:
                        newfile.write("\t" + rec[i] + "\t" + "MM" + "\t" + "MM")
                        MMfile.write(line)            
      else:
            M = A[1]
            m = A[0]
            newfile.write("\t" + M+"/"+m + "\t" + rec[4] + "\t" + rec[3])#white control inverted
            for i in range(5,len(rec),3): #work with every 3 records
                  A = string.split(rec[i],"/")
                  if A[0] == m and A[1] == M:
                        newfile.write("\t" + M+"/"+m + "\t" + string.strip(rec[i+2]) + "\t" + rec[i+1])#sample inverted
                  else:
                        newfile.write("\t" + rec[i] + "\t" + "MM" + "\t" + "MM")
                        MMfile.write(line)
      newfile.write("\n")
      line = file.readline()
newfile.close()
file.close()
MMfile.close()
print "END"

