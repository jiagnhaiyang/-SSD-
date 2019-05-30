#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import cv2
input_pic_path = "./Drone_make_picture"
input_xml_path = "./Drone_transform_xml"
out_pic = "./pic_out/"
list_pic = os.listdir(input_pic_path)
for i , xml_file_name in enumerate(os.listdir(input_xml_path)):
    print "处理第:%d"% i
    pic_file_name = os.path.splitext(xml_file_name)[0] + ".jpg"
    pic_file_path = os.path.join(input_pic_path,pic_file_name)
    image = cv2.imread(pic_file_path)
    cv2.imwrite(out_pic + pic_file_name, image)









