## Chapter 7: Amplifiers

### Formulas

**7.1.3**

Amplifier gain, $v_{DS}=V_{DD}-i_DR_D$  
$\Rightarrow v_{DS}=V_{DD}-k_n\frac{1}{2}(v_{GS}-V_T)^2R_D$

$\Rightarrow V_{GS}|_{B}=V_t+\frac{\sqrt{2k_nR_DV_{DD}+1}-1}{k_nR_D}$ or  
$\Rightarrow V_{OV}|_{B}=\frac{\sqrt{2k_nR_DV_{DD}+1}-1}{k_nR_D}$ and  
$V_{DS}|_{B}=V_{OV}|_{B}$

Voltage gain, $A_v=-\frac{I_CR_C}{V_T}$


**7.1.4**

$v_{GS}(t)=V_{GS}+v_{gs}(t)$

$v_{DS}(t)=V_{DD}-k_nR_D\frac{1}{2}(v_{GS}(t)-V_T)^2$

For BJT,

$V_{CE}=V_{CC}-R_CI_Se^{v_{BE}/V_T}$  

$I_C=I_Se^{V_{BE}/V_T}$  

$v_{BE}(t)=V_{BE}+v_{be}(t)$


**7.1.5**

$A_v=\frac{dv_{DS}}{dv_{GS}}$  
$\Rightarrow A_v=-k_nV_{OV}R_D$

$A_v=-\frac{I_DR_D}{V_{OV}/2}$

$\Rightarrow A_v=-\frac{V_{DD}-V_{DS}}{V_{OV}/2}$  

Max gain at point B, $A_{vmax}=-\frac{V_{DD}-V_{OV}}{V_{OV}/2}$

### 7.1 Basic Principles
#### 7.1.1 The Basis for Amplifier Operation

A voltage-controlled current source is created by operating a MOSFET or BJT in the active region.

For an NMOS transistor operated in saturated/pinch-off region, $v_{DS}\ge v_{OV}$, where $v_{GS}=V_{tn}+v_{OV}$. Then $v_{GS}$ controls $i_D$ according to square-law relationship.

$i_D=\frac{1}{2}k_n\left(v_{GS}-V_{tn}\right)^2$

For an npn BJT is operated in the active region, CBJ reverse bias condition is ensured by keeping $v_{CE}\ge0.3$ V. Usually $v_{BE}\simeq 0.7$ V, $v_{BC}\le0.4$ V is maintianed to prevent CBJ from conducting.

$v_{BE}$ controls $i_C$ according to the exponential relationship.

$i_C=I_Se^{v_{BE}/V_T}$

#### 7.1.2 Obtaining a Voltage Amplifier
Transistor is a transconductance amplifier: input signal is a voltage and output signal is a current. To convert it to a voltage amplifier, we can pass the output current through a resistor and take the voltage across the resistor as the output. Doing this for a MOSFET, we have $v_{GS}$ as the input voltage, $R_D$ (known as a **load resistance**) converts the drain current $i_D$ to a voltage ($i_DR_D$), and $V_{DD}$ is the supply voltage that powers up the amplifier, and together with $R_D$, establishes operation in the active region.

![Figure 7.2](/home/sunzid/Study/LaTech/ELEN353_Adv_Microelectronics/Figs/Fig7_2.png)

For MOSFET, the output voltage $v_{DS}=V_{DD}-i_DR_D$

And for BJT, the output voltage $v_{CE}=V_{CC}-i_CR_C$

#### 7.1.3 The Voltage-Transfer Characteristics (VTC)

Voltage-transfer characteristic (VTC) is a plot of the out/in voltage. $v_{DS}/v_{GS}$ in case of MOSFET common source amp.

When $v_{GS}\lt V_t$, the amplifier is in cutoff, and $v_{DS}=V_{DD}-i_DR_D=V_{DD}-0\times R_D=V_{DD}$.  
As $v_{GS}$ increases, $i_D=\frac{1}{2}k_nv_{OV}^2$ increases, $v_{DS}=V_{DD}-i_DR_D$ decreases.  
As $v_{DS}$ becomes less than $v_{GS}-V_t$, the transistor goes to triode region, $i_d=\frac{1}{2}k_n(v_{OV}v_{DS}-\frac{1}{2}v_{DS}^2)$ decrease slows, and $v_{DS}$ decrease slows.

