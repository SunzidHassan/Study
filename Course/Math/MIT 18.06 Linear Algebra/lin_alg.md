$AB=C$

##### Dot product

For 
$
\underset{(3\times 3)}{A}\times
\underset{(B\times 3)}{B}=\underset{(3\times 3)}{C}
$,

$\left[\begin{array}{ccc}
a_{11} & a_{12} & a_{13}\\
[\mathbf{a_{21}}] & [\mathbf{a_{22}}] & [\mathbf{a_{23}}]\\
a_{31} & a_{32} & a_{33}\\
\end{array}\right]
\left[\begin{array}{ccc}
b_{11} & [\mathbf{b_{12}}] & b_{13}\\
b_{21} & [\mathbf{b_{22}}] & b_{23}\\
b_{31} & [\mathbf{b_{32}}] & b_{33}\\
\end{array}\right]=
\left[\begin{array}{ccc}
c_{11} & c_{12} & c_{13}\\
c_{21} & [\mathbf{c_{22}}] & c_{23}\\
c_{31} & c_{32} & c_{33}\\
\end{array}\right]$

$c_{22}=
\left[\begin{array}{ccc}
a_{21} & a_{22} & a_{23}\\
\end{array}\right].
\left[\begin{array}{c}
b_{12}\\
b_{22}\\
b_{32}\\
\end{array}\right]=
b_{12}.[a_{21}]+b_{22}.[a_{22}]+b_{32}.[a_{23}]=
\sum_{k=1}^{k=3}{b_{k2}a_{2k}}$

