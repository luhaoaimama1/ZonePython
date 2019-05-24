from fold.core.DealFilesByFolder import *
import shutil

'''
使用说明：
对xxhdpi文件 内的某个文件  关联删除,或者关联移动到底层库
注意路径要是drawable-xxhdpi 而不能是别的
'''
rootPath = "/home/fuzhipeng/AndroidStudioProjects/andruid2/"
libPath = "/home/fuzhipeng/AndroidStudioProjects/andruid2/common/bpluscommon/basePlus/src/main/res"
maps = {
    # "app/following/bplusFollowing/src/main/res/drawable-xxhdpi/ic_video_recommend_circle.png": libPath,
    "app/following/painting/src/main/res/drawable-xxhdpi/ic_feedback_support_grey.png": "",
}
checkRelatePath = [
    "drawable-xxhdpi",
    "drawable-xhdpi",
    "drawable-hdpi",
    "drawable",
    "drawable-night-xxhdpi",
    "drawable-night-xhdpi",
    "drawable-night-hdpi",
    "drawable-night",
]

'''
对处理的文件进行匹配后rename
'''
if __name__ == '__main__':
    for key in maps.keys():
        path = rootPath + key
        if not os.path.isdir(path):
            for index in range(len(checkRelatePath)):
                newPath = str(path).replace(checkRelatePath[0], checkRelatePath[index])
                if os.path.exists(newPath):
                    # os.path.split(newPath)
                    if os.path.exists(maps[key]):
                        fileSplitName = os.path.split(newPath)
                        fileNewFile = os.path.join(libPath, checkRelatePath[index], fileSplitName[1])
                        shutil.move(newPath, fileNewFile)
                        print("移动文件from{0} =======> {1}:".format(newPath, fileNewFile))
                    else:
                        os.remove(newPath)
                        print(newPath + "移除")
                else:
                    print("{0}文件不存在".format(newPath))
            break
        # else:
        #     print("path {0}:不存在!".format(path))
