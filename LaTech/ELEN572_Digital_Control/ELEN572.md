## 2. Discrete Time Systems and Z-Transform

Analog/Digital: y-axis
Continuous/Discrete: x-axis

Sample times (x-values) and sample values (y-values).

Continuous time - Analog and Digital  
Discrete time - Analog and Digital  

### Discrete time systems
Systems whose inputs and outputs are discrete-time signals.

Example: bank interest
- Step $k$
- Current balance, $y[k]$
- Previous balance $y[k-1]$
- Current deposit $u[k]$
- Interest rate, $r$

Difference equation for current balance,
$$y[k]=u[k]+y[k-1](1+r)$$

Differential (continuous-time) vs Difference (discrete-time) equations.

General form of difference equations:
$$y(k+n)=f\left[y(k+n-1),y(k+n-2),...,y(k+1),y(k),u(k+n),u(k+n-1),...,u(k+1),u(k)\right]$$

### Linear difference equation
$$y(k+n)+a_{n-1}y(k+n-1)+...+a_{1}y(k+1)+a_{0}y(k)=b_{n}u(k+n)+b_{n-1}u(k+n-1)+...+b_{1}u(k+1)+b_{0}u(k)$$
Properties:
- **System order**: the difference between highest and lowest arguments of $y(.)$ and $u(.)$
- **Time invariant**: if the coefficients ($a_o, ..., a_{n-1},b_0,...,b_n$) are constants, then the difference is time invariant. Apple (time variant) vs goat (time invariant)
- **Homogeneous**: if $u(.)=0$, then the difference equation is homogeneous.

Examples:

$y(k+2)+0.8y(k+1)+0.07y(k)=u(k)$
- The equation linear
- The coefficients are constant: time invarient
- We have u(k) in RHS: not homogenous
- System order = $y(k+2)-y(k)$ or 2

$y(k+4)+sin(0.4k)y(k+1)+0.3y(k)=0$
- Linear (Elements have function coefficient, but they are not functions)
- Time variant
- Homogeneous
- System order is 4

$y(k+1)=-0.1y^2(k)$
- Non-linear, time invarient, homogeneous.

Practice:
$y(k+2)-y(k+1)y(k)=u(k)$
- Non-linear
- Time-variant: constant coefficients
- Non-homogeneous
- Order: 2

$y(k+3)+2y(k)=0$
- Lienar
- Time invariant
- Homogeneous
- Order 3

$y(k+4)+y(k-1)=u(k)$
- System order is 5
- Linear
- Time invarient
- Non-homogeneous

### Z-transform
Motivation: similar to Laplace transform - converting convolution (for discrete, integration for continuous) into multiplication - by transforming time domain into z domain.

Z-transform is the discrete time version of Laplace-tranform.
$z=e^{sT}$


$Z\{u_k\}=1+3.z^{-1}+2z^{-2}+0z^{-3}+4z^{-4}$


$u_k=\{0,1,2,4,0,... \}$  
$Z\{u_k\}=0+1.z^{-1}+2.z^{-2}+4.z^{-3}$

$u_k=\{0,0,0,1,1,1,0,0,0,... \}$  
$Z\{u_k\}=1.z^{-3}+1.z^{-4}+1.z^{-5}$

$u_k=\{0,0,0,1,1,1,0,0,0,... \}$  
$Z\{u_k\}=1.z^{-3}+1.z^{-4}+1.z^{-5}$

$u_k=\{1,1,1,... \}$  
$Z\{u_k\}=\sum_{k=0}^\infin{z^{-k}}$

$$|a|\lt1\rightarrow\sum_{k=0}^\infin{a^{k}}=\frac{1}{1-a}$$

$$|z^{-1}|\lt1\rightarrow\sum_{k=0}^\infin{z^{-k}}=\frac{1}{1-k^{-1}}=\frac{z}{z-1}$$

15:

...

## 3. z-Transform Inversion and Final Value Theorem
### Method 1: Long Division
