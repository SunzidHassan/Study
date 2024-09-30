## Chapter 7: Amplifiers

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
