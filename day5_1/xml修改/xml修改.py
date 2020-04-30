#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-30 下午 16:11
#  @Note    :

import xml.etree.ElementTree as edit
tree=edit.parse("xml_test.xml")
root=tree.getroot()
print(root.tag)

for node in root.iter('sex'):
    new_sex="fe"
    node.text=new_sex
    node.set("update","yes")
tree.write("xml_test.xml")
