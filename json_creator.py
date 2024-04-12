# Intel-NOC
# University of Florida
# Maneesh Merugu
# Srinivas Balusu
# Code to create Routers Json from given interconnect file

from json_creator_class import *
import json

with open('variables.json', 'r') as json_file:
    json_variable = json.load(json_file)


# Function to call classes and functions related to routers json creation
def json_creator_fun(interconnect_file, output_router_file):
    obj = JsonCreator(interconnect_file, output_router_file)
    obj.json_creator_function()
    return obj


# Calling above function
json_creator_obj = json_creator_fun(json_variable["path"]+json_variable["interconnect_file"], json_variable["path"]+json_variable["output_router_file"])
