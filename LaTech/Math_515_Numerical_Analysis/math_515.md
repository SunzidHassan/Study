

## Chapter 5: Initial-Value Problems for Ordinary Differential Equations
### 5.1: The Elementary Theory of Initial-Value Problems
#### 5.1 Excise
##### 5.1 Excise - 3: 



(a) $f(t, y) = t^2y + 1$  
Since $t^2y + 1$ is a polynomial expression in$t$ and $y$, it is continuous for all $(t, y)$.
The partial derivative of $f$ with respect to $y$:  
$\frac{\partial f}{\partial y} = t^2$  
On $0 \le t \le 1$, the quantity $|t^2| \le 1$. Thereby,$\left| \frac{\partial f}{\partial y} \right| \le 1$  
So, $f$ is Lipschitz in $y$ with Lipschitz constant,$L=1$.  
By Theorem 5.6, $f$ being continuous and Lipschitz on $D$ implies the initial-value problem is well-posed.  

(b) $f(t, y) = ty$  
$\rightarrow ty$is polynomial, so it is continuous for all$(t, y)\rightarrow \frac{\partial f}{\partial y} = t$, hence $|t| \le 1$ is Lipschitz in $y$.  
Therefore, by Theorem 5.6, the initial-value problem is posed.  

(c) $f(t, y) = 1 - y$ is continuous everywhere. $\frac{\partial f}{\partial y} = -1$ is constant, and $|-1| = 1$, so $f$ is Lipschitz in$y$.  
Again, the IVP is well-posed.  

(d) $f(t, y) = -ty + \frac{4t}{y}$ is continuous except at $y=0$, where it becomes undefined, therefore $f$ is not continuous there.  
$\frac{\partial f}{\partial y} = -t - \frac{4t}{y^2}$  
Here, $(-t)$is bounded by $1$ on$[0, 1]$, but $\left[-\frac{4t}{y^2}\right]$ can be infinite if $y$ is nearly zero.  
There is no finite $L$ such that,$\left[ \frac{\partial f}{\partial y} \right] \le L \quad \text{for all } (t, y) \in D$  
$\therefore f$ is not Lipschitz. Hence, part $d$ is not well-posed.


### 5.2: Euler’s Method
#### 5.2 Excise
##### 5.2 Excise - 5: Use Euler’s method to approximate the solutions for each of the following initial-value problems.
###### 5.2 Exercise - 5a: $y'=\frac{y}{t}-(\frac{y}{t})^2, 1\le t \le 2, y(1)=1, h=0.1$
$w_0=y(1)=1$  
$w_{i+1}=w_i+hf(t_i,w_i)$  
$w_1=w_0+hf(t_0,w_0)=w_0+h(\frac{w_0}{t_0}-(\frac{w_0}{t_0})^2)=1+0.1(\frac{1}{1}-(\frac{1}{1})^2)=1$  
$w_2=w_1+hf(t_1,w_1)=w_1+h(\frac{w_1}{t_1}-(\frac{w_0}{t_1})^2)=1+0.1(\frac{1}{1.1}-(\frac{1}{1.1})^2)=1.0082644628$  

```python
t = 1.0
t_max = 2
w = 1.0
h = 0.1
i = 0
while t < t_max+h:
    print("i:",i," t:",round(t,1)," w:",round(w,5))
    w = w+h*((w/t)-(w/t)**2)
    t += h
    i += 1

# Output:
i: 0  t: 1.0  w: 1.0
i: 1  t: 1.1  w: 1.0
i: 2  t: 1.2  w: 1.00826
i: 3  t: 1.3  w: 1.02169
i: 4  t: 1.4  w: 1.03851
i: 5  t: 1.5  w: 1.05767
i: 6  t: 1.6  w: 1.07846
i: 7  t: 1.7  w: 1.10043
i: 8  t: 1.8  w: 1.12326
i: 9  t: 1.9  w: 1.14672
i: 10  t: 2.0  w: 1.17065
```

