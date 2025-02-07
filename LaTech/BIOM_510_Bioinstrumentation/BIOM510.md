## Biomedical Instrumentation

- [Biomedical Instrumentation](#biomedical-instrumentation)
- [Chapter 1](#chapter-1)
- [Chapter 2: Review](#chapter-2-review)
  - [2.1 Kirchov's Laws](#21-kirchovs-laws)
  - [2.2 Resistance, Inductance, Capacitance](#22-resistance-inductance-capacitance)
  - [2.3 Elements in Series and Parallel](#23-elements-in-series-and-parallel)
  - [2.4 Time Constant](#24-time-constant)
  - [2.5 Impedance](#25-impedance)
  - [2.6 Diodes](#26-diodes)
  - [2.7 Linearity](#27-linearity)
  - [2.8 Input and Output Impedance](#28-input-and-output-impedance)
  - [2.9 AC vs DC Signals](#29-ac-vs-dc-signals)
  - [2.10 Euler's Rule](#210-eulers-rule)
  - [2.11 Transfer Functions](#211-transfer-functions)
  - [2.12 Semiconductors](#212-semiconductors)
- [Chapter 4: Ideal Op Amp](#chapter-4-ideal-op-amp)
  - [Differential Amp](#differential-amp)
  - [Inverting Amp](#inverting-amp)
  - [Generalized Inverting Amp](#generalized-inverting-amp)
  - [Low-pass filter](#low-pass-filter)
  - [High-pass filter](#high-pass-filter)
  - [Band-pass filter](#band-pass-filter)
    - [Example](#example)
- [HW](#hw)
  - [HW 1](#hw-1)
    - [1. Design criteria examples:](#1-design-criteria-examples)
    - [2. Specificity as environmental factor:](#2-specificity-as-environmental-factor)
    - [3. Oscilloscope](#3-oscilloscope)
    - [4. Mean and RMS](#4-mean-and-rms)
    - [5. Mean and RMS](#5-mean-and-rms)
    - [6. Bode plot](#6-bode-plot)
  - [HW 2](#hw-2)
    - [1. Gain of inverting amplifier](#1-gain-of-inverting-amplifier)
    - [2. Low-pass filter](#2-low-pass-filter)
      - [a. Sketch](#a-sketch)
      - [b. $C\_f$ and $R\_f$](#b-c_f-and-r_f)
      - [c. Transfer function](#c-transfer-function)
    - [3. High-pass filter](#3-high-pass-filter)
      - [a. Sketch](#a-sketch-1)
      - [b. $C\_i$ and $R\_i$](#b-c_i-and-r_i)
      - [c. Transfer function](#c-transfer-function-1)
    - [4. Band-pass filter](#4-band-pass-filter)
      - [a. Sketch](#a-sketch-2)
      - [b. $C\_i$ and $C\_f$](#b-c_i-and-c_f)
      - [c. Gain](#c-gain)
      - [d. Transfer function](#d-transfer-function)
  - [HW 3](#hw-3)
    - [1](#1)
    - [2](#2)
    - [3](#3)
    - [4](#4)
    - [5](#5)
    - [6](#6)
    - [7](#7)
    - [8](#8)
  - [HW 4](#hw-4)
    - [1](#1-1)
    - [2](#2-1)
    - [3](#3-1)
    - [4](#4-1)
    - [5](#5-1)
    - [6](#6-1)
  - [HW 6](#hw-6)
    - [HW 6.1](#hw-61)
    - [HW 6.2](#hw-62)
    - [HW 6.3](#hw-63)
    - [HW 6.4](#hw-64)
    - [HW 6.5](#hw-65)


## Chapter 1

Goals:
1. Highlight connections between instrumentation and mechanical, electrical, and chemical engineering disciplines.
2. Provide an understanding of the basic concepts of instrumentation that are needed to take measurements from the body, design biomedical instruments, and to model, theoretically, certain aspects of the body.
3. Highlight aspects of electrical engineering concepts, such as positive and negative feedback, that can be used to understand and quantitatively model physiological phenomena, such as oscillatory cycles.

## Chapter 2: Review

### 2.1 Kirchov's Laws

![2-1 Simple circuit to illustrate Kirchov's laws](LaTech\BIOM_510_Bioinstrumentation\Figs\2-1.png)

Charge that enters $v_1$ must be equal to sum of currents leaving it.  
$$i_1=i_2+i_3$$
$$\Rightarrow C_1\frac{d}{dt}(v_{in}-v_1)=C_2\frac{d}{dt}(v_1-0)+\frac{v_1-0}{R_1+R_2}$$

By convention, the dependent variable $v_1$ is placed on the left-hand side of the equation, and the independent variable $v_{in}$ is placed on the right-hand side of the equation to obtain  
$$(C_1+C_2)\frac{dv_1}{dt}+\frac{v_1}{R_1+R_2}=C_1\frac{dv_{in}}{dt}$$

Voltage can have one value at a location, so if voltage changes across elements in a loop, the sum of changes will be zero. The example circuit has two loops.

$$v_{in}-\frac{1}{C_1}\int{i_1dt}-\frac{1}{C_2}\int{i_2dt}=0$$
Here positive $v_{in}$ is voltage gain, and the remaining two terms are voltage losses.

### 2.2 Resistance, Inductance, Capacitance

|Element|Equation|
|--------|--------|
|Resistor, $R$|$$v=iR$$|
|Inductor, $L$|$$v=L\frac{di}{dt}$$  |
|Capacitor, $C$|$$i=C\frac{dv}{dt}$$  |

Here, voltage is "across" variable, and current is "through" variable.

In mass spring damper system, force $F$ is "across" variable - analogous to inductance, and velocity $v$ is "through" variable - analogous to current, and damper is analogous to resistor.

In blood flow model, flow $Q$ is analogous to current, pressure $P$ is analogous to voltage, and $\rho$ is analogous to inductance.

### 2.3 Elements in Series and Parallel

Resistance
$$R_{Series}=R_1+R_2$$
$$\frac{1}{R_{Parallel}}=\frac{1}{R_1}+\frac{1}{R_2}$$

Inductance
$$L_{Series}=L_1+L_2$$
$$\frac{1}{L_{Parallel}}=\frac{1}{L_1}+\frac{1}{L_2}$$

Conductance
$$\frac{1}{C_{Series}}=\frac{1}{C_1}+\frac{1}{C_2}$$
$$C_{Parallel}=C_1+C_2$$

### 2.4 Time Constant

**Step function**
$$
H(t) =
\begin{cases} 
0 & \text{if } t < 0, \\
1 & \text{if } t \geq 0.
\end{cases}
$$

Output of a first order linear system to a step function is an exponential of the from:
$$v_{out}=V_{max}(1-e^{-t/\tau})u_s(t)$$
Where $\tau$ is the time constant, $V_{max}$ is the maximum value tha t$v_{out}$ can attain, and $u_s(t)$ is the unit step function.
When $t=\tau$, the output is
$$v_{out}=V_{max}(1-e^{-1})\approx0.631V_{max}$$
To estimate the time function, a step function is used as input, and time to reach 0.632 of final value is measured.



### 2.5 Impedance

### 2.6 Diodes

### 2.7 Linearity

### 2.8 Input and Output Impedance

### 2.9 AC vs DC Signals

### 2.10 Euler's Rule

### 2.11 Transfer Functions

### 2.12 Semiconductors

## Chapter 4: Ideal Op Amp

Create amplifiers and filters that can perform mathematical operation on signals:
* sum
* integration
* differentiation
* logarithms
* multiplication

### Differential Amp
An op amp is a differential amp with specific characteristics:
* If $v_1$ is voltage at the negative input, and $v_2$ is the voltage at the positive input, then $v_{out}$ is: $v_{out}=A(v_2-v_1)$.

Characteristics:
* Very high input impedance (doesn't absorb current from input)
* Infinite gain

### Inverting Amp
$$i=\frac{v_{in}-v^-}{R_i}$$
The current doesn't enter $v^-$, so travels through the feedback loop. Thus,
$$i=\frac{v^--v_{out}}{R_f}$$

$v^+\approx v^-=0$
$$\frac{v_{in}}{R_i}=\frac{-v_{out}}{R_f}$$
$$\Rightarrow\frac{v_{out}}{v_{in}}=-\frac{R_f}{R_i}$$

### Generalized Inverting Amp
$Z_R=R$  
$Z_C=\frac{1}{j\omega C}$  
$Z_L=j\omega L$  

### Low-pass filter
$$Z_i=R_i$$
$$Z_f=Z_C||Z_R=\frac{Z_CZ_R}{Z_C+Z_R}=\frac{\frac{1}{j\omega C_f}R_f}{\frac{1}{j\omega C_f}+R_f}=\frac{R_f}{1+j\omega C_fR_f}$$

$$H(j\omega)=-\frac{Z_f}{Z_i}=-\frac{R_f}{R_i}\left(\frac{1}{1+j\omega C_fR_f}\right)$$

If $\omega$ is close to zero, the gain the signal scaled by $-\frac{R_f}{R_i}$. But if $\omega$ is very large, the gain approaches 0 for $\frac{1}{j\omega C_fR_i}$.

### High-pass filter
$$Z_i=Z_C+Z_R=\frac{1}{j\omega C_i}+R_i$$
$$Z_f=R_f$$

$$H(j\omega)=-\frac{Z_f}{Z_i}=-\frac{R_f}{\frac{1}{j\omega C_i}+R_i}=-\frac{j\omega C_iR_f}{1+j\omega C_iR_i}=-\frac{R_f}{R_i}\left(\frac{j\omega C_iR_i}{1+j\omega C_iR_i}\right)$$

If $\omega$ is close to zero, the gain the signal scaled by $-\frac{R_f}{R_i}\frac{0}{1}=0$. But if $\omega$ is very large, the gain is scaled by $-\frac{R_f}{R_i}\frac{j\omega C_iR_i}{j\omega C_iR_i}=-\frac{R_f}{R_i}$.

### Band-pass filter
$$Z_i=Z_C+Z_R=\frac{1}{j\omega C_i}+R_i$$
$$Z_f=Z_C||Z_R=\frac{Z_CZ_R}{Z_C+Z_R}=\frac{\frac{1}{j\omega C_f}R_f}{\frac{1}{j\omega C_f}+R_f}=\frac{R_f}{1+j\omega C_fR_f}$$
$$H(j\omega)=-\frac{Z_f}{Z_i}=-\frac{\frac{R_f}{1+j\omega C_fR_f}}{\frac{1+j\omega C_iR_i}{j\omega C_i}}=-\frac{j\omega C_iR_f}{(1+j\omega C_fR_f)(1+j\omega C_iR_i)}$$

The gain grows in proportion to $\omega$ at frequencies below $\frac{1}{R_iC_i}$ and decays in proportion to $\frac{1}{\omega}$ for frequencies above $\frac{1}{R_fC_f}$ with gain of $\frac{R_f}{R_i}$.

#### Example
Design band pass filter for an electrocardiogram amplifier that removes baseline drift below 0.1 Hz and high frequency noise above 100 Hz with gain of 10.

**Solution**


## HW

### HW 1

#### 1. Design criteria examples:

Signal factors: amplitude.
Economic factors: financing option.
Social factors: usage fear.
Environmental factors: weight.
Medical safety factors: noise or vibration.

#### 2. Specificity as environmental factor:

Specificity is the property of discerning the target signal from other signals in the envrionment. This is determined not only by the signal requirement, but also on other signals in the environment. That's why it's more appropriate to classify it in environmental factors.

#### 3. Oscilloscope

a. Input has 4 divisions from peak-to-peak, resulting in $4\times0.5=2$ volts.
Output has 2 divisions from peak-to-peak, resulting in $2\times0.1=0.2$ volts.

b. Gain for this system is $V_{out}/V_{in}=0.2/2=0.1$

c. Frequency: the signal has period of about 6.6 divisions with time base of 0.2ms/div, resulting in $T=0.2\times6.6=1.32$ ms. Frequency = $(1/1.32)\times1000=757$ Hz.

d. The output signal lag is about 1.6 divisions, with period of about 6.6 divisions. Lag in degrees: $1.6/6.6\times360=87.3\degree$

e. The input signal is 1.8 division above arrow 1, so the offset is $1.8\times0.5=0.9$ volts.  
The output signal is 0.6 division above arrow 2, so the offset is $0.6\times0.1=0.006$ volts.

#### 4. Mean and RMS

For the mean
$\bar{s}=\frac{1}{T} \int_0^T \left( B + A \sin(\omega t) \right)dt$

$= \frac{1}{T} \int_0^T B \, dt + \frac{A}{T} \int_0^T \sin(\omega t) \, dt$

$= \frac{B(T - 0)}{T} + \frac{A}{T} \left[ -\frac{1}{\omega} \cos(\omega t) \right]_0^T$

$= \frac{1}{T} \int_0^T \left( B + A \sin(\omega t) \right) \, dt$

$= \frac{1}{T} \int_0^T B \, dt + \frac{A}{T} \int_0^T \sin(\omega t) \, dt$

$= B + \frac{A}{T} \left( -\frac{1}{\omega} \right) \left[ \cos(\omega T) - \cos(0) \right]$

$= B - \frac{A}{T \omega} \left[ \cos(\omega T) - 1 \right]$

With $T = \frac{2\pi}{\omega}$

$B - \frac{A}{2\pi}\left[\cos(2\pi) - 1 \right]$

$B + {A}({1-1})=B$

For RMS, $s_{rms}=\frac{1}{T}\int_0^T\left(s(t)-\bar{s}\right)^2dt$

Given $\bar{s}=B$, $s(t)-\bar{s}=B+A\sin(\omega t)-B=A\sin(\omega t)$

$=\left(\frac{\omega}{2\pi}\int_0^{\frac{2\pi}{\omega}}\left(A^2\sin^2(\omega t)\right)dt\right)^\frac{1}{2}$

$=\left(\frac{A^2\omega}{2\pi}\int_0^{\frac{2\pi}{\omega}}\left(\frac{t}{2}-\frac{1}{4\omega}sin(2\omega t)\right)dt\right)^\frac{1}{2}$

$=\left(\frac{A^2\omega}{4\pi}\left(\frac{2\pi}{\omega}-\left[\frac{\sin(2\omega t)}{2\omega}\right]_0^\frac{2\pi}{\omega}\right)\right)^\frac{1}{2}$

$=\left(\frac{A^2\omega}{4\pi}\left(\frac{2\pi}{\omega}-0\right)\right)^\frac{1}{2}$

$=\left(\frac{A^2}{2}\right)^\frac{1}{2}=\frac{A^2}{\sqrt2}$

b. For $T=\frac{3\pi}{\omega}$

Mean is $B - \frac{A}{3\pi}\left[\cos(3\pi) - 1 \right]$

$B - \frac{A}{3\pi}\left[-1-1\right]$

$B - \frac{2A}{3\pi}$

#### 5. Mean and RMS

For a complex number, $a+jb$  
Magnitude = $|a+jb|=\sqrt{a^2+b^2}$  

$\frac{V_{\text{out}}}{V_{\text{in}}} = K \frac{\tau_1 j \omega}{\tau_1 j \omega + 1}$

$|K\tau_1 j \omega|=|K|\tau_1 j \omega$

$\tau_1 j \omega + 1=\sqrt{1+(\tau_1\omega)^2}$

Magnitude = $|K|\frac{\tau_1 j \omega}{\sqrt{1+(\tau_1\omega)^2}}$

Phase shift:
$\angle K \frac{\tau_1 j \omega}{\tau_1 j \omega + 1}=\angle{K}+\angle{\tau_1 j \omega}-\angle{(\tau_1 j \omega + 1)}$

For a complex number, $a+jb$, 
Phase = $\angle(a+jb)=\arctan{(\frac{b}{a})}$

$\angle K \frac{\tau_1 j \omega}{\tau_1 j \omega + 1}=\arctan{\frac{0}{K}}+\angle{\arctan{\frac{\tau_1\omega}{0}}}-\angle{\arctan{\frac{\tau_1\omega}{1}}}$

$=0\degree+90\degree-\angle{\arctan{(\tau_1\omega)}}$

#### 6. Bode plot

$T(s)=\frac{V_{out}}{V_{in}}=\frac{s+3}{s^2+10s+100}$

Taking $s=j\omega$  
$T(j\omega)=\frac{V_{out}}{V_{in}}=\frac{j\omega+3}{(j\omega)^2+10(j\omega)+100}=\frac{j\omega+3}{100-\omega^2+10(j\omega)}$

Magnitude $=|T(j\omega)|=\frac{|j\omega+3|}{|100-\omega^2+10(j\omega)|}$  
$=\frac{\sqrt{9+\omega^2}}{\sqrt{(100-\omega^2)^2+100\omega^2}}$  

Phase shift $\angle{\frac{j\omega+3}{100-\omega^2+10(j\omega)}}=\arctan(\frac{\omega}{3})-\arctan(\frac{10\omega}{100-\omega^2})$

### HW 2

#### 1. Gain of inverting amplifier

$$Z_i=Z_R||Z_C$$
$$=\frac{Z_RZ_C}{Z_R+Z_C}$$
$$=\frac{R_i\frac{1}{j\omega C_i}}{R_i+\frac{1}{j\omega C_i}}$$
$$=\frac{\frac{R_i}{j\omega C_i}}{\frac{j\omega C_iR_i+1}{j\omega C_i}}$$
$$=\frac{R_i}{j\omega C_i}\times\frac{j\omega C_i}{j\omega C_iR_i+1}$$
$$=\frac{R_i}{j\omega C_iR_i+1}$$

$$Z_f=Z_C=\frac{1}{j\omega C_f}$$

$$\frac{V_{out}}{V_{in}}=-\frac{Z_{f}}{Z_i}$$
$$=-\frac{\frac{1}{j\omega C_f}}{\frac{R_i}{j\omega C_iR_i+1}}$$
$$=-\frac{1}{j\omega C_f}\times\frac{j\omega C_iR_i+1}{R_i}$$
$$=\frac{-j\omega C_iR_i-1}{R_ij\omega C_f}$$

#### 2. Low-pass filter

$A=20$  
$R_f=100k$  

##### a. Sketch

##### b. $C_f$ and $R_f$

For low-pass filter, 
$$\text{Cutoff frequency}=\frac{1}{C_f\times R_f}$$
$$\Rightarrow C_f=\frac{1}{2\pi500\times 100k}=3.18\text{nF}$$

$$A=\frac{v_o}{v_i}=\frac{R_f}{R_i}$$
$$\Rightarrow20=\frac{100k}{R_i}$$
$$\Rightarrow R_i=\frac{100k}{20}=5k\Omega$$

##### c. Transfer function

$$\frac{v_o}{v_i}=\frac{R_f}{R_i}\frac{1}{j\omega R_fC_f+1}$$
$$=\frac{R_f}{R_i}\frac{1}{j\omega\tau+1}$$

#### 3. High-pass filter

$A=20$  
$R_f=660k$  

##### a. Sketch

##### b. $C_i$ and $R_i$

$$A=-\frac{R_f}{R_i}\Rightarrow R_i=\frac{660k}{20}=33k\Omega$$

$$\text{Cutoff frequency}=\frac{1}{C_i\times R_i}$$
$$C_i=\frac{1}{2\pi\times2\times 33k}=2.41\mu\text{F}$$

##### c. Transfer function

$$\frac{v_o}{v_i}=\frac{R_f}{R_i}\frac{j\omega R_iC_i}{j\omega R_iC_i+1}$$
$$=\frac{R_f}{R_i}\frac{j\omega\tau}{j\omega\tau+1}$$

#### 4. Band-pass filter

$\text{High-pass corner frequency, }f_c=2$  
$\text{Low-pass corner frequency, }f_c=500$  
$R_i=33k$  
$R_f=100k$

##### a. Sketch

##### b. $C_i$ and $C_f$

$$\text{High-pass corner frequency, }f_c=2=\frac{1}{R_iC_i}$$  
$$\Rightarrow C_i=\frac{1}{33k\times2\pi\times2}=2.41\mu\text{F}$$

$$\text{Low-pass corner frequency, }f_c=500=\frac{1}{R_fC_f}$$
$$\Rightarrow C_f=\frac{1}{100k\times2\pi\times500}=3.18\text{nF}$$

##### c. Gain

$$A=-\frac{R_f}{R_i}=\frac{R_f}{R_i}=3.303$$

##### d. Transfer function

$$\frac{v_o}{v_i}=\frac{R_f}{R_i}\frac{j\omega R_iC_i}{(j\omega R_iC_i+1)({j\omega R_fC_f+1})}$$


### HW 3
#### 1
$$C=\frac{\epsilon_0\epsilon_rA}{thickness}=\frac{8.85\times10^{-12}\times12\times(10^{-4})}{150\times10^{-6}}=7.08\times10^{-11}$$

$$Q=KF=23\times10^{-12}(20\times10^{-3}\times9.8)=4.508\times10^{-12}$$

$$V=Q/C=63.8\text{mV}$$

#### 2
When $T=0$, $R_1=500k$
$$R=R_0[1+\alpha(37-0)]=573$$
$$v_0=10\left(\frac{1}{1+1}-\frac{0.5}{0.5+0.573}\right)=0.34\text{V}$$

$$R=R_0[1+\alpha(34-0)]=567$$
$$v_0=10\left(\frac{1}{1+1}-\frac{0.5}{0.5+0.567}\right)=0.314\text{V}$$

$$\Delta V=26\text{mV}$$

#### 3
#### 4
#### 5
#### 6
#### 7
#### 8

### HW 4
#### 1
$$f\left(a_1x_1+a_2x_2\right)=m\left(a_1x_1+a_2x_2\right)+b=ma_1x_1+ma_2x_2+b$$
$$f\left(a_1x_1\right)+f\left(a_2x_2\right)=m\left(a_1x_1\right)+b+m\left(a_2x_2\right)+b=ma_1x_1+ma_2x_2+2b$$

If $b\neq0$, then $b\neq2b$ and characteristic $mx+b$ is not linear.

Review: OK
#### 2
$$\mathcal{L}\{x_1+x_2\}=\int_0^{\infin}(x_1(t)+x_2(t))e^{-st}\text{dt}$$
$$=\int_0^{\infin}x_1(t)e^{-st}\text{dt}+\int_0^{\infin}x_2(t)e^{-st}\text{dt}$$
$$=\mathcal{L}\{x_1\}+\mathcal{L}\{x_2\}$$

Laplace transform is linear.

Review: OK

#### 3
Voltage $v_a$ and $v_b$ are determined by voltage dividers.
$$v_a=V_s\times\frac{R_3}{R_1+R_3}$$
$$v_b=V_s\times\frac{R_4}{R_2+R_4}$$
$$v_a-v_b=V_s\times\left(\frac{R_3}{R_1+R_3}-\frac{R_4}{R_2+R_4}\right)$$
Review: OK

#### 4
$R_1=R_2+\Delta R$ and replace $R_4$ with $R_3$

$$v_a-v_b=V_s\times\left(\frac{R_3}{R_2+\Delta R+R_3}-\frac{R_3}{R_2+R_3}\right)$$
Review: OK


#### 5
Review:
$$v_a-v_b=V_s\times\left(\frac{R_3}{R_2+\Delta R+R_3}-\frac{R_3}{R_2+R_3}\right)$$
$$v_a-v_b=V_s\times\left(\frac{R_3/(R_2+R_3)}{1+\Delta R/(R_2+R_3)}-\frac{R_3}{R_2+R_3}\right)$$
$$v_a-v_b=V_s\times\left(\frac{R_3}{(R_2+R_3)}(1-\Delta R)/(R_2+R_3)-\frac{R_3}{R_2+R_3}\right)$$
$$v_a-v_b\approx -V_s(R_3/(R_2+R_3)^2)\Delta R$$

#### 6
Review:

$R_2=5$  
$R_3=10$
$\Delta R=0.5$
$V_S=20$

$$v_a-v_b=20\times\left(\frac{10}{5+0.5+10}-\frac{10}{5+10}\right)=-0.44$$

$$v_a-v_b\approx 20\times\left(\frac{10}{(5+10)^2}\times 0.5\right)=-0.44$$


### HW 6
#### HW 6.1
Nerst potential of a monovalent cation (+valence) at 37-deg C given intracellular ion concentration is 10mM and th extracellular ion concentration is $80mM$.

$$V=\frac{RT}{zF}\ln{\frac{C_0}{C_i}}=10$$

#### HW 6.2

#### HW 6.3

For a linear time‐invariant (LTI) system, if the input is** $\delta(t)$, the output $v(t)$ is the *impulse response* of the system, which is the inverse Fourier transform of $H(j\omega)$.

Inverse Fourier transform of $H(j\omega)$.  In the (angular‐frequency) Fourier‐transform convention,
$
v(t)
\;=\;
\frac{1}{2\pi}\,\int_{-\infty}^{\infty} H(j\omega)\,e^{\,j\omega t}\,d\omega
\;=\;
\frac{1}{2\pi}\,\int_{-\omega_0}^{\omega_0} e^{\,j\omega t}\,d\omega,
$
because $H(j\omega)$ is $1$ only for $-\omega_0 \le \omega \le \omega_0$.

$
v(t)
\;=\;
\frac{1}{2\pi}
\int_{-\omega_0}^{\omega_0} e^{\,j\omega t}\,d\omega
\;=\;
\frac{1}{2\pi}\,\biggl[\,\frac{e^{\,j\omega t}}{j\,t}\biggr]_{\omega=-\omega_0}^{\omega=\omega_0}.
$

$
v(t)
= \frac{1}{2\pi j t}\,\Bigl(e^{\,j\omega_0 t} - e^{-\,j\omega_0 t}\Bigr)
= \frac{1}{2\pi j t}\,(2j)\,\sin(\omega_0 t)
= \frac{1}{\pi t}\,\sin(\omega_0 t).
$

$
\frac{\sin(\omega_0 t)}{\pi t}
\;=\;
\frac{\omega_0}{\pi}\,\frac{\sin(\omega_0 t)}{\omega_0 t}
\;\equiv\;
\frac{\omega_0}{\pi}\,\mathrm{sinc}\bigl(\omega_0 t\bigr),
$

$
v(t) 
\;=\;
\frac{\sin(\omega_0 t)}{\pi\,t}
\;=\;
\frac{\omega_0}{\pi}\,\mathrm{sinc}\bigl(\omega_0 t\bigr).
$


#### HW 6.4

#### HW 6.5
