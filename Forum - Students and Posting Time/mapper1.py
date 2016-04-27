#!/usr/bin/python
import sys

data = sys.stdin.read()
lines = data.split('\t')

id = None

for i, line in enumerate(lines):
    if i % 18 == 3 and id is None:
        if line.startswith('\"'):
            line = line[1:-1]
        id = line
    elif i % 18 == 8 and id is not None:
        if line.startswith('\"'):
            line = line[1:-1]
        time = line.split(' ')[1].split(':')[0]
        print("{0}\t{1}".format(id, time))
        id = None