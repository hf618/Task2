from database import *  # 自己写的数据库函数的包
import random
import copy
import numpy as np

a=['kim','hwang','lee','ye','wu']
#a = gain_namelist()  # 名字列表
ori = a             #原始数据
random.shuffle(a)  # 随机排序后名字列表
print(a)
baocun = copy.deepcopy(a)
a.pop(1)
print(a)

print(baocun)

samples = random.sample(a, 3)
print(samples)

