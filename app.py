# -*- coding: utf-8 -*-

"""
@Time : 2022/4/10
@Author : user
@File : app
@Description : pthon练习题
"""

# 1.进制转换
v1 = 675
print(bin(v1))

v2 = "0b11000101"
print(int(v2, 2))

v3 = "11000101"
print(int(v3, 2))

v1 = 123
v2 = 456
v3 = bin(v1)[2:] + bin(v2)[2:]
print(int(v3, 2))

v1 = 123
v2 = 456
v3 = bin(v1)[2:].zfill(16) + bin(v2)[2:].zfill(16)
print(int(v3, 2))

# 2.布尔值True、False。
# False：0, 空类型， None
# True："武沛齐"
# 456、666、345
if "":
    print(123)
else:
    print(456)

if 0:
    print(999)
else:
    print(666)

if "武沛齐":
    print(345)
else:
    print(110)

# 3.字符串操作：
# 让用户输入一段文本，请实现将文本中的敏感词 `苍老师`、`波波老师`替换为 `***`，最后并输入替换后的文本。
# 敏感词替换
text = input("请输入：") # 苍老师  波波老师  武沛齐
text = text.replace("苍老师 ", "***")
text = text.replace("波波老师", "***")
name = "aleX leNb "
# 移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 判断 name 变量是否以 "al" 开头,并输出结果
print(name.startswith("al"))
# 判断name变量是否以"Nb"结尾,并输出结果
print(name.endswith("Nb"))
# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
print(name.replace("l", "p"))
# 将 name 变量对应的值根据 所有的"l" 分割,并输出结果
print(name.split("l"))
# 将name变量对应的值根据第一个"l"分割,并输出结果
print(name.split("l", 1))
# 将 name 变量对应的值变大写,并输出结果
print(name.upper())
# 将 name 变量对应的值变小写,并输出结果
print(name.lower())
# 如何实现字符串的翻转？
print(name[::-1])
# 有字符串
s = "123a4b5c"
# 通过对s切片形成新的字符串 "123"
print(s[0:3])
# 通过对s切片形成新的字符串 "a4b"
print(s[3:6])
# 通过对s切片形成字符串 "c"
print(s[-1])
# 通过对s切片形成字符串 "ba2"
print(s[-3:0:-2])

# 4.循环字符串
# while循环输出
message = "伤情最是晚凉天，憔悴厮人不堪言"
# index = 0
# while index < int(len(message)):
#     print(message[index])
#     index += 1
# for循环输出
# for item in message:
#     print(item)
# 倒叙输出
for item in range(len(message))[::-1]:
    print(message[item])
# 使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"。
num_list = [3,2,1]
for item in num_list:
    print("倒计时{}秒".format(item))
# 让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果。
text = input("请输入：")
count = 0
for item in text:
    if item == "浪":
        count += 1
print(count)
# 获取用户两次输入的内容，并提取其中的数字，然后实现数字的相加（转换为整型再相加）：
# 要求：
# 将num1中的的所有数字找到并拼接起来：1232312
# 将num1中的的所有数字找到并拼接起来：1218323
# 然后将两个数字进行相加。
# 请补充代码
num1 = input("请输入：")# asdfd123sf2312
num1_list = []
for item in num1:
    if item.isdecimal():
        num1_list.append(item)
data1 = "".join(num1_list)
print(data1)

num2 = input("请输入：") # asdfd123sf2312
num2_list = []
for item in num2:
    if item.isdecimal():
        num2_list.append(item)
data2 = "".join(num2_list)
print(data2)

result = int(data1) + int(data2)
print(result)




