#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import xml.dom.minidom as minidom
reload(sys)
trace = []
crack = []
line = []
def resize_xml(xml):
    #global counter
    global trace
    global crack
    global line
    annotation = minidom.parse(xml)
    object = annotation.getElementsByTagName("object")

    for i, obj in enumerate(object):
        name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        if name == "trace":
            trace.append(name)
        elif name == "crack":
            crack.append(name)
        else:
            line.append(name)
if __name__ == "__main__":
    XML_path='./xml_out'
    for xml_file in os.listdir(XML_path):
        xml = os.path.join(XML_path,xml_file)
        resize_xml(xml)
    print trace
    print "trace =",len(trace)
    print crack
    print "crack =",len(crack)
    print line
    print "line =",len(line)





