import numpy as np

def max_trans(Max_x, Min_x, x): #极大型
    x = list(x)
    ans = [((i - Min_x) / (Max_x - Min_x)) for i in x]
    return np.array(ans)

def min_trans(Max_x, Min_x, x):  #极小型
    x = list(x)
    ans = [((Max_x - i) / (Max_x -Min_x)) for i in x]
    return np.array(ans)

def mid(Best_x, x):  #中间型
    x = list(x)
    a = [abs(i - Best_x) for i in x]

    M = max(a)
    if M == 0:  #防止M为0
        M = 1
    
    ans = [(1 - i / M) for i in a]
    return np.array(ans)

def ran(Low_x, High_x, x):  #区间型
    x = list(x)
    M = max(Low_x - min(x), max(x) - High_x)
    if M == 0:  #防止M为0
        M = 1
    
    ans = []
    for i in range(len(x)):
        if x[i] < Low_x:
            ans.append(1 - (Low_x - x[i]) / M)
        elif Low_x <= x[i] <= High_x:
            ans.append(1)
        else:
            ans.append(1 - (x[i] - High_x) / M)
    return np.array(ans)

m = eval(input("请输入方案个数："))
n = eval(input("请输入指标个数："))

print("请按照指标顺序依次输入指标类型：1:极大型，2：极小型，3：中间型，4：区间型")
kind = input().split(" ")  #按空格分隔，形成列表

for i in range(n):
    if kind[i] not in ['1', '2', '3', '4']:  
        print("输入的指标类型有误，请退出程序重新检查")
        exit() 

print("请输入原始矩阵：")
A = np.zeros((m, n))
for i in range(m):
    A[i,:] = input().split(" ")  #按空格分隔，打完一列按回车即可输入下一列
    A[i] = list(map(float, A[i]))
    
print(f"输入的矩阵为：{A}")

X = np.zeros((m,1))

for i in range(n):
    if kind[i] == '1':
        Max_x = max(A[:,i])
        Min_x = min(A[:,i])
        line = max_trans(Max_x, Min_x, A[:,i])
    elif kind[i] == '2':
        Max_x = max(A[:,i])
        Min_x = min(A[:,i])
        line = min_trans(Max_x, Min_x, A[:,i])
    elif kind[i] == '3':
        j = i + 1
        Best_x = eval(input(f"第{j}个数据检测到为中间型指标，请输入理想值："))
        line = mid(Best_x, A[:,i])
    elif kind[i] == '4':
        j = i + 1
        Low_x = eval(input(f"第{j}个数据检测到为区间型指标，请输入区间下限："))
        High_x = eval(input("请输入区间上限："))
        line = ran(Low_x, High_x, A[:,i])
    
    if i == 0:
        X = line.reshape(-1, 1)
    else:
        X = np.hstack([X, line.reshape(-1, 1)])
print(f"正向化后的矩阵为：\n{X}")



'''以上均为正向化过程'''

#统一量刚
Mean = np.mean(X, 0)
A_Norm = X / np.tile(Mean, (m, 1))

#构造母序列和子序列
Mom = np.max(A_Norm, 0)
Son = A_Norm

#计算母序列和子序列的差值
diff = np.abs(Son - np.tile(Mom, (m, 1)))

#计算两级最小差
a = np.min(diff)
#计算两级最大差
b= np.max(diff)
#分辨系数（一般取0.5）
rho = 0.5

#计算关联系数
gamma = (a + rho * b) / (diff + rho * b)

#计算关联度
w = np.array(eval(input('请输入权重向量（按Python格式输入）')))  # 接收用户输入的权重
print(f"各指标权重为：{w}")  # 打印权重w

r = np.dot(gamma, w.reshape(-1, 1))
print("各方案与理想最佳方案的关联度为：")
print(r)

