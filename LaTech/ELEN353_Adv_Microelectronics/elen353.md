#### Table 5.2 Regions of Operation of the Enhancement NMOS Transistor
$v_{GS}\lt V_{tn}$: no channel, transistor in cutoff, $i_D=0$

**Triode Region:**

$v_{GD}\gt V_{tn}$ or $v_{DS}\lt v_{OV}$

$i_D=k_n'\left(\frac{W}{L}\right)\left[\left(v_{GS}-V_{tn}\right)v_{DS}-\frac{1}{2}v_{DS}^2\right]$
or 
$i_D=k_n'\left(\frac{W}{L}\right)\left(|v_{OV}|-\frac{1}{2}v_{DS}\right)v_{DS}$

**Saturation Region:**

$v_{GD}\le V_{tn}$ or $v_{DS}\ge v_{OV}$

$i_D=k_n'\left(\frac{W}{L}\right)\left(v_{GS}-V_{tn}\right)^2$
or 
$i_D=\frac{1}{2}k_n'\left(\frac{W}{L}\right)v_{OV}^2$

#### Table 5.2 Regions of Operation of the Enhancement PMOS Transistor

**Triode Region:**

$v_{DG}\gt|V_{tp}|$ or $v_{SD}\lt|v_{OV}|$

$i_D=k_p'\left(\frac{W}{L}\right)\left[\left(v_{SG}-|V_{tp}|\right)v_{SD}-\frac{1}{2}v_{SD}^2\right]$
or 
$i_D=k_p'\left(\frac{W}{L}\right)\left(|v_{OV}|-\frac{1}{2}v_{SD}\right)v_{SD}$

**Saturation Region:**

$v_{DG}\le|V_{tp}|$ or $v_{SD}\ge|v_{OV}|$

$i_D=k_p'\left(\frac{W}{L}\right)\left(v_{SG}-|V_{tp}|\right)^2$
or 
$i_D=\frac{1}{2}k_p'\left(\frac{W}{L}\right)v_{OV}^2$


### Exercise
#### 5.14

$t_{OX}=4$ nm

$\mu_n=450 \frac{{cm}^2}{V}.s$

$V_{OX}=4$ nm

$V_t=0.5$ V

$W/L=10$

**(a)**
$v_{GS}=1.8$ V and 
$v_{DS}=1$ V

$v_{OV}=v_{GS}-V_t=1.8-0.5=1.3$ V

$v_{DS}\lt v_{OV}$, so the transistor is in triode region.

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

$i_D=k_n'\left(\frac{W}{L}\right)\left(|v_{OV}|-\frac{1}{2}v_{DS}\right)v_{DS}$


**(b)**
$v_{GS}=0.7$ V and 
$v_{DS}=1.5$ V

$I_D=$

**(c)**
$v_{GS}=1.8$ V and 
$v_{DS}=0.1$ V

$I_D=$

**(d)**
$v_{GS}=v_{DS}=1.8$ V

$I_D=$