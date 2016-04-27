#!/usr/bin/python
import sys
oldKey = None
imgs = set()
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped
    if oldKey and oldKey != thisKey:
        s = oldKey
        for url in imgs:
            s += "\t{0}".format(url)
        print(s)
        oldKey = thisKey
        imgs.clear()

    oldKey = thisKey
    imgs.add(thisValue)