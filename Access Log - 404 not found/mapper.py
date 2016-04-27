#!/usr/bin/python
import sys
for line in sys.stdin:
    tuples = line.split()
    if len(tuples)<2:
        continue
    ip = tuples[0]
    status = tuples[len(tuples)-2]
    if status=="404":
        print("{0}\t{1}".format(ip, 1))