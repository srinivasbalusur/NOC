# Intel-NOC
# University of Florida
# Maneesh Merugu
# Srinivas Balusu
# Class to create Routers Json from given interconnect file

import re
import random
import json

# Opening json variables file
with open('variables.json', 'r') as json_file:
    json_variable = json.load(json_file)


# Class to create routers json
class JsonCreator:
    def __init__(self, interconnect_file, output_router_file):
        self.interconnect_file = interconnect_file
        self.output_router_file = output_router_file

    # Function to create routers json
    def json_creator_function(self):
        file1 = open(self.interconnect_file, "r")  # Interconnect file
        file2 = open(self.output_router_file, "w")  # Output router file
        content1 = file1.readlines()
        length = len(content1)
        count = 0
        i = 0
        x = 0
        a = 0
        router_list = []

        for line in content1:
            i = i + 1
            # Searching for required router suffix
            for match in re.finditer(json_variable["router_suffix"],
                                     line):  # Required Router name needs to be updated here
                y = line.split('(')
                router_list.append((y[0].lstrip('\t')).rstrip())

        # Selecting random routers based on count
        random_select = random.sample(router_list, json_variable["random_routers_count"])
        print("Routers found = ", len(router_list))
        print("Router List = ", router_list)
        print('{')
        print("\t \"routers\": ", end="")
        print(random_select)
        print("}")

        # Writing routers into output file
        list_str = json.dumps(random_select)
        file2.writelines('{' + '\n' + '\t' + '\"routers\":')
        file2.writelines(list_str)
        file2.writelines('\n' + '}')
        file2.close()
        file1.close()
