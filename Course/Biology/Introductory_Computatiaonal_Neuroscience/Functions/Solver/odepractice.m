% odepractice.m
clear
x0 = 2;                           % the first value of x, the variable
t0 = 0;                           % the first value of time to be used
dt = 0.001;                       % the time step for simulations
tmax = 20;                        % the maximum time used
tvec = t0:dt:tmax                 % creates a vector of time points
[t, x] = ode45(@test_ode, tvec, x0)  % use built-in function
plot(t,x)                         % plot x against t