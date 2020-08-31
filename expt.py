#!/usr/bin/python3

import glob
def expt(path):
    res=[]
    for i in glob.glob(path+"/*.list"):
        print("#", "reading from", i)
        for j in open(i, encoding="utf-8").read().split("\n"):
            val = j.split('#', 1)[0].strip()
            if val != "":
                res.extend(val.split(" "))
    return res

if __name__ == "__main__":
    expt(input())