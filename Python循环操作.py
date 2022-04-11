# -*- coding: utf-8 -*-

"""
@Time : 2022/4/11
@Author : user
@File : Python循环操作
@Description : 
"""

message = "伤情最是晚凉天，憔悴厮人不堪言"
index = 0
while index < len(message):
    print(message[index])
    index = index + 1

for item in message:
    print(item)

for item in range(len(message))[::-1]:
    print(message[item])

# "倒计时3秒"，"倒计时2秒"，"倒计时1秒"
for item in range(3,0,-1):
    print("倒计时{}秒".format(item))

# 让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果。
text = input("请输入：")
count = 0
for item in text:
    if item == "浪":
        count = count + 1
print(count)

num1 = input("请输入：")  # asdfd123sf2312
data1 = ""
for item in num1:
    if item.isdecimal():
        data1 += item

num2 = input("请输入：")  # a12dfd183sf23
data2 = ""
for item in num2:
    if item.isdecimal():
        data2 += item
print(data1)
data3 = int(data1) + int(data2)
print(data3)