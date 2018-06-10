import os;


fold='''/Users/fuzhipeng/Desktop/test'''
if not os.path.exists(fold):
    os.mkdir(fold)
    print( "|->", fold)
for index in range(3):
    newFold=os.path.join(fold, "_"+repr(index))
    if not os.path.exists(newFold):
        os.mkdir(newFold)
        print("|","\t" * 1,"|->" ,repr(index))
        for index2 in range(3):
            thirdFile=os.path.join(newFold, repr(index2) + ".txt")
            f=open(thirdFile,"w")
            f.close()
            print("|", "\t" * 2, "|->", repr(index2) + ".txt")
