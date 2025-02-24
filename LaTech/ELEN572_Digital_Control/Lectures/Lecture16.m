%% Page 9
t(1) = 0;
x{1} = [1;0]; % Initial state
T = 0.02; % Sampling period
N = 150; % Number of steps
S = diag([10,1]);
r = 0.1; % Weights
Q = diag([10,1]);
A = [1,T;0,1];
B = [T^2/2;T]; % System matrices

for i=N:-1:1
    K{i} = (B'*S*A)/(r + B'*S*B); % Calculate the optimal feedback gains
    % Note that K(1) is really K(0)
    kp(i) = K{i}(1); % Position gain
    kv(i) = K{i}(2); % Velocity gain
    Acl = A-B*K{i};
    S = Acl'*S*Acl + K{i}'*r*K{i}+Q; % Iterate backward (Riccati Equation)
end

for i=1:N
    t(i+1) = t(i) + T;
    u(i) = -K{i} * x{i};
    x{i+1} = A*x{i} + B*u(i); % State equation
end

xmat = cell2mat(x); % Change cell to mat to extract data
xx = xmat(1,:); % Position
xv = xmat(2,:); % Velocity
figure(1)
subplot(2, 1, 1)
plot(t,xx,'.') % Plot Position
title('Subplot 1: Position Plot')
subplot(2, 1, 2)
plot(t,xv,'.') % Plot Velocity
title('Subplot 2: Velocity Plot')
xlabel('time (s)')

figure(2) % New figure
plot(t(1:N),u,'.') % Plot control input
title('Control Efforts')
xlabel('time (s)')

figure(3) % New figure
plot(t(1:N),kp,'.',t(1:N),kv,'.') % Plot position gain & velocity gain
title('Control Gains')
legend('Position Gain', 'Velocity Gain')
xlabel('time (s)')