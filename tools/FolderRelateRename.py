import os;
from fold.core.DealFilesByFolder import *;


'''
使用说明：
对文件夹内的所有文件 从命名；（主要应用 UI给的 android多个资源目录  资源名字一样，进行统一修改）
根据maps key找到文件前椎名，换成 value的名字
'''
#/Users/fuzhipeng/Desktop/新手引导-互推 Asserts
# /Users/fuzhipeng/AndroidStudioProjects/bililive-android-myfollowing/followingCard/src/main
maps = {
    "showmap": "ic_following_lbs_detail_location",
    "showmap": "ic_following_lbs_detail_location",
}

'''
对处理的文件进行匹配后rename
'''
class FileCallback2(FileCallback):

    def dealFile(self, fold, fileName):
        path = os.path.join(fold, fileName)
        for key in maps.keys():
            fileSplitName = os.path.splitext(fileName);
            if fileSplitName[0] == key:
                newName = maps[key] + fileSplitName[1]
                print("文件夹{0} ******* 改名：{1}=====>{2}".format(fold, fileName, newName))
                os.rename(path, os.path.join(fold, newName))


if __name__ == '__main__':
    selectFold(FilterCallback(),FileCallback2())

