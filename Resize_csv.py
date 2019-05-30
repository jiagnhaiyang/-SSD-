#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import os
from PIL import Image


def WriteinCSV(OutputCSVFileName,image_name,xmin,ymin,xmax,ymax,label_name,score):
    WriteCSVFile = open(OutputCSVFileName, 'a')
    one_line_data = [image_name,xmin,ymin,xmax,ymax,label_name,score]
    WriteCSVFile.write(",".join(one_line_data) + "\n")
    WriteCSVFile.close()

def Resize_csv(lines,image,pic_file,m,n):

      width, height = image.size
      weight_avg = int(width / m)
      heigh_avg = int(height / n)
      for i , name in enumerate(lines):

          img_name = name.split(",")[0].split("/")[1].split("_")[1].split(".")[0]
          org_img_name = name.split(",")[0].split("/")[1].split("_")[0] + ".jpg"
          label_name = name.split(",")[5]
          score = name.split(",")[6]
          #score = float(score)
          if org_img_name == pic_file:
              if img_name == "DS01":
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4])
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax), label_name, str(score))
              elif img_name == "DS02":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4])
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS03":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 2
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 2
                  new_ymax = int(name.split(",")[4])
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS04":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 3
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 3
                  new_ymax = int(name.split(",")[4])
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS05":
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS06":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS07":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS08":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS09":
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS10":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS11":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS12":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS13":
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS14":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS15":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
              elif img_name == "DS16":
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3
                  WriteinCSV("new_csv", pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
if __name__ == "__main__":
    m = 4
    n = 4
    with open('./result.csv', 'r') as p:
    #with open('./result.csv', 'r') as p:
      lines = p.read().splitlines()
    #input_pic = "/home/jhy/caffe-ssd/examples/images/ssd_test_image"
    input_pic = "./INTER_cubic"
    #font = cv2.FONT_HERSHEY_DUPLEX
    for pic_file in os.listdir(input_pic):
        file_path = os.path.join(input_pic, pic_file)
        image = Image.open(file_path)
        #img = cv2.imread(file_path)
        Resize_csv(lines,image,pic_file,m,n)






















