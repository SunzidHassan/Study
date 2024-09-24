## Chapter 2

### Examples
#### 1
Show that $f(x)=x^3+4x^2-10=0$ has a root in $[1,2]$ and use the Bisection method to determine an approximation to the root that is accurate to at least within $10^{-4}$

**Solution**:

Because $f(1)=-5$ and $f(2)=14$, the Intermediate Value Theorem ensure that this continuous function has a root in $[1,2]$.

For the first iteration of the Bisection method, we use the fact that at the midpoint of $[1,2]$, we have $f(1.5)=2.375 > 0$. This indicates we should select the interval $[1,1.5]$ for our second iteration. Then we find that $f(1.25)=-1.796875 < 0$. This indicates we should select the interval $[1.25,1.5]$ whose midpoint is $1.375$. Continuing in this manner gives us the following table.