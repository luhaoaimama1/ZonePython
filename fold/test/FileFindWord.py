
import os;

def acess(file):
    print("文件存在==>",os.access(file,os.F_OK),end="\t")
    print("可读==>",os.access(file,os.R_OK),end="\t")
    print("可写==>",os.access(file,os.W_OK),end="\t")
    print("可执行==>",os.access(file,os.X_OK))

def main():
    paths=[]
    fold="/Users/fuzhipeng/Desktop/文章"
    newFold=os.path.join(fold, "zonehaha")
    if not os.path.exists(newFold):
        os.mkdir(newFold)
    else :
        os.rmdir(newFold)

    for file in os.listdir(fold):
        if(str(file).find("DS_Store")==-1):
            print(file,end='\t*******')
            acess(os.path.join(fold,file))
            paths.append(file)
            '''
            统计文字出现的次数   String.count
            '''
            try:
                with open(os.path.join(fold,file),"r") as rf:
                    content=rf.readlines()
                    print("我出现的次数:",repr(content).count("我"))
            except:
                pass

    print("存入的文件：",paths)

if __name__ == '__main__':
    main()