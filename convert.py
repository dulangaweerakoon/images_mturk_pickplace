from os import listdir
import re
from os.path import isfile, join
import os
mypath = 'dist3'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for file_ in onlyfiles:
    val  = list(map(int, re.findall(r'\d+', file_)))
    os.rename(mypath+"/"+file_,mypath+"/"+"Configuration_"+str(val[0])+"_v"+str(val[1])+".png")

