## Biomedical Instrumentation


## Chapter 1
Goals:
1. Highlight connections between instrumentation and mechanical, electrical, and chemical engineering disciplines.
2. Provide an understanding of the basic concepts of instrumentation that are needed to take measurements from the body, design biomedical instruments, and to model, theoretically, certain aspects of the body.
3. Highlight aspects of electrical engineering concepts, such as positive and negative feedback, that can be used to understand and quantitatively model physiological phenomena, such as oscillatory cycles.

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
$\bar{s}=$

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