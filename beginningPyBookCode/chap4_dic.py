#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'neptune'
myphonebook = {"anderson": 88888, "candreva": 9999}     # 字典的使用
print(myphonebook["anderson"])
print(len(myphonebook))
myphonebook["candreva"] = 10000
print(myphonebook)
myphonebook.clear()
print(myphonebook)
dic = {"hello": "world", "anderson": 10}
print(dic.get("hello"))     # 用get来获取值不会有异常发生
myphonebook.update(dic)     # 用另一个字典来更新
print(myphonebook)



