function squaresig = squarewave(n)
% Construct a square wave (squaresig) from the first n terms of the Fourier series
npts = 1000.;
totaltime = 1.0; %seconds
dt = totaltime/npts;
t = 0:dt:totaltime-dt;
f = 1.0/totaltime;
wt = 2*pi*f*t;
a0 = 2/pi;
squaresig = zeros(1,npts);
for k = 1:2:n
 a = a0/k;
 squaresig = squaresig + a*sin(k*wt);
end
plot(t,squaresig);
end