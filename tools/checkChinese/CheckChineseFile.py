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
    "/Users/fuzhipeng/Desktop/aaba",
    "/Users/fuzhipeng/AndroidStudioProjects/ZoneStudio/Android_Zone_Test/src/com/example/mylib_test/activity/checkchinese",
]

notCheckFilePathRules = [
    ".*res/values.*",
]

class FilterCallback2(FilterCallback):
    def filter(self, fold, fileName):
        path = os.path.join(fold, fileName)
        for rule in notCheckFilePathRules:
            isFound = re.match(rule, path) != None
            # 找到 true  结果应该返回false
            return not isFound
        return True


class FileCallback2(FileCallback):
    # /Users/fuzhipeng/Desktop/文章/entity
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        fileSplitName = os.path.splitext(fileName)

        # 核心处理
        if fileSplitName[1] == ".xml":
            noteDealCallback = XmlNoteCallback()
        else:
            noteDealCallback = JavaKtNoteCallback()

        pathPrint = False
        with open(path, "r") as file:
            lineNumber = 0
            for line in file.readlines():  # 依次读取每行
                lineNumber = lineNumber + 1
                line = line.strip()  # 去掉每行头尾空白
                # 核心处理
                validContent = noteDealCallback.dealFile(line)

                if validContent.strip() != '':
                    if (content_is_chinese(validContent)):
                        if pathPrint == False:
                            print("FilePath=====>", path)
                            pathPrint = True
                        print("\t LineNumber:{0} \t Content: {1}".format(lineNumber, validContent))


if __name__ == '__main__':
    for folder in checkFolders:
        findFileByFold(folder, FilterCallback2(), FileCallback2())
