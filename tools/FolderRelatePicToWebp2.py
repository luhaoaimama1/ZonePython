# -*- coding: UTF-8 -*-
from fold.core.DealFilesByFolder import *
'''
官方文档：https://developers.google.com/speed/webp/download
'''
# webp google工具包 地址
webpath = "/Users/fuzhipeng/Downloads/libwebp-0.4.1-mac-10.82/bin/cwebp"
path = {
    # "/Users/fuzhipeng/Desktop/webptest",
    "/Users/fuzhipeng/Desktop/原图2",
}
newPathSuffix="_copy"# 压缩后的文件夹后缀名
compassVar ="-q 100"  # 压缩75

class FileCallback2(FileCallback):
    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        print path
        # isImage = str(path).endswith(".jpg") or str(fileName).endswith(".png")
        imgToWebp(fold, fileName, fold + newPathSuffix)
        print("========================关联文件 over=======================")

def imgToWebp(fold, fileName,newFold):
    oldPath = os.path.join(fold, fileName)
    fileSplitName = os.path.splitext(fileName)
    if not os.path.exists(newFold):
        os.makedirs(newFold)
    newPath = os.path.join(newFold, fileSplitName[0] + ".webp")
    commandline = "{0} {3} {1} -o {2}".format(webpath, oldPath, newPath, compassVar)
    # print ("commandline:"+commandline)
    os.system(commandline)
    # print("文件夹{0} ******* 改名：{1}------> 转换成功".format(fold, fileName))
    # os.remove(oldPath) //移除老的文件

if __name__ == '__main__':
    for item in path:
        if os.path.exists(item):
            findFileByFold(item, FilterCallback(), FileCallback2())
            break
        else:
            print("path {0}:目录不存在!".format(path))
