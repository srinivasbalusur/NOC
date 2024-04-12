# Intel-NOC
# University of Florida
# Maneesh Merugu
# Srinivas Balusu
# Code to create crossbar and activation package code

import re
import json

with open('variables.json', 'r') as json_file:
    json_variable = json.load(json_file)

file1 = open(json_variable["path"]+json_variable["crbar"], "r+")
file2 = open(json_variable["path"]+json_variable["act_pkg_ldr"], "r+")
file3 = open(json_variable["path"]+json_variable["module"], "w")

content1 = file1.readlines()

for line in content1:
    file3.writelines(line)
file3.writelines('\n')
file3.writelines('\n')

content2 = file2.readlines()

for line in content2:
    file3.writelines(line)
file3.writelines('\n')
file3.writelines('\n')

file3.close()
