#!/usr/bin/python
import sys
oldKey = None
count=0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, _ = data_mapped
    if oldKey and oldKey != thisKey:
        if count>0:
            print(oldKey, count)
        count = 0
        oldKey = thisKey;

    oldKey = thisKey
    count = count+1

if oldKey != None:
    if count>0:
        print(oldKey, count)
