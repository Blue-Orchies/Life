# -*- coding: utf-8 -*-

"""
@Time : 2022/4/11
@Author : user
@File : Python扑克牌
@Description : 
"""

color_list = ["红桃","黑桃","方片","梅花"]

num_list = []
for num in range(1, 14):
    num_list.append(num)

result = []
for color in color_list:
    for num in num_list:
        item = (color, num)
        result.append(item)
print(result)
