# -*- coding: UTF-8 -*-
import re

from fold.core.DealFilesByFolder import *

ky_ = "/Users/fuzhipeng/PythonProjects/ZonePython/tools/ky2"
if not os.path.exists(ky_):
    os.makedirs(ky_)

# >100k 就转
parseFile = 100 * 1024
path = {
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-app",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-debug",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-dependencies",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-framework",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-third-party",
}
notCheckFilePathRules = [
    ".*/build/.*",
    ".*.java",
    ".*.kt",
    ".*.aar",
    ".*.so",
    ".*.class",
    ".*/.cxx/.*",
    ".*/cpp/.*",
]

'''
对处理的文件进行匹配后rename
'''

class FileCallback2(FileCallback):
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        if os.path.getsize(path) > parseFile:
            print("文件夹{0}------> 大小越界  文件大小:{1}".format(path, os.path.getsize(path)))



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

# if __name__ == '__main__':
    # for item in path:
    #     if os.path.exists(item):
    #         print("迭代目录path {0}:".format(item))
    #         findFileByFold(item, FilterCallback2(), FileCallback2())
    #     else:
    #         print("path {0}:目录不存在!".format(path))
