# -*- coding: UTF-8 -*-
from fold.core.DealFilesByFolder import *

'''
使用说明：
对制定目录下的 drawable-xxhdpi 检测 .jpg .png 大于某个设置的大小的文件 的转换成 webp。并且其他关联的文件夹也会变成webp
'''
# /Users/fuzhipeng/Desktop/新手引导-互推 Asserts
# /Users/fuzhipeng/AndroidStudioProjects/bililive-android-myfollowing/followingCard/src/main

# 不转 仅仅看log false才转web
onlyLogNoParseWeb = False
# webp google工具包 地址
webpath = "/Users/fuzhipeng/Downloads/libwebp-0.4.1-mac-10.8/bin/cwebp"
# >400k 就转
parseFile = 80
path = {
    # "/Users/fuzhipeng/Desktop/webptest",
    "/Users/fuzhipeng/Desktop/原图 2",
}
checkRelatePath = [
    "drawable-xxhdpi",
    "drawable-xhdpi",
    "drawable-hdpi",
    "drawable",
]

'''
对处理的文件进行匹配后rename
'''

class FileCallback2(FileCallback):
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        isImage = str(fileName).endswith(".jpg") or str(fileName).endswith(".png")
        if str(fold).endswith(checkRelatePath[0]) and isImage:
            # 转成webp
            if os.path.getsize(path) > parseFile:
                print("文件夹{0}------> 大小越界  文件大小:{1}".format(path, os.path.getsize(path)))
                print("========================关联文件 start=======================")
                for index in range(len(checkRelatePath)):
                    newfold=str(fold).replace(checkRelatePath[0],checkRelatePath[index])
                    newPath = os.path.join(newfold, fileName)
                    if os.path.exists(newPath):
                        print(newPath)
                        imgToWebp(newfold,fileName)

                print("========================关联文件 over=======================")

def imgToWebp(fold, fileName):
    if not onlyLogNoParseWeb:
        oldPath = os.path.join(fold, fileName)
        fileSplitName = os.path.splitext(fileName)
        newPath = os.path.join(fold, fileSplitName[0] + ".webp")
        commandline = "{0} {1} -o {2}".format(webpath, oldPath, newPath)
        os.system(commandline)
        print("文件夹{0} ******* 改名：{1}------> 转换成功".format(fold, fileName))
        os.remove(oldPath)

if __name__ == '__main__':
    for item in path:
        if os.path.exists(item):
            findFileByFold(item, FilterCallback(), FileCallback2())
            break
        else:
            print("path {0}:目录不存在!".format(path))
