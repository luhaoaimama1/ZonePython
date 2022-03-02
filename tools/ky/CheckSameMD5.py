# -*- coding: UTF-8 -*-
import re
from fold.core.DealFilesByFolder import *

notCheckFilePathRules = [
    ".*/build/.*",
    ".*/.cxx/.*",
    ".*/cpp/.*",
    ".*.java",
    ".*.kt",
    ".*.aar",
    ".*.so",
    ".*.class",
]
# parseFile = 100 * 1024
path = {
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-app",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-debug",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-dependencies",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-framework",
    "/Users/fuzhipeng/AndroidStudioProjects/androidv2/ky-third-party",
}

'''
对处理的文件进行匹配后rename
'''

tinydict = {}


class FileCallback2(FileCallback):
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        # if os.path.getsize(path) > parseFile:
        md5Str = md5(path)
        if tinydict.has_key(md5Str):
            print("文件夹{0}------> md5:{1}  相同md5:{2}".format(path, md5Str, tinydict[md5Str]))
        else:
            tinydict[md5Str] = path
            # print("文件{0}------>添加_ md5:{1}".format(path, md5Str))

        # if tinydict.has_key(md5):
        #     print("文件夹{0}------> 大小越界  md5:{1}  相同md5:{2}".format(path, md5, tinydict[md5]))
        # else:
        #     tinydict[md5] = path
        #     print("文件{0}------>添加_ md5:{1}".format(path, md5))


def md5(path):
    md__format = "md5 {0}".format(path)
    return os.popen(md__format).readlines()[0].split("=")[1].strip()


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


if __name__ == '__main__':
    for item in path:
        if os.path.exists(item):
            print("迭代目录path {0}:".format(item))
            findFileByFold(item, FilterCallback2(), FileCallback2())
        else:
            print("path {0}:目录不存在!".format(path))
