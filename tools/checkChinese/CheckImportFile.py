# -*- coding: UTF-8 -*-
from fold.core.DealFilesByFolder import *
import re

'''
给陈浩检查文件夹内所有文件的 import语句 放入集合中


checkFolders：选择要检测的父文件夹
notCheckFilePathRules：正则过滤掉不想要的文件 通过路径过滤
'''
checkFolders = [
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-app/app/src/main/java/com/kuaiyin/live/sdk",
]

notCheckFilePathRules = [
    ".*res/values.*",
    ".*/build/.*",
    ".*.jpg",
    ".*.png",
]
result = []

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

        with open(path, "r") as file:
            lineNumber = 0
            for line in file.readlines():  # 依次读取每行
                lineNumber = lineNumber + 1
                line = line.strip()  # 去掉每行头尾空白

                if (not result.__contains__(line)) and line.startswith("import"):
                    result.append(line)
                # 核心处理
                # validContent = noteDealCallback.dealFile(line)
                #
                # if validContent.strip() != '':
                #     if (content_is_chinese(validContent)):
                #         if pathPrint == False:
                #             print("FilePath=====>", path)
                #             pathPrint = True
                #         print("\t LineNumber:{0} \t Content: {1}".format(lineNumber, validContent))


if __name__ == '__main__':
    for folder in checkFolders:
        findFileByFold(folder, FilterCallback2(), FileCallback2())
    result.sort()# 排序下
    for it in result:
        print("{0} \n ".format(it))