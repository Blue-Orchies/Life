# -*- coding: utf-8 -*-

"""
@Time : 2022/4/11
@Author : user
@File : Python列表作业
@Description : 
"""

li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]

# print(len(li))

li.append("seven")


li.insert(1, "Tony")


li.insert(2, "Kelly")


li[3] = "妖怪"


data=[1,"a",3,4,"heart"]
li.extend(data)


s = "qwert"
li.extend(s)

li.remove("barry")

li.pop(1)

del li[2:5]


li = [1, 3, 2, "a", 4, "b", 5,"c"]
new_list1 = li[0:3]
new_list2 = li[3:6]
new_list3 = li[::2]
new_list4 = li[1:-2:2]
new_list5 = li[1::2]
new_list6 = li[-1]
new_list7 = li[-3:0:-2]

lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[2] = lis[2].upper()

lis[1] = "100"
lis[3][2][1][1] = "100"

lis[3].insert(0, "火车头")
print(lis)

