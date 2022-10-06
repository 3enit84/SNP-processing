
LOCATION_INPUT = "U:/Exome_Seq/InDel/"
INPUT = "Indel_Unidir_80prcnt_call.txt"


LOCATION_OUTPUT = "U:/Exome_Seq/InDel/"

OUTPUT = "Indel_Unidir_80prcnt_call_chi_fish.txt"


#calculate chi square and fisher exact on thefile with 3 descriptive
# entries
###################################################################

import scipy.stats
import numpy as np
from numpy import *
from array import *
import string

file = open(LOCATION_INPUT + INPUT,'r')#
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')
line = file.readline()#title
rec = string.split(line,"\t")
newfile.write(rec[0] + "\t" + rec[1] + "\t" + rec[2]\
                      + "\tX2" + "\tX2 P value\t"\
                      + "Fisher Exact\t" + "FE P value\n")
line = file.readline()
Lst = []
print "START"
while line != "":
        rec = string.split(line,"\t")
        obs = np.array([float(rec[3]),float(rec[4]),float(rec[5]),float(rec[6])])
        exp = np.array([float(rec[7]),float(rec[8]),float(rec[9]),float(rec[10])])
        cntrl = np.array([float(rec[3]),float(rec[4])])
        ards = np.array([float(rec[5]),float(rec[6])])

        Chi = scipy.stats.chisquare(obs,exp,2)
        Fish = scipy.stats.fisher_exact([cntrl,ards])

        newfile.write(rec[0] + "\t" + rec[1] + "\t" + rec[2]\
                      + "\t" + `Chi[0]` + "\t" + `Chi[1]`\
                      + "\t" + `Fish[0]` + "\t" + `Fish[1]`)

        newfile.write("\n")
        line = file.readline()
      
newfile.close()
file.close()
print "END"
