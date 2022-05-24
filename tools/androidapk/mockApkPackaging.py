# -*- coding: UTF-8 -*-
from base.ZipUtils import add_file_to_zip
from fold.core.DealFilesByFolder import *
import os
import shutil

# config
# ====>用来练习的android的项目：https://github.com/luhaoaimama1/MockApkPackaging

aaptPath = "/Users/fuzhipeng/Library/Android/sdk/build-tools/30.0.3/aapt2"
dxPath = "/Users/fuzhipeng/Library/Android/sdk/build-tools/30.0.3/dx"
apkSignerPath = "/Users/fuzhipeng/Library/Android/sdk/build-tools/30.0.3/apksigner"
sdkPath = "/Users/fuzhipeng/Library/Android/sdk/platforms/android-28/android.jar"

projectMainPath = "/Users/fuzhipeng/AndroidStudioProjects/Aapt2/app/src/main"
packageName = "com/example/aapt2"



# -----------------------------------内部变量-------------------------------------------------------------
assetFilePaths = []
genFlatPath = os.path.join(projectMainPath, "genFlat")
genPath = os.path.join(projectMainPath, "gen")
buildPath = os.path.join(projectMainPath, "build")
classesPath = os.path.join(buildPath, "classes.dex")
genOutApkPath = os.path.join(genPath,"output.apk")
genOutApkPathForSign = os.path.join(genPath,"outputForSign.apk")
resPath = os.path.join(projectMainPath, "res")
javaPath = os.path.join(projectMainPath, "java/%s" % packageName)

def createExtreFold():
    if os.path.exists(genFlatPath):
        shutil.rmtree(genFlatPath)
    if os.path.exists(genPath):
        shutil.rmtree(genPath)
    if os.path.exists(buildPath):
        shutil.rmtree(buildPath)

    # gen save aapt中间层 R.java aapt的apk
    if not os.path.exists(genFlatPath):
        os.makedirs(genFlatPath)
    if not os.path.exists(genPath):
        os.makedirs(genPath)
    if not os.path.exists(buildPath):
        os.makedirs(buildPath)


def aapt():
    createExtreFold()

    # aapt 资源编译 获取flat等中间资源
    commandline = aaptPath + \
                  " compile" + \
                  " --dir " + resPath + \
                  " -o " + genFlatPath
    print(commandline)
    os.system(commandline)

    # aapt 链接资源

    # 拼接所有资源文件的路径
    class FileCallback3(FileCallback):
        def dealFile(self, fold, fileName):
            filePath = os.path.join(fold, fileName)
            assetFilePaths.append(" " + filePath)

    findFileByFold(genFlatPath, FilterCallback(), FileCallback3())
    assetFilePathStrings = "".join(assetFilePaths)

    # 生成资源文件的apk 包括arsc与mainfest还有资源
    # --java 生成R.java 等待javac编译
    commandline2 = aaptPath + \
                   " link" + \
                   " -o " + genOutApkPath + \
                   " -I " + sdkPath + \
                   " {0}" \
                   " --java " + genPath + \
                   " --manifest " + projectMainPath + "/AndroidManifest.xml -v"
    commandline__format = commandline2.format(assetFilePathStrings)
    print(commandline__format)
    os.system(commandline__format)

def javac():
    # 编译java文件  这里跳过 编译aidl文件
    # 　-source 1.7 -target 1.7：指定编译的jdk版本，如果不指定的话，会报错。
    # 　-encoding ：编码方式，这里设置UTF-8  　
    # 　-bootclasspath :引导类文件的路径，这里需要使用到android.jar中的Android API。  　　
    #   -d ：生成的class文件存放路径
    os.system("javac -source 1.7 -target 1.7 -encoding UTF-8"
              " -bootclasspath " + sdkPath +
              " -d " + buildPath +
              " " + javaPath + "/*.java" +
              " " + os.path.join(genPath, packageName) + "/R.java"
              )

def javacDex():
    # 把编译的java文件变成dex
    os.system(dxPath +
              " --dex "
              "--output=" + classesPath +
              " " + buildPath)


def packageDexToApk():
    # 把dex 添加到apk 中
    add_file_to_zip(classesPath, genOutApkPath)


def apkSign():
    # apk文件复制到最终的输出目录
    os.system("cp"
              " " + genOutApkPath +
              " " + genOutApkPathForSign)

    # 签名
    # 不签名 不能安装  会报错[INSTALL_PARSE_FAILED_NO_CERTIFICATES: Failed to collect certificates from
    # 默认签名：For Linux or Mac OS User: ~/.android/debug.keystore 参考:https://developer.android.com/studio/publish/app-signing#debug-mode
    # " $ jarsigner -verbose -keystore ~/.android/debug.keystore " \
    # "-storepass android " \
    # "-keypass android app/src/main/out/app.apk androiddebugkey"
    # 获取签名
    # keytool -list -v -keystore /Users/fuzhipeng/AndroidStudioProjects/Aapt2/app/src/main/keytools/keystore.jks
    # 最后需要签名密码才能获取信息
    # 新版签名apksigner
    os.system(apkSignerPath +
              " sign"
              " --ks /Users/fuzhipeng/AndroidStudioProjects/Aapt2/app/src/main/keytools/keystore.jks"
              " --ks-key-alias key0 --ks-pass pass:123456 --key-pass pass:123456 "
              " " + genOutApkPathForSign)
    # 签名认证下 看有没有效
    os.system(apkSignerPath +
              " verify"
              " " + genOutApkPathForSign)

if __name__ == '__main__':
    # aapt：https://developer.android.com/studio/command-line/apksigner
    # apksigner：https://developer.android.com/studio/command-line/apksigner#usage-sign
    # 编译打包流程参考文章：https://juejin.cn/post/6844903466465230856

    aapt()

    javac()

    javacDex()

    packageDexToApk()

    apkSign()

    # 安装
    os.system("adb install " + genOutApkPathForSign)
