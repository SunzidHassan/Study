t=[0:1:200]; 			% Time in seconds
wt=2.*pi*0.005*t;		% base frequency is 0.005 Hz

z=1 + cos(10*wt) + 0.5.*cos(20.*wt) + 0.25.*cos(30.*wt) + 0.125.*cos(40.*wt);
figure(1);
plot(wt,z);
b=fft(z);
c=b.*conj(b);
figure(2);
plot(c);
