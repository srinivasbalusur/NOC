# Intel-NOC
# University of Florida
# Maneesh Merugu
# Srinivas Balusu
# Class to create new obfuscated routers from given interconnect file and router file

import random
import json
from all_functions import *

with open('variables.json', 'r') as json_file:
    json_variable = json.load(json_file)

with open(json_variable["output_router_file"], 'r') as router_json_data:
    router_data = json.load(router_json_data)


class RouterGen:
    def __init__(self, interconnect_file, output_router_file):
        self.interconnect_file = interconnect_file  # Interconnect file
        self.output_router_file = output_router_file  # Router file

    def router_creator_function(self):
        router_list = router_data['routers']
        select_lines = []

        # write select lines into a file
        file2 = open(json_variable["select_lines_file"], "w")

        def updated_connections(io_list, name):
            in_array, out_array = tuple_separator(io_list)
            indexed_array_1 = [(element, index) for index, element in enumerate(out_array)]

            # write original order into a file in a json format
            file2.writelines("\n" + "########## " + name + " Before Shuffle" + " ##########" + "\n")
            json.dump(indexed_array_1, file2)
            file2.writelines("\n")

            original_indices_1 = [index for element, index in indexed_array_1]
            # Shuffle the indexed_array
            random.shuffle(indexed_array_1)

            # write shuffled order into a file in a json format
            file2.writelines("\n" + "########## " + name + " After Shuffle" + " ##########" + "\n")
            json.dump(indexed_array_1, file2)
            file2.writelines("\n")

            # Extract the randomized array and the original indices
            randomized_array_1 = [element for element, index in indexed_array_1]
            shuffled_indices_1 = [index for element, index in indexed_array_1]

            # Getting Select Lines
            sel = get_cb_config(shuffled_indices_1, out_array)

            return randomized_array_1, shuffled_indices_1, sel

        def get_cb_connections(cb_in_list, cb_out_list, generic_r_in, arr_in_1, sel, cb_sel):

            cb_in_tuple = merge(cb_in_list, arr_in_1)
            cb_out_tuple = merge(cb_out_list, generic_r_in)
            cb_sel_tuple = merge(sel, cb_sel)
            cb_connections = cb_in_tuple + cb_out_tuple + cb_sel_tuple

            return cb_connections

        generic_r_in = json_variable["generic_r_in"]
        generic_r_out = json_variable["generic_r_out"]

        act_pkg = []
        mer_pkg = []

        # ===========================================

        # open the sample file used

        file1 = open(self.interconnect_file)
        content = file1.readlines()

        count = 0

        for router in router_list:
            cb_in_name = json_variable["cb_in_suffix"] + str(count)
            cb_out_name = json_variable["cb_out_suffix"] + str(count)

            r_in, r_out, r_cnst, r_misc = router_IO_extractor(content, router)
            arr_in_1, arr_in_2, sel_in = updated_connections(r_in, cb_in_name)

            # Write correct in router select lines into a file
            cb_in_router_name1 = "\n" + cb_in_name + '_sel' + ' : ' + sel_in + "\n"
            file2.writelines(cb_in_router_name1)

            arr_out_1, arr_out_2, sel_out = updated_connections(r_out, cb_out_name)
            # Write correct out router select lines into a file
            cb_out_router_name1 = "\n" + cb_out_name + '_sel' + ' : ' + sel_out + "\n"
            file2.writelines(cb_out_router_name1)

            cb_in_router_name = cb_in_name + '_sel' + ' : '
            cb_out_router_name = cb_out_name + '_sel' + ' : '

            mer_pkg.append(sel_in)
            mer_pkg.append(sel_out)
            act_pkg.append(cb_in_router_name)
            act_pkg.append(sel_in)
            act_pkg.append('\n')
            act_pkg.append(cb_out_router_name)
            act_pkg.append(sel_out)
            act_pkg.append('\n')

            r_in_mod = [(json_variable["generic_r_in"][0], cb_in_name + json_variable["out_suffix"][0]),
                        (json_variable["generic_r_in"][1], cb_in_name + json_variable["out_suffix"][1]),
                        (json_variable["generic_r_in"][2], cb_in_name + json_variable["out_suffix"][2]),
                        (json_variable["generic_r_in"][3], cb_in_name + json_variable["out_suffix"][3])]

            r_out_mod = [(json_variable["generic_r_out"][0], cb_out_name + json_variable["in_suffix"][0]),
                         (json_variable["generic_r_out"][1], cb_out_name + json_variable["in_suffix"][1]),
                         (json_variable["generic_r_out"][2], cb_out_name + json_variable["in_suffix"][2]),
                         (json_variable["generic_r_out"][3], cb_out_name + json_variable["in_suffix"][3])]

            router_connections = r_in_mod + r_out_mod + r_cnst + r_misc

            cb_in_in_list, cb_in_out_list, cb_in_sel = print_cb_switch(cb_in_name)
            cb_out_in_list, cb_out_out_list, cb_out_sel = print_cb_switch(cb_out_name)

            cb_in_sel_list = []
            cb_out_sel_list = []
            cb_in_sel_list.append(cb_in_sel)
            cb_out_sel_list.append(cb_out_sel)

            print_connections(router, router_connections)
            print("\n")

            cb_in_list = json_variable["cb_in_list"]
            cb_out_list = json_variable["cb_out_list"]
            sel = ['sel0']

            cb_in_connections = get_cb_connections(cb_in_list, cb_out_list, cb_in_out_list, arr_in_1, sel,
                                                   cb_in_sel_list)
            print_connections(cb_in_name, cb_in_connections)
            print("\n")

            cb_out_connections = get_cb_connections(cb_in_list, cb_out_list, generic_r_out, cb_out_in_list, sel,
                                                    cb_out_sel_list)
            print_connections(cb_out_name, cb_out_connections)
            print("\n")

            count = count + 1

        # Print Merged select lines
        merged_pkg = ''.join(mer_pkg)

        # write select lines into a file
        file2 = open(json_variable["select_lines_file"], "w")
        file2.writelines("\n" + "\n" + "########## Routers Correct Select Lines ##################" + "\n")
        file2.writelines(act_pkg)
        file2.writelines("\n" "########## Merged Correct Select Lines ##################" + "\n")
        file2.writelines(merged_pkg)
        file2.close()

        # Activation package code
        file3 = open(json_variable["activation_pkg_ldr"], "r+")  # Required file name needs to be updated here
        content1 = file3.readlines()
        for line in content1:
            print(line, end='')
        file3.close()
