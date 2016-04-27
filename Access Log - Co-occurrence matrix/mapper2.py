#!/usr/bin/python

import sys, pickle

stripes = {}

for line in sys.stdin:
    tuples = line.split()
    ip = tuples[0]
    urls = tuples[1:]

    for idx1 in range(0, len(urls)):
        url = urls[idx1]
        if not url in stripes.keys():
            stripes[url] = {}

        if not url in stripes[url].keys():
            stripes[url][url] = 0
        stripes[url][url] += 1

        for idx2 in range(0, len(urls)):
            if idx1 == idx2:
                continue
            url2 = urls[idx2]
            if not url2 == "primary-news-1.jpg":
                continue

            if not url2 in stripes[url].keys():
                stripes[url][url2] = 0
            stripes[url][url2] += 1
            if not url in stripes[url2].keys():
                stripes[url2][url] = 0
            stripes[url2][url] += 1

    if len(stripes.keys()) > 1000:
        for tkey in stripes.keys():
            print("{0}\t{1}".format(tkey, pickle.dumps(stripes[tkey]).replace("\n", "@")))
        stripes.clear()

for tkey in stripes.keys():
    print("{0}\t{1}".format(tkey, pickle.dumps(stripes[tkey]).replace("\n", "@")))