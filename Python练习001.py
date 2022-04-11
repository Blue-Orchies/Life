# -*- coding: utf-8 -*-

"""
@Time : 2022/4/11
@Author : user
@File : Python练习001
@Description : 
"""

# 写代码实现一个整数加法计算器(两个数相加)
# 需求：提示用户输入：5+9或5+9或5+9，计算出两个值的和（提示：先分割再转换为整型，再相加）
# text = input("请输入：")
# num_list = text.split("+", 1)
# result = int(num_list[0]) + int(num_list[1])
# print(result)

# 将 name 变量对应的值中的 所有的"l"替换为 "p",并输出结果
name = "alex"
name = name.replace("l", "p")
print(name)

# 字符串翻转
print(name[::-1])

# 通过对s切片形成字符串 "ba2"
s = "123a4b5c"
s1 = s[-3:0:-2]
print(s1)

# 通过对s切片形成新的字符串 "a4b"
s2 = s[3:6]
print(s2)

# 使用while循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。
message = "伤情最是晚凉天，憔悴厮人不堪言"
index = 0
while index < len(message):
    print(message[index])
    index += 1

# 使用for循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。
for item in message:
    print(item)

# 使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"。
for num in range(3,0,-1):
    print("倒计时{}秒".format(num))
print("出发!")

# 请在列表的第1个索引位置插入元素"Tony",并输出添加后的列表
# li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]
# li.insert(0, "Tony")
# print(li)

# 请将字符串 `s = "qwert"`的每一个元素到列表 `li` 中。
# s = "qwert"
# li.extend(s)
# print(li)

# 请删除列表中的第2个元素，并输出删除元素后的列表
li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]
li.remove("WuSir")

li.pop(1)

# 通过对li列表的切片形成新的列表 ["a",4,"b"]
li = [1, 3, 2, "a", 4, "b", 5,"c"]
v1 = li[3:6]
print(v1)

# 通过对li列表的切片形成新的列表 [3,"a","b","c"]
v2 = li[1::2]
print(v2)




lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# - 将列表lis中的第2个索引位置的值变成大写，并打印列表。
lis[2] = lis[2].upper()
print(lis)

# - 将列表中的数字3变成字符串"100"
lis[1] = "100"
lis[3][2][1][1] = "100"
print(lis)

# - 将列表中的字符串"tt"变成数字 101
lis[3][2][1][0] = 101
print(lis)

# - 在 "qwe"前面插入字符串："火车头"
lis[3].insert(0, "火车头")
print(lis)

# 1. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
#
#    1 武沛齐
#    2 景女神
#    3 肖大侠
users = ["武沛齐","景女神","肖大侠"]
count = 0
for item in users:
    count += 1
    print(count,item)



# - 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
#
#   0,汽车
#   1,飞机
#   2,火箭
# 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
goods = ['汽车', '飞机', '火箭']
while True:
    for index,item in enumerate(goods,0):
        print(index, item)
    chose = input("输入选择的商品：").strip()
    if chose.isdecimal():
        chose = int(chose)
        if index < len(goods):
            print("您选择的商品为：{}".format(goods[index]))
            break
        else:
            print("您输入的有误")
    else:
        print("您输入的非数字{}".format(chose))











