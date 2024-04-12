# Intel-NOC
# University of Florida
# Maneesh Merugu
# Srinivas Balusu
# Class to create new interconnect file from given interconnect file and router file

import re
import json
from all_functions import *

with open('variables.json', 'r') as json_file:
    json_variable = json.load(json_file)


class NocTop:
    def __init__(self, interconnect_file, output_cb_file):
        self.interconnect_file = interconnect_file
        self.output_cb_file = output_cb_file

    def noc_top_function(self):
        file1 = open(json_variable["interconnect_file"], "r+")  # Interconnect File
        file2 = open(json_variable["output_cb_file"], 'rb').read()
        file3 = open(json_variable["new_interconnect_file"], "w")  # New file name

        content1 = file1.readlines()
        content2 = file2.decode('utf-16')
        length = len(content1)
        count = 0
        i = 0
        x = 0
        a = 0

        last_line = 0

        with open(json_variable["output_router_file"], 'r') as file:
            data = json.load(file)

        routers = data['routers']

        z = 0
        for line in content1:
            z = z + 1
            for match in re.finditer('timescale', line):  # Required string name needs to be updated here
                content1[z - 1] = content1[z - 1] + ' `include "module.v" ' + '\n' + '\n'

            def comment_router(router):
                i = 0
                count = 0
                x = 0

                # Code to comment existing routers config in old interconnect file
                for line in content1:
                    i = i + 1
                    for match in re.finditer(router, line):  # Required Router name needs to be updated here
                        y = line.split('(')
                        print("Commented below routers in old interconnect file and written new obfuscated router:-")
                        print(' Matched router line %s:%s' % (i, y[0]))  # Print matched routers with linenumbers
                        count = count + 1
                        content1[i - 1] = '/*' + content1[i - 1]  # Comment start for Routers
                        text = content1[i + 13]
                        text1 = text.strip()
                        text1 = '\t' + text1 + ' */' + '\n'  # Comment end for Routers
                        content1[i + 13] = text1
                        x = i + 14

                return x

        for router in routers:
            x = comment_router(router)
            if x >= last_line:
                last_line = x

        content1[last_line] = content2  # Updating the commented content

        for line in content1:  # Writing obfuscated output to new file
            a = a + 1
            if a == (last_line + 1):
                file3.writelines('\n')
                file3.writelines('//.............Appending output..............//' + '\n')
            elif a == (last_line + 2):
                file3.writelines('//.............Appending output Done..............//' + '\n')
                file3.writelines('\n')
            file3.writelines(line)

        file1.close()
        file3.close()