The segment of greatest slope (negative), therefore highest gain is $AB$, the saturation/active region.

For MOSFET in saturation,
$i_D=k_n\frac{1}{2}v_{OV}^2$  
$\Rightarrow i_D=k_n\frac{1}{2}(v_{GS}-V_T)^2$  

Amplifier gain, $v_{DS}=V_{DD}-i_DR_D$  
$\Rightarrow v_{DS}=V_{DD}-k_n\frac{1}{2}(v_{GS}-V_T)^2R_D$

At point B, $v_{GS}=V_{GS}|_{B}$ and $v_{DS}=V_{DS}|_{B}=V_{GS}|_{B}-V_t$

$\Rightarrow V_{GS}|_{B}=V_t+\frac{\sqrt{2k_nR_DV_{DD}+1}-1}{k_nR_D}$ or  
$\Rightarrow V_{OV}|_{B}=\frac{\sqrt{2k_nR_DV_{DD}+1}-1}{k_nR_D}$ and  
$V_{DS}|_{B}=V_{OV}|_{B}$

Similarly, in BJT active region, the output voltage $v_{CE}$ is related to the input voltage $v_{BE}$ by:

$v_{CE}=V_{CC}-R_CI_Se^{v_{BE}/V_T}$

#### Exercise
##### 7.1
The amplifier in Fig. 7.2(a) with  
$V_{DD}=1.8$ V  
$R_D=17.5$ $k\Omega$  
$V_t=0.4$ V  
$k_n=4$ $mA/V^2$  
$\lambda=0$  
Determine coordinates of the end points of the active-region segment of the VTC. Also determine $V_{DS}|_C$ assuming $V_{GS}|_C=V_{DD}$

**Solution:**

At point A, $v_{GS}|_A=V_t=0.4$ V and  
$V_{DS}|_{A}=V_{DD}=1.8$ V
  
At point B,  
$V_{GS}|_{B}=V_t+\frac{\sqrt{2k_nR_DV_{DD}+1}-1}{k_nR_D}=0.613$ V and  
$V_{DS}|_{B}=V_{GS}|_{B}-V_t=0.213$ V

$V_{GS}|_C=V_{DD}$, the MOSFET is in Triode.

$V_{DS}|_{C}=V_{DD}-i_DR_D$  
$\Rightarrow V_{DS}=1.8-(0.5\times4m\times17.5k)\times(v_{DS}v_{OV}-0.5\times V_{DS}^2)$  
$\Rightarrow V_{DS}=1.8-35\times(1.4v_{DS}-0.5\times V_{DS}^2)$  
$\Rightarrow V_{DS}=1.8-35\times v_{DS}(1.4-0.5V_{DS})$  

#### 7.1.4 Obtaining Linear Amplification by Biasing the Transistor

A dc voltage $V_{GS}$ is applied to obtain operation at point Q on the segment AB. The coordinates of Q are dc voltage $V_{DS}$ and $V_{GS}$, which are related by:

$V_{DS}=V_{DD}-k_nR_D\frac{1}{2}(v_{GS}-V_T)^2$

Point Q or the **bias point**, or the **dc operating point**, or the **quiescent point**.

Next, the signal to be amplified, $v_{gs}$, a function of time $t$, is superimposed on the bias voltage $V_{GS}$, and thus, the total instanteneous value of $v_{GS}$ becomes, 
$v_{GS}(t)=V_{GS}+v_{gs}(t)$, and $v_{DS}(t)=V_{DD}-k_nR_D\frac{1}{2}(v_{GS}(t)-V_T)^2$

If the amplitude of the signal $v_{gs}$ is increased, it'll go outside the almost-linear segment of AB, and can leave AB. Then negative peaks of $v_{gs}$ can enter cutoff region, and $v_{ds}$ will be 'clipped off'. Similarly, positive peaks of $v_{ds}$ will enter triode, and $v_{ds}$ will be flattened.

For BJT,  
$V_{CE}=V_{CC}-R_CI_Se^{v_{BE}/V_T}$  
$I_C=I_Se^{V_{BE}/V_T}$  
Also, superimposing a small-signal $v_{be}$ on the dc bias voltage $V_{BE}$ results in $v_{BE}(t)=V_{BE}+v_{be}(t)$


#### 7.1.5 The small-signal voltage gain

