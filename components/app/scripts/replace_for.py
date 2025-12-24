#!/usr/bin/python3 -OO

##################################################################
### SABnzbd - Replace underscores with dots                     ##
##################################################################
##                                                              ##
## NOTE: This script requires Python 3                          ##
##                                                              ##
## Author: miker                                                ##
##                                                              ##
## Install:                                                     ##
## 1. Copy script to sabnzbd's script folder                    ##
## 2. run: sudo chmod +x replace_for.py                         ##
## 3. in SABnzbd go to Config > Categories                      ##
## 4. Assign replace_for.py to the required category            ##
##################################################################

from time import time
import sys
import os
import os.path

try:
    (scriptname, directory, orgnzbname, jobname, reportnumber, category, group, postprocstatus, url) = sys.argv
except:
    print("No commandline parameters found")
    sys.exit(1)    # exit with 1 causes SABnzbd to ignore the output of this script

files = os.listdir(directory)

for src in files:
    orig_path = os.path.join(directory, src)
    st_info = os.stat(orig_path)
    os.utime(orig_path, (st_info.st_atime, time()))
    if src.find("_") !=-1:
        dst = src.replace('_', '.')
        new_path = os.path.join(directory, dst)
        os.rename(orig_path, new_path)
        print(src, "renamed to ",dst)

print()
print()
print()
print()
# 0 means OK
sys.exit(0)
