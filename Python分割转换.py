# -*- coding: utf-8 -*-

"""
@Time : 2022/4/11
@Author : user
@File : Python分割转换
@Description : 
"""

text = "wupeiqi|alex|eric"
data_list = text.split("|")
result = tuple(data_list)
print(result)