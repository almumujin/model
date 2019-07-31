import numpy as np
import geatpy as ga

# 简单连续型决策变量最大优化目标的单目标优化问题
'''
    max f = x * np.sin(10 * np.pi * x) + 2.0
    s.t
    -1 <= x <= 2
'''


class MyProblem(ga.Problem):
    def __init__(self):
        # 初始化name(函数名称，可以随意设置)
        self.name = 'MyProblem'
        self.M = 1
        self.maxormins = [-1]
        self.Dim = 1
        self.varTypes = np.array([0] * self.Dim)
        lb = [-1]
        ub = [2]
        self.ranges = np.array([lb ,ub])
        lbin = [1] * self.Dim
        ubin = [1] * self.Dim
        self.borders = np.array([lbin, ubin])

        def aimFuc(self, x, cv):
            f = x * np.sin(10 * np.pi * x) + 2.0
            return f, cv

        def calBest(self):
            realBestObjv = None
            return realBestObjv