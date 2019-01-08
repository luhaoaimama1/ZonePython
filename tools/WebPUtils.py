import os
import time
#
# # 遍历指定目录，显示目录下的所有文件名
def convertWebp2JpgInDirectory(dir):
    if os.path.isdir(dir):
        allfiles = os.listdir(dir)
        for fi in allfiles:
            fi_d = os.path.join(dir, fi)
            if os.path.isdir(fi_d):
                convertWebp2JpgInDirectory(fi_d)
            else:
                if fi_d.endswith(".jpg"):
                    webp = os.path.join(dir, fi_d)
                    filename = webp.split("/")[-1]
                    filedir = "/".join(webp.split("/")[:-1])
                    filedir = "%s_jpg"%filedir
                    if not os.path.exists(filedir):
                        os.makedirs(filedir)
                    jpg = "%s/%s"%(filedir, filename)
                    commandline = "./dwebp %s -o %s" % (webp, jpg)
                    os.system(commandline)
                    print(webp + " ------> 转换成功")


if __name__ == "__main__":
    # webp google工具包 地址
    webpath="/Users/fuzhipeng/Downloads/libwebp-0.4.1-mac-10.8/bin/cwebp"
    convertWebp2JpgInDirectory("/path/to/directory")

# 作者：orzangleli
# 链接：https://www.jianshu.com/p/e940397d8822