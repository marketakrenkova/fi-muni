import sys, subprocess

for line in sys.stdin:
    columns = line.rstrip('\r\n').split("\t")
    if len(columns) < 4:
        print(line, end = "")
        continue
    code = columns[2]
    new_codes = columns[3].split(":")[2::2]
    if code not in new_codes:
        print(line, end = "")     
        


    
