## Chapter 5: MOSFET
### 5.1 Device Structure and Physical Operation
#### 5.1.1 Device Structure

Built on a p-type substrate of thickness $1-10$ mm.
Two heavily doped n-type region are source and drain.
A layer of SiO2 insulator covers surface of the substrate. Metal is deposited on top as gate electrode.
Metal contacts are made to the source, drain, body.

- In normal operation, the pn junctions are kept reverse biased.
- Drain is positive voltage relative to the source. Current flows from drain to source in the channel region (with length $L$ and width $W$) if voltage is applied to the gate.
- The two pn junctions can be cut off by connecting the body terminal to the source terminal. The body has no effect. The three terminals are Gate, Source, Drain.

#### 5.1.2 Operation with Zero Gate Voltage
- If $V_G=0$, and $v_{DS}$ is applied, diodes are reversed biased and $I_{DS}=0$, because of high channel resistance $~10^{12}\Omega$.

#### 5.1.3 Create a Channel for Current Flow
- Ground Drain, Source, apply sufficient positive voltage, **threshold voltage**, $v_{GS}\geq V_t$ to gate.
- Holes of Body are repelled down, and free electrones from Drain and Source are accumulated under gate.
- If $v_{DS}$ is applied, current flows from Drain to Source.
- This is NMOS transistor.
- The gate and the channel form a parallel-plate capacitor - positive charge in gate plate, negative in chennel. An electric field develops in vertical direction, hence field effect transistor.
- When $v_{DS}=0$, $V$ along channel is $0$, $v{oxide}=v_{GS}$
- Overdrive or effective voltage, $v_{ov}\equiv v_{GS}-V_t$, where $V_t$ is controlled to be $0.3-1.0$ V.
- Magnitude of electron charge in the channel $|Q|=C_{OX}(WL)v_{OV}$

- Oxide capacitance, $C_{OX}=\frac{\epsilon_{OX}}{t_{OX}}$, where $\epsilon_{OX}=3.45\times 10^{-11}$ F/m is permittivity of the silicon dioxide, and $t_{OX}$ is oxide thickness.

- 

#### 5.1.4 Applying a small $v_{DS}$
- electron flows from source to drain (hence naming), current, $i_D$ from drain to source.
- Since $v_{DS}$ is small, voltage between gate and various points in channel remains constant and equal to value at the source end, $v_{GS}$, and effective voltage between gate and various points in channel remains $v_{OV}$, and channel charge $Q$ is $\frac{|Q|}{L}=C_{OX}Wv_{OV}$

- The voltage $v_{DS}$ establishes an electric field $E$ across the length of the channel, $|E|=\frac{v_{DS}}{L}$

This electric field causes the channel electrons to drift toward the drain with a electron drift velocity $\mu_n|E|=\mu_n\frac{v_{DS}}{L}$, where $\mu_n$ is the mobility of the electrons at the surface of the channel.

For small $v_{DS}$, the channel behaves as a linear resistance whose value is controlled by $v_{OV}$, which in turn is determined by $v_{GS}$.

$i_D=$ electron dift velocity $\times$ charge per unit channel length  

$i_D=\mu_n|E|\times\frac{|Q|}{L}$

$i_D=[\mu_n\times\frac{v_{DS}}{L}]\times[C_{ox}Wv_{OV}]$

$i_D=\left[\left(\mu_nC_{ox}\right)\left(\frac{W}{L}\right)v_{OV}\right]v_{DS}$  
or  
$i_D=\left[\left(\mu_nC_{ox}\right)\left(\frac{W}{L}\right)(v_{GS}-V_T)\right]v_{DS}$  

Conductance of the channel, $g_{DS}=\left(\mu_nC_{ox}\right)\left(\frac{W}{L}\right)v_{OV}$  
or  
$g_{DS}=\left(\mu_nC_{ox}\right)\left(\frac{W}{L}\right)(v_{GS}-V_t)$

Here, $\mu_nC_{ox}=k_n'$ is **process transconductance** parameter, and $\frac{W}{L}$ is **aspect ratio**. 

The **MOSFET transconductance parameter**, $k_n=k_n'\frac{W}{L}=\left(\mu_nC_{ox}\right)\left(\frac{W}{L}\right)$ A/V^2

$v_{OV}$ determines the magnitude of electron charge in the channel.

When $v_{DS}$ is small, the MOSFET behaves as a linear resistance $r_{DS}$ whose values is controlled by $v_{GS}$.  
$r_{DS}=\frac{1}{g_{DS}}$  
$r_{DS}=\frac{1}{\left(\mu_nC_{ox}\right)\left(\frac{W}{L}\right)v_{OV}}$  
$r_{DS}=\frac{1}{\left(\mu_nC_{ox}\right)\left(\frac{W}{L}\right)(v_{GS}-V_t)}$  

