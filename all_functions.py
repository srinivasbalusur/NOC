import re
import os
import itertools
from itertools import permutations



def get_cb_config(list_1, list_2):
# list_1 = ['1','2','3','4']
# list_2 = ['a','b', 'c', 'd']
    unique_combinations = []
    permut = itertools.permutations(list_1, len(list_2))


    count = 0
    for comb in permut:
        zipped = zip(comb, list_2)
        unique_combinations.append(list(zipped))
        count = count+1
    #print(unique_combinations)

    i=0
    x=0
    for i in range(0,len(unique_combinations)):
        count=0
        list_updated = []
        for [a,b] in unique_combinations[i]:
            if(count<4):
                list_updated.append(a)
                count=count+1
        #print(list_updated)


    if(list_updated[0] == 0 and list_updated[1] == 1 and list_updated[2] == 2 and list_updated[3] == 3) :
        sel='000001'
        #print(sel)
    elif (list_updated[0] == 0 and list_updated[1] == 1 and list_updated[2] == 3 and list_updated[3] == 2) :
        sel = '000010'
        #print(sel)
    elif (list_updated[0] == 0 and list_updated[1] == 2 and list_updated[2] == 1 and list_updated[3] == 3):
        sel = '000011'
        #print(sel)
    elif (list_updated[0] == 0 and list_updated[1] == 2 and list_updated[2] == 3 and list_updated[3] == 1):
        sel = '000100'
        #print(sel)
    elif (list_updated[0] == 0 and list_updated[1] == 3 and list_updated[2] == 1 and list_updated[3] == 2):
        sel = '000101'
        #print(sel)
    elif (list_updated[0] == 0 and list_updated[1] == 3 and list_updated[2] == 2 and list_updated[3] == 1):
        sel = '000110'
        #print(sel)
    elif (list_updated[0] == 1 and list_updated[1] == 0 and list_updated[2] == 2 and list_updated[3] == 3):
        sel = '000111'
        #print(sel)
    elif (list_updated[0] == 1 and list_updated[1] == 0 and list_updated[2] == 3 and list_updated[3] == 2):
        sel = '001000'
        #print(sel)
    elif (list_updated[0] == 1 and list_updated[1] == 2 and list_updated[2] == 0 and list_updated[3] == 3):
        sel = '001001'
        #print(sel)
    elif (list_updated[0] == 1 and list_updated[1] == 2 and list_updated[2] == 3 and list_updated[3] == 0):
        sel = '001010'
        #print(sel)
    elif (list_updated[0] == 1 and list_updated[1] == 3 and list_updated[2] == 0 and list_updated[3] == 2):
        sel = '001011'
        #print(sel)
    elif (list_updated[0] == 1 and list_updated[1] == 3 and list_updated[2] == 2 and list_updated[3] == 0):
        sel = '001100'
        #print(sel)
    elif (list_updated[0] == 2 and list_updated[1] == 0 and list_updated[2] == 1 and list_updated[3] == 3):
        sel = '001101'
        #print(sel)
    elif (list_updated[0] == 2 and list_updated[1] == 0 and list_updated[2] == 3 and list_updated[3] == 1):
        sel = '001110'
        #print(sel)
    elif (list_updated[0] == 2 and list_updated[1] == 1 and list_updated[2] == 0 and list_updated[3] == 3):
        sel = '001111'
        #print(sel)
    elif (list_updated[0] == 2 and list_updated[1] == 1 and list_updated[2] == 3 and list_updated[3] == 0):
        sel = '010000'
        #print(sel)
    elif (list_updated[0] == 2 and list_updated[1] == 3 and list_updated[2] == 0 and list_updated[3] == 1):
        sel = '010001'
        #print(sel)
    elif (list_updated[0] == 2 and list_updated[1] == 3 and list_updated[2] == 1 and list_updated[3] == 0):
        sel = '010010'
        #print(sel)
    elif (list_updated[0] == 3 and list_updated[1] == 0 and list_updated[2] == 1 and list_updated[3] == 2):
        sel = '010011'
        #print(sel)
    elif (list_updated[0] == 3 and list_updated[1] == 0 and list_updated[2] == 2 and list_updated[3] == 1):
        sel = '010100'
        #print(sel)
    elif (list_updated[0] == 3 and list_updated[1] == 1 and list_updated[2] == 0 and list_updated[3] == 2):
        sel = '010101'
        #print(sel)
    elif (list_updated[0] == 3 and list_updated[1] == 1 and list_updated[2] == 2 and list_updated[3] == 0):
        sel = '010110'
        #print(sel)
    elif (list_updated[0] == 3 and list_updated[1] == 2 and list_updated[2] == 0 and list_updated[3] == 1):
        sel = '010111'
        #print(sel)
    elif (list_updated[0] == 3 and list_updated[1] == 2 and list_updated[2] == 1 and list_updated[3] == 0):
        sel = '011000'
        #print(sel)
    else:
        sel = '000000'
        #print(sel)
    x=x+1
    #print(x)
    return sel


def tuple_separator(tuples):
    list1 = [x[0] for x in tuples]
    list2 = [x[1] for x in tuples]

    return list1, list2


