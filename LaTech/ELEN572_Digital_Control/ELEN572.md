# Lecture
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


# HW
## 1
### 1. Find the z-transforms of the following sequences:
* $\{0, 1, 1, 1, 2, 0, 0, 0, ...\}$  
$z^{-1}+z^{-2}+z^{-3}+2z^{-4}$

* $\{0, 0, 1, 1, 2, 3, 5, 0, ...\}$  
$z^{-2}+z^{-3}+2z^{-4}+3z^{-5}+5z^{-6}$

* $\{1, 4, 2, 0, 0.5, 0, 0, ...\}$  
$1+4z^{-1}+2z^{-2}+0.5z^{-4}$


### 2. Find the z-transform of $cos(k\omega T)$
$$cos(k\omega T)=\frac{1}{2}(e^{kj\omega T}+e^{-kj\omega T})$$
$$z\{cos(k\omega T)\}=\frac{1}{2}[z(\{e^{kj\omega T}\}+z\{e^{-kj\omega T}\})]$$
$$=\frac{1}{2}\left[\frac{z}{z-e^{j\omega T}}+\frac{z}{z-e^{-j\omega T}}\right]$$
$$=\frac{z}{2}\left[\frac{z-e^{-j\omega T}+z-e^{j\omega T}}{(z-e^{j\omega T})(z-e^{-j\omega T})}\right]$$
$$=\frac{z}{2}\left[\frac{2z-\cos{\omega T}-j\sin{\omega T}+\cos{\omega T}-j\sin{\omega T}}{z^2-z(e^{j\omega T}+e^{j\omega T})+1}\right]$$
$$=\frac{z}{2}\left[\frac{2z-2\cos{\omega T}}{z^2-z\cos{\omega T}+1}\right]$$
$$=\frac{z^2-2z\cos{\omega T}}{z^2-z\cos{\omega T}+1}$$

### 3.
a.
$$F(z)=5z^{-1}+4z^{-5}$$
$$=0z^0+5z^{-1}+0z^{-2}+0z^{-3}+0z^{-4}+4z^{-5}+...$$
$$f(k)=\{0,5,0,0,0,4,0,...\}$$

b.
$$F(z)=\frac{z-0.1}{z^2+0.04z+0.25}$$

||$z^{-1}-0.14z^{-2}-0.2444z^{-3}$|
|-----------------|---------|
|${z^2+0.04z+0.25}$|${z-0.1}$|
||$z+0.04+0.25z^{-1}$|
|||
||$-0.14-0.25z^{-1}$|
||$0.14-0.0056z^{-1}-0.035z^{-2}$|
|||
||$-0.2444z^{-1}+0.035z^{-2}$|

$$F(z)=z^{-1}-0.14z^{-2}-0.2444z^{-3}$$
$$f(k)=\{0,1,-0.14,-0.2444,...\}$$


### 4.

### 5. Find the final value for the function: $$F(z)=\frac{z}{z^2-7z+6}$$
$$F(z)=\frac{z}{z^2-7z+6}=\frac{z}{z^2-z-6z+6}=\frac{z}{z(z-1)-6(z-1)}=\frac{z}{(z-1)(z-6)}$$

$$f(\infin)=\lim_{z\rightarrow1}\left[(z-1)F(z)\right]$$
$$=\lim_{z\rightarrow1}\left[(z-1)\frac{z}{(z-1)(z-6)}\right]$$
$$=\lim_{z\rightarrow1}\left[\frac{z}{(z-6)}\right]=\frac{1}{1-6}=-0.2$$

### 6.


### 7. Find convolution of
$\{f(k)\}=\{2,3,4\}$  
$\{g(k)\}=\{1,2\}$  
$y(k)=f(k)*g(k)=\sum_{i=0}^kf(k-i)g(i)$  

$k=0$  
$y(0)=f(0)*g(0)=2\times1=2$  

$k=1$  
$y(1)=f(1)*g(0)+f(0)*g(1)=3\times1+2\times2=10$  

$k=2$  
$y(2)=f(2)*g(0)+f(1)*g(1)=4\times1+3\times2=10$  

$k=3$  
$y(3)=f(3)*g(0)+f(2)*g(1)=4\times2=8$  

$k\ge4$  
$y(4)=0$  


### 8. Find the transfer function of the following system
$y(k+5)=y(k+4)+u(k+1)-u(k)$  

Apply the Z-transform to $y(k+5): Z\{y(k+5)=z^5Y(z)\}$  
Apply the Z-transform to $y(k+4): Z\{y(k+4)=z^4Y(z)\}$  
Apply the Z-transform to $u(k+1): Z\{u(k+1)=zU(z)-zu(0)=zU(z)$  
Apply the Z-transform to $u(k): Z\{u(k)=U(z)$  

Substituting into the equation:  
$$z^5Y(z)=z^4Y(z)+zU(z)-U(z)$$
$$\Rightarrow z^5Y(z)-z^4Y(z)=zU(z)-U(z)$$
$$\Rightarrow  Y(z)(z^5-z^4)=U(z)(z-1)$$
$$H(z)=\frac{Y(z)}{U(z)}=\frac{z-1}{z^5-z^4}$$


### 9.

### 10.




















