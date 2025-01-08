function [m, s] = stat_2(x)
    m = mean(x, 2);
    s = std(x,0,2);
end