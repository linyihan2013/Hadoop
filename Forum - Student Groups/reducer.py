#!/usr/bin/python

import sys

oldKey = None
authors = []
question = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    question_id, author_id = data_mapped
    if oldKey and oldKey != question_id:
        authors.sort()
        print("{0}\t{1}".format(oldKey, authors))
        authors = []
        question = None

    oldKey = question_id
    authors.append(int(author_id))

if oldKey != None:
    authors.sort()
    print("{0}\t{1}".format(oldKey, authors))