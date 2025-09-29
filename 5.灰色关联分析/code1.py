import numpy as np
#该程序是求不同指标的灰色关联度
#输入的矩阵规则：指标在列

X = np.array(eval(input('请输入原始矩阵=')))
#[[120, 130, 128, 140, 138, 150], [20, 25, 23, 28, 27, 30], [5.5, 5.7, 5.6, 5.9, 6, 6.2], [85, 88, 87, 90, 89, 91]]
[m, n] = np.shape(X)

Mean = np.mean(X, 1)
A_Norm = X / np.tile(Mean.reshape(-1, 1), (1, n)) #统一量纲

print(f"统一量纲后的矩阵为：\n{A_Norm}")

#求出母序列
Mom = A_Norm[0,:]

#求出子序列
Son = A_Norm[1:,:]

#计算母序列和子序列的差值
diff = np.abs(Son - np.tile(Mom, (Son.shape[0], 1)))

#计算两级最小差
a = np.min(diff)

#计算两级最大差
b = np.max(diff)

#分辨系数（一般取0.5）
rho = 0.5

#计算关联系数
gamma = (a + rho * b) / (diff + rho * b)

print("请输入各指标的权重，用空格分隔：")
#w = list(map(float, input().split()))  # （如有需要）输入权重
w = np.array(np.tile([1/n], (1, n))) #默认每个指标权重相等

#计算灰色关联度
r = np.dot(gamma, w.reshape(-1, 1))

print("子序列中各方案灰色关联度分别为：")
print(r)
