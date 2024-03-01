import numpy as np
import matplotlib.pyplot as plt

# 输入两个点的坐标
x1, y1 = -10000, 2200
x2, y2 = 10000, 1200

# 计算斜率和截距
slope = (y2 - y1) / (x2 - x1)
intercept = y1 - slope * x1

# 输入 x 坐标值列表
# x_values = np.linspace(-9000, 9000, 10)
x_values = np.linspace(-10000, 10000, 41)
# 计算对应的 y 坐标值
y_values = slope * x_values + intercept

# 将结果保存为矩阵形式
result_matrix = np.column_stack((x_values, y_values))

# 输出结果矩阵
print("Result Matrix:")
print(result_matrix)
