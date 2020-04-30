#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-30 下午 15:54
#  @Note    :

import xml.etree.ElementTree as ET

tree=ET.parse("xml_test.xml")
root=tree.getroot()
print(root.tag)


#遍历xml_test 文档
# for child in root:
#     print("------",child.tag,child.attrib)
#     for i in child:
#         print("*****",i.tag,i.attrib,i.text)
#         for j in i:
#             print("ssss",j.tag,j.text)

#只遍历 节点
for node in root.iter("sex"):
    print(node.tag,node.text)