For 
$
\underset{(m\times n}{A}\times
\underset{(n\times p)}{B}=\underset{(m\times p)}{C}
$,
$\left[\begin{array}{ccc}
a_{11} & ... & a_{1n}\\
... & ... & ...\\
[a_{m1}] & [...] & [a_{mn}]\\
\end{array}\right]
\left[\begin{array}{ccc}
b_{11} & ... & [b_{1n}]\\
... & ... & [...]\\
b_{n1} & ... & [b_{np}]\\
\end{array}\right]=
\left[\begin{array}{ccc}
c_{11} & ... & c_{1p}\\
... & ... & ...\\
c_{m1} & ... & [c_{mp}]\\
\end{array}\right]$

$c_{mp}=
\left[\begin{array}{ccc}
a_{m1} & ... & a_{mn}\\
\end{array}\right].
\left[\begin{array}{c}
b_{1p}\\
...\\
b_{np}\\
\end{array}\right]=
b_{1p}.[a_{m1}]+...+b_{np}.[a_{mn}]=
\sum_{k=1}^{k=n}{b_{kp}a_{mk}}$


##### Combination of columns
For 
$
\underset{(3\times 3)}{A}\times
\underset{(3\times 3)}{B}=\underset{(3\times 3)}{C}
$,

$\left[\begin{array}{ccc}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\\
\end{array}\right]
\left[\begin{array}{ccc}
b_{11} & [b_{12}] & b_{13}\\
b_{21} & [b_{22}] & b_{23}\\
b_{31} & [b_{32}] & b_{33}\\
\end{array}\right]=
\left[\begin{array}{ccc}
c_{11} & [c_{12}] & c_{13}\\
c_{21} & [c_{22}] & c_{23}\\
c_{31} & [c_{32}] & c_{33}\\
\end{array}\right]$

$\left[\begin{array}{c}
c_{12}\\
c_{22}\\
c_{32}\\
\end{array}\right]=
\left[\begin{array}{ccc}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\\
\end{array}\right].
\left[\begin{array}{c}
b_{12}\\
b_{22}\\
b_{32}\\
\end{array}\right]=
b_{12}.
\left[\begin{array}{c}
a_{11}\\
a_{21}\\
a_{31}\\
\end{array}\right]+
b_{22}.
\left[\begin{array}{c}
a_{12}\\
a_{22}\\
a_{32}\\
\end{array}\right]+
+
b_{32}.
\left[\begin{array}{c}
a_{13}\\
a_{23}\\
a_{33}\\
\end{array}\right]=
\left[\begin{array}{c}
\sum_{k=1}^{k=3}{b_{k1}a_{1k}}\\
\sum_{k=1}^{k=3}{b_{k2}a_{2k}}\\
\sum_{k=1}^{k=3}{b_{k3}a_{3k}}\\
\end{array}\right]$

For 
$
\underset{(m\times n}{A}\times
\underset{(n\times p)}{B}=\underset{(m\times p)}{C}
$,

$\left[\begin{array}{ccc}
a_{11} & ... & a_{1n}\\
... & ... & ...\\
[a_{m1}] & [...] & [a_{mn}]\\
\end{array}\right]
\left[\begin{array}{ccc}
b_{11} & ... & [b_{1n}]\\
... & ... & [...]\\
b_{n1} & ... & [b_{np}]\\
\end{array}\right]=
\left[\begin{array}{ccc}
c_{11} & ... & [c_{1p}]\\
... & ... & [...]\\
c_{m1} & ... & [c_{mp}]\\
\end{array}\right]$

$\left[\begin{array}{c}
c_{1p}\\
...\\
c_{mp}\\
\end{array}\right]=
\left[\begin{array}{ccc}
a_{11} & ... & a_{1n}\\
... & ... & ...\\
a_{m1} & ... & a_{mn}\\
\end{array}\right].
\left[\begin{array}{c}
b_{1p}\\
...\\
b_{np}\\
\end{array}\right]=
b_{1p}.
\left[\begin{array}{c}
a_{11}\\
...\\
a_{mn}\\
\end{array}\right]+
...+
b_{np}.
\left[\begin{array}{c}
a_{1n}\\
...\\
a_{mn}\\
\end{array}\right]=
\left[\begin{array}{c}
\sum_{k=1}^{k=n}{b_{k1}a_{1k}}\\
...\\
\sum_{k=1}^{k=n}{b_{kp}a_{mk}}\\
\end{array}\right]$

Columns of $C$ are combinations of columns of $A$. The combination is specified by elements of a column of $B$.

##### Combination of rows
For 
$
\underset{(3\times 3)}{A}\times
\underset{(3\times 3)}{B}=\underset{(3\times 3)}{C}
$,

$\left[\begin{array}{ccc}
a_{11} & a_{12} & a_{13}\\
[a_{21}] & [a_{22}] & [a_{23}]\\
a_{31} & a_{32} & a_{33}\\
\end{array}\right]
\left[\begin{array}{ccc}
b_{11} & b_{12} & b_{13}\\
b_{21} & b_{22} & b_{23}\\
b_{31} & b_{32} & b_{33}\\
\end{array}\right]=
\left[\begin{array}{ccc}
c_{11} & c_{12} & c_{13}\\
[c_{21}] & [c_{22}] & [c_{23}]\\
c_{31} & c_{32} & c_{33}\\
\end{array}\right]$

\left[\begin{array}{ccc}
c_{21} & c_{22} & c_{32}\\
\end{array}\right]=
\left[\begin{array}{ccc}
a_{21} & a_{22} & a_{23}\\
\end{array}\right].
\left[\begin{array}{ccc}
b_{11} & b_{12} & b_{13}\\
b_{21} & b_{22} & b_{23}\\
b_{31} & b_{32} & b_{33}\\
\end{array}\right]=
\left[\begin{array}{ccc}
\left[\begin{array}{ccc}
a_{21} & a_{22} & a_{23}\\
\end{array}\right].
\left[\begin{array}{c}
b_{11}\\
b_{21}\\
b_{31}\\
\end{array}\right]
&
\left[\begin{array}{ccc}
a_{21} & a_{22} & a_{23}\\
\end{array}\right].
\left[\begin{array}{c}
b_{12}\\
b_{22}\\
b_{32}\\
\end{array}\right]
&
\left[\begin{array}{ccc}
a_{21} & a_{22} & a_{23}\\
\end{array}\right].
\left[\begin{array}{c}
b_{13}\\
b_{23}\\
b_{33}\\
\end{array}\right]\\
\end{array}\right]=
\left[\begin{array}{ccc}
b_{11}.a_{21}+b_{21}.a_{22}+b_{31}.a_{23}
&
b_{12}.a_{21}+b_{22}.a_{22}+b_{32}.a_{23}
&
b_{13}.a_{21}+b_{23}.a_{22}+b_{33}.a_{23}\\
\end{array}\right]=
\left[\begin{array}{ccc}
\sum_{k=1}^{k=3}{b_{k1}a_{1k}}
&
\sum_{k=1}^{k=3}{b_{k1}a_{1k}}
&
\sum_{k=1}^{k=3}{b_{k1}a_{1k}}\\
\end{array}\right]$



Rows of $C$ are combinations of rows of $B$. The combination is specified by elements of a row of $A$.