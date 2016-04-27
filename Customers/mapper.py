#!/usr/bin/python
import sys
for line in sys.stdin:
    data = line.strip().split("|")
    if len(data)<4:
        continue
    l = len(data[3])
    ss=data[3][-l:-6]
    if len(data)==4 and ss<"1996":
        print("%d\t%s\t%d"%(int(data[0]),data[1],1))