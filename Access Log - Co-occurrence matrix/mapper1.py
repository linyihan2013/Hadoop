#!/usr/bin/python
import sys
for line in sys.stdin:

    url_start_idx = line.find("\"GET ")
    if url_start_idx==-1:
         url_start_idx = line.find("\"POST ")
    if url_start_idx==-1:
         continue
    url_end_idx = line.find(" HTTP/")
    if url_end_idx==-1:
          continue
    url = line[url_start_idx+5:url_end_idx]

    pos = url.rfind("/")
    if pos == -1 or not url.endswith(".jpg"):
        continue
    url_key = url[pos + 1:]
    tuples = line.split()
    ip = tuples[0]
    print("{0}\t{1}".format(ip, url_key))