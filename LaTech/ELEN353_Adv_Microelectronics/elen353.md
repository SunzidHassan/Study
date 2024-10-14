## Chapter 7: Amplifiers

### Formulas
Amplifier gain, $v_{DS}=V_{DD}-i_DR_D$  
$\Rightarrow v_{DS}=V_{DD}-k_n\frac{1}{2}(v_{GS}-V_T)^2R_D$

$\Rightarrow V_{GS}|_{B}=V_t+\frac{\sqrt{2k_nR_DV_{DD}+1}-1}{k_nR_D}$ or  
$\Rightarrow V_{OV}|_{B}=\frac{\sqrt{2k_nR_DV_{DD}+1}-1}{k_nR_D}$ and  
$V_{DS}|_{B}=V_{OV}|_{B}$


### 7.1 Basic Principles
#### 7.1.1 The Basis for Amplifier Operation

A voltage-controlled current source is created by operating a MOSFET or BJT in the active region.

For an NMOS transistor operated in saturated/pinch-off region, $v_{DS}\ge v_{OV}$, where $v_{GS}=V_{tn}+v_{OV}$. Then $v_{GS}$ controls $i_D$ according to square-law relationship.

$i_D=\frac{1}{2}k_n\left(v_{GS}-V_{tn}\right)^2$

For an npn BJT is operated in the active region, CBJ reverse bias condition is ensured by keeping $v_{CE}\ge0.3$ V. Usually $v_{BE}\simeq 0.7$ V, $v_{BC}\le0.4$ V is maintianed to prevent CBJ from conducting.

$v_{BE}$ controls $ $i_C$ according to the exponential relationship.

$i_C=I_Se^{v_{BE}/V_T}$

#### 7.1.2 Obtaining a Voltage Amplifier
Transistor is a transconductance amplifier: input signal is a voltage and output signal is a current. To convert it to a voltage amplifier, we can pass the output current through a resistor and take the voltage across the resistor as the output. Doing this for a MOSFET, we have $v_{GS}$ as the input voltage, R_D (known as a **load resistance**) converts the drain current $i_D$ to a voltage ($i_DR_D$), and $V_{DD}$ is the supply voltage that powers up the amplifier, and together with $R_D$, establishes operation in the active region.

![Figure 7.2](/home/sunzid/Study/LaTech/ELEN353_Adv_Microelectronics/Figs/Fig7_2.png)

For MOSFET, the output voltage $v_{DS}=V_{DD}-i_DR_D$

And for BJT, the output voltage $v_{CE}=V_{CC}-i_CR_C$

#### 7.1.3 The Voltage-Transfer Characteristics (VTC)

Voltage-transfer characteristic (VTC) is a plot of the out/in voltage. $v_{DS}/v_{GS}$ in case of MOSFET common source amp.

Expression of $AB$ saturated region,

For MOSFET in saturation,
$i_D=k_n\frac{1}{2}v_{OV}^2$  
$i_D=k_n\frac{1}{2}(v_{GS}-V_T)^2$  

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
$\Rightarrow V_{GS}|_{B}=V_t+\frac{\sqrt{2k_nR_DV_{DD}+1}-1}{k_nR_D}=0.613$ V and  
$V_{DS}|_{B}=V_{GS}|_{B}-V_t=0.213$ V

$V_{GS}|_C=V_{DD}$

#### 7.1.4 Obtaining Linear Amplification by Biasing the Transistor


#### Problems

##### 7.2



##### 7.6



##### 7.8



##### 7.10



##### 7.15


##### 7.33



##### 7.53