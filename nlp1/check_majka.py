#!/usr/bin/env python3

import sys
import fileinput


def mistake_type(tag, new_tags, line, columns):
    matched = []

    #no tag
    if tag =="":
        return("no tag", None)
    
    #no match
    if new_tags == []:
        return ("no match", None)

    #prefix
    l = len(tag)
    for t in new_tags:
        if len(t) > l and t[:l] == tag:
            matched.append(t)
    if matched != []:
        return ("prefix", matched)
            
    #order
    tag_list = list(tag)
    tag_list.sort()
    for t in new_tags:
        t_list = list(t)
        t_list.sort()
        if tag_list == t_list:
            return ("order", t)

    #different                                
    return ("different", None)


#for line in sys.stdin:
for line in fileinput.input():
    columns = line.rstrip('\r\n').split("\t")
    if len(columns) < 4:
        continue
    tag = columns[2]
    if len(columns[3]) == 1:
        new_tags = columns[3]
    else:
        new_tags = columns[3].split(":")[2::2]
    if tag not in new_tags:
        #print(line, end = "")
        (mistake, result) = mistake_type(tag, new_tags, line, columns)
        if mistake == "no tag":
            print("no tag\t", line, end = "", sep = "")
        elif mistake == "no match":
            print("no match\t", line, end = "", sep = "")
        elif mistake == "prefix":
            print("prefix", "\t", columns[0], "\t", columns[1], "\t", tag, "\t", columns[0], ":",columns[1], ":", ":".join(result), sep = "")
        elif mistake == "order":
            print("order", "\t", columns[0], "\t", columns[1], "\t", tag, "\t", columns[0], ":",columns[1], ":", result, sep = "")
        else:
            print("different\t", line, end = "", sep = "")
        



        
        


    
