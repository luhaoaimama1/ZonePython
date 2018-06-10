
# 创建目录
# os.mkdir("D:\\python\\2")
# 删除目录
# os.rmdir("D:\\python\\2")
# 获取当前目录
# os.getcwd()
#  命令行 更换目录 相当于cd 某个文件
# os.chdir("/Users/fuzhipeng/blog")
'''os.popen("cd /Users/fuzhipeng/blog") 这种方式是无效的！'''
# 重命名
# os.rename(pathStr,newPathStr)


# Tips os.path 才是 file的感觉

# 该路径是否是文件夹
# os.path.isdir("文件路径")
# 该路径是否是文件夹
# os.path.isfile("文件路径")

# 该路径是否存在
# os.path.exists(fold)

# 分离路径得到后缀名 和前椎名 [0]前椎名 [1]后缀名
# os.path.splitext(fileName)


def acess(file):
    print("文件存在==>",os.access(file,os.F_OK),end="\t")
    print("可读==>",os.access(file,os.R_OK),end="\t")
    print("可写==>",os.access(file,os.W_OK),end="\t")
    print("可执行==>",os.access(file,os.X_OK))
