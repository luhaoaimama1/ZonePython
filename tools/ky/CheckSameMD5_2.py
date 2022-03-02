# -*- coding: UTF-8 -*-
import re
import os


#当前文件路径 :os.path.realpath(__file__)
# 确定在任何地方执行都能获取到项目的根目录
from fold.core.DealFilesByFolder import findFileByFold, FilterCallback, FileCallback

'''
对项目md5 相同 的检测

notCheckFilePathRules ：文件忽略的格式
path：要检查的路径
f：打印结果存在的位置
projectPath代表项目路径

对处理的文件进行匹配后rename
'''
tinydict = {}
tinydict2 = {}

class FileCallback2(FileCallback):
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        md5Str = md5(path)

        tinydict[path.replace("/Users/fuzhipeng/Desktop/ks/a", "")] = md5Str

class FileCallback3(FileCallback):
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        # if os.path.getsize(path) > parseFile:
        md5Str = md5(path)
        tinydict2[path.replace("/Users/fuzhipeng/Desktop/ks/b", "")] = md5Str

def md5(path):
    md__format = "md5 {0}".format(path)
    return os.popen(md__format).readlines()[0].split("=")[1].strip()

# tinydict3={1:"2",2:"3"}
if __name__ == '__main__':
    # tinydict3.iterkeys()

    findFileByFold("/Users/fuzhipeng/Desktop/ks/a", FilterCallback(), FileCallback2())
    findFileByFold("/Users/fuzhipeng/Desktop/ks/b", FilterCallback(), FileCallback3())
    for key in tinydict2.keys():
        if key in tinydict:
            if tinydict2[key]!=tinydict[key]:
                print("文件md5不同 地址" + key)
        else :
            print("新的文件：" + key)

    print("1")
