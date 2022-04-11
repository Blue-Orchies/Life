# -*- coding: utf-8 -*-

"""
@Time : 2022/4/11
@Author : user
@File : Python进制转换
@Description : 
"""

v1 = 675
v2 = "0b11000101"
v3 = "11000101"
print(bin(v1))
print(int(v2, base=2))
print(int(v3, base=2))

v1=123
v2=456
# 63432
v3 = bin(v1)[2:] + bin(v2)[2:]
print(int(v3, 2))

v1=123
v2=456
# 8061384
v3 = bin(v1)[2:].zfill(16) + bin(v2)[2:].zfill(16)
print(int(v3, 2))

