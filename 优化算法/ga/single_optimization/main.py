# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea

"""
该案例展示了一个简单的连续型决策变量最大化目标的单目标优化问题。
max f = x * np.sin(10 * np.pi * x) + 2.0
s.t.
-1 <= x <= 2
"""


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):
        self.name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        self.M = 1  # 初始化M（目标维数）
        self.maxormins = [-1]  # 初始化maxormins（目标最小最大化标记列表）
        self.Dim = 1  # 初始化Dim（决策变量维数）
        self.varTypes = np.array([0] * self.Dim)  # 初始化varTypes（决策变量的类型）
        lb = [-1]  # 决策变量下界
        ub = [2]  # 决策变量上界
        self.ranges = np.array([lb, ub])  # 初始化ranges（决策变量范围矩阵）
        lbin = [1] * self.Dim
        ubin = [1] * self.Dim
        self.borders = np.array([lbin, ubin])  # 初始化borders（决策变量范围边界矩阵）

    def aimFuc(self, x, CV):
        f = x * np.sin(10 * np.pi * x) + 2.0
        return f, CV

    def calBest(self):
        realBestObjV = None
        return realBestObjV

"""==================================实例化问题对象================================"""
problem = MyProblem() # 生成问题对象

"""==================================种群设置================================"""
Encoding = 'R'             # 编码方式
conordis = 0               # 表示染色体解码后得到的变量是连续的
NIND = 40                  # 种群规模
Field = ea.crtfld(Encoding, conordis, problem.ranges, problem.borders) # 创建区域描述器
population = ea.Population(Encoding, conordis, Field, NIND) # 实例化种群对象（此时种群还没被真正初始化）
"""==================================算法参数设置================================"""
myAlgorithm = ea.soea_studGA_templet(problem, population) # 实例化一个算法模板对象
myAlgorithm.MAXGEN = 25 # 最大遗传代数
"""=======================调用算法模板进行种群进化=============================="""
[population, obj_trace, var_trace] = myAlgorithm.run() # 执行算法模板
# 输出结果
best_gen = np.argmax(obj_trace[:, 1]) # 记录最优种群是在哪一代
best_ObjV = obj_trace[best_gen, 1]
print('最优的目标函数值为：%s'%(best_ObjV))
print('最优的控制变量值为：')
for i in range(var_trace.shape[1]):
    print(var_trace[best_gen, i])
print('有效进化代数：%s'%(obj_trace.shape[0]))
print('最优的一代是第 %s 代'%(best_gen + 1))
print('评价次数：%s'%(myAlgorithm.evalsNum))
print('时间已过 %s 秒'%(myAlgorithm.passTime))