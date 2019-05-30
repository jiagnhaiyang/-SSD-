#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
对超声波图片进行批量裁剪
"""
import os
import cv2

def clear_line(ic_path):
    img1 = cv2.imread(ic_path)[41:233]      #192
    # img1 = cv2.imread(ic_path)[84: 276]
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ii = []
    wight, long = img1.shape[:2]
    for i in range(wight):
        if img[i][0] > 230 or img[i][long - 1] > 230:
            ii.append(i)
    for i in ii:
        for j in range(long):
            if img[i + 1][j] == 0 and img[i - 1][j] == 0:
                img1[i][j] = 0
            elif img[i + 1][j] == 0 and img[i - 1][j] != 0:
                img1[i][j] = img1[i - 1][j]
            elif img[i + 1][j] != 0 and img[i - 1][j] == 0:
                img1[i][j] = img1[i + 1][j]
            elif img[i + 1][j] != 0 and img[i - 1][j] != 0:
                img1[i][j] = img1[i + 1][j]
    return img1

def Ato_run(loadpath,savepath):
    load_path = loadpath
    save_path = savepath
    for i in os.listdir(load_path):
        # # pic_name = i
        iw = i.split('.')[0]
        ni = '{}.jpg'.format(iw)
        picload_path = os.path.join(load_path,i)
        picsave_path = os.path.join(save_path,ni)
        print(picsave_path)
        imge2 = clear_line(picload_path)
        cv2.imwrite(picsave_path, imge2)

if __name__ == '__main__':
    load_path = './111'
    save_path = './pic_out'
    Ato_run(load_path, save_path)
    # for i in os.listdir('456/'):
    #     picfile_path = os.path.join('456', i)
    #     load_path = os.path.join('456', i)
    #     save_path = os.path.join('cuted',i)
    #     Ato_run(load_path, save_path)

# for i in os.listdir('456批数据分类/'):
#     picfile_path = os.path.join('456批数据分类/',i)
#     for c in os.listdir(picfile_path):
#         # print(c)
#         pic_path = os.path.join(picfile_path,c)
#         im = cv2.imread(pic_path)[84: 276]

