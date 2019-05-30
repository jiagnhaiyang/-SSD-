#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image
import os
def cut_image(image):
    width, height = image.size
    item_width = int(width / 4)
    item_height = int(height / 4)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0,4):
     for j in range(0,4):
         #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
         box = (j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height)
         box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list
#保存
def save_images(image_list,pic_file):
    index = 1
    with open('somefile.txt', 'r') as f:
        content = f.read().splitlines()
    for image in image_list:
        image.save("./ceshi/" + content[index] + "_" + pic_file)
        index += 1
if __name__ == '__main__':
    filepath = "./INTER_cubic"
    #filepath = r"./DSC00001.jpg_2.jpg"
    for pic_file in os.listdir(filepath):
        print(pic_file)
        file_path = os.path.join(filepath, pic_file)
        image = Image.open(file_path)
        image_list = cut_image(image)
        save_images(image_list,pic_file)
