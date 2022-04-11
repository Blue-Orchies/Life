# -*- coding: utf-8 -*-

"""
@Time : 2022/4/11
@Author : user
@File : Python列表循环
@Description : 
"""

# users = ["武沛齐","景女神","肖大侠"]
# count = 0
# for item in users:
#     print(count, item)
#     count += 1
# for index in range(len(users)):
#     print(index, users[index])

# users = ["武沛齐","景女神","肖大侠"]
# count = 1
# for item in users:
#     print(count, item)
#     count += 1
# for index in range(len(users)):
#     print(index+1, users[index])

# goods = ['汽车','飞机','火箭']
# for index in range(len(goods)):
#     print(index, goods[index])
# index = input("请输入索引：")
# index= int(index)
# text = goods[index]
# message = "您选择的商品是{}".format(text)
# print(message)
#
# # 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
# data_list = []
# for num in range(0,51):
#     if num == 0:
#         continue
#     data = num % 3
#     if data == 0:
#         data_list.insert(0, num)
# print(data_list)
#
# li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# data_list = []
# for item in li:
#     data = item.strip()
#     if data.startswith("a"):
#         data_list.append(data)
# print(data_list)
#
# result = []
# data = ["京1231", "冀8899", "京166631", "晋989"]
# for item in data:
#     if not item.startswith("京"):
#         continue
#     else:
#         result.append(data)
# count = len(result)
# print("京牌的数据为：{}.".format(count))
#
# name = "aleX leNb "
# value = input("请输入：")
# if value.startswith("al"):
#     print("是的")
# else:
#     print("不是的")
#
# value = input("请输入：")
# if value.endswith("Nb"):
#     print("是的")
# else:
#     print("不是的")
#
# name = name.replace("l", "p")
# print(name)
#
# value = input("请输入：")
# if value.isdecimal():
#     print(int(value))
# else:
#     print("请输入数字")
#
# data = input("请输入：")
# data_list = data.split("+", 1)
# if data_list[0].isdecimal() and data_list[1].isdecimal():
#     print("都是整数")
# else:
#     print("不全是整数")

# data = input("请输入：")
# data_list = data.split("+", 1)
# v1 = int(data_list[0].strip())
# v2 = int(data_list[1].strip())
# result = v1 + v2
# print(result)

import random

# code = random.randrange(1000, 9999)  # 生成动态验证码，整型
# code = str(code)  # 字符串类型
# msg = "欢迎登录PythonAV系统，您的验证码为：{},手机号为：{}".format(code, "15131266666")
# print(msg)
#
# phone = input("请输入手机号：")
# data = input("请输入验证码：")  # 字符串类型
# if code.lower() == data.lower() and phone == "15131266666":
#     print("登录成功")
# else:
#     print("登录失败")

data_list = []
while True:
    hobby = input("请输入你的爱好（Q/q退出）：")
    if hobby.upper() == 'Q':
        break
    # 把输入的值添加到 data_list 中，如：data_list = ["小姨子","哥们的女朋友"]
    data_list.append(hobby)
result = "、".join(data_list)
    # 将所有的爱好通过符号 "、"拼接起来并输出
print(result)