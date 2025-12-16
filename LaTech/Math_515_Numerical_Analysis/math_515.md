

## Chapter 6: Direct Methods for Solving Linear Systems
### 6.3 Linear Algebra and Matrix Inversion
A singular matrix has a determinant of zero - it is not invertible (has linearly dependent rows/columns). A non-singular matrix has a non-zero determinant, is invertible.

#### 6.3 Exercise
##### 6.3 Exercise - 5a: Determine if the matrix is non-singular and compute the inverse.
Applying row reduction:  
$\left[\begin{array}{ccc|ccc}
4 & 2 & 6 & 1 & 0 & 0\\
3 & 0 & 7 & 0 & 1 & 0\\
-2 & -1 & -3 & 0 & 0 & 1\\
\end{array}\right] R1 \rightarrow \frac{R1}{4}\\
\left[\begin{array}{ccc|ccc}
1 & 1/2 & 3/2 & 1/4 & 0 & 0\\
3 & 0 & 7 & 0 & 1 & 0\\
-2 & -1 & -3 & 0 & 0 & 1\\
\end{array}\right]R2-3R1\rightarrow R2\\
\left[\begin{array}{ccc|ccc}
1 & 1/2 & 3/2 & 1/4 & 0 & 0\\
0 & -3/2 & 5/2 & -3/4 & 1 & 0\\
-2 & -1 & -3 & 0 & 0 & 1\\
\end{array}\right]R3+2R1\rightarrow R3\\
\left[\begin{array}{ccc|ccc}
1 & 1/2 & 3/2 & 1/4 & 0 & 0\\
0 & -3/2 & 5/2 & -3/4 & 1 & 0\\
0 & 0 & 0 & 1/2 & 0 & 1\\
\end{array}\right]R2-3R1\rightarrow R2\\$

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


### 6.6 Special Types of Matrices