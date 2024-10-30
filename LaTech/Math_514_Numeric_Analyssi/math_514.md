### Exercise 2.1
#### 3(c)
$f(x)=x^3-7x^2+14x-6=0$
Interval: $[3.2, 4]$

$f(3.2)=-0.11$ and $f(4)=2$, the Intermediate Value Theorem ensure that this continuous function has a root in $[3.2,4]$.

The following table is generated for the bisection method:

|  $n$  |  $a_n$  |  $b_n$  |  $p_n$   |  $f(p_n)$  |
|-------|---------|---------|----------|------------|
| $1$   | $3.2$   | $4$     | $3.6$    | $0.336$    |
| $2$   | $3.2$   | $3.6$   | $3.4$    | $-0.016$   |
| $3$   | $3.4$   | $3.6$   | $3.5$    | $0.125$    |
| $4$   | $3.4$   | $3.5$   | $3.45$   | $0.046$    |
| $5$   | $3.4$   | $3.45$  | $3.425$  | $0.013$    |
| $6$   | $3.4$   | $3.425$ | $3.4125$ | $-0.002$   |

The Solution is 3.4125.

### Exercise 2.2
#### 7
Use FPI method to determine a solution accurate within $10^{-2}$ for $x^4-3x^2-3=0$ on $[1,2]$. Use $p_0=1$.

**Solution:**

$f(x)=x^4-3x^2-3=0$  
$\Rightarrow x^4=3x^2+3$  
$\Rightarrow x=(3x^2+3)^{1/4}$  

$x=g(x)=(3x^2+3)^{1/4}$  

|   | $p_n$ | $g(p_n)$ | $p_{n+1}-p_n$ |
|---|-------|----------|---------------|
| 0 | 1     | 1.565    |               |
| 1 | 1.565 | 1.794    | 0.565         |
| 2 | 1.794 | 1.886    | 0.228         |
| 3 | 1.886 | 1.923    | 0.092         |
| 4 | 1.923 | 1.938    | 0.037         |
| 5 | 1.938 | 1.943    | 0.015         |
| 6 | 1.943 | 1.946    | 0.006         |

Root=$1.943$

### 2.3
#### 6a
Use Newton's method to find solution accurate within $10^{-5}$ for: $e^x+2^{-x}+2\cos{x}-6=0$ for $1\le x\le2$

Let's take $p_0=1$

Newton's method: $$p_1=p_0-\frac{f(p_0)}{f'(p_0)}=p_0-\frac{e^{p_0}+2^{-p_0}+2\cos{p_0}-6}{e^{p_0}-\ln(2)2^{-p_0}-2\sin{p_0}}$$


$=1-\frac{f(1)}{f'(1)}=1-\frac{e^1+2^{-1}+2\cos{1}-6}{f'(1)}$

|   | $p_n$   | $p_n-\frac{f(p_n)}{f(p_n)}$ | $p_{n+1}-p_n$ |
|---|---------|-----------------------------|---------------|
| 0 | 1.5     | 1.95649                     |               |
| 1 | 1.95649 | 1.84153                     | 0.114957      |
| 2 | 1.84153 | 1.82951                     | 0.012027      |
| 3 | 1.82951 | 1.82938                     | 0.000122      |
| 4 | 1.82938 | 1.82938                     | 0.0           |

Root=$1.82938$

### 2.4
#### 7a
Show that for any positive integer k, the sequence defined by $p_n=\frac{1}{n^k}$ converges linearly to $p=0$.

**Solution:**

$\lim_{n\rightarrow \infin}{\frac{|p_{n+1}-p|}{|p_{n}-p|^{\alpha=1}}}$  
$=\lim_{n\rightarrow \infin}{\frac{|\frac{1}{(n+1)^k}-0|}{|\frac{1}{(n)^k}-0|}}$  
$=\lim_{n\rightarrow \infin}{(\frac{n}{n+1})^k}$  
$=\lim_{n\rightarrow \infin}{(\frac{n}{n(1+\frac{1}{n})})^k}$  
$=\lim_{n\rightarrow \infin}{(\frac{1}{1+\frac{1}{n}})^k}$  
$=1\gt0$  
So the sequence $p_n=\frac{1}{n^k}$ converges linearly to $p=0$.