If input signal $v_{gs}$ is kept small, $v_{ds}$ will be slope at point Q times $v_{gs}$.\
Voltage gain, $A_v=\frac{dv_{DS}}{dv_{GS}}$  
$\Rightarrow A_v=-k_nV_{OV}R_D$

- The gain is negative (inverting amplifier).
- The gain is proportional to the load resistance $R_D$, the transistor transconductance parameter $k_n$, and the overdrive voltage $V_{OV}$.
- For maximising gain, the bias point Q should be close to point B, while allowing desired negative swing.

$A_v=-\frac{I_DR_D}{V_{OV}/2}$

$\Rightarrow A_v=-\frac{V_{DD}-V_{DS}}{V_{OV}/2}$  

The max slope of VTC is at point B, thus max gain, $A_{vmax}=-\frac{V_{DD}-V_{OV}}{V_{OV}/2}$

#### Example
##### 7.1
$V_t=0.4$ V  
$k_n'=0.4m$ $A/V^2$  
$W/L=10$  
$\lambda=0$  
$V_{DD}=1.8$ V  
$R_D=17.5k$ $\Omega$  
$V_{GS}=0.6$ V

(a) For $v_{gs}=0$ (and hence $v_{ds}=0$), find $V_{OV}$, $I_D$, $V_{DS}$, and $A_v$.

(b) max symmetrical signal swing at drain. Max allowable amplitude of a sinusoidal $v_{gs}$.

**Solution**

(a)

$V_{OV}=V_{GS}-V_t=0.6-0.4=.2$ V

$I_D=\frac{1}{2}k_n'(W/L)V_{OV}^2=0.5\times0.4m\times10\times0.2^2=0.08m$ A

$V_{DS}=V_{DD}-I_DR_D=1.8-0.08m\times17.5k=0.4$ V

$A_v=-\frac{V_{DD}-V_{DS}}{V_{OV}/2}=-\frac{1.8-0.4}{.1}=-14$

(b)

Since $V_{OV}=0.2$ V, and $V_{DS}=0.4$ V, max allowable negative signal swing is 0.2 V. In positive direction, 0.2 V will not cause cut-off, since $V_{DD}=1.8$ V. But symmetrical signal swing is $\pm0.2$ V.

The corresponding max amplitude of $v_{gs}=\frac{v_{ds}}{|A_v|}=\frac{0.2}{14}=14.3m$ V.

#### Exercise
##### 7.2
$V_t=0.4$ V  
$k_n'=0.4m$ $A/V^2$  
$W/L=10$  
$\lambda=0$  
$V_{DD}=1.8$ V  
$R_D=17.5k$ $\Omega$  
$V_{GS}=0.6$ V

(a)
get voltage gain of -10 by changing $R_D$ and keeping $V_{OV}$ constant.

(b)
changing $V_{OV}$ while keeping $R_D$ constant.

For each design, specify $V_{GS}$, $I_D$, $R_D$, and $V_{DS}$.

**Solution**

(a)

$V_{OV}=0.6$

$V_{OV}=V_{GS}-V_t=0.2$ V

$I_D=\frac{1}{2}k_n'(W/L)V_{OV}^2=0.08m$

$A_v=-\frac{I_DR_D}{V_{OV}/2}$  
$\Rightarrow R_D=-\frac{A_vV_{OV}}{2I_D}=12.5k$

$V_{DS}=V_{DD}-I_DR_D=0.8$ V


(b)
$A_v=-k_n(W/L)V_{OV}R_D$  
$\Rightarrow V_{OV}=\frac{A_v}{-k_n(W/L)R_D}=0.143$ V

$V_{OV}=V_{GS}-V_t\Rightarrow V_{GS}=V_{OV}+V_t=0.543$ V

$I_D=\frac{1}{2}k_n'(W/L)V_{OV}^2=0.04m$ A

$R_D=17.5k$ $\Omega$

$V_{DS}=V_{DD}-I_DR_D=1.1$ V

**The BJT Case**

Similarly for BJT, $A_v=\frac{dv_{CE}}{dv_{BE}}$

$A_v=-\frac{I_CR_C}{V_T}=-\frac{V_{CC}-V_{CE}}{V_T}$

$A_{vmax}=-\frac{V_{CC}-0.3}{V_T}$


