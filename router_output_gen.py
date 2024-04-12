# Intel-NOC
# University of Florida
# Maneesh Merugu
# Srinivas Balusu
# Code to create new obfuscated routers from given interconnect file and router file

from router_output_gen_class import *
import json

with open('variables.json', 'r') as json_file:
    json_variable = json.load(json_file)


# Function to call classes and functions related to obfuscated routers creation
def router_creator_fun(interconnect_file, output_router_file):
    obj = RouterGen(interconnect_file, output_router_file)
    obj.router_creator_function()
    return obj


# Calling above function
router_creator_obj = router_creator_fun(json_variable["path"]+json_variable["interconnect_file"], json_variable["path"]+json_variable["output_router_file"])
