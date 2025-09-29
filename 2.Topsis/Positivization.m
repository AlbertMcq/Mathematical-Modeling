function [A] = Positivization(x, type, i)
    A =[];
    if type == 1
        A = x;
    elseif type == 2
        A = max(x) - x;
    elseif type == 3
        x_best = input(sprintf('检测到第%d个数据是中间型指标，请输入理想值：', i));
        M = max(abs(x - x_best));
        A = 1 - abs(x - x_best) / M;
    elseif type == 4
        x_low = input(sprintf('检测到第%d个数据是区间型指标，请输入区间下限：', i));
        x_high = input(sprintf('检测到第%d个数据是区间型指标，请输入区间上限：', i));
        M = max([(x_low - min(x)), (max(x) - x_high)]);
        for i = 1:length(x)
            if x(i) < x_low
                x(i) = 1 - (x_low - x(i)) / M;
            elseif x(i) <= x_high
                x(i) = 1;
            elseif x(i) > x_high
                x(i) = 1 - (x(i) - x_high) / M;
            end
        end
        A = x;

    end
end