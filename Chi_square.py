
LOCATION_INPUT = "//cmh/user/Folders2/dgrigoryev/Genetics/"
INPUT = "Candidate_ARDS_SNP_stats.txt"


LOCATION_OUTPUT = "//cmh/user/Folders2/dgrigoryev/Genetics/"

OUTPUT = "Candidate_ARDS_SNP_stats_prcssd.txt"



###########################  select Major Minior positions in the list ########################################

import scipy.stats
import numpy as np
from numpy import *
from array import *
import string

file = open(LOCATION_INPUT + INPUT,'r')#
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')
line = file.readline()#title
rec = string.split(line,"\t")
newfile.write(rec[0] + "\t" + rec[1] + "\tX2" + "\tX2 P value\t"\
                      + "Fisher Exact\t" + "FE P value\n")
line = file.readline()
Lst = []
while line != "":
        rec = string.split(line,"\t")
        obs = np.array([float(rec[2]),float(rec[3]),float(rec[4]),float(rec[5])])
        exp = np.array([float(rec[6]),float(rec[7]),float(rec[8]),float(rec[9])])
        cntrl = np.array([float(rec[2]),float(rec[3])])
        ards = np.array([float(rec[4]),float(rec[5])])

        Chi = scipy.stats.chisquare(obs,exp,2)
        Fish = scipy.stats.fisher_exact([cntrl,ards])

        newfile.write(rec[0] + "\t" + rec[1] + "\t" + `Chi[0]` + "\t" + `Chi[1]`\
                      + "\t" + `Fish[0]` + "\t" + `Fish[1]`)

        newfile.write("\n")
        line = file.readline()
      
newfile.close()
file.close()
print "END"
