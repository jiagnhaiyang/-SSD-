#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image
import os
imgname = 0
def pingjie(imgs,weigh_size,high_size):
    print('------------pingjie-------------')
    global imgname
    target = Image.new('RGB', (weigh_size * 4, high_size * 1))  # 拼接前需要写拼接完成后的图片大小 1200*600
    for i in range(len(imgs)):
        a = weigh_size * i  # 图片距离左边的大小
        b = 0  # 图片距离上边的大小
        c = weigh_size * (i + 1)  # 图片距离左边的大小 + 图片自身宽度
        d = high_size  # 图片距离上边的大小 + 图片自身高度
        target.paste(imgs[i], (a, b, c, d))
        print('拼接图片的路径为：', path1 + str(imgname) + '.jpg')
    target.save(path1 + "/" + str(imgname) + '.jpg')
    imgname += 1
def pj(k):
    print('------------pj-------------')
    # 取1,3是因为每行拼接完整都是最后那个，第一行是0，1命名，第二行是2,3命名，所以取后面那个值
    imglist = os.listdir(path1)
    #imglist = [0,1,2,3]
    print(imglist)
    j = int(4*k)
    img = []
    for i in range(4):
        print('完整行的拼接路径为：%s' % (path1 + "/" + imglist[i+j] + '.jpg'))
        img.append(Image.open(path1 + "/" + str(i+j) + '.jpg'))
    target = Image.new('RGB', (weigh_size * 4, high_size * 4))  # 拼接前需要写拼接完成后的图片大小 1200*1200
    for i in range(4):
        a = 0  # 图片距离左边的大小
        b = high_size * i  # 图片距离上边的大小
        c = weigh_size * 4  # 图片距离左边的大小 + 图片自身宽度
        d = high_size * (i + 1)  # 图片距离上边的大小 + 图片自身高度
        target.paste(img[i], (a, b, c, d))
        global imgname
        with open('somefile.txt', 'r') as f:
            content = f.read().splitlines()
        target.save(path2 + "/" + content[k] + '.jpg')
if __name__ == '__main__':
    weigh_size = 1840  # 图片的宽高都为600像素
    high_size = 1228
    after_spli_img_path = '/home/jhy/wave_test/result'  # 存放要拼接图片的目录
    path1 = '/home/jhy/wave_test/Temporary_img'  # 拼接后图片的存放目录
    path2 = "/home/jhy/wave_test/ultimate_img"
    img_list = os.listdir(after_spli_img_path)
    for k in range(int(len(img_list) / 16)):
        print(img_list)
        for i in range(4):  # 有两行，所以需要循环两次
            images = []  # 每一次拼接只能一行一行拼接，不能在第一行拼接完后再在其基础上拼接第二行的图片，矩阵不允许这样操作
            for j in range(4):  # 每行有两张图片，所以也要循环两次
                a = k * 16 + i * 4 + j
                images.append(Image.open(after_spli_img_path + "/" + img_list[a]))
            print('第 {} 行拼接完成'.format(i))
            pingjie(images, weigh_size, high_size)
        pj(k)


