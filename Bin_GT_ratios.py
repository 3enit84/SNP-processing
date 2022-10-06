
import string

file = open("D:/JHBMC/Simon/Agilent_canine/Signal_data/251380710151.txt", 'r')
newfile = open("D:/JHBMC/Simon/Agilent_canine/Signal_data/Norm_ND.txt", 'w')
line = file.readline()#title
line = file.readline()
rec = string.split(line, "\t")
BinSize = 20
BIN = BinSize
while line != "":
    n = 0
    while float(rec[3]) < BIN:
        n = n + 1
        line = file.readline()
        if line == "":
            break
        rec = string.split(line, "\t")
    #print BIN, n
    newfile.write(`BIN` + "\t" + `n` + "\n")
    if BIN == 50000:
        break
    BIN = BIN + BinSize
file.close()
newfile.close()
print "END"