#### 7b
For each pair of integers $k$ and $m$, determine a number $N$ for which $\frac{1}{N^k}\lt10^{-m}$

**Solution:**

$\frac{1}{N^k}\lt10^{-m}$  
$N^k\gt10^{m}$  
$N\gt10^{m/k}$, which is the desired number.

### 2.6
#### 1b
Find the approximations to within $10^{-4}$ to all the real zeros of the following polynomial using Netton's method.  
$f(x)=x^3+3x^2-1$

**Solution:**

Choosing $x_0=1$

| 1 | 3 | 0 | -1 |         |
|---|---|---|----|---------|
|   | 1 | 4 | 4  |         |
| 1 | 4 | 4 | 3  | $f(1)$  |
|   | 1 | 5 |    |         |
| 1 | 5 | 9 |    | $f'(1)$ |

$x_1=x_0-\frac{f(x)}{f'(x)}=1-\frac{3}{9}=0.6667$

Choosing $x_1=0.6667$

| 0.6667 | 1 | 3      | 0       | -1     |              |
|--------|---|--------|---------|--------|--------------|
|        |   | 0.6667 | 2.44444 | 1.6296 |              |
|        | 1 | 3.6667 | 2.44444 | 0.6296 | $f(0.6667)$  |
|        |   | 0.6667 | 2.8889  |        |              |
|        | 1 | 4.3333 | 5.3333  |        | $f'(0.6667)$ |

$x_2=0.6667-\frac{f(0.6667)}{f'(0.6667)}=1-\frac{0.6296}{5.3333}=0.54861$

$x_3=0.54861-\frac{f(0.54861)}{f'(0.54861)}=0.53239$

$x_4=0.53239-\frac{f(0.53239)}{f'(0.53239)}=0.53208$

$x_5=0.53208-\frac{f(0.53208)}{f'(0.53208)}=0.53208$

$|x_5-x_4|\lt10^{-4}$, $x_5=0.53208$ is a zero of the function $f(x)$.

Choosing $x_0=-1$

$x_1=-1-\frac{f(-1)}{f'(-1)}=-0.66667$

$x_2=0.66667-\frac{f(0.66667)}{f'(0.66667)}=0.65277$

$x_3=0.65277-\frac{f(0.65277)}{f'(0.65277)}=0.65270$

$|x_3-x_2|\lt10^{-4}$, $x_5=0.65270$ is a zero of the function $f(x)$.

Choosing $x_0=-3$

$x_1=-3-\frac{f(-3)}{f'(-3)}=-2.88889$

$x_2=-2.88889-\frac{f(-2.88889)}{f'(-2.88889)}=-2.87945$

$x_3=-2.87945-\frac{f(-2.87945)}{f'(-2.87945)}=-2.87938$

$|x_3-x_2|\lt10^{-4}$, $x_5=-2.87938$ is a zero of the function $f(x)$.


### 3.1

#### Lagrange Interpolating Polynomials
The problem of determining the polynomial of degree one that passes through the distainct points $(x_0,y_0)$ and $(x_1,y_1)$ is same as approximating a function $f$ for which $f(x_0)=y_0$ and $f(x_1)=y_1$

$L_0(x)=\frac{x-x_1}{x_0-x_1}$ and

$L_1(x)=\frac{x-x_0}{x_1-x_0}$

$P(x)=L_0(x)f(x_0)+L_1(x)f(x_1)=\frac{x-x_1}{x_0-x_1}f(x_0)+L_1(x)=\frac{x-x_0}{x_1-x_0}f(x_1)$

Where, $L_0(x)f(x_0)=1$, $L_0(x)f(x_1)=0$, $L_1(x)f(x_0)=0$, and $L_1(x)f(x_1)=1$, which implies that

$P(x_0)=1.f(x_0)+0.f(x_1)=f(x_0)=y_0$

and

$P(x_1)=0.f(x_0)+1.f(x_1)=f(x_1)=y_1$


#### 1a
$f(x)=cosx$  
$f(0)=1$  
$f(0.6)=0.8258$  

$L_0(x)=\frac{x-x_1}{x_0-x_1}=\frac{x-0.6}{0-0.6}=\frac{x-0.6}{-0.6}$ 
and

$L_1(x)=\frac{x-x_0}{x_1-x_0}=\frac{x-0}{0.6-0}=\frac{x}{0.6}$

$P(x)=L_0(x)f(x_0)+L_1(x)f(x_1)=\frac{x-0.6}{-0.6}\times1+\frac{x}{0.6}\times0.8258$

$P(0.45)=\frac{0.45-0.6}{-0.6}\times1+\frac{0.45}{0.6}\times0.8258=0.869$

Absolute error=$|f(0.45)-P_1(0.45)|=0.0314$



### 4.3
#### Exercise
##### 5(a) Approximate integral using the Simpson's rule
$\int_{0.5}^1{x^4}dx$

Simpson's rule: $\int_{x_0}^{x_2}{(x)}dx=\frac{h}{3}[f(x_0)+4f(x_1)+f(x_2)]$
,

where $h=\frac{x_2-x_0}{n}$.

For $n=2$, $h=\frac{1-0.5}{2}=0.25$

$\int_{0.5}^1{x^4}dx=\frac{0.25}{3}[f(0.5)+4f(0.75)+f(1)]=\frac{0.25}{3}[(0.5)^4+4(0.75)^4+(1)^4]=0.1940104$

### 4.4
#### Exercise
##### 1(a) Use Composite Trapezoidal rule with indicated values of n to approximate integral: $\int_{1}^{2}x\ln{x}dx$

$h=\frac{b-a}{n}=\frac{2-1}{4}=1/4$

Composite Trapezoid rule:  

$\int_{a}^{b}f(x)=\frac{h}{2}\left[f(a)+2\sum_{j=1}^{j=n-1}{f(x_j)}+f(b)\right]=\frac{1}{8}\left[f(1)+2\sum_{j=1}^{j=3}{f(x_j)}+f(2)\right]=\frac{1}{8}\left[\ln{1}+2[1.25\ln{1.25}+1.5\ln{1.5}+1.75\ln{1.75}]+\ln{2}\right]=0.639900$


### 4.5
#### Exercise
##### 1(a) Use Romberg integration to compute $R_{3,3}$ for the integral: $\int_{1}^{1.5}{x^2\ln{x}dx}$

The Composite Trapezoid rule:

$R_{1,1}=\frac{1.5-1}{2^1}\left[1^2\ln{1}+1.5^2\ln{1.5}\right]=0.228074$  
$R_{2,1}=\frac{1.5-1}{2^2}\left[1^2\ln{1}+2\times1.25^2\ln{1.25}+1.5^2\ln{1.5}\right]=0.201202$  
$R_{3,1}=\frac{1.5-1}{2^3}\left[1^2\ln{1}+2\times[1.125^2\ln{1.125}+1.25^2\ln{1.25}+1.375^2\ln{1.375}]+1.5^2\ln{1.5}\right]=0.194494$  
$R_{4,1}=\frac{1.5-1}{2^4}\left[1^2\ln{1}+2\times[1.0625^2\ln{1.0625}+1.125^2\ln{1.125}+1.25^2\ln{1.25}+1.375^2\ln{1.375}+1.4375^2\ln{1.4375}]+1.5^2\ln{1.5}\right]=0.192818$  

The $O(h^4)$ approximations are
$R_{2,2}=R_{2,1}+\frac{1}{4^1-1}(R_{2,1}-R_{1,1})=0.192245$  
$R_{3,2}=R_{3,1}+\frac{1}{4^1-1}(R_{3,1}-R_{2,1})=0.192258$  
$R_{4,2}=R_{4,1}+\frac{1}{4^1-1}(R_{4,1}-R_{3,1})=0.192259$  

The $O(h^6)$ approximations are
$R_{3,3}=R_{3,2}+\frac{1}{4^2-1}(R_{3,2}-R_{2,2})=0.1922593$  