I_R_IN = ['sink_valid', 'sink_startofpacket', 'sink_endofpacket', 'src_ready']
I_R_OUT = ['sink_ready', 'src_valid', 'src_startofpacket', 'src_endofpacket']
I_R_CNST = ['sink_data', 'clk', 'reset', 'src_data']
I_R_EX = ['src_channel']


def router_IO_extractor(content, router_name):
    index1 = 0
    j = 0
    for line1 in content:
        index1 = index1 + 1
        # checking string is present in line or not
        if router_name in line1:
            #            j=j+1
            # generate each router
            # for a in range(-1,14,14):
            #     router_old =content[index1+a]
            # take the inputs value
            r_in01 = content[index1 + 1]
            r_in02 = content[index1 + 3]
            r_in03 = content[index1 + 4]
            r_in04 = content[index1 + 7]

            #            print(r_in01)
            #            print(r_in02)
            # take the output value
            r_out01 = content[index1 + 0]
            r_out02 = content[index1 + 8]
            r_out03 = content[index1 + 11]
            r_out04 = content[index1 + 12]

            # take the constant IO
            r_cnst01 = content[index1 + 2]
            r_cnst02 = content[index1 + 5]
            r_cnst03 = content[index1 + 6]
            r_cnst04 = content[index1 + 9]
            r_cnst05 = content[index1 + 10]

            # take the start and end portion
            r_start = content[index1 - 1]
            r_end = content[index1 + 13]

            #            #  search for the exact input string
            a00 = re.search( '\(([^)]+)', r_in01 ).group( 1 )
            a01 = re.search( '\(([^)]+)', r_in02 ).group( 1 )
            a02 = re.search( '\(([^)]+)', r_in03 ).group( 1 )
            a03 = re.search( '\(([^)]+)', r_in04 ).group( 1 )

            #            print(a01)
            #
            #            #  search for the exact output string
            b00 = re.search( '\(([^)]+)', r_out01 ).group( 1 )
            b01 = re.search( '\(([^)]+)', r_out02 ).group( 1 )
            b02 = re.search( '\(([^)]+)', r_out03 ).group( 1 )
            b03 = re.search( '\(([^)]+)', r_out04 ).group( 1 )
            #
            #            #  search for the constant string
            c00 = re.search( '\(([^)]+)', r_cnst01 ).group( 1 )
            c01 = re.search( '\(([^)]+)', r_cnst02 ).group( 1 )
            c02 = re.search( '\(([^)]+)', r_cnst03 ).group( 1 )
            c03 = re.search( '\(([^)]+)', r_cnst04 ).group( 1 )
            c04 = re.search( '\(([^)]+)', r_cnst05 ).group( 1 )

            # make a list of connection for inputs of router connected in interconnect
            R_IN_Connection = [(I_R_IN[0], a00), (I_R_IN[1], a01), (I_R_IN[2], a02), (I_R_IN[3], a03)]
            #            #print("router_00"+str(j)+ " Input List:", R_IN_Conenction)
            #            # make a list of connection for outputs of router connected in interconnect
            R_OUT_Connection = [(I_R_OUT[0], b00), (I_R_OUT[1], b01), (I_R_OUT[2], b02), (I_R_OUT[3], b03)]
            #            #print("router_00"+str(j)+" Output List:", R_OUT_Conenction)
            R_CNST_Connection = [(I_R_CNST[0],c00), (I_R_CNST[1],c01), (I_R_CNST[2],c02), (I_R_CNST[3],c03)]
            R_EX_Connection = [(I_R_EX[0],c04)]

            return R_IN_Connection, R_OUT_Connection, R_CNST_Connection, R_EX_Connection


def print_connections(router_name, IO_list):
    matches = re.findall('altera', router_name)
    if matches:
        print(router_name + " (" )
    else:
        print("crbar4x4 " + router_name + " (")
    for x in range( 0, len( IO_list ) ):
        if (x != len( IO_list ) - 1):
            print( "\t ." + IO_list[x][0] + "(" + IO_list[x][1] + ")," )
        else:
            print( "\t ." + IO_list[x][0] + "(" + IO_list[x][1] + ")" )
            print( ");" )


def print_cb_switch(cb_name):
    print( "/* Printing wires     */" )

    cb_in_list = []
    cb_out_list = []
    n = 4

    if "cb_in" in cb_name:
        for i in range( 0, n ):
            #    print("input "+cb_name+"_in"+str(i)+";")
            print( "wire " + cb_name + "_out" + str( i ) + ";" )
            cb_out_list.append( cb_name + "_out" + str( i ) )

    if "cb_out" in cb_name:
        for i in range( 0, n ):
            print( "wire " + cb_name + "_in" + str( i ) + ";" )
            cb_in_list.append( cb_name + "_in" + str( i ) )
            #print("output "+cb_name+"_out"+str(i)+";")

    print( "wire [0:5] " + cb_name + "_sel;" )
    cb_sel = cb_name + "_sel"
    print("\n")

    return  cb_in_list,cb_out_list, cb_sel


def merge(list1, list2):
    merged_list = [(p1, p2) for idx1, p1 in enumerate( list1 )
                   for idx2, p2 in enumerate( list2 ) if idx1 == idx2]
    return merged_list


