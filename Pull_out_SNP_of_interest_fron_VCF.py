#The input file should be sorted by gene symbol, then by time point
#INPUT full vcf file
#OUTPUT SNP of interest


import string
file = open("//cmh/user/Folders2/dgrigoryev/Genetics/VCF_test.vcf",'r')
newfile = open("//cmh/user/Folders2/dgrigoryev/Genetics/VCF_test_OUT.vcf",'w')

SNPlst = ['rs11785822','rs176960','rs1613780','rs28533004','rs73313922']

line = file.readline()
while line != "":
        rec = string.split(line,"\t")
        if rec[0][1] == "#":
                line = file.readline()
                continue
        else:          
                if rec[0][0] == "#": # Title line
                        newfile.write(line)
                else:
                        for i in range(len(SNPlst)):
                                if SNPlst[i] == rec[2]:
                                       newfile.write(line)
        line = file.readline()
        if line == "":# check for the last line
                print "LAST Empty line"
                break
            
newfile.close()
file.close()
print "END"