- The gain is negative (inverting amp)
- The gain is proportional to the collector bias current $I_C$ and load resistance $R_C$.
- For maximising gain, the transistor should be biased at the lowest possible $V_{CE}$ while allowing desired negative swing.

BJT gain is higher (as $V_T$ is lower than $V_{OV}$), but MOSFET is preferred to BJT for amp.

#### Example
##### 7.2
$I_S=10^{-15}$ A  
$R_C=6.8k$ $\Omega$  
$V_{CC}=10$ V

(a) $V_{BE}$ required to operate transistor at $V_{CE}=3.2$ V, $I_C=?$

(b) $A_v$ at bias point. If an input sine-wave signal of 5-mv peak amplitude is superimposed on $V_{BE}$, find amplitude of the output sine-wave signal.

(c) Find the positive increment in $v_{BE}$ (above $V_{BE}$) that drives the transistor to the edge of saturation, where $v_{CE}=0.3$ V.

(d) find the negative increment in $v_{BE}$ that drives the transistor to within 1\% of cutoff (i.e., to $v_{CE}=0.99V_{CC}$)

**Solution**

(a)
$I_C=\frac{V_{CC}-V_{CE}}{R_C}=1m$ A

$I_C=I_Se^{V_{BE}/V_{T}}$  
$\Rightarrow V_{BE}=690m$ V  

(b)
$A_v=-\frac{V_{CC}-V_{CE}}{V_T}=-272$

$v_{ce}=272\times5m=1.36$ V

(c)
If $v_{BE}$ (input) is increased, or $v_{CE}$ (output) is decreased, the transistor approaches edge of sat in VTC.

$i_c=\frac{V_{CC}-v_{CE}}{R_C}=\frac{10-0.3}{6.8k}=1.426m$ A

$\Delta v_{BE}=V_T\ln(\frac{i_{c2}}{i_{c1}})=V_T\ln(\frac{1.426}{1})=9m$ V

(d)
If $v_{BE}$ (input) is decreased, or $v_{CE}$ (output) is increased, the transistor approaches cutoff in VTC.
$v_{CE}=0.99v_{CC}$

$i_c=\frac{V_{CC}-v_{CE}}{R_C}=\frac{10-0.99}{6.8k}=0.0147m$ A

$\Delta v_{BE}=V_T\ln(\frac{i_{c2}}{i_{c1}})=V_T\ln(\frac{0.0147}{1})=-105.5m$ V

##### 7.3
$I_S=10^{-15}$ A  
$R_C=6.8k$ $\Omega$  
$V_{CC}=10$ V
$I_C=1m$ A

Keep $I_C$ unchanged, find $R_C$ that will cause gain of -320 V/V. What's the largest negative signal swing allowed at the output (assum $v_{CE}$ can't decrease below 0.3 V)? What is corresponding input signal amplitude?

$A_v=-\frac{I_CR_C}{V_T}$  
$\Rightarrow R_C=-\frac{A_vV_T}{I_C}=8k$ $\Omega$  

$A_v=\frac{V_{CC}-V_{CE}}{V_T}$  
$\Rightarrow V_{CE}=V_{CC}-A_vV_T=2$ V

Largest negative signal swing at the output $=2-0.3=1.7$ V

Corresponding input signal amplitude
$A_v=\frac{v_{CE}}{v_{BE}}$  
$\Rightarrow v_{BE}=\frac{v_{CE}}{A_v}=5.3m$ V.  

### 7.1
#### 7.1.6

#### 7.1.7 Deciding Q point
As close to point B as possible, while allowing for required nengative swing (having enough 'legroom').
Allowing for positive swing (having enough 'headroom').

### 7.2 Small-Signal Operation and Models
#### 7.2.1 The MOSFET Case
Signal $v_{gs}$ is superimposed on bias voltage $V_{GS}$ to be amplified.

**The DC Bias Point**

By setting $v_{gs}=0$, we can find bias current $I_D$.  
$I_D=k_n\frac{1}{2}V_(OV)^2$

The DC voltage at drain,  
$V_{DS}=V_{DD}-I_DR_D$

For sat, $V_{DS}\gt V_{OV}$

Furthermore, since total voltage at the drain will have a signal superimposed on $V_{DS}$, $V_{DS}$ has to be sufficiently greater than $V_{OV}$ to allow for required negative signal swing.

**The Signal Current in the Drain Terminal**

