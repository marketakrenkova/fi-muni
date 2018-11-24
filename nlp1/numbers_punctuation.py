#!/usr/bin/env python3
import sys


for line in sys.stdin:
    if line[0] == "<":
        sys.stdout.write(line)
        continue
    columns = line.rstrip('\r\n').split("\t")
    if len(columns) < 3 and columns[0][0].isalpha():
        continue
    if len(columns) < 3:
        columns.append("")
        if columns[0][0].isdigit():
            if columns[0][len(columns[0])-1].isalpha():
                continue
            nlist = list(columns[0])
            base = ""         #base - zakladni tvar
            for n in nlist:
                if n.isdigit():
                    base += "#"
                else:
                    base += n
            tag = "k4"
            columns.append(":".join([columns[0], base, tag]))

        else:       #XXX ocekavam, ze v columns[0] je jen 1 znak 
            base = columns[0]
            tag = "kIx"
            if base == "." or base == "!" or base == "?":
                tag += "."
            elif base == "," or base == ":" or base == ";":
                tag += ","
            elif base == '"'or base == "’" or base == "‘" or base == "„" or base == "“":
                tag += ""
            elif base == "("or base == "{"or base == "["or base == "<":
                tag += "("
            elif base == ")" or base == "}" or base == "]" or base == ">":
                tag += ")"
            else:
                tag +="~"

            if base == ":":
                columns.append(":")     #XXX nejsem si jista, jestli tam ma byt jen : nebo i kIx,
            else:
                columns.append(":".join([columns[0], base, tag]))

        sys.stdout.write("\t".join(columns)+"\n")

    else:
        sys.stdout.write(line)
