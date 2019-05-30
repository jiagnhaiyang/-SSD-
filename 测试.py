#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import xml.dom.minidom as minidom
reload(sys)
fork = []
def resize_xml(xml,out_path,xml_file):
    # global counter
    annotation = minidom.parse(xml)
    object = annotation.getElementsByTagName("object")
    for i, obj in enumerate(object):
        name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        if name == "fork":
            obj.getElementsByTagName("name")[0].childNodes[0].nodeValue = unicode("crack",encoding='utf-8')
            fork.append(name)
    f = open(os.path.join(out_path, xml_file), 'w')
    annotation.writexml(f, encoding='utf-8')
    f.close()
if __name__ == "__main__":
    XML_path = './Drone_transform_xml'
    out_path = './xml_out'
    for xml_file in os.listdir(XML_path):
        xml = os.path.join(XML_path, xml_file)
        resize_xml(xml,out_path,xml_file)
    print "fork=", len(fork)