Applying signal $v_{gs}$, the total instantaneous gate-to-source voltage will be $v_{GS}=V_{GS}+v_{gs}$

Resulting in total instanteneous drain current $i_D=k_n\frac{1}{2}v_{OV}^2=k_n\frac{1}{2}(v_{GS}-V_t)^2=k_n\frac{1}{2}(V_{GS}+v_{gs}-V_t)^2=k_n\frac{1}{2}(V_{GS}-V_t)^2+k_n(V_{GS}-V_t)v_{gs}+k_n\frac{1}{2}v_{gs}^2$

The First term is the dc bias current $I_D$, the second term is current component related to input signal $v_{gs}$, the third term is nonlinear distortion. To reduce distortion, $v_{gs}\lt\lt2V_{OV}$.

If the small signal condition is satisfied, $i_D=I_D+i_d$, where $i_d=k_n(V_{GS}-V_t)v_{gs}$

MOSFET transconductance, $g_m$ relates $i_d$ and $v_{gs}$.

$g_m=\frac{i_d}{v_{gs}}=k_n(V_{GS}-V_t)=k_nV_{OV}$

$g_m=\frac{\delta i_d}{\delta v_{GS}}$

**The Voltage Gain**

$v_{DS}=V_{DD}-i_DR_D=V_{DD}-(I_D+i_d)R_D=V_{DS}-R_Di_d$

The signal component of drain voltage, $v_{ds}=-i_dR_D=-g_mv_{gs}R_D$

$A_v=\frac{v_{ds}}{v_{gs}}=-g_mR_D$

For operation in the active region, $v_{DS}$ will have to be within $V_{DD}$ and $v_{GS}-V_t$

**Separating the DC Analysis and the Signal Analysis**

Given $v_{DS}=V_{DS}+v_{ds}$ and $i_D=I_D+i_d$, once we establish stable dc point, we can seperate dc and signal to perform signal analysis.

**Small-Signal Equivalent-Circuit Models**

From signal point of view, FET accepts a signal $v_{gs}$, and provides current $i_d=g_mv_{gs}$ at drain. Fig 7.13(a) is the small signal equivalent circuit.

- the signal current of an idean constant dc current source will always be zero
- thus, an ideal constant dc current source can be replaced by an open circuit in the small-signal equivalent circuit of the amp.

Drain current depends on $v_{DS}$, which is modeled by resistance $r_o$ between drain and source, where $r_o=\frac{|V_A|}{I_D}$, where early voltage $V_A=1/\lambda$ is a MOSFET parameter, and $I_D=k_n\frac{1}{2}V_{OV}^2$

$A_v=\frac{v_{ds}}{v_{gs}}=-g_m(R_D||r_o)$

**The Transconductance $g_m$**

$g_m=k_n'(W/L)(V_{GS}-V_t)$

$=k_n'(W/L)V_{OV}$

