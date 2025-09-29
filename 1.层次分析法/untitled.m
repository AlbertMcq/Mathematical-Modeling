
A = input('请输入判断矩阵A=');

[~,n] = size(A);
[V,D] = eig(A);
Max_lambda = max(max(D));
[r,c] = find(Max_lambda == D, 1);
w = V(:,c) ./ sum(V(:,c));

disp('权重=');
disp(w);

CI = (Max_lambda - n) / (n-1);
disp(["CI=",CI])

RI = [0 0.0001 0.52 0.89 1.12 1.26 1.36 1.41 1.46 1.49 1.52 1.54 1.56 1.58 1.59];  %这里的RI最多支持 n = 15，注意检查！
CR = CI / RI(1,n);

disp(["CR=",CR])
disp(["Max_lambda=",Max_lambda])

if CR < 0.10
    disp('该判断矩阵的一致性可接受');
else
    disp('该判断矩阵一致性不可接受，需要修改');
end
