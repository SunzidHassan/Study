%% Introduction: Mass-Spring-Damper System

% Transfer Function
m = 1;
b = 10;
k = 20;

s = tf('s');
sys = 1/(m*s^2+b*s+k);

Ts = 1/100;

% Discrete Transfer Function
sys_d = c2d(sys,Ts,'zoh')

% Continuous-time State-Space Model
A = [0       1;
    -k/m   -b/m];

B = [  0;
    1/m];

C = [1 0];

D = [0];

Ts = 1/100;

% Discrete-time State-Space Model
sys = ss(A,B,C,D);
sys_d = c2d(sys,Ts,'zoh')

% Stability and Transient Response
numDz = 1;
denDz = [1 -0.3 0.5];
sys = tf(numDz,denDz,-1); % the -1 indicates that the sample time is undetermined

% Pole-Zero Map
figure(1)
pzmap(sys)
axis([-1 1 -1 1])
zgrid

% Step Response Plot
sys_d2 = tf(numDz, denDz, 1/20);
figure(2)
step(sys_d2, 2.5)

% Discrete-time Root Locus Diagram
numDz = [1 -0.3];
denDz = [1 -1.6 0.7];
sys = tf(numDz,denDz,-1);

figure(3)
rlocus(sys)
axis([-1 1 -1 1])

zeta = 0.4;
Wn = 0.3;
zgrid(zeta,Wn)


%% Cruise Control
% Discrete-time Transfer Function

% Root Locus Diagram in the z-Plane

% Closed-loop Step Response

% Compenstation Digital Controller Root Locus

% Step Response of the Closed-loop System with the Compensation Controller


%% Motor Speed Control
% The continuous Transfer Function

% The Discrete Transfer Function

% The closed-loop step Response

% The Closed-loop Step Response with Original PID Controller

% The closed-loop step Response with PID + Conpensator Controller



