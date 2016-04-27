#!/usr/bin/python

import sys
import collections

dict = collections.defaultdict(set)
for line in sys.stdin:
    data = line.split('\t')
    ip, img = data
    dict[img].add(ip)

dict = sorted(dict.items(), key = lambda a : a[0])
primary = set
for i in dict:
    if i[0] == 'primary-news-1.jpg':
        primary = i[1]
        break

for i in dict:
    if i[0] != 'primary-news-1.jpg':
        ips = i[1]
        inter = set.intersection(primary, ips)
        probility = 1.0 * len(inter)/len(ips)
        print("{0}\t{1}".format(i[0], probility))