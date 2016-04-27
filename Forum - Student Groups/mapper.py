#!/usr/bin/python
import sys

curr_line = None
def dequote(t):
    if t.startswith("\"") and t.endswith("\""):
        return t[1:-1]
    else:
        return t

def map_a_record(curr_line):
    items = curr_line.replace("\n", " ").split("\t")
    if len(items) != 19 or items[0] == 'id':
        return

    id = dequote(items[0])
    abs_parent_id = dequote(items[7])
    node_type = dequote(items[5])
    author_id = dequote(items[3])

    if node_type == "question":
        print("{0}\t{1}".format(id, author_id))
    elif node_type == "answer":
        print("{0}\t{1}".format(abs_parent_id, author_id))
    elif node_type == "comment":
        print("{0}\t{1}".format(abs_parent_id, author_id))

for line in sys.stdin:
    items = line.split("\t")
    if len(items) > 4 and dequote(items[0]).isdigit() and dequote(items[3]).isdigit():
        if curr_line != None:
            map_a_record(curr_line)
        curr_line = line
    else:
        if curr_line != None:
            curr_line += line

if curr_line != None:
    map_a_record(curr_line)