import os;

'''
更换文字
'''
# with open('''/Users/fuzhipeng/blog/source/_posts/uptest.md''',"r") as f:
#     content=f.readlines()
#
# with open('''/Users/fuzhipeng/blog/source/_posts/uptest.md''',"w") as f:
#     for line in content:
#         f.writelines(line.replace("test","test_"))


cdClean='''hexo c'''
cdGenerate='''hexo g'''
cdDeploy='''hexo d'''

cds=[
    cdClean,
    cdGenerate,
    cdDeploy,
]
os.chdir("/Users/fuzhipeng/blog")
# os.popen是阻塞的，不执行完不会执行下条语句的
for cd in cds:
    print(os.popen(cd).readlines())