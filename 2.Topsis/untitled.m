clear;clc;

A = input('请输入原始矩阵：');

Type = input('请输入各指标的类型（1:极大型，2：极小型，3：中间型，4：区间型）：');


for i = 1:length(Type)
    A(:,i) = Positivization(A(:,i), Type(i), i);  
end

disp("正向化后的矩阵为：");
disp(A);

denominator = sqrt(sum(A .* A, 1));
for i = 1:size(A, 2)
    A(:,i) = A(:,i) / denominator(i);  % 标准化
end

disp("标准化后的矩阵为：");
disp(A);

% 找出理想最优解和理想最劣解
z_best = max(A, [], 1);
z_worst = min(A, [], 1);

w = input("请输入权重向量：");

[m, n] = size(A);
d_best = zeros(m, 1); 
d_worst = zeros(m, 1);

for i = 1:m  
    d_best(i) = sqrt(sum(w .* (z_best - A(i,:)) .^ 2));
    d_worst(i) = sqrt(sum(w .* (z_worst - A(i,:)) .^ 2));
end

S = d_worst ./ (d_best + d_worst);
disp("各方案的最终得分为：");
disp(S);