#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
input_pic_path = "./Drone_make_picture"
txt1 = './picture.txt'#图片文件名存放txt文件地址
f1 = open(txt1,'a')#打开文件流
for filename in os.listdir(input_pic_path):
    f1.write(filename.rstrip('.JPG'))#只保存名字，去除后缀.jpg
    f1.write("\n")#换行
f1.close()#关闭文件流











