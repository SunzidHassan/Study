### 1.6 Transposes, Permutations, Vector Spaces

Vector spaces and their subspaces is introduced in this lecture.

#### Permutations
Permutations execute row exchanges.

For invertible matrix $A$ and permutation matrix $P$:

$A=L\mathcal{U}$ becomes $PA=L\mathcal{U}$

There are $n!$ permutations matrices. They are all invertible, and $P^{-1}=P^{T}$ or $P^{T}P=I$.

$(A^{T})_{ji}=A_{ij}$

##### Symmetric matrices
$A^T=A$

For example
$\left[\begin{array}{ccc}
1 & 4 & 5\\
4 & 2 & 6\\
5 & 6 & 3
\end{array}\right]$

For matrix 
$R=\left[\begin{array}{cc}
1 & 2\\
3 & 4\\
5 & 6
\end{array}\right]$

$R^{T}=\left[\begin{array}{ccc}
1 & 2 & 4\\
3 & 3 & 1\\
\end{array}\right]$

$RR^T$ is always symmetric.

$\overset{R^T}
{\left[\begin{array}{ccc}
1 & 2 & 4\\
3 & 3 & 1\\
\end{array}\right]}
\overset{R}
{\left[\begin{array}{cc}
1 & 3\\
2 & 3\\
4 & 1
\end{array}\right]}=
{\left[\begin{array}{cc}
1+4+16 & 3+6+4\\
3+6+4 & 9+9+1
\end{array}\right]}=
\overset{R^TR}
{\left[\begin{array}{cc}
21 & 13\\
13 & 19
\end{array}\right]}$


$\overset{R^T}
{\left[\begin{array}{cc}
1 & 3\\
2 & 3\\
4 & 1
\end{array}\right]}
\overset{R}
{\left[\begin{array}{ccc}
1 & 2 & 4\\
3 & 3 & 1\\
\end{array}\right]}=
{\left[\begin{array}{ccc}
1+9 & 2+9 & 4+3\\
2+9 & 4+9 & 8+3\\
4+3 & 8+3 & 16+1
\end{array}\right]}=
\overset{R^TR}
{\left[\begin{array}{cc}
10 & 11 & 7\\
11 & 13 & 11\\
7 & 11 & 17
\end{array}\right]}$

$(R^TR)^T=R^TR^{TT}=R^TR$


#### Vector Spaces
It's possible to take linear combinations of vectors in vector space.

$R^2$ is all column vectors with 2 real components, all 2-dimensional real vectors, the $xy$ plane.  Examples:

$\left[\begin{array}{c}
3\\
2
\end{array}\right]$

$\left[\begin{array}{c}
0\\
0
\end{array}\right]$

$\left[\begin{array}{c}
\pi\\
e
\end{array}\right]$

We can't remove a point from the vector space. For example, if we remove the origin, we won't be able to multiply a vector by zero in that space.

$R^3$ is all column vectors with 3 real components.

$\left[\begin{array}{c}
3\\
2\\
0
\end{array}\right]$

If we take the upper-right quadrant of 2-dimensional $xy$ plane, we get a space that is not closed under multiplication with all real scalers (e.g., multiplication with a negative number). Thus, it's not a vector space.

A proper vector space within $R^2$ is a line through the origin. It's a subspace of $R^2$. It's not the same as $R^1$, as it's inside $R^2$ and thus has 2 components. $R^1$ has just 1 component.

Subspaces of $R^2$:
1. All of $R^2$
2. Any line through
$\left[\begin{array}{c}
0\\
0
\end{array}\right]$.
3. The zero vector
$\left[\begin{array}{c}
0\\
0
\end{array}\right]$
itself.

Subspaces of $R^3$:
1. All of $R^3$
2. Planes through origin 
$\left[\begin{array}{c}
0\\
0\\
0
\end{array}\right]$.
3. Any line through
$\left[\begin{array}{c}
0\\
0\\
0
\end{array}\right]$.
4. The zero vector
$\left[\begin{array}{c}
0\\
0\\
0
\end{array}\right]$
itself.


#### Column space

Columns of $R^n$: all their combinations form a subspace called column space.

$A=\left[\begin{array}{cc}
1 & 3\\
2 & 3\\
4 & 1
\end{array}\right]$

Column space of $A$ is all linear combinations of the two columns - that creates a plane through origin in $R^3$. If the two columns were in the same line, the column space would've been a line.