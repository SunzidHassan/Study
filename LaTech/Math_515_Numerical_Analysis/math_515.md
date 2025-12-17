

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