$=\sqrt{2k_n'}\sqrt{W/L}\sqrt{I_D}$

$=\frac{I_D}{V_{OV}/2}$

Three different relationship for determining $g_m$, three design parameters-$(W/L)$, $V_{OV}$, $I_D$

- 

### Example
#### 7.3
$V_t=1.5$ V  
$k_n'(W/L)=0.25m$ $A/V^2$  
$V_A=50$ V  

**Solutiion**

Eliminate $v_i$ and open-circuit two coupling capacitors for dc operating point.
Here, $I_G=0$, thus, $V_{GS}=V_{DS}=V_{DD}-I_DR_D$

Since $V_{DS}=V_{GS}$, sat $I_D=k_n\frac{1}{2}V_{OV}^2=1.06m$ A

$V_{GS}=V_{DS}=4.4$ V  
$V_{OV}=2.9$ V  

Small-signal analysis: fig 7.16(c)

$g_m=k_nV_{OV}=0.725m$ A/V  
$r_o=\frac{V_A}{I_D}=47k$ $\Omega$

$R_{in}=v_i/i_i$  
$A_v=v_o/v_i$

$R_L'=R_L||R_D||r_o=10||10||47=4.52k$ $\Omega$

$A_v=-g_mR_L'=-3.3$ V/V

#### Problems

##### 7.2
$V_{DD}=3$ V  
$k_n=5$ $mA/V^2$  
$V_{DS}=0.3$ V  
$R_D=?$ $k\Omega$  

If $k_n=10$ $mA/V^2$,  
$R_D=?$ $k\Omega$  

**Solution:**

At point B, $V_{DS}|_{B}=V_{OV}=0.3$ V  

$I_D=k_n\frac{1}{2}V_{OV}^2=5m\times0.5\times0.3^2=0.225m$ A

$R_D=\frac{V_{DD}-V_{DS}}{I_D}=12k$ $\Omega$

If $k_n=10$ $mA/V^2$
$I_D=k_n\frac{1}{2}V_{OV}^2=10m\times0.5\times0.3^2=0.45m$ A

$R_D=\frac{V_{DD}-V_{DS}}{I_D}=6k$ $\Omega$


##### 7.6
$R_D=20$ $k\Omega$  
$V_{RD}=2$ V  
$V_{GS}=0.75$ V  
$A_v=-16$ V/V  
$V_t=?$  
If $k_n'=400$ $\mu A/V^2$, $W/L=?$

Voltage gain, $A_v=-\frac{V_{RD}}{V_{OV}/2}$  
$\Rightarrow V_{GS}-V_t=\frac{2V_{RD}}{-A_v}$  
$\Rightarrow V_t=V_{GS}-\frac{2V_{RD}}{-A_v}$  
$\Rightarrow V_t=0.75-\frac{4}{16}=0.5$ V  

$I_D=k_n'(\frac{W}{L})\frac{1}{2}v_{ov}^2$  
$\Rightarrow \frac{W}{L}=\frac{I_D}{k_n'\frac{1}{2}(v_{GS}-V_t)^2}$  
$\Rightarrow \frac{W}{L}=\frac{2/20k}{400\mu\frac{1}{2}(0.75-0.5)^2}=8$  


##### 7.8
$v_{DS}=\pm0.2$ V  
$V_{DD}=2$ V  
$v_{OV}=2$ V  

**Solution:**  
**(a)**
For max gain, $V_{DS}$ at point B, $V_{DS}=v_{OV}=0.2$ V  

**(b)**
$A_{vmax}=-\frac{V_{DD}-v_{DS}}{v_{OV}/2}$  
$\Rightarrow A_{vmax}=-\frac{V_{DD}-v_{OV}}{v_{OV}/2}$  
$A_{vmax}=-\frac{2-0.2}{0.1}=-18$  

$A_{v}=\frac{v_{DS}}{v_{GS}}$  
$\Rightarrow v_{GS}=\frac{v_{DS}}{A_{v}}$  
$\Rightarrow v_{GS}=\frac{0.2}{18}=0.1111$ V  

**(c)**
$R_D=\frac{V_{DD}-v_{DS}}{I_D}$  
$\Rightarrow R_D=\frac{1.8}{100\mu}=18k\Omega$  

**(d)**
$I_D=k_n'(\frac{W}{L})\frac{1}{2}v_{ov}^2$  
$\frac{W}{L}=\frac{I_D}{k_n'\frac{1}{2}v_{ov}^2}$  
$\frac{W}{L}=\frac{100\mu}{400\mu\frac{1}{2}0.2^2}=12.5$  

##### 7.10

$A_v=-\frac{V_{CC}-V_{CE}}{V_T}$  
$\Rightarrow A_v=-\frac{3-0.5}{25m}=-100$ V/V  

Without entering negative swing, maximum allowed output negative swing is $0.5-0.3=0.2$, or -2 V.

$A_{vmax}=\frac{V_{CC}-0.3}{V_T}$  
$\Rightarrow A_v=-\frac{3-0.3}{25m}=-108$ V/V  

$A_{vmax}=\frac{v_o}{v_i}$  
$\Rightarrow v_i=\frac{v_o}{A_vmax}$  
$\Rightarrow v_i=\frac{0.3}{-108}=2.778$ mV  

##### 7.15
$I_C=0.2$ mA  
$V_{CC}=3$ V  
$R_C=10$ $k\Omega$  

$V_{CCth}=3\frac{10}{10+10}=1.5$ V  
$R_{Cth}=(\frac{1}{10}+\frac{1}{10})^{-1}=5$ $K\Omega$

$A_v=-\frac{I_CR_{Cth}}{V_T}$  
$\Rightarrow A_v=-\frac{0.2m5k}{25m}=-40$ V/V  



## Chapter: Microfabrication
### VLSI Fabrication Tech
 