#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'neptune'
from math import pi
from string import maketrans
format = "Pi with three decimals: %.3f" #格式化字符串
print(format % pi)
title = "My Lazio is the champion" #find查找
print(title.find('Lazio'))
myList = ["totti", "is", "shabi"] #join方法
print(myList[-1])
print(" ".join(myList))
dirs = "", "usr", "bin", "env"
print("C:" + "\\".join(dirs))
print("this is a test replace".replace("this", "that")) #replace方法
print("      remove the blank     ".strip()) #去除首尾空格
table = maketrans('cs', 'kz')   #效率替换语法translate
print(table[97 : 123])