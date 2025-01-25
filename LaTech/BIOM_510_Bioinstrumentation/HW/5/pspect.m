function [pspec, farray, errno] = pspect(signal,dt,npts, hanwin, subdc, overlap, zeropad)
% Calculate the power spectrum of "signal"
% Inputs:
% signal:   The signal to be transformed.
% dt:       The sample rate of the signal.
% npts:     The number of points per record.
% hanwin:   If hanwin is 1, apply a hanning window to each record.
% subdc:    If subdc is 1, subtract DC from each record before
%           transforming.
% overlap:  If overlap is 1, overlap successive records by 50%.
% zeropad:  Number of points to zero pad to.  If zero, no zero padding is done.
%
% Outputs:
% pspect:   The scaled, ensembled power spectrum.
% farray:   The scaled frequency spectrum.
%
% errno:    If errno is 1, it means that the number of input points was not
%           adequate.

global hspecfig; % handle to the plot
clear srecord;
errno = 0;
if(nargin < 3)
        fprintf('Pspect: Please specify the signal, the sample time (sec), and the number of points per record\n');
       return;
end;

subdc = 0;
overlap = 0;
zeropad = 0;
if(nargin < 4)
    hanwin = 0;
end
if(nargin < 5)
    subdc = 0;
end
if(nargin < 6)
    overlap = 0.0;
end
if(nargin < 7)
    zeropad = 0;
end
if(zeropad == 0)
    zeropad = 1;
end
ntotal = length(signal);
% scale the frequency array for the power spectrum
fnpts = double(npts);
fmax = 1/(2*dt);
deltaf = 2*fmax/(fnpts*zeropad);
farray = -fmax:deltaf:fmax-deltaf;

% Determine how many records need to be processed
nrecs = fix(ntotal/fnpts);
fnrecs = double(nrecs);

% initialize the output array
pspec = zeros(1,zeropad*npts,'double');

% Make sure the signal has enough points to transform
if(nrecs < 1)
    fprintf('signal length is less than the transform record size\n');
    errno = 1;
    return;
end

% if requested, generate the hanning window.
if(hanwin == 1)
    winhan = hanning(double(npts));
end

if(overlap == 1)
        nrecs = 2*nrecs - 1;
end
padding = zeros(1, (zeropad - 1)*npts);
% loop for each record to be averaged
% plot the signal
chk = exist('hspecfig');
sklr = isscalar(hspecfig);
if(chk == 1 && sklr == 1)
%        figure(hspecfig);
else
%    hspecfig = figure('units','normalized','position',[.7 .6 .3 .3])
end
%    hspecfig = figure('units','normalized','position',[.7 .6 .3 .3])
%figure('units','normalized','position',);
figure('units','normalized','position',[.7 .6 .3 .3])
for k = 1:nrecs
    kstart = (k-1)*npts+1;

    if(overlap)
        kstart = (k-1)*npts/2 + 1;
    else
        kstart = (k-1)*npts + 1;
    end
    kend = kstart + npts - 1;
    srecord = signal(kstart:kend);
% if requested, apply a hanning window.
    if(subdc == 1)
        sigaverage = mean(srecord);
        srecord = srecord - sigaverage;
    end
    if(hanwin == 1)
    	srecord = srecord.*winhan';
    end
% take the fast Fourier transform
output='srecord'
size srecord;
    b = fft([srecord padding]);
    
    output='b'
    size b;

% find the power spectrum and add it to the power spectrum from the
% previous record.
    showit = abs(b).*abs(b);
    pspec = pspec + showit;
    h = subplot(2,1,2);
    showit = showit/fnpts;
    showit = showit/double(fnpts);

    showit = showit/2;
    showit = showit/double(2);
    deltaf
    showit = double(showit)/double(deltaf);
    showit = fftshift(showit);
    size(farray)
    size(showit)
    plot(farray,showit);
    TheYLims = get(h,'Ylim');
    ylim([0 TheYLims(2)]);
    
    if(k == 1)
        xlabel('Frequency (Hz)');
        ylabel('Power Density (Volts^2/Hz)');

 %       ylims = ylim;
 %       ylims(1)=0;
 %       ylim(ylims);
    end
    legend('Single Spectrum');
    legend('boxoff');    
    accum = pspec/fnpts/fnpts/k/deltaf;
    accum = fftshift(accum);
    h = subplot(2,1,1);
    plot(farray, accum);
    TheYLims = get(h,'Ylim');
    if(k == 1)
        xlabel('Frequency (Hz)');
        ylabel('Power Density (Volts^2/Hz)');
    end
    legend('Ensembled Spectrum');
    legend('boxoff');
    ylim([0 TheYLims(2)]);
    pause(0.01);
    if(k == 1)
        savefirst = pspec;
    end
end
% scale with respect to the number of data points and the nmber of records
pspec = pspec/fnpts/fnpts/fnrecs/deltaf/deltaf;
savefirst = savefirst/fnpts/fnpts/deltaf/deltaf;

% swap the values of the FFT output so that the amplitudes appear at the
% correct freqencies

%pspec = rearrange(pspec,npts);
pspec = fftshift(pspec);
%savefirst = rearrange(savefirst,npts);
savefirst = fftshift(savefirst);

% make sure that the total power in the power spectrum is the same as the
% total power in the input signal (take integral with respect to freqency)
spectrumpower = sum(pspec)*deltaf;

%fprintf('Power in the signal is %f\n',power);
fprintf('Power in the spectrum is %f\n',spectrumpower);

% Plot the power spectrum
pspctlog = 20*log10(pspec);

subplot(2,1,1);
plot(farray,pspec);
xlabel('Frequency (Hz)');
ylabel('Power Density (Volts^2/Hz)');
title('Averaged Spectrum','units','normalized','position',[0.7 0.85 0]);
%legend('boxoff');
ylims = ylim;
ylims(1)=0;
ylim(ylims);

subplot(2,1,2);
plot(farray,savefirst);
xlabel('Frequency (Hz)');
ylabel('Power Density (Volts^2/Hz)');
title('Single Spectrum','units','normalized','position',[0.7 0.85 0]);
%legend('boxoff');
ylims = ylim;
ylims(1)=0;
ylim(ylims);
pside = sum(savefirst)*deltaf
sg = signal.*signal;
sside = sum(sg)*dt
end