#!/usr/bin/python

import sys, pickle

oldKey = None
aggregate_map = {}

for line in sys.stdin:
    pos = line.find("\t")
    thisKey = line[:pos]
    mcode = line[pos + 1:]

    strip_map = pickle.loads(mcode.replace("@", "\n"))
    if oldKey and oldKey != thisKey:
        total_A = aggregate_map[oldKey]
        assert total_A != 0

        for tkey in aggregate_map.keys():
            if tkey == oldKey:
                continue
            if tkey == "primary-news-1.jpg":
                print("{0}\t{1}".format(oldKey, float(aggregate_map[tkey]) / float(total_A)))
        aggregate_map.clear()

    oldKey = thisKey
    for tkey in strip_map.keys():
        if not tkey in aggregate_map.keys():
            aggregate_map[tkey] = 0
        aggregate_map[tkey] += strip_map[tkey]

if oldKey != None:
    total_A = aggregate_map[oldKey]

    for tkey in aggregate_map.keys():
        if tkey == oldKey:
            continue
        if tkey == "primary-news-1.jpg":
            print("{0}\t{1}".format(oldKey, float(aggregate_map[tkey]) / float(total_A)))