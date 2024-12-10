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