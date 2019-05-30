#-*-coding: UTF -8-*-
###############################
# 按照图片最短边缩放到512的比例对图片进行缩小或者放大
# 同时对XML进行更改
###############################
import cv2
import sys
import os
import xml.dom.minidom as minidom
reload(sys)
sys.setdefaultencoding( "utf-8" )

def resize_image(imageName, filepath,resultPath,TargetSize):
    pre_image=cv2.imread(filepath)
    pre_height = pre_image.shape[0]  #垂直像素
    print("11111111111")
    print(pre_height)
    pre_width = pre_image.shape[1]   #水平像素
    if (pre_width < pre_height):
        ratio =float(TargetSize)/ pre_width
        need_width=TargetSize
        need_height=pre_height*ratio
    else:
        ratio = float(TargetSize) / pre_height
        need_height=TargetSize
        need_width=pre_width*ratio
    image_resize=cv2.resize(pre_image,(int(need_width),int(need_height)),interpolation=cv2.INTER_AREA)  #(fx,fy)
    height=image_resize.shape[0]
    width=image_resize.shape[1]
    print width
    print height
    cv2.imwrite(resultPath + imageName, image_resize)

def resize_xml(xmlname,xml_path,result_path,TargetSize):
    annotation = minidom.parse(xml_path)
    size = annotation.getElementsByTagName("size")
    width = size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue
    height = size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue
    width = int(str(width))
    height = int(str(height))

    # 宽长高短
    if(width > height):
        ratio = float(TargetSize) / height
        print ratio
        des_pic_width=int(ratio*width)
        des_pic_height=TargetSize
        print des_pic_width
        print des_pic_height
        size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue = unicode(str(des_pic_width), encoding='utf-8')
        size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue = unicode(str(des_pic_height), encoding='utf-8')
        bndbox = annotation.getElementsByTagName("bndbox")
        for one in bndbox:
            xmin = one.getElementsByTagName("xmin")[0].childNodes[0].nodeValue
            xmin = int(str(xmin))
            one.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(int(ratio * xmin)),
                                                                                  encoding='utf-8')
            xmax = one.getElementsByTagName("xmax")[0].childNodes[0].nodeValue
            xmax = int(str(xmax))
            one.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(int(ratio * xmax)),
                                                                                  encoding='utf-8')
            ymin = one.getElementsByTagName("ymin")[0].childNodes[0].nodeValue
            ymin = int(str(ymin))
            one.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(int(ratio * ymin)),
                                                                                  encoding='utf-8')
            ymax = one.getElementsByTagName("ymax")[0].childNodes[0].nodeValue
            ymax = int(str(ymax))
            one.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(int(ratio * ymax)),
                                                                                  encoding='utf-8')

        f = open(os.path.join(result_path, xmlname), 'w')
        annotation.writexml(f, encoding='utf-8')
        f.close()
    else:
        ratio = float(TargetSize) / width
        #print ratio
        des_pic_width=TargetSize
        des_pic_height=int(ratio*height)
        #print des_pic_width
        #print des_pic_height
        size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue = unicode(str(des_pic_width), encoding='utf-8')
        size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue = unicode(str(des_pic_height),
                                                                                    encoding='utf-8')
        bndbox = annotation.getElementsByTagName("bndbox")
        for one in bndbox:
            xmin = one.getElementsByTagName("xmin")[0].childNodes[0].nodeValue
            xmin = int(str(xmin))
            one.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(int(ratio * xmin)),
                                                                                  encoding='utf-8')
            xmax = one.getElementsByTagName("xmax")[0].childNodes[0].nodeValue
            xmax = int(str(xmax))
            one.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(int(ratio * xmax)),
                                                                                  encoding='utf-8')
            ymin = one.getElementsByTagName("ymin")[0].childNodes[0].nodeValue
            ymin = int(str(ymin))
            one.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(int(ratio * ymin)),
                                                                                  encoding='utf-8')
            ymax = one.getElementsByTagName("ymax")[0].childNodes[0].nodeValue
            ymax = int(str(ymax))
            one.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(int(ratio * ymax)),
                                                                                  encoding='utf-8')

        f = open(os.path.join(result_path, xmlname), 'w')
        annotation.writexml(f, encoding='utf-8')
        f.close()


if __name__ == "__main__":
    TargetSize=512
    pic_path='./Drone_make_picture'
    pic_out_path='./pic_out/'
    XML_path='./Drone_transform_xml/'
    XML_out='./xml_out/'

    print "pic started"
    for pic_file in os.listdir(pic_path):
        filename=pic_file
        file_path = os.path.join(pic_path, filename)#路径拼接
        resize_image(filename,file_path,pic_out_path,TargetSize)
    print "xml started"
    for xml_file in os.listdir(XML_path):
        xmlname = xml_file
        xml = os.path.join(XML_path, xmlname)
        resize_xml(xmlname, xml, XML_out, TargetSize)
    print("process finish\n")
