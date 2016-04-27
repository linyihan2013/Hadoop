#!/usr/bin/python
import sys
arr={}
ss=None
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data)!=3:
        continue
    thiskey,thisname,thisc=data
    #print "%d\t%s\t%d"%(int(thiskey),thisname,int(thisc))
    ss=thiskey+"\t"+thisname
    if not ss in arr.keys():
        arr[ss]=0
    arr[ss]+=1

rel=sorted(arr.iteritems(),key=lambda d:d[1],reverse=True)
for i in range(len(rel)):
    (k,v)=rel[i]
    if int(v)>=25:
        print("%s\t%d"%(k,int(v)))
