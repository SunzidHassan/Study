x = rand(1,256000)-0.5;
dt = 0.001;
npts = 256;
%[p, farray] = pspect(x,dt,npts);


c = [1 1 1 1 1 1 1 1 1 1];
s = filter(c,1,x);
[p, farray] = pspect(s,dt,npts);


%win = hanning(npts);
%x_seg = x(1:npts);     % just an example with first 256 samples
%x_win = x_seg .* win;
%[p, farray] = pspect(x_win, dt, npts);


deriv = filter([-1 1],dt,x);
[p, farray] = pspect(s,dt,npts);