###### 5.2 Exercise - 5b: $y'=1+\frac{y}{t}-(\frac{y}{t})^2, 1\le t \le 3, y(1)=0, h=0.2$
$w_0=y(1)=0$  
$w_{i+1}=w_i+hf(t_i,w_i)$  
$w_1=w_0+hf(t_0,w_0)=w_0+h(1+\frac{w_0}{t_0}+(\frac{w_0}{t_0})^2)=0+0.2(1+\frac{0}{1}+(\frac{0}{1})^2)=0.2$  
$w_2=w_1+hf(t_1,w_1)=w_1+h(1+\frac{w_1}{t_1}+(\frac{w_1}{t_1})^2)=0.2+0.2(1+\frac{0.2}{1}+(\frac{0.2}{1})^2)=0.43889$  

```python
t = 1.0
t_max = 3
w = 0.0
h = 0.2
i = 0
while t < t_max+h:
    print("i:",i," t:",round(t,1)," w:",round(w,5))
    w = w+h*(1+(w/t)+(w/t)**2)
    t += h
    i += 1
# Output:
i: 0  t: 1.0  w: 0.0
i: 1  t: 1.2  w: 0.2
i: 2  t: 1.4  w: 0.43889
i: 3  t: 1.6  w: 0.72124
i: 4  t: 1.8  w: 1.05204
i: 5  t: 2.0  w: 1.43725
i: 6  t: 2.2  w: 1.88426
i: 7  t: 2.4  w: 2.40227
i: 8  t: 2.6  w: 3.00284
i: 9  t: 2.8  w: 3.7006
i: 10  t: 3.0  w: 4.51428
```

### 5.3: Higher-Order Taylor Methods
#### 5.3 Excise
##### 5.3 Excise - 1: Use Taylor’s method of order two to approximate the solutions for each of the following initial-value problems.
###### 5.3 Exercise - 1a: $y'=te^{3t}-2y, 0\le t \le 1, y(0)=0, h=0.5$
For order two, we need the first derivative of $f(t,y(t))=te^{3t}-2y(t)$ with respect to $t$.  
$f'(t,y(t))=\frac{d}{dt}(te^{3t}-2y(t))$  
$=te^{3t}+e^{3t}-2y'$  
$=e^{3t}+3te^{3t}-2(te^{3t}-2y)$  
$=e^{3t}+te^{3t}+4y$

$T^{(2)}(t_i,w_i)=f(t_i,w_i)+\frac{h}{2}f'(t_i,w_i)$  
$=te^{3t}-2y+\frac{h}{2}(e^{3t}+te^{3t}+4y)$  
$=te^{3t}-2y+\frac{h}{2}e^{3t}+\frac{h}{2}te^{3t}+2hy$  
$=te^{3t}(1+\frac{h}{2})+\frac{h}{2}e^{3t}-2y(1-h)$  
$=1.25te^{3t}+0.25e^{3t}-y$

$w_0=0$  
$w_1=w_0+hT^{(2)}(t_0,w_0)$  
$=w_0+h(1.25t_0e^{3t_0}+0.25e^{3t_0}-w_0)$  
$=0+0.5(0\times e^{0}+0.25e^{0}-0)=0.125$

```python
import math

t = 0.0
t_max = 1
w = 0.0
h = 0.5
i = 0
while t < t_max+h/2:
    print("i:",i," t:",round(t,1)," w:",round(w,5))
    w = w + h * (1.25 * t * math.exp(3 * t) + 0.25 * math.exp(3 * t) - w)
    t += h
    i += 1

#output:
i: 0  t: 0.0  w: 0.0
i: 1  t: 0.5  w: 0.125
i: 2  t: 1.0  w: 2.02324
```

