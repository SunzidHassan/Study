### Homework

#### 6.15


Formulas:
$I_E=I_B+I_C$  

$I_C=\alpha I_E\Rightarrow\alpha=\frac{I_C}{I_E}$  

$I_B=\frac{I_C}{\beta}\Rightarrow\beta=\frac{I_C}{I_B}$

$I_C=I_S e^{\frac{v_{BE}}{V_T}}\Rightarrow I_S=\frac{I_C}{e^{\frac{v_{BE}}{V_T}}}$  

Let $V_T=25$ mV at room temperature.

| **Transistor** | **a**                | **b**                | **c**                | **d**                | **e**                |
|----------------|----------------------|----------------------|----------------------|----------------------|----------------------|
| **V_BE (mV)**  | 700                  | 690                  | 580                  | 780                  | 820                  |
| **I_C (mA)**   | 1000                 | 1000                 | 0.23                 | 10.10                | 73.95                |
| **I_B (uA)**   | 10                   | 20                   | 5                    | 120                  | 1050                 |
| **I_E (mA)**   | 1.01                 | 1.020                | 0.235                | 10.22                | 75.00                |
| **\alpha**     | 0.99                 | 0.98                 | 0.979                | 0.988                | 0.986                |
| **\beta**      | 100                  | 50                   | 46                   | 84.17                | 70.43                |
| **I_S**        | $6.91\times10^{-13}$ | $1.03\times10^{-12}$ | $1.93\times10^{-11}$ | $2.85\times10^{-13}$ | $4.21\times10^{-13}$ |


#### 6.23
$I_C=I_S e^{\frac{v_{BE}}{V_T}}$  

$\Rightarrow I_S=\frac{I_C}{e^{\frac{v_{BE}}{V_T}}}$  

$\Rightarrow V_{BE}=V_T\ln(\frac{I_C}{I_S})$  

Assuming $V_T=0.025$ V

$I_S=\frac{0.1}{e^{\frac{0.6}{0.025}}}=3.77\times10^{-12}$ mA  

For $I_C=1$ mA, $V_{BE}=0.025\ln(\frac{1}{I_S})=0.658$ V. 

For $I_C=10$ mA, $V_{BE}=0.025\ln(\frac{10}{I_S})=0.715$ V.


#### 6.28
##### (a) *pnp* transistor
$I_1=\frac{10.7-0.7}{10k}=1$ mA  

For large $\beta$, $I_2\approx I_1=1$ mA  

$I_2=\frac{V_2-(-10.7)}{10k}\Rightarrow V_2=I_2(10k)-10.7=-0.7$ V.

##### (b) *pnp* transistor
$I_C=\frac{-4-(-10)}{2.4k}=2.5$ mA  

For large $\beta$, $I_E\approx I_C=2.5$ mA  

$I_3=\frac{12-V_3}{5.6k}\Rightarrow V_3=12-I_3(5.6k)=-2$ V.

##### (c) *pnp* transistor
$I_C=\frac{0-(-10)}{10k}=1$ mA  
For large $\beta$, $I_5\approx I_C=1$ mA  
And $I_B=0$ mA  
$I_B=\frac{V_4-1}{20}\Rightarrow V_4=1$ V

##### (d) *npn* transistor
For large $\beta$, $I_B=\frac{V_B-V_7}{10k}=0\Rightarrow V_B=V_7$

$V_{BC}=V_B-V_C=0.7\Rightarrow V_B=V_C+0.7$ V  

$I_C=I_E\Rightarrow\frac{V_C-(-5)}{3k}=\frac{5-V_7}{9.1k}$

$\Rightarrow 9.1(V_C+5)=3(5-V_B)$

$\Rightarrow 9.1(V_C+5)=3(5-V_C-0.7)$  

$\Rightarrow 9.1V_C+45.5=3(4.3-V_C)$  

$\Rightarrow 9.1V_C+45.5=12.9-3V_C$  

$\Rightarrow 12.1V_C=12.9-45.5$  

$\Rightarrow V_C=-32.6/12.1=-2.69$ V  

$I_C=\frac{V_C-(-5)}{3k}=\frac{-2.69+5}{3k}=2.31/3 = 0.77$ mA

$V_7=V_C+0.7=-2.69+0.7\approx2$ V

#### 6.29
##### (a)
$I_C=\frac{2-0}{2k}=1$ mA  

$I_B=\frac{4.3-0}{200k}=0.0215$ mA  

$\beta=\frac{I_C}{I_B}=1/0.0215=46.5$

##### (b)
$I_C=\frac{3-0}{750}=4$ mA  

$I_B=\frac{4.3-3}{27k}=0.048$ mA  

$\beta=\frac{I_C}{I_B}=4/0.048=83.3$

##### (c)
$I_E=\frac{10-7}{1k}=3$ mA  


