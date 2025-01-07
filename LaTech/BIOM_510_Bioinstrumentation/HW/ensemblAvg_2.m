function ensemblAvg = ensemblAvg_2(x)
    [m, n] = size(x);
    xavg = zeros(1,n);
    for k = 1:m
        xavg = xavg + x(k,:);
    end
    ensemblAvg = xavg/m;
end