###### 5.3 Exercise - 1c: $y'=1+y/t, 1\le t \le 2, y(1)=2, h=0.25$
For order two, we need the first derivative of $f(t,y(t))=1+y/t$ with respect to $t$.  
$f'(t,y(t))=\frac{d}{dt}(1+y/t)$  
$=\frac{y't-y}{t^2}$  
$=\frac{(1+y/t)t-y}{t^2}=1/t$  

$T^{(2)}(t_i,w_i)=f(t_i,w_i)+\frac{h}{2}f'(t_i,w_i)$  
$=1+w_i/t_i+\frac{h}{2t_i}$  
$=1+w_i/t_i+\frac{0.125}{t_i}$  

$w_0=2$  
$w_1=w_0+hT^{(2)}(t_0,w_0)$  
$=w_0+h(1+w_0/t_0+\frac{0.125}{t_0})$  
$=2+0.25(1+2/1.0+\frac{0.125}{1.0})=2.78125$

```python
t = 1.0
t_max = 2
w = 2.0
h = 0.25
i = 0
while t < t_max+h/2:
    print("i:",i," t:",round(t,1)," w:",round(w,5))
    w = w + h * (1+(w/t)+(0.125/t))
    t += h
    i += 1
# Output:
i: 0  t: 1.0  w: 2.0
i: 1  t: 1.2  w: 2.78125
i: 2  t: 1.5  w: 3.6125
i: 3  t: 1.8  w: 4.48542
i: 4  t: 2.0  w: 5.39405
```

### 5.4: Runge-Kutta Methods
#### 5.4 Exercise
##### 5.4 Exercise 1
###### 5.4 Exercise 1a

$y' = te^{3t} - 2y, \quad 0 \le t \le 1, \quad y(0) = 0, \quad h = 0.5$  
Here, $t_0 = 0, \quad y_0 = 0$  

Predict:  
$\tilde{y}_1$:$\tilde{y}_1 = y_0 + 0.5[f(0, 0)]= 0 + 0.5[0 \cdot e^0 - 2 \cdot 0] = 0$  

Correct:  
$y_1:y_1 = y_0 + \frac{0.5}{2}[f(0, 0) + f(0.5, \tilde{y}_1 = 0)]$  
$\therefore y_1 = 0 + 0.25[0 + \{0.5e^{1.5} - 0\}]= 0.56021$  
Now, $t_1 = 0.5 \rightarrow t_2 = 1.0$  

Predict:  
$f(0.5, 0.56021) = 0.5e^{1.5} - 2(0.56021)= 1.12043$  
$\therefore \tilde{y}_2 = 0.56021 + 0.5 \times 1.12043 = 1.120425$  

Correct:  
$f(1, \tilde{y}_2 = 1.120425) = 1 \cdot e^3 - 2 \times 1.120425= 17.8447$  
$\therefore y_2 = 0.56021 + \frac{0.5}{2}[1.12043 + 17.8447]= 5.30149$  

Exact Solution:  
$y(t_1) = \frac{1}{5}(0.5)e^{3(0.5)} - \frac{1}{25}e^{3(0.5)} + \frac{1}{25}e^{-2(0.5)}= 0.28362$  
$y(t_2) = \frac{1}{5}e^3 - \frac{1}{25}e^3 + \frac{1}{25}e^{-2} = 3.2191$

###### 5.4 Exercise 5a
Using the Midpoint Method:  
$t_0 = 0, \quad w_0 = 0, \quad y(t_0) = 0, \quad t_1 = 0.5$  
$w_1 = w_0 + hf(t_0 + h/2, w_0 + \frac{h}{2}f(t_0, w_0))= 0 + 0.5f(0.25, 0 + 0.25f(0, 0))= 0.5f(0.25, 0)= 0.5[(0.25)e^{0.75} - 2(0.25)(0)]= 0.2696250$  
$y(t_1) = 0.28362$  
$w_2 = w_1 + hf(t_1 + h/2, w_1 + \frac{h}{2}f(t_1, w_1))= 0.269625 + 0.5f(0.75, 0.269625 + 0.25f(0.5, 0.269625))= 0.2696250 + 0.5[(0.75)e^{2.25} - 2\{(0.269625 + 0.25[(0.5)e^{1.5} - 2(0.269625)])\}]= 3.13$  
$y(t_2) = 3.2191$  


### 5.6: Multistep Methods
#### 5.6 Excise
##### 5.6 Excise - 1: Use all the Adams-Bashforth methods to approximate the solutions to the following initial-value problems. In each case, use exact starting values and compare the results to the actual values
###### 5.6 Exercise - 1a: $y'=te^{3t}-2y, 0\le t \le 1, y(0)=0, h=0.2$; actual solution $y(t)=\frac{1}{5}te^{3t}-\frac{1}{25}e^{3t}+\frac{1}{25}e^{-2t}$


Two step explicit method
$w_{i+1} = w_i + \frac{h}{2}[3f(t_i, w_i) - f(t_{i-1}, w_{i-1})]$  

$w_0=0$  
$w_1=0.0268128$  
$w_2 = 0.0268128 + \frac{0.2}{2} [3f(0.2, 0.0268128) - f(0, 0)]$  
$w_2 = 0.120052$

Three-Step Explicit Method:
$w_{i+1} = w_i + \frac{h}{12}[23f(t_i, w_i) - 16f(t_{i-1}, w_{i-1}) + 5f(t_{i-2}, w_{i-2})]$  
$w_3 = w_2 + \frac{0.2}{12}[23f(t_2, w_2) - 16f(t_1, w_1) + 5f(t_0, w_0)]$  
$w_3 = 0.461387$  

Four-Step Explicit Method:
$w_{i+1} = w_i + \frac{h}{24}[55f_i - 59f_{i-1} + 37f_{i-2} - 9f_{i-3}]$  
$w_4 = 1.296126$  


Five-Step Explicit Method
$w_{i+1} = w_i + \frac{h}{720}[1901f_i - 2774f_{i-1} + 2616f_{i-2} - 1274f_{i-3} + 251f_{i-4}]$  
$w_5 = 3.18540$

| $i$ | $t$ | 2-step Approx ($w_i$) | 3-step Approx ($w_i$) | 4-step Approx ($w_i$) | 5-step Approx ($w_i$) | Actual Value $y(t)$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | **0.0** | 0 | 0 | 0 | 0 | **0.0** |
| **1** | **0.2** | 0.268128| 0.268128| 0.268128| 0.268128| **0.268128** |
| **2** | **0.4** | 0.120052 | 0.150778| — | — | **0.150778** |
| **3** | **0.6** | 0.45355 | 0.461387 | 0.496020| — | **0.496020** |
| **4** | **0.8** | 1.146284 | 1.285245 | 1.296126 | — | **1.330857** |
| **5** | **1.0** | 2.824168 | 3.036068 | 3.146140 | 3.18540 | **3.2190993** |

## Chapter 6: Direct Methods for Solving Linear Systems
### 6.3 Linear Algebra and Matrix Inversion
A singular matrix has a determinant of zero - it is not invertible (has linearly dependent rows/columns). A non-singular matrix has a non-zero determinant, is invertible.

#### 6.3 Exercise
##### 6.3 Exercise - 5a: Determine if the matrix is non-singular and compute the inverse.
Applying row reduction:

$
\left[\begin{array}{ccc|ccc}
4 & 2 & 6 & 1 & 0 & 0\\
3 & 0 & 7 & 0 & 1 & 0\\
-2 & -1 & -3 & 0 & 0 & 1\\
\end{array}\right]
$

$R_1 \rightarrow \frac{R_1}{4}$

$
\left[\begin{array}{ccc|ccc}
1 & 1/2 & 3/2 & 1/4 & 0 & 0\\
3 & 0 & 7 & 0 & 1 & 0\\
-2 & -1 & -3 & 0 & 0 & 1\\
\end{array}\right]
$

$R_2 - 3R_1 \rightarrow R_2$

$
\left[\begin{array}{ccc|ccc}
1 & 1/2 & 3/2 & 1/4 & 0 & 0\\
0 & -3/2 & 5/2 & -3/4 & 1 & 0\\
-2 & -1 & -3 & 0 & 0 & 1\\
\end{array}\right]
$

$R_3 + 2R_1 \rightarrow R_3$

$
\left[\begin{array}{ccc|ccc}
1 & 1/2 & 3/2 & 1/4 & 0 & 0\\
0 & -3/2 & 5/2 & -3/4 & 1 & 0\\
0 & 0 & 0 & 1/2 & 0 & 1\\
\end{array}\right]
$
We have a row of all zeros, the matrix is singular.


##### 6.3 Exercise - 5c
Applying row reduction:  
$\left[\begin{array}{cccc|cccc}
1 & 1 & -1 & 1 & 1 & 0 & 0 & 0\\
1 & 2 & -4 & -2 & 0 & 1 & 0 & 0\\
2 & 1 & 1 & 5 & 0 & 0 & 1 & 0\\
-1 & 0 & -2 & -4 & 0 & 0 & 0 & 1\\
\end{array}\right] R2-R1 \rightarrow R2, R3-2R1\rightarrow R3, R4+R1\rightarrow R4\\
\left[\begin{array}{cccc|cccc}
1 & 1 & -1 & 1 & 1 & 0 & 0 & 0\\
0 & 1 & -3 & -3 & -1 & 1 & 0 & 0\\
0 & -1 & 3 & 3 & -2 & 0 & 1 & 0\\
0 & 1 & -3 & -3 & 1 & 0 & 0 & 1\\
\end{array}\right] R2+R3 \rightarrow R3, R2-R4\rightarrow R4\\
\left[\begin{array}{cccc|cccc}
1 & 1 & -1 & 1 & 1 & 0 & 0 & 0\\
0 & 1 & -3 & -3 & -1 & 1 & 0 & 0\\
0 & 0 & 0 & 0 & -3 & 1 & 1 & 0\\
0 & 0 & 0 & 0 & 2 & -1 & 0 & 1\\
\end{array}\right]$

We have two rows with all zeros, the matrix is singular.

##### 6.3 Exercise - 6c
Applying row reduction:  
$\left[\begin{array}{ccc|ccc}
1 & 2 & -1 & 1 & 0 & 0\\
0 & 1 & 2 & 0 & 1 & 0\\
-1 & 4 & 3 & 0 & 0 & 1\\
\end{array}\right] R1+R3 \rightarrow R3\\
\left[\begin{array}{ccc|ccc}
1 & 2 & -1 & 1 & 0 & 0\\
0 & 1 & 2 & 0 & 1 & 0\\
0 & 6 & 2 & 1 & 0 & 1\\
\end{array}\right] R3-6R2 \rightarrow R3, R1-2R2\rightarrow R1\\
\left[\begin{array}{ccc|ccc}
1 & 0 & -5 & 1 & -2 & 0\\
0 & 1 & 2 & 0 & 1 & 0\\
0 & 0 & -10 & 1 & -6 & 1\\
\end{array}\right]R3/-10\rightarrow R3\\
\left[\begin{array}{ccc|ccc}
1 & 0 & -5 & 1 & -2 & 0\\
0 & 1 & 2 & 0 & 1 & 0\\
0 & 0 & 1 & -1/10 & 3/5 & -1/10\\
\end{array}\right]R1+5R3\rightarrow R1, R2-2R3\rightarrow R2\\
\left[\begin{array}{ccc|ccc}
1 & 0 & 0 & 1/2 & 1 & -1/2\\
0 & 1 & 0 & 1/5 & -1/5 & 1/5\\
0 & 0 & 1 & -1/10 & 3/5 & -1/10\\
\end{array}\right]$

The matrix is non-singular, the inverse is:
$\left[\begin{array}{ccc}
1/2 & 1 & -1/2\\
1/5 & -1/5 & 1/5\\
-1/10 & 3/5 & -1/10\\
\end{array}\right]$

### 6.4 The Determinant of a Matrix
#### 6.14
Suppose A is a square matrix.
1. If $A=[a]$ is a $1\times 1$ matrix, then $\det A=a$
2. If $A$ is an $n\times n$ matrix, with $n\gt 1$, the minor $M_{ij}$ is the determinant of the $(n-1)\times(n-1)$ submatrix of $A$ obtained by deleting the i-th row and j-th column of the matrix $A$.
3. The cofactor $A_{ij}$ associated with $M_{ij}$ is defined by $A_{ij}=(-1)^{i+j}M_{ij}$
4. The determinant of the $n\times n$ matrix $A$, when $n\gt 1$, is given either by
$$
\det A = \sum_{j=1}^{n} a_{ij}A_{ij} = \sum_{j=1}^{n} (-1)^{i+j} a_{ij}M_{ij}, \quad \text{for any } i = 1, 2, \ldots, n,
$$

or by

$$
\det A = \sum_{i=1}^{n} a_{ij}A_{ij} = \sum_{i=1}^{n} (-1)^{i+j} a_{ij}M_{ij}, \quad \text{for any } j = 1, 2, \ldots, n.
$$

#### 6.4 Exercise
##### 6.4 Exercise - 1c
$\left[\begin{array}{cccc}
1 & 1 & -1 & 1\\
1 & 2 & -4 & -2\\
2 & 1 & 1 & 5\\
-1 & 0 & -2 & -4\\
\end{array}\right]=A$

$\det A=(-1)^{4+1}(-1)
\left[\begin{array}{ccc}
1 & -1 & 1\\
2 & -4 & -2\\
1 & 1 & 5\\
\end{array}\right]
+0
+(-1)^{4+3}(-2)
\left[\begin{array}{ccc}
1 & 1 & 1\\
1 & 2 & -2\\
2 & 1 & 5\\
\end{array}\right]
+(-1)^{4+4}(-4)
\left[\begin{array}{ccc}
1 & 1 & -1\\
1 & 2 & -4\\
2 & 1 & 1\\
-1 & 0 & -2\\
\end{array}\right]
=(-1\times -1){(1\times -4\times 5+(-1)\times -2\times 1+1\times 2\times 1)-(1\times -4\times 1+(-1)\times 2\times 5+1\times -2\times 1)}
+0
+(-1\times -2){(1\times 2\times 5+1\times -2\times 2+1\times 1\times 1)-(1\times 2\times 2+1\times 1\times 5+1\times -2\times 1)}
+(1\times -4){(1\times 2\times 1+1\times -4\times 2+(-1)\times 1\times 1)-(-1\times 2\times 2+1\times 1\times 1+1\times -4\times 1)}
=0$

### 6.5 Matrix Factorization
#### 6.5 Exercise
##### 6.5 Exercise - 5a
Factor the following matrices into the LU decomposition using hte LU Factorization Algorithm with $l_{ij}=1$ for all $i$.
$\left[\begin{array}{ccc}
2 & -1 & 1\\
3 & 3 & 9\\
3 & 3 & 5\\
\end{array}
\right]=
\left[\begin{array}{ccc}
1 & 0 & 0\\
m_{21} & 1 & 0\\
m_{31} & m_{32} & 1\\
\end{array}\right]
\left[\begin{array}{ccc}
a_{11} & a_{12} & a_{13}\\
0 & a_{22} & a_{23}\\
0 & 0 & a_{33}\\
\end{array}
\right]$

$1.a_{11}=2$, $1.a_{12}=-1$, $1.a_{13}=1$,  
$m_{21}.a_{11}=3\Rightarrow m_{21}=3/2$,  
$m_{21}.a_{12}+1.a_{22}=3\Rightarrow (3/2)(-1)+a_{22}=3\Rightarrow a_{22}=9/2$,  
$m_{21}.a_{13}+1.a_{23}=9\Rightarrow (3/2)(1)+a_{23}=9\Rightarrow a_{23}=15/2$,  
$m_{31}.a_{11}=3\Rightarrow m_{31}=3/2$,  
$m_{31}.a_{12}+m_{32}.a_{22}=3\Rightarrow (3/2)(-1)+m_{32}(9/2)=3\Rightarrow m_{32}=1$,  
$m_{31}.a_{13}+m_{32}.a_{23}+1.a_{33}=5\Rightarrow (3/2)(1)+(1)(15/2)+a_{33}=5\Rightarrow a_{33}=-4$

$A=\left[\begin{array}{ccc}
1 & 0 & 0\\
3/2 & 1 & 0\\
3/2 & 1 & 1\\
\end{array}
\right]
\left[\begin{array}{ccc}
2 & -1 & 1\\
0 & 9/2 & 15/2\\
0 & 0 & -4\\
\end{array}
\right]$

### 6.6 Special Types of Matrices
#### 6.6 Exercise
##### 6.6 Exercise - 1
Determine which of the following matrices are (1) symmetric, (2) singular, (3) strictly diagonally doinant, and (4) positive definite.

(a)
$\left[\begin{array}{cc}
2 & 1\\
1 & 3\\
\end{array}\right]$

1) $A$ is symmetric since $A=A^T$
2) $det(A)=(3)(2)-(1)(1)=5\neq 0$, non-singular.
3) $|2|\gt|1| and |3|\gt|1|$; strictly diagonally dominant.
4) $\det A_1=\det[2]\gt 0$
$\det A_2=\det
\left[\begin{array}{cc}
2 & 1\\
1 & 3\\
\end{array}\right]=5\gt 0$
So, $A$ is positive definite.

