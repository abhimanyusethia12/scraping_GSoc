#importing required libraries
import csv
import re
import json
import sys

#opening json file
file = open(sys.argv[2])
data = json.load(file)
final_string=''
#running the loop on every row in csv file
with open(sys.argv[1],encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        curr_name = row[0]
        #nwe use if conditions to find official names
        #official name must have at least one capital letter
        if re.search(r'[A-Z]+',curr_name):
            #official name has to have at least two words, hence at least one space          
            if re.search(r'[\s]+',curr_name):
                #official name must not have any special characters/numbers            
                if len(re.search(r'[\w\s]+',curr_name).group())== len(curr_name):
                    #'\W' would have allowed for underscore (_), however official name cannot have '_'
                    # as it is a special character. hence, we check separately for '_'       
                    if re.search(r'_+',curr_name):          
                        print(curr_name)
                    else:
                        for entry in data:
                            if entry['n']== curr_name:
                                final_string = final_string + curr_name+ ', '+ entry['i']+', '+entry['d']+', '+row[1]+ ', ' + row[2]+'\n'
                                break
                else:
                    print(curr_name)
            else:
                print(curr_name)
        else:
            print(curr_name)
                                
print(final_string)