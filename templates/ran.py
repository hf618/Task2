import numpy as np
# import random
import copy
# # 定义从正态分布中获取随机数的函数
# def get_normal_random_number(loc, scale):
#     """
#     :param loc: 正态分布的均值
#     :param scale: 正态分布的标准差
#     :return:从正态分布中产生的随机数
#     """
#     # 正态分布中的随机数生成
#     number = np.random.normal(loc=loc, scale=scale)
#     # 返回值
#     return number
#
#
# # 主模块
# if __name__ == "__main__":
#     # 函数调用
#     #n = get_normal_random_number(loc=2, scale=2)
#     n = np.random.randint(1, 5, size=1)[0]
#     res = random.sample(range(1,5),4)
#     a = ['lee','hwang','ye','kim']
#     random.shuffle(a)
#     # 打印结果
#     print(n)
#     print(res)
#     print(a)
#
#
#
# # 结果:3.275192443463058
from database import *  # 自己写的数据库函数的包
import random

hang = get_hang()
#hang = 5#这里行为5
n = np.random.randint(1, hang + 1, size=1)[0]#1<=n<=hang 标准答案名字所在数据库中行数
# res = random.sample(range(1, 5), 4)
#name=['kim','hwang','lee','ye','wu']
name = gain_namelist()  # 名字列表
#ori = a             #原始数据
random.shuffle(name)  # 随机排序后名字列表
print(name[n-1])

num = n-1 #标准答案名字所在列表索引
#name = gain_allist()
pos = np.random.randint(0, 4, size=1)[0]#随机选取标准答案所在选项位置

# opt = []#选项列表
# #nnn[pos] = name[num][1]
# opt.insert(pos,name[num][1])
name_ori = copy.deepcopy(name)
daan = name_ori[num]

#random.shuffle(name)
name_sui_ori = copy.deepcopy(name)
name.pop(num)
samples = random.sample(name, 3)#三个错误选项
n_1 = samples[0]
n_2 = samples[1]
n_3 = samples[2]########
#没被打乱的option
option = [n_1,n_2,n_3,daan]
random.shuffle(option)
n1 = option[0]
n2 = option[1]
n3 = option[2]
n4 = option[3]

print(option)
print(name)
print(name_ori)
print(name_sui_ori)
print(n1,n2,n3,n4)
# sql = "select count(*) from user"
# cur.execute(sql)
# re = cur.fetchone()
# print(int(re[0]))

#
# def get_hang():
#     sql = "select count(*) from user"
#     cur.execute(sql)
#     re = cur.fetchone()
#     return int(re[0])
#
# sql="select * from user"
# cur.execute(sql)
# re = cur.fetchall()
# a = []
# hang = get_hang()
#
# for id in range(0,hang):
#     a.append(re[id])
#     # print(re[id][1])
# print(a[2][1])
#
# for shu in range(0, 4):
#     if shu == 2:
#         shu = shu - 1
#         continue
#     else:print(shu)

