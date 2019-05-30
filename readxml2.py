#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import sys
import os
import time
import xml.dom.minidom as minidom
reload(sys)
def new_size(old, new_xmin, new_ymin, new_xmax, new_ymax):
    old.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(int(new_xmin)),
                                                                          encoding='utf-8')
    old.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(int(new_xmax)),
                                                                          encoding='utf-8')
    old.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(int(new_ymin)),
                                                                          encoding='utf-8')
    old.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(int(new_ymax)),
                                                                          encoding='utf-8')
def resize_xml(xml,xmlname,result_path,n):
    annotation = minidom.parse(xml)
    print(annotation)
    size = annotation.getElementsByTagName("size")
    name = annotation.getElementsByTagName("filename")

    width = size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue
    width = int(width)

    height = size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue
    name = name[0].childNodes[0].data

    height = int(height)
    item_width = int(width / n) #将图片的宽分成n份
    item_height = int(height / n) #将图片的高分成n份
    box_list = []
    # (left, upper, right, lower)
    for i in range(0, n):
        for j in range(0, n):
            box = (j * item_width, i * item_height, (j + 1) * item_width, (i + 1) * item_height)
            box_list.append(box)
    for i in range(len(box_list)):
        ef = False
        new_ann = minidom.parse(xml)
        obj = new_ann.getElementsByTagName("object")
        bndbox = new_ann.getElementsByTagName("bndbox")
        for j, z in enumerate(bndbox):
            xmin = int(str(z.getElementsByTagName("xmin")[0].childNodes[0].nodeValue))
            xmax = int(str(z.getElementsByTagName("xmax")[0].childNodes[0].nodeValue))
            ymin = int(str(z.getElementsByTagName("ymin")[0].childNodes[0].nodeValue))
            ymax = int(str(z.getElementsByTagName("ymax")[0].childNodes[0].nodeValue))
            #box_list[i][0],box_list[i][1],box_list[i][2],box_list[i][3]
            if (xmin > box_list[i][2] or ymin > box_list[i][3] or ymax < box_list[i][1] or xmax < box_list[i][0]):
                new_ann.documentElement.removeChild(obj[j])
                continue
            else:
                ef = True
                #f = open(os.path.join(result_path, (str(i) + "_" + xmlname.split('.')[0] + "_" + str(j) + '.xml')), 'w')
                if xmin > box_list[i][0] and xmax < box_list[i][2]:
                    if ymin > box_list[i][1] and ymax < box_list[i][3]:
                        new_size(z, xmin - box_list[i][0], ymin - box_list[i][1], xmax - box_list[i][0],
                                 ymax - box_list[i][1])
                    elif ymin < box_list[i][1] and ymax < box_list[i][3]:
                        new_size(z, xmin - box_list[i][0], 0, xmax - box_list[i][0],
                                 ymax - box_list[i][1])
                    elif ymin > box_list[i][1] and ymax > box_list[i][3]:
                        new_size(z, xmin - box_list[i][0], ymin - box_list[i][1], xmax - box_list[i][0],
                                 box_list[i][3] - box_list[i][1])
                    else:
                        new_size(z, xmin - box_list[i][0], 0, xmax - box_list[i][0], box_list[i][3] - box_list[i][1])
                elif xmin < box_list[i][0] and xmax < box_list[i][2]:
                    if ymin > box_list[i][1] and ymax < box_list[i][3]:
                        new_size(z, 0, ymin - box_list[i][1], xmax - box_list[i][0],
                                 ymax - box_list[i][1])
                    elif ymin < box_list[i][1] and ymax < box_list[i][3]:
                        new_size(z, 0, 0, xmax - box_list[i][0],
                                 ymax - box_list[i][1])
                    elif ymin > box_list[i][1] and ymax > box_list[i][3]:
                        new_size(z, 0, ymin - box_list[i][1], xmax - box_list[i][0],
                                 box_list[i][3] - box_list[i][1])
                    else:
                        new_size(z, 0, 0, xmax - box_list[i][0], box_list[i][3] - box_list[i][1])

                elif xmin > box_list[i][0] and xmax > box_list[i][2]:
                    if ymin > box_list[i][1] and ymax < box_list[i][3]:
                        new_size(z, xmin - box_list[i][0], ymin - box_list[i][1], box_list[i][2] - box_list[i][0],
                                 ymax - box_list[i][1])
                    elif ymin < box_list[i][1] and ymax < box_list[i][3]:
                        new_size(z, xmin - box_list[i][0], 0, box_list[i][2] - box_list[i][0],
                                 ymax - box_list[i][1])
                    elif ymin > box_list[i][1] and ymax > box_list[i][3]:
                        new_size(z, xmin - box_list[i][0], ymin - box_list[i][1], box_list[i][2] - box_list[i][0],
                                 box_list[i][3] - box_list[i][1])
                    else:
                        new_size(z, xmin - box_list[i][0], 0, box_list[i][2] - box_list[i][0], box_list[i][3] - box_list[i][1])
                else:
                    if ymin > box_list[i][1] and ymax < box_list[i][3]:
                        new_size(z, 0, ymin - box_list[i][1], box_list[i][2] - box_list[i][0],
                                 ymax - box_list[i][1])
                    elif ymin < box_list[i][1] and ymax < box_list[i][3]:
                        new_size(z, 0, 0, box_list[i][2] - box_list[i][0],
                                 ymax - box_list[i][1])
                    elif ymin > box_list[i][1] and ymax > box_list[i][3]:
                        new_size(z, 0, ymin - box_list[i][1], box_list[i][2] - box_list[i][0],
                                 box_list[i][3] - box_list[i][1])
                    else:
                        new_size(z, 0, 0, box_list[i][2] - box_list[i][0], box_list[i][3] - box_list[i][1])

        if ef == True:
            f = open(os.path.join(result_path, (str(i) + "_" + str(j) + os.path.splitext(xmlname)[0] + '.xml')), 'w')
            size = new_ann.getElementsByTagName("size")
            for k, z in enumerate(size):
                z.getElementsByTagName("width")[0].childNodes[0].nodeValue = unicode(str(item_width),
                                                                                      encoding='utf-8')
                z.getElementsByTagName("height")[0].childNodes[0].nodeValue = unicode(str(item_height),
                                                                                     encoding='utf-8')
            # new_ann = minidom.parse(xml)
            # annotation = new_ann.getElementsByTagName("annotation")
            # for n in annotation:
            #     n.getElementsByTagName("filename")[0].childNodes[0].nodeValue = unicode(
            #         str(i) + "_" + str(j) + os.path.splitext(xmlname)[0] + '.xml',
            #         encoding='utf-8')
            new_ann.writexml(f, encoding='utf-8')
            f.close()
        else:
            continue

if __name__ == "__main__":
    n=4
    XML_path='./Drone_transform_xml'
    #XML_path='DSC00001.xml'
    XML_out='./xml_out'
    for xml_file in os.listdir(XML_path):
        xmlname = xml_file
        xml = os.path.join(XML_path, xmlname)

        resize_xml(xml, xmlname, XML_out,n)
