#coding=utf-8

import os
import json
import re
#视频合并
path='D:/meinv/afree/2.ts'
f=open(path,'wb')
for i in range(0,3000):
 try:
    file='1'+' ('+str(i)+')'+'.ts'
    path1='D:/meinv/afree/20171021/'+file
    f1=open(path1,'rb')           #  要读取二进制文件，比如图片、视频等等，用’rb’模式打开文件即可
    data=f1.read()
    f1.close()
    f.write(data)
    print '成功合并了文件：',file
 except:
     pass
f.close()