(b)
$B=\left[\begin{array}{ccc}
2 & 1 & 0\\
0 & 3 & 0\\
1 & 0 & 4\\
\end{array}\right]$

1) $B$ is not symmetric since $B\neq B^T$
2) $\det(B)=(2)(3)(4)=24\neq 0$, non-singular.
3) $|2|\gt|1|+|0|$, $|3|\gt|0|+|0|$, $|4|\gt|1|+|0|$, ; strictly diagonally dominant.
4) Since $B$ is not symmetric, it's not positive definite.

(c)
$C=\left[\begin{array}{ccc}
4 & 2 & 6\\
3 & 0 & 7\\
-2 & -1 & -3\\
\end{array}\right]$

1) $C$ is not symmetric since $C\neq C^T$
2) $\det(C)=(4)(0+7)-(2)(-9+14)+(6)(-3)=0$, singular.
3) $|4|\lt|2|+|6|$, $C$ is not strictly diagonally dominant.
4) Since $C$ is not symmetric, it's not positive definite.

(D)
$D=\left[\begin{array}{cccc}
4 & 0 & 0 & 0\\
6 & 7 & 0 & 0\\
9 & 11 & 1 & 0\\
5 & 4 & 1 & 1\\
\end{array}\right]$

1) $D$ is not symmetric since $D\neq D^T$
2) $\det(D)=(4)(7)(1)(1)=28$, non-singular.
3) $|1|\lt|5|+|4|+|1|$, $D$ is not strictly diagonally dominant.
4) Since $D$ is not symmetric, it's not positive definite.

##### 6.6 Exercise - 5a
Use the Cholesky Algorithm to find a factorization of the form $A=LL*$ for the matrix:
(a)
$A=\left[\begin{array}{ccc}
2 & -1 & 0\\
-1 & 2 & -1\\
0 & -1 & 2\\
\end{array}\right]=
\left[\begin{array}{ccc}
l_{11} & 0 & 0\\
l_{21} & l_{22} & 0\\
l_{31} & l_{32} & l_{33}\\
\end{array}\right]=
\left[\begin{array}{ccc}
l_{11} & l_{21} & l_{31}\\
0 & l_{22} & l_{32}\\
0 & 0 & l_{33}\\
\end{array}\right]=
\left[\begin{array}{ccc}
l_{11}^2 & l_{11}l_{21} & l_{11}l_{31}\\
l_{11}l_{21} & l_{21}^2+l_{22}^2 & l_{21}l_{31}+l_{22}l_{32}\\
l_{11}l_{31} & l_{21}l_{31}+l_{22}l_{32} & l_{31}^2+l_{32}^2+l_{33}^2\\
\end{array}\right]
$

$l_{11}^2=2\Rightarrow l_{11}=\sqrt{2}$,  
$l_{11}l_{21}=-1\Rightarrow l_{21}=-1/\sqrt{2}$,  
$l_{11}l_{31}=0\Rightarrow l_{31}=0$,  
$l_{21}^2+l_{22}^2=2\Rightarrow l_{22}=\sqrt{6}/2$,  
$l_{21}l_{31}+l_{22}l_{32}=-1\Rightarrow l_{32}=-\sqrt{6}/3$,  
$l_{31}^2+l_{32}^2+l_{33}^2=2\Rightarrow l_{33}=2\sqrt{3}/3$ 

