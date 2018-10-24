#!/usr/bin/env python3

import sys


def mistake_type(code, new_codes, line, columns):
    matched = []

    #no match
    if new_codes == []:
        return ("no match", None)

    #prefix
    l = len(code)
    for c in new_codes:
        if len(c) >= l and c[:l] == code:
            matched.append(c)
    if matched != []:
        return ("prefix", matched)
            
    #order
    code_list = list(code)
    code_list.sort()
    for c in new_codes:
        c_list = list(c)
        c_list.sort()
        if code_list == c_list:
            return ("order", c)

    #different                                
    return ("different", None)


for line in sys.stdin:
    columns = line.rstrip('\r\n').split("\t")
    if len(columns) < 4:
        continue
    code = columns[2]
    new_codes = columns[3].split(":")[2::2]
    if code not in new_codes:
        #print(line, end = "")
        (mistake, result) = mistake_type(code, new_codes, line, columns)
        if mistake == "no match":
            print("no match\t", line, end = "", sep = "")
        elif mistake == "prefix":
            print("prefix", "\t", columns[0], "\t", columns[1], "\t", code, "\t", columns[0], ":",columns[1], ":", ":".join(result), sep = "")
        elif mistake == "order":
            print("order", "\t", columns[0], "\t", columns[1], "\t", code, "\t", columns[0], ":",columns[1], ":", result, sep = "")
        else:
            print("different\t", line, end = "", sep = "")
        



        
        


    
