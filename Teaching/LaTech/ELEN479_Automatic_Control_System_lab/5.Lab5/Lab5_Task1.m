clear
clc

% Input coefficients
e = [1 10 32 37 20];
l = length(e);

% First two rows of Routh
if mod(l,2) == 0
a = zeros(1, l/2);
b = zeros(1, l/2);
for i = 1:(l/2)
a(i) = e(2*i - 1);
b(i) = e(2*i);
end
else
e1 = [e 0];
a = zeros(1, (l+1)/2);
b = zeros(1, (l+1)/2);
for i = 1:((l+1)/2)
a(i) = e1(2*i - 1);
b(i) = e1(2*i);
end
end

% Build Routh array
l1 = length(a);
c = zeros(l, l1);
c(1,:) = a;
c(2,:) = b;

for r = 3:l
% Special handling if leading element becomes 0 (avoid division by zero)
if c(r-1,1) == 0
c(r-1,1) = eps;
end
for n = 1:l1-1
% 2x2 determinant: [c(r-2,1) c(r-2,n+1); c(r-1,1) c(r-1,n+1)]
num = c(r-1,1)*c(r-2,n+1) - c(r-2,1)*c(r-1,n+1);
c(r,n) = num / c(r-1,1);
end
end

disp('the routh matrix:')
disp(c)

% Stability check: need ALL first-column entries > 0
if all(c(:,1) > 0)
disp('System is Stable')
else
disp('System is Unstable')
end