**Enhancement mode ($v_{GS}\ge V_t$)**: is required for a MOSFET to operate.


#### 5.1.5 Operation as $v_{DS}$ is Increased
Assuming $v_{GS}$ is contant and $\geq V_t\Rightarrow v_{OV}$ is constant.

$v_{DS}$ controls channel depth. As $v_{DS}$ increases, channel becomes more tapered.

As we move from source to drain along channel, voltage changes from $0$ to $v_{DS}$

Voltage between the gate and points along the channel decreases from $v_{GS}=V_t+v_{OV}$ to $v_{GD}=v_{GS}-v_{DS}$. Channel is deepest at source end (proportional to $v_{OV}$), and shallowest at Drain end (proportional to $v_{OV}-v_{DS}$)

Instead of $v_{OV}$, the channel is proportional to $\frac{1}{2}[v_{OV}+(v_{OV}-v_{DS})]=v_{OV}-\frac{1}{2}v_{DS}$

Thus,
$i_D=k_p'\left(\frac{W}{L}\right)\left(v_{OV}-\frac{1}{2}v_{DS}\right)v_{DS}$  
or  
$i_D=k_p'\left(\frac{W}{L}\right)\left((v_{GS}-V_t)v_{DS}-\frac{1}{2}v_{DS}^2\right)$


#### 5.1.6 Operation for $v_{DS}\gt v_{OV}$: Channel pinch-off and current saturation

When $v_{DS}\gt v_{OV}$, channel depth at drain end reduces to zero.
Increasing $v_{DS}$ doesn't increase current flow.

$i_D=k_p'\left(\frac{W}{L}\right)\left(\frac{1}{2}v_{OV}^2\right)$  
or  
$i_D=k_p'\left(\frac{W}{L}\right)\frac{1}{2}(v_{GS}-V_t)^2$  

Further increase in $v_{DS}$appears as a voltage drop across the depleton region. Thus, both the current through the channel and the voltage drop across remain constant.

#### Example 5.1
$L_{min}=0.18$ $\mu m$

$t_{OX}=4$ nm

$\mu_n=450$ $\frac{cm^2}{V}s$

$V_t=0.5$ V

**(a)** Find $C_{OX}$ and $k_n'$

**(b)** For a MOSFET with $W/L=1.8/0.18$ $\mu m/\mu m$, calcuate values of $v_{OV}$, $v_{GS}$, $v_{DSmin}$ needed to operate the transistor in the saturation region with a current $i_{D}=100$ $\mu A$

**(C)** For the device in (b), find the values of $v_{OV}$ and $v_{GS}$ required to cause the device to operate as a 1000-$\Omega$ resistor for very small $v_{DS}$

**Solution:**

**(a)**

$C_{OX}=\frac{\epsilon_{OX}}{t_{OX}}$

$=\frac{3.45\times 10^{-11} F/m}{4\times 10^{-9} m}$

$=8.63\times 10^{-3}F/m^2$

$=8.63\times 10^{-15}F/\mu m^2$

$=8.63fF/\mu m^2$

$k_n'=\mu_nC_{ox}$

$=450\times\frac{10^{12}}{10^{4}}\frac{\mu m^2}{V}s(8.63\times10^{-15}F/\mu m^2)$

$=450\times10^{8}\frac{\mu m^2}{V}s(8.63\times10^{-15}F/\mu m^2)$

$=388\times10^{-6}\frac{Fs}{V}$

$=388\frac{\mu A}{V^2}$


**(b)**

For operation in the saturation region,

$i_D=\frac{1}{2}k_n'\frac{W}{L}v_{OV}^2$

$\Rightarrow100\mu A=\frac{1}{2}(388\frac{\mu A}{V^2})\frac{1.8\mu m}{0.18\mu m}v_{OV}^2$

$\Rightarrow\frac{200\mu A}{388\frac{\mu A}{V^2}}=v_{OV}^2$

$\Rightarrow v_{OV}=0.23$ V

$v_{GS}=V_t+v_{OV}=0.23+0.5=0.73$ V

$v_{DSmin}=v_{OV}=0.23$ V

**(c)**

For the MOSFET in triode region with very small $v_{DS}$

$r_{DS}=\frac{1}{k_n'\frac{W}{L}v_{OV}}$

$v_{OV}=\frac{1}{k_n'\frac{W}{L}r_{DS}}$

$v_{OV}=\frac{1}{388\times10^{-6}\frac{A}{V^2}\times10\times1000\Omega}$

$v_{OV}=\frac{1}{388\times10^{-6}\frac{A}{V^2}\times10\times1000\Omega}$

$v_{OV}=0.26$ V

$v_{GS}=v_{OV}+V_t=0.76$ V


#### 5.1.7 The p-Channel MOSFET