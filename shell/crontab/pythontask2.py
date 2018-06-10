# -*- coding: utf-8 -*-

print("执行任务！")

import os
path='''/Users/fuzhipeng/Desktop/test'''
if not os.path.exists(path):
    os.mkdir(path)
try:
    with open(os.path.join(path,"1.txt"),"r") as f:
        try:
            c=f.readline();
            print(c)
            content=int(c)
            content=content+1
        except:
            content=0
except:
    content=0
with open(os.path.join(path,"1.txt"),"w") as f:
    f.write(repr(content))
