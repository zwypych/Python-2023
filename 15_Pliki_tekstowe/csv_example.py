# import csv
#
# with open('data\\foods.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)


import csv
import sys

data = []

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

print(
    sum([float(x['Budget']) for x in data if x['Director'] == sys.argv[2]])
)