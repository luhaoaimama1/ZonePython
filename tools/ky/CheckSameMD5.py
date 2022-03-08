# -*- coding: UTF-8 -*-
import re
from fold.core.DealFilesByFolder import *

notCheckFilePathRules = [
    ".*/build/.*",
    ".*/.cxx/.*",
    ".*/cpp/.*",
    ".*/.gradle/.*",
    ".*.gitignore",
    ".*.java",
    ".*.kt",
    ".*.aar",
    ".*.so",
    ".*.class",

    # 重复不会影响 打包出来的东西的大小
    ".*.proguard-rules.pro",
    ".*.consumer-rules.pro",
    ".*.gradle",
    ".*.colors.xml",
    # 分析了lib包里面 path="/res/mipmap-xhdpi-v4" 就有一个不会出现多个所以也过滤掉
    ".*.ic_launcher.*",
    ".*.styles.xml",
    ".*./res/values.*",
    ".*.ky_iconfont.ttf",
    ".*.specific.ttf",
]
path = {
    "/Users/fuzhipeng/AndroidStudioProjects/android2/ky-app",
    "/Users/fuzhipeng/AndroidStudioProjects/android2/ky-debug",
    "/Users/fuzhipeng/AndroidStudioProjects/android2/ky-dependencies",
    "/Users/fuzhipeng/AndroidStudioProjects/android2/ky-framework",
    "/Users/fuzhipeng/AndroidStudioProjects/android2/ky-third-party",
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
            tinydict[md5Str].append(path)
            # print("文件夹{0}------> md5:{1}  相同md5:{2}".format(path, md5Str, tinydict[md5Str]))
        else:
            tinydict[md5Str] = []
            tinydict[md5Str].append(path)
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

    print("=====输出=====\n ")

    for it in tinydict.keys():
        if len(tinydict[it]) > 1 :
            print("md5:{0} \n ".format(it))
            for line in tinydict[it]:
                print("\t {0} \n ".format(line))
