#!/usr/bin/python
import sys
import collections

dict = collections.defaultdict(list)
set1 = set()
most = collections.defaultdict(list)

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 2:
        id, date = data[0], int(data[1])
        dict[id].append(date)
        if id not in set1:
            set1.add(id)

for i in dict:
    most_common = {}
    for j in dict[i]:
        if j not in most_common:
            most_common[j] = 1
        else:
            most_common[j] += 1
    most_common = sorted(most_common.items(), key = lambda x : x[1], reverse = True)
    greatest_times = most_common[0][1]
    for j in most_common:
        if j[1] == greatest_times:
            most[i].append(j[0])
    most[i] = sorted(most[i])

set1 = sorted(set1)

for i in set1:
    print("{0}\t{1}".format(i, most[i][0]))