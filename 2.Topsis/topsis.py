import numpy as np

def min_trans(Max_x, x):  #极小型
    x = list(x)
    ans = [(Max_x - i) for i in x]
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
        line = A[:,i]
    elif kind[i] == '2':
        Max_x = max(A[:,i])
        line = min_trans(Max_x, A[:,i])
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

X = X.astype('float')
for i in range(n):
    X[:,i] = X[:,i] / np.sqrt(sum(pow(X[:,i], 2)))
print(f"标准化后的矩阵为：\n{X}")

print("请依次输入各指标的权重（以空格为分隔）：")
w = list(map(float, input().split(' ')))
print(f"各指标权重为：{w}")

#找到理想最优解和理想最劣解
Z_best = []
Z_worst = []
for i in range(n):
    Best_x = max(X[:,i])
    Worst_x = min(X[:,i])
    Z_best.append(Best_x)
    Z_worst.append(Worst_x)
    
Z_best = np.array(Z_best)
Z_worst = np.array(Z_worst)
w = np.array(w)

#计算各方案与最优解、最劣解的距离
d_best = np.sqrt(np.sum(w * np.square(X - np.tile(Z_best, (m, 1))) , 1))
d_worst = np.sqrt(np.sum(w * np.square(X - np.tile(Z_worst, (m, 1))) , 1))

S = []
for i in range(m):
    S.append(d_worst[i] / (d_best[i] + d_worst[i]))

S = np.array(S)
S = S.reshape(-1,1)

print(f"各方案的得分为：\n{S}")
    

    
    
    


        

        
        
        
        
        
    
            
    
    
   
    