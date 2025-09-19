STAT 620: Theory of Probability - Fall 2025

- [1. Chapter 1: Probability](#1-chapter-1-probability)
  - [1.1. Sample Spaces](#11-sample-spaces)
  - [1.2. Probability Axioms and Rules](#12-probability-axioms-and-rules)
  - [1.3. Odds](#13-odds)
  - [1.4. Conditional Probability and Independence](#14-conditional-probability-and-independence)
  - [1.5. Bayes' Theorem](#15-bayes-theorem)
- [2. Chapter 2: Random Variables](#2-chapter-2-random-variables)
  - [2.1. Discrete Random Variables](#21-discrete-random-variables)
  - [2.2. Continuous Random Variables](#22-continuous-random-variables)
  - [2.3. Cumulative Distribution Functions](#23-cumulative-distribution-functions)
  - [2.4. Expected Values and Variance](#24-expected-values-and-variance)
- [3. Chapter 3: Widely Used Discrete Random Variables](#3-chapter-3-widely-used-discrete-random-variables)
  - [3.1. Counting Techniques](#31-counting-techniques)
  - [3.2. Bernoulli](#32-bernoulli)
  - [3.3. Binomial](#33-binomial)


# 1. Chapter 1: Probability

## 1.1. Sample Spaces
**Sample space, $S={...}$** is set of all possible outcomes.
**Events ($A={...}$, $B={...}$, ...)** are one or more outcomes taken together as a unit.
If $A$ is an event, probability that $A$ occurs is $P(A)$ or $P$ of $A$.
$P(A)=\frac{\text{number of outcomes in} A}{n}$.

If $A\cap B=∅$, then $A$ and $B$ are mutually exclusive.

## 1.2. Probability Axioms and Rules

Probability axioms:
1. $P(A)\ge0$ for every event $A$ in $S$.
2. $P(S)=1$
3. For mutually exclusive events $A$, $B$, ... in $S$: $P(A\cup B\cup ...)=P(A)+P(B)+...$

Probability rules:
1. $0\lt P(A)\lt 1$ for every event $A$ in $S$.
2. $P(A^C)=1-P(A)$ (complement rule).
3. $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ Probability of Union.
4. For mutually exclusive $A$ and $B$, $P(A\cup B)=P(A)+P(B)$.
5. For three events $A$, $B$, and $C$, $P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(A\cap B)-P(B\cap C)-P(A\cap C)+P(A\cap B\cap C)$

**Example 1.3**
If $A$ and $B$ are events in a sample space for which $P(A) = 0.50$,  
$P(B) = 0.40$, and $P(A \cap B) = 0.25$, compute  
(a) $P(A \cup B)$,  
(b) $P(B^c)$, and  
(c) $P(A^c \cap B)$.

Solution:  
(c) $P(B)=P(A\cap B)+P(A^C\cap B)\Rightarrow 0.4=0.25+P(A^C\cap B)\Rightarrow P(A^C\cap B)=0.15$.

**Exercise 1**


## 1.3. Odds
Odds of $A=\frac{P(A)}{P(A^C)}$  
$P(A\cap B)=P(A|B)P(B)=P(B|A)P(A)$  

**Exercise 1**  
When rolling a dice, what are the odds (a) for and (b) against getting 5.  

$\frac{1}{5}$  
$\frac{5}{1}$


## 1.4. Conditional Probability and Independence
$P(A|B)=\frac{P(A\cap B)}{P(B)}\Rightarrow P(A\cap B)=P(A|B)P(B)$

$A$ and $B$ are independent if $P(A\cap B)=P(A)P(B)$

**Exercise 08**  
15% completely stop at a certain four way stop. Of the next 10 motorists to go through the intersection: (a) none come to a complete stop, (b) at least one comes to a complete stop, (c) exactly two come to a complete stop.

(a) $\left(\frac{85}{100}\right)^{10}=0.1969$  
(b) $1-0.1969=8031$  
(c) $10C2\times\left(\frac{15}{100}\right)^{2}\times \left(\frac{85}{100}\right)^{8}=0.2759$

**Exercise 10**  
Suppose one is four soft drink bottle tops are winners. If you randomly buy six bottles of soft drink, what's the probability you win at least once?

Probability of winning none is $\frac{3}{4}^6=0.1779$  
Probability of winning at least once is $1-0.1779=0.8220$

## 1.5. Bayes' Theorem
$P(B|A)=\frac{P(A\cap B)}{P(A)}=\frac{P(A|B)P(B)}{P(A|B)P(B)+P(A|B^C)P(B^C)}$

$P(A\cap B)=P(A|B)P(B)$

$P(A)=P(A\cap B)+P(A\cap B^C)=P(A|B)P(B)+P(A|B^C)P(B^C)$

**Exercise 7**
Three different factories, $F_1$, $F_2$, and $F_3$ are used to manufacture a large batch of cell phones. $F_1$ produces 20%, $F_2$ 30%, $F_3$ 50%. $F_1$ has 1% defective, $F_2$ has 2%, $F_3$ has 3%. If one phone is selected at random and is defective, probability that it's (a) F1, (b) F2.

$P(F_1|D)=\frac{P(D|F_1)P(F_1)}{P(D|F_1)P(F_1)+P(D|F_2)P(F_2)+P(D|F_3)P(F_3)}=\frac{0.01\times 0.2}{0.01\times 0.2+0.02\times 0.3+0.03\times 0.5}=0.0869$


# 2. Chapter 2: Random Variables
RV's (typically $X$ or other upper case) assigns numbers to outcomes of an experiment. Example: an experiment consists of tossing three coins and a RV $X$ counts the number of heads that come up, then the event $A$ that you get at least two heads can be written as $A=\{X\ge 2\}$, and $P(\{X\ge 2\})=P(X\ge 2)=\frac{4}{8}$

## 2.1. Discrete Random Variables
Discrete RV's take countable values. Associated with each discrete RV $X$ is a *probability mass function* $p(x)$ defined by $p(x)=P(X=x)$.

**Probability Mass Function** has the following properties:
1. $p(x)\ge 0$ for all $x$
2. $\sum_xp(x)=1$, the sum over all values that the RV can take.
3. $P(A)=\sum_{x\in A} p(x)$, where the sum is taken over all outcomes $x$ in the event $A$.

**Example 2.1.**  
Random variable $X$ counts the number of heads you get when you toss a balanced coin three times.  
$S={HHH, HHT, HTT, TTT, HTH, THH, TTH, THT}$  
${X=0}={TTT}, {X=1}={HTT, TTH, THT}, {X=2}={HHT, HTH, THH}, {X=3}={HHH}, {X=k}=∅$ for all $k\neq 0,1,2,3$.  

$$p(x)=\begin{cases}
  1/8 \text{ if } x=0\\
  3/8 \text{ if } x=1\\
  3/8 \text{ if } x=2\\
  1/8 \text{ if } x=3\\
  0 \text{ otherwise}
\end{cases}$$

$$\sum_x p(x)=\sum_{k=0}^3 p(k)=\frac{1}{8}+\frac{3}{8}+\frac{3}{8}+\frac{1}{8}=1.$$

$$p(x)=\begin{cases}
 0.17 \text{ if } x\lt 4\\
 0.28 \text{ if } 4 \le x\lt 7\\
 0.25 \text{ if } 7 \le x\lt 10\\
 0.10 \text{ if } x\ge 10\\
 0.20 \text{ if they lose }
\end{cases}$$



## 2.2. Continuous Random Variables


## 2.3. Cumulative Distribution Functions


## 2.4. Expected Values and Variance


# 3. Chapter 3: Widely Used Discrete Random Variables

## 3.1. Counting Techniques

## 3.2. Bernoulli

## 3.3. Binomial
