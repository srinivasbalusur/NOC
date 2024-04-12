# Intel-NOC
# University of Florida
# Maneesh Merugu
# Srinivas Balusu
# Code to create new interconnect file from given interconnect file and router file

from noc_top_clean_class import *
import json

with open('variables.json', 'r') as json_file:
    json_variable = json.load(json_file)


# Function to call classes and functions related to new interconnect file
def noc_top_fun(interconnect_file, output_cb_file):
    obj = NocTop(interconnect_file, output_cb_file)
    obj.noc_top_function()
    return obj


# Calling above function
noc_top_obj = noc_top_fun(json_variable["path"]+json_variable["interconnect_file"], json_variable["path"]+json_variable["output_cb_file"])
