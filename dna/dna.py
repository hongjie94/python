from sys import argv, exit
from cs50 import get_string

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)
    
databases = open(argv[1], "r")

strs_type = []
peoples = {}
for index, row in enumerate(databases):
    if index == 0:
       strs_type = [data for data in row.strip().split(',')[1:]]
    else:
        new_row = row.strip().split(',')
        peoples[new_row[0]] = [int(x) for x in new_row[1:]]

sequences = open(argv[2], "r").read()

result = []
for data in strs_type:
    i = 0
    max_count = 0
    strs_count = 0
    while i < len(sequences):
        strs = sequences[i:i+len(data)]
        if strs == data:
            strs_count += 1
            max_count = max(max_count, strs_count)
            i += len(data)
        else:
            strs_count = 0
            i += 1
    result.append(max_count)
    
for name, data_count in peoples.items(): 
    if data_count == result:
        print(name)
        exit(0)

else:
    print('No match')