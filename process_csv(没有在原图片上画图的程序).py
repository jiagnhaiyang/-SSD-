#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import os
from PIL import Image
import time
from multiprocessing import Pool
def bouding_box(lines,input_pic,m,n,out_csv_path):
   for pic_file in os.listdir(input_pic):
      file_path = os.path.join(input_pic,pic_file)
      image = Image.open(file_path)
      img = cv2.imread(file_path)
      width, height = image.size  #获取测试图片的宽和高
      weight_avg = int(width / m) #获取原始图片分割后每张小图的宽
      heigh_avg = int(height / n)  #获取原始图片分割后每张小图的高
      for i , name in enumerate(lines):
         #从csv文件每一行的第一列里获取原始图片的名字以及分割后生成的每一张小图片名字的后半部分
         #具体可参照csv文件里图片的命名方式
         img_name = name.split(",")[0].split("/")[1].split("_")[1].split(".")[0]  # 分割后小图片名字的后半部分
         org_img_name = name.split(",")[0].split("/")[1].split("_")[0] + ".jpg"  # 测试图片的名字
         label_name = name.split(",")[5]  # 获取对应方框的类别名
         score = name.split(",")[6] #获取每一个类别的得分值
         score = float(score)
         text = label_name + ":" + str(round(score,2))  #图片上每个框的类别及得分值

         #当类别名为crack时
         if label_name == "crack":
            if org_img_name == pic_file:    # 如果原图片的名字和分割后图片名字的前半部分一样，说明分割后的图片是由这个原图片生成的
               if img_name == "DS01":  #原始图片分割出来的第一张小图片
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4])

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS02":  #原始图片分割出来的第二张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3])+ int(weight_avg)
                  new_ymax = int(name.split(",")[4])

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS03":  #原始图片分割出来的第三张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)*2
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)*2
                  new_ymax = int(name.split(",")[4])

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS04":  #原始图片分割出来的第四张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)*3
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)*3
                  new_ymax = int(name.split(",")[4])

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS05":  #原始图片分割出来的第五张小图片
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS06":  #原始图片分割出来的第六张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS07":  #原始图片分割出来的第七张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)*2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)*2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS08":   #原始图片分割出来的第八张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)*3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)*3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS09":  #原始图片分割出来的第九张小图片
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)*2
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)*2

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS10":  #原始图片分割出来的第十张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS11":  #原始图片分割出来的第十一张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)*2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)*2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS12":  #原始图片分割出来的第十二张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)*3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)*3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS13":  #原始图片分割出来的第十三张小图片
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS14":  #原始图片分割出来的第十四张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS15":  #原始图片分割出来的第十五张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)*2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)*2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS16":  #原始图片分割出来的第十六张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)*3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)*3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
         #当类别名为line时
         else:
            if org_img_name == pic_file:
               if img_name == "DS01":     #原始图片分割出来的第一张小图片
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4])

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS02":  #原始图片分割出来的第二张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4])

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS03":  #原始图片分割出来的第三张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 2
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 2
                  new_ymax = int(name.split(",")[4])

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS04":  #原始图片分割出来的第四张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 3
                  new_ymin = int(name.split(",")[2])
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 3
                  new_ymax = int(name.split(",")[4])

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS05":  #原始图片分割出来的第五张小图片
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS06":  #原始图片分割出来的第六张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS07":  #原始图片分割出来的第七张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS08":  #原始图片分割出来的第八张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg)
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg)

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS09":  #原始图片分割出来的第九张小图片
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS10":  #原始图片分割出来的第十张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS11":   #原始图片分割出来的第十一张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS12":  #原始图片分割出来的第十二张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 2
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 2

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS13":  #原始图片分割出来的第十三张小图片
                  new_xmin = int(name.split(",")[1])
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3])
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS14":  #原始图片分割出来的第十四张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg)
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg)
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS15": #原始图片分割出来的第五张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 2
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 2
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
               elif img_name == "DS16": #原始图片分割出来的第十六张小图片
                  new_xmin = int(name.split(",")[1]) + int(weight_avg) * 3
                  new_ymin = int(name.split(",")[2]) + int(heigh_avg) * 3
                  new_xmax = int(name.split(",")[3]) + int(weight_avg) * 3
                  new_ymax = int(name.split(",")[4]) + int(heigh_avg) * 3

                  WriteinCSV(out_csv_path, pic_file, str(new_xmin), str(new_ymin), str(new_xmax), str(new_ymax),
                             label_name, str(score))
      #cv2.imwrite("/home/jhy/wave_test/ultimate_img/" + pic_file, img)

   end_time = time.time()
   print "一共耗时:%ds" % (end_time-start_time)

#写入新的csv文件中
def WriteinCSV(OutputCSVFileName,image_name,xmin,ymin,xmax,ymax,label_name,score):
    WriteCSVFile = open(OutputCSVFileName, 'a')
    one_line_data = [image_name,xmin,ymin,xmax,ymax,label_name,score]
    WriteCSVFile.write(",".join(one_line_data) + "\n")
    WriteCSVFile.close()

def remove(InputImagePath):
   for i in os.listdir(InputImagePath):
      ri = os.path.join(InputImagePath, i)
      os.remove(ri)

if __name__ == "__main__":
   start_time = time.time()
   m = 4
   n = 4
   #T = os.path.exists('/var/caffe/img_segment/models/reult_forktest_images/result.csv')
   T = os.path.exists('./result.csv')
   if T == True:
      #with open('/var/caffe/img_segment/models/reult_forktest_images/result.csv', 'r') as p:
      with open('./result.csv', 'r') as p:
         # with open('./result.csv', 'r') as p:
         lines = p.read().splitlines()  # 读出csv文件的每一行数据
      #input_pic = "/var/caffe/img_segment/src_1"
      input_pic = "./INTER_cubic"
      # input_pic = "./INTER_cubic"
      # out_csv_path = "./out_result/new_result.csv"
      #out_csv_path = "/var/caffe/img_segment/1.csv"
      out_csv_path = "./out_result/new_result1.csv"
      font = cv2.FONT_HERSHEY_DUPLEX  # 画框标注时的字体
      bouding_box(lines, input_pic, m, n, out_csv_path)
      print "1.csv文件已生成"
      # InputImagePath_1 = "/var/caffe/img_segment/models/split_16_img"
      # InputImagePath_2 = "/var/caffe/img_segment/models/reult_forktest_images"
      # InputImagePath_3 = "/var/caffe/img_segment/src_1"
      # InputImagePath_4 = "/var/caffe/img_segment/models/result"
      InputImagePath_1 = "./Drone_make_picture"
      InputImagePath_2 = "./Drone_transform_xml"
      InputImagePath_3 = "./INTER_nearest"
      InputImagePath_4 = "./ceshi"
      InputImagePath = [InputImagePath_1,InputImagePath_2,InputImagePath_3,InputImagePath_4]
      po = Pool(4)
      for i , InputImagePath in enumerate(InputImagePath):
         po.apply_async(remove,(InputImagePath,))
      print("----start----")
      po.close()  # 关闭进程池，关闭后po不再接收新的请求
      po.join()  # 等待po中所有?进程执?完成，必须放在close语句之后
   else:
      WriteCSVFile = open("1.csv", 'w')
      WriteCSVFile.close()
      remove()







































