import csv
from collections import Counter

MostCareerTriples = dict()

with open('baseballdatabank/core/Batting.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # First row contains column headers, so we will ignore it
            line_count += 1
        else:
            playerId = row[0]
            if playerId in MostCareerTriples:
                MostCareerTriples[playerId] += int(row[10])
            else:
                MostCareerTriples[playerId] = int(row[10])
            line_count += 1
    print(f"Processed {line_count} lines.")

counterMCT = Counter(MostCareerTriples)

# Retrieve top 25
top25MCT = counterMCT.most_common(25)

print("Most Career Triples:")

for i in top25MCT:
    print(f"{i[0]}: {i[1]}")