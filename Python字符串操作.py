# -*- coding: utf-8 -*-

"""
@Time : 2022/4/11
@Author : user
@File : Python字符串操作
@Description : 
"""

# 让用户输入一段文本，请实现将文本中的敏感词 `苍老师`、`波波老师`替换为 `***`，最后并输入替换后的文本。
text = input("请输入：")
text.replace("苍老师", "***")
text.replace("波波老师", "***")
print(text)

name = "aleX leNb "
print(name.strip())
print(name.startswith("al"))
print(name.endswith("Nb"))
print(name.replace("l", "b"))
print(name.split("l"))
print(name.split("l", 1))
print(name.upper())
print(name.lower())

print(name[::-1])

s = "123a4b5c"
s1 = s[0:3]
s2 = s[3:6]
s3 = s[-1]
s4 = s[-3:0:-2]
