t=[0:1:200]; 			% Time in seconds
wt=2.*pi*0.005*t;		% base frequency is 0.005 Hz

z=1 + cos(10*wt) + 0.5.*cos(20.*wt) + 0.25.*cos(30.*wt) + 0.125.*cos(40.*wt);
figure(1);
plot(wt,z);
b=fft(z);
c=b.*conj(b);
figure(2);
plot(c);

a=[0:1:400];
wt=2.*3.14159.*a/200;
z1=1 + cos(10*wt)+ 0.5.*cos(20.*wt) + 0.25.*cos(30.*wt) + 0.125.*cos(40.*wt);
z2 = 1+zeros(1,401);
a2 = [0:1:801];
wt2=2*3.14159*a2/400;
h1 = figure(1);
z = [z1 z2];
plot(wt2,z);
b=fft(z);
c=b.*conj(b);
h2 = figure(2);
plot(c);


figure;
hold on;
results1 = squarewave(1);
results2 = squarewave(2);
results10 = squarewave(10);
results100 = squarewave(100);
results1000 = squarewave(1000);
legend('n=1','n=2','n=10','n=100','n=1000');
hold off;
