#!/usr/bin/python
# -*- coding: utf-8 -*-
# 条件语句和逻辑判断的使用，pass,eval,exec等函数并为列出，只作为了解
__author__ = 'neptune'
print(bool(0))
print(bool("hahaha"))
name = raw_input("what's your name?")
if name.endswith("csm"):
    print "hello. mr csm"
elif name.__eq__("lazio"):
    print "champion"
else:
    print "hello. stranger"

print("alpha" < "beta")

if "111" == "111" or 33 == 33:      # and和or是逻辑与和逻辑或语法
    print("ok,equals")
dic = {"jw", "csm", "xuli"}
for i in dic:       # for 循环
    print(i)
for idx, string in enumerate(dic):  # 使用编号迭代
    print(idx, string)

print(sorted(dic))  # 排序
print(list(reversed([111, 333, 222, 000])))     # 反转列表

innerLoop = [x*x*x for x in xrange(10) if x % 3 == 0]       # 轻量级循环
print(innerLoop)

# 优选方案，判断男孩女孩名字列表首字母相同的项
girls = ['alice', 'bernate', 'clarice']
boys = ['arnold', 'chris', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)        # 默认字典是key，空列表，再放入girl名称到key对应的列表中
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]
#
x = -1
while x < 20:
    print x
    x += 1

assert 30 < x < 100, "this is not legal value"       # 断言语法



