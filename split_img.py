#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image
import os
def cut_image(image,m,n):
    width, height = image.size
    item_width = int(width / m)
    item_height = int(height / n)
    box_list = []
    for i in range(0,n):
     for j in range(0,m):
         #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
         box = (j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height)
         box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    print box_list
    return image_list
#保存
def save_images(image_list,pic_file):
    index = 1
    with open('somefile.txt', 'r') as f:
        content = f.read().splitlines()
    for image in image_list:
        image.save("/home/jhy/wave_test/split_16_img/" + os.path.splitext(pic_file)[0] + "_" + content[index] + ".jpg")
        index += 1
if __name__ == '__main__':
    m = 4
    n = 4
    #org_img_path = "./INTER_cubic"
    org_img_path = "/home/jhy/caffe-ssd/examples/images/ssd_test_image"
    # filepath = r"./DSC00001.jpg_2.jpg"
    for pic_file in os.listdir(org_img_path):
        print(pic_file)
        file_path = os.path.join(org_img_path, pic_file)
        image = Image.open(file_path)
        image_list = cut_image(image,m,n)
        save_images(image_list, pic_file)
    print("图片分割完毕")



