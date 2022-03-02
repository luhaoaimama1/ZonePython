# -*- coding: UTF-8 -*-
from fold.core.DealFilesByFolder import *
import re

'''
给陈浩检查文件夹内所有文件的  哪些文件 的导包字符包含了 匹配的数据 找到对应的文件和匹配的数据 
并且排除 他自身想排除的文件夹

checkFolders：选择要检测的父文件夹
notCheckFilePathRules：正则过滤掉不想要的文件 通过路径过滤
'''
checkFolders = [
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-app/app/src/main/java",
]

notCheckFilePathRules = [
    # ".*res/values.*",
    # ".*/build/.*",
    # ".*.jpg",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-app/app/src/main/java/com/kuaiyin/live",
]

maps = {
}

findRules = [
    "com.kuaiyin.player.editor",
    "com.kuaiyin.sdk",
]

class FilterCallback2(FilterCallback):
    def filter(self, fold, fileName):
        path = os.path.join(fold, fileName)
        # print(path)
        for rule in notCheckFilePathRules:
            isFound = re.match(rule, path) != None
            if isFound:
                # 找到 true  结果应该返回false
                return not isFound
        return True


class FileCallback2(FileCallback):
    # /Users/fuzhipeng/Desktop/文章/entity
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        fileSplitName = os.path.splitext(fileName)

        fileImports=[]
        with open(path, "r") as file:
            lineNumber = 0
            for line in file.readlines():  # 依次读取每行
                lineNumber = lineNumber + 1
                line = line.strip()  # 去掉每行头尾空白
                for it in findRules:
                    if(line.startswith("import") and line.__contains__(it) and (not fileImports.__contains__(line))):
                        fileImports.append(line)
        if (fileImports.__len__() > 0):
            maps[path] = fileImports
                    # else:                #无视

if __name__ == '__main__':
    for folder in checkFolders:
        findFileByFold(folder, FilterCallback2(), FileCallback2())

    for it in maps.keys():
        print("文件名字{0} \n ".format(it))
        for line in maps[it]:
            print("\t {0} \n ".format(line))