#The set of subjects, which are used for Major allele selection should be the first.

LOCATION_INPUT = "//cmh/user/Folders2/dgrigoryev/Genetics/"
INPUT = "ALL_ARDS_Alleles.txt"


LOCATION_OUTPUT = "//cmh/user/Folders2/dgrigoryev/Genetics/"

OUTPUT = "ALL_ARDS_Alleles_Major_Minor.txt"



###########################  select Major Minior positions in the list ########################################

import string

file = open(LOCATION_INPUT + INPUT,'r')#VCF_tst.txt
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')

line = file.readline()#title
newfile.write("SNP_location" + "\t" + "SNP_ID")#New title
rec = string.split(line,"\t")
for i in range(2,len(rec),8):#each patient group takes 8 cplumns
      Ptnt_grp = string.split(rec[i],"_")
      newfile.write("\t" + Ptnt_grp[0] + " " + Ptnt_grp[1] + " Major_al" + \
                    "\t" + Ptnt_grp[0] + " " + Ptnt_grp[1] + " Minor_al" + \
                    "\t" + Ptnt_grp[0] + " " + Ptnt_grp[1] + " Major_Homo" + \
                    "\t" + Ptnt_grp[0] + " " + Ptnt_grp[1] + " Minor_Homo")
newfile.write("\t" + "Major mixed\t" + "Minor mixed\n")
line = file.readline()
Lst = []
while line != "":
      rec = string.split(line,"\t")
      newfile.write(rec[0] + "\t" + rec[1])
      Allele_lst = []
      for i in range(6,10,1):#control EA alleles start at rec[6]
            Allele_lst = Allele_lst + [int(rec[i])]
      if rec[1] == "rs147252685":
            print "MINOR", Minor, Allele_lst
      Major = Allele_lst.index(max(Allele_lst))
      newfile.write("\t" + `Allele_lst[Major]`)
      Allele_lst[Major] = 0
      Minor = Allele_lst.index(max(Allele_lst))
      newfile.write("\t" + `Allele_lst[Minor]`)
      if rec[1] == "rs147252685":
            print "MINOR", Allele_lst[Minor]
      if Allele_lst[Minor] == 0:#no minor allele
            newfile.write("\t" + "Minor=" +`Minor` + "\n")    
            line = file.readline()
            continue
      for i in range(2,6,1):#write first control's genotype homo
            Lst = Lst + [string.strip(rec[i])]
      newfile.write("\t" + string.strip(Lst[Major]) + "\t" + string.strip(Lst[Minor]))

################################  analysis of other groups  ################################ 

      Lst = []
      Lst_copy = []
      Lst_homo = []
      Ptnts_lst = ["AA_Cntrl","AA_pneu","EA_pneu","AA_seps","EA_seps"]
      n = 14
      Mix_maj = Mix_min = 0#variable for counting different major and minor alleles
      Mix_maj_lst = Mix_min_lst = []
      while n < len(rec):
            Major_temp = int(Major)#set temporary Major to test each group for switched Major
            Minor_temp = int(Minor)#same thing for Minor
            if rec[1] == "rs75454623":
                  print Major, Minor
                  print Major_temp, Minor_temp
            for i in range(n,n+4):
                  Lst = Lst + [string.strip(rec[i])]#create list of allele count per patient group
                  Lst_copy = Lst_copy + [string.strip(rec[i])]
            if rec[1] == "rs75454623":
                  print Lst, Major, Minor, "int", int(Lst[Minor]), int(Lst[Major])
            if int(Lst[Minor]) == 0:#check for mixed minor alleles
                  #if rec[1] == "rs75454623":
                        #print "IN Manor"
                  Lst_copy[Major] = 0
                  Minor_temp = Lst_copy.index(max(Lst_copy))
                  if int(Lst[Minor_temp]) > 0:
                        Mix_min = Mix_min + 1
                        Mix_min_lst = Mix_min_lst + [Ptnts_lst[(n-14)/8]]
            if int(Lst[Major]) == 0:#check for mixed major alleles
                  #if rec[1] == "rs75454623":
                        #print "IN MAJOR"
                  Lst_copy[Minor] = 0
                  Major_temp = Lst_copy.index(max(Lst_copy))
                  if int(Lst[Major_temp]) > 0:
                        Mix_maj = Mix_maj + 1
                        Mix_maj_lst = Mix_maj_lst + [Ptnts_lst[(n-14)/8]]
            if rec[1] == "rs75454623":
                  print "after mix check", Lst , Major_temp, Minor_temp
            newfile.write("\t" + string.strip(Lst[Major_temp]) + "\t" + string.strip(Lst[Minor_temp]))          
            for i in range(n-4,n,1):#write genotypes homozig
                  Lst_homo = Lst_homo + [string.strip(rec[i])]
            if rec[1] == "rs75454623":
                  print "homo", Lst_homo, Major_temp, Minor_temp
            newfile.write("\t" + string.strip(Lst_homo[Major_temp]) + "\t" + string.strip(Lst_homo[Minor_temp]))

            n = n + 8
            Lst = Lst_copy = Lst_homo = []
      newfile.write("\t" + `Mix_maj`)
      if Mix_maj > 0:
            for i in range(len(Mix_maj_lst)):
                  newfile.write("/" + Mix_maj_lst[i])
      newfile.write("\t" + `Mix_min`)
      if Mix_min > 0:
            for i in range(len(Mix_min_lst)):
                  newfile.write("/" + Mix_min_lst[i])
              
      newfile.write("\n")    
      line = file.readline()
      
newfile.close()
file.close()
print "END"

