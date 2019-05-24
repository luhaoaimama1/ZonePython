from fold.core.DealFilesByFolder import *
from fold.string.StringUtils import *
from tools.checkChinese.noteDeals.XmlNoteCallback import *
from tools.checkChinese.noteDeals.JavaKtNoteCallback import *
import re

'''
checkFolders：选择要检测的父文件夹
notCheckFilePathRules：正则过滤掉不想要的文件 通过路径过滤
'''
checkFolders = [
    "/home/fuzhipeng/AndroidStudioProjects/andruid/app/following",
    # "/home/fuzhipeng/AndroidStudioProjects/andruid2/app/following/bplusFollowing",
]

notCheckFilePathRules = [
    ".*res/values.*",
    ".*/build/.*",
    ".*.jpg",
    ".*.png",
    ".*.xml",
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


setList = set()


class FileCallback2(FileCallback):
    # /Users/fuzhipeng/Desktop/文章/entity
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        fileSplitName = os.path.splitext(fileName)
        # 核心处理
        if fileSplitName[1] == ".java" or fileSplitName[1] == ".kt":
            arr = []
            with open(path, "r") as file:
                lineNumber = 0
                for line in file.readlines():  # 依次读取每行
                    lineNumber = lineNumber + 1
                    line = line.strip()  # 去掉每行头尾空白
                    if line.count('com.bilibili.bilibililive.uibase') > 0:
                        if line.endswith(";"):
                            line = line[:-1]
                        arr.append(line)
                        setList.add(line)
                if len(arr) > 0:
                    print("path  ======> {0}".format(
                        path.replace("/home/fuzhipeng/AndroidStudioProjects/andruid/app/following/",
                                     "")))
                    for item in arr:
                        print("\t \t lineNumber:{0} \t content:{1} ".format(lineNumber, item))


if __name__ == '__main__':
    for folder in checkFolders:
        findFileByFold(folder, FilterCallback2(), FileCallback2())
    print("涉及的类:")
    for item in setList:
        print("\t {0} ".format(item))
