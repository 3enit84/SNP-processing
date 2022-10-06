

LOCATION_INPUT = "//cmh/user/Folders2/dgrigoryev/Genetics/ARDS_SNP/"
INPUT = "Diff_SNPcall_gt80_ARDS.txt"


LOCATION_OUTPUT = "//cmh/user/Folders2/dgrigoryev/Genetics/ARDS_SNP/"

OUTPUT = "Diff_SNPcall_gt80_ARDS_cum_pos_prcssd.txt"



###################################################################
#File should be sorted first accending, then deccending

import string

file = open(LOCATION_INPUT + INPUT,'r')#VCF_tst.txt
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')

line = file.readline()#title
line = file.readline()
rec = string.split(line, "\t")
BinSize = 1
BIN = 100
n = 0
while line != "":  
    while float(rec[4]) >= BIN:
        n = n + 1
        line = file.readline()
        if line == "":
            break
        rec = string.split(line, "\t")
    #print BIN, n
    newfile.write(`BIN` + "\t" + `n` + "\n")
    if BIN == 0:
        break
    BIN = BIN - BinSize
file.close()
newfile.close()
print "END"