Hence,
$L=\left[\begin{array}{ccc}
\sqrt{2} & 0 & 0\\
-\sqrt{2}/2 & \sqrt{6}/2 & 0\\
0 & -\sqrt{6}/3 & 2\sqrt{3}/3\\
\end{array}\right]$


## Chapter 7: Iterative Techniques in Matrix Algebra

### 7.1 Norms of Vectors and Matrices
#### 7.1 Exercise
##### 7.1 Exercise - 1: find $l_\infin$ and $l_2$ norms of the vectors.
###### 7.1 Exercise - 1a: $x=(3,-4,0,3/2)^t$

$||x||_\infin=max{|3|,|-4|,|0|,|3/2|}=4$  
$||x||_2=\sqrt{\sum_{i=1}^n x_i^2}=\sqrt{3^2+(-4)^2+0^2+(3/2)^2}=5.220153$  

###### 7.1 Exercise - 1c: $x=(\sin{k},\cos{k},2^k)^t$ for positive integer k

$||x||_\infin=max{|\sin{k}|,|\cos{k}|,|2^k|}=2^k$  
$||x||_2=\sqrt{\sum_{i=1}^n x_i^2}=\sqrt{\sin{k}^2+\cos{k}^2+(2^k)^2}=\sqrt{1+4^k}$  

##### 7.1 Exercise - 5: find $l_\infin$ norm of the matrices.
###### 7.1 Exercise - 5a: $\left[\begin{array}{cc}10 & 15 \\ 0 & 1\end{array}\right]$

$\sum_{j=1}^2|a_{1j}|=|10|+|15|=25$  
$\sum_{j=2}^2|a_{2j}|=|0|+|1|=1$  

$||A||_\infin=max(25, 1)=25$  

###### 7.1 Exercise - 5c: $\left[\begin{array}{ccc}2 & -1 & 0\\ -1 & 2 & -1\\0 & -1 & 2\end{array}\right]$

$\sum_{j=1}^2|a_{1j}|=|2|+|-1|+|0|=3$  
$\sum_{j=2}^2|a_{2j}|=|-1|+|2|+|1|=4$  
$\sum_{j=3}^2|a_{3j}|=|0|+|-1|+|2|=3$  

$||A||_\infin=max(3, 4, 3)=4$  
