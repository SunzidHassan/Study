# Lecture

---

## Overview

- [Lecture](#lecture)
  - [Overview](#overview)
  - [1. Introduction to Digital Control Systems](#1-introduction-to-digital-control-systems)
    - [1.1 Analog vs. Digital Signals](#11-analog-vs-digital-signals)
    - [1.2 Why Digital Control](#12-why-digital-control)
    - [1.3 Structure of a Digital Control System](#13-structure-of-a-digital-control-system)
    - [1.4 ADC and DAC](#14-adc-and-dac)
    - [1.5 Closed-loop System Examples](#15-closed-loop-system-examples)
  - [2. Discrete Time Systems and Z-Transform](#2-discrete-time-systems-and-z-transform)
    - [Overview](#overview-1)
    - [Discrete time systems](#discrete-time-systems)
    - [Linear difference equation](#linear-difference-equation)
    - [Z-transform](#z-transform)
  - [3. z-Transform Inversion and Final Value Theorem](#3-z-transform-inversion-and-final-value-theorem)
    - [3.1 Motivation](#31-motivation)
    - [3.2 Inversion of the Z-transform](#32-inversion-of-the-z-transform)
    - [3.3 Partial Fraction Expansion](#33-partial-fraction-expansion)
    - [3.4 Repeated Roots](#34-repeated-roots)
    - [3.5 Final Value Thorem](#35-final-value-thorem)
    - [3.6 Z-Transform Solutions of Difference Equations](#36-z-transform-solutions-of-difference-equations)
  - [4. Time and Frequency Response of Discrete-time System](#4-time-and-frequency-response-of-discrete-time-system)
    - [4.1 Time Response of Discrete-time Systems](#41-time-response-of-discrete-time-systems)
    - [4.2 The Convolution Theorem](#42-the-convolution-theorem)
    - [4.3 Frequency Response of Discrete-time Systems](#43-frequency-response-of-discrete-time-systems)
    - [4.4 The Sampling Theorem](#44-the-sampling-theorem)
    - [4.5 Selection of Sampling Frequency](#45-selection-of-sampling-frequency)
  - [5. Modeling of Digital Control Systems](#5-modeling-of-digital-control-systems)
    - [5.1 DAC Model](#51-dac-model)
    - [5.2 Transfer Function of Zero Order Hold](#52-transfer-function-of-zero-order-hold)
    - [5.3 Frequency Response of Zero Order Hold](#53-frequency-response-of-zero-order-hold)
    - [5.4 ADC Model](#54-adc-model)
    - [5.5 DAC, Analog Subsystem, and ADC Combination Transfer Function](#55-dac-analog-subsystem-and-adc-combination-transfer-function)
      - [Example](#example)
  - [6. Systems with Transport Lag and Block Diagram Reduction](#6-systems-with-transport-lag-and-block-diagram-reduction)
    - [6.1 Transport Lag](#61-transport-lag)
    - [6.2 The Modified z-Transform](#62-the-modified-z-transform)
    - [6.3 Systems with Transport Lag](#63-systems-with-transport-lag)
    - [6.4 Closed-loop Transfer Function](#64-closed-loop-transfer-function)
  - [7. Steady-state Error and Error Constants](#7-steady-state-error-and-error-constants)
    - [7.1 Steady-state Error](#71-steady-state-error)
    - [7.2 Type Number](#72-type-number)
    - [7.3 Steady-state Error of Step Input](#73-steady-state-error-of-step-input)
    - [7.4 Steady-state Error of Ramp Input](#74-steady-state-error-of-ramp-input)
    - [7.5 Steady-state Error of Parabolic Input](#75-steady-state-error-of-parabolic-input)
  - [8. Stability of Digital Control Systems, Nyquist Criterion, Phase Margin, and Gain Margin](#8-stability-of-digital-control-systems-nyquist-criterion-phase-margin-and-gain-margin)
    - [8.1 Stability in Discrete-time Systems](#81-stability-in-discrete-time-systems)
    - [8.2 Stable z-domain Pole Locations](#82-stable-z-domain-pole-locations)
    - [8.3 Pole Location-based Stability Test](#83-pole-location-based-stability-test)
    - [8.4 Jury Test](#84-jury-test)
    - [8.5 Internal Stability](#85-internal-stability)
    - [8.6 Nyquist Criterion](#86-nyquist-criterion)
    - [8.7 Nyquist Curve](#87-nyquist-curve)
    - [8.8 Gain Margin and Phase Margin](#88-gain-margin-and-phase-margin)
    - [8.9 Undefined Stability Margins](#89-undefined-stability-margins)
  - [10. Analog Control System Design](#10-analog-control-system-design)
- [HW](#hw)
  - [1](#1)
    - [1. Find the z-transforms of the following sequences:](#1-find-the-z-transforms-of-the-following-sequences)
    - [2. Find the z-transform of $cos(k\\omega T)$](#2-find-the-z-transform-of-coskomega-t)
    - [3.](#3)
    - [4.](#4)
    - [5. Find the final value for the function: $$F(z)=\\frac{z}{z^2-7z+6}$$](#5-find-the-final-value-for-the-function-fzfraczz2-7z6)
    - [6.](#6)
    - [7. Find convolution of](#7-find-convolution-of)
    - [8. Find the transfer function of the following system](#8-find-the-transfer-function-of-the-following-system)
    - [9.](#9)
    - [10.](#10)
  - [2](#2)
    - [1](#1-1)
    - [2](#2-1)
    - [3](#3-1)
    - [4](#4-1)
    - [5](#5)
    - [6](#6-1)
    - [7](#7)
    - [8](#8)
  - [HW 4](#hw-4)
    - [HW 4.1](#hw-41)
    - [HW 4.2](#hw-42)
    - [HW 4.3](#hw-43)
    - [HW 4.4](#hw-44)
    - [HW 4.5](#hw-45)
    - [HW 4.6](#hw-46)
    - [HW 4.7](#hw-47)
    - [HW 4.8](#hw-48)
    - [HW 4.9](#hw-49)

---

## 1. Introduction to Digital Control Systems

### 1.1 Analog vs. Digital Signals

### 1.2 Why Digital Control

### 1.3 Structure of a Digital Control System

### 1.4 ADC and DAC

### 1.5 Closed-loop System Examples

---

## 2. Discrete Time Systems and Z-Transform

### Overview

Analog/Digital: y-axis
Continuous/Discrete: x-axis

Sample times (x-values) and sample values (y-values).

Continuous time - Analog and Digital  
Discrete time - Analog and Digital  

### Discrete time systems

Systems whose inputs and outputs are discrete-time signals.

Example: bank interest
* Step $k$
* Current balance, $y[k]$
* Previous balance $y[k-1]$
* Current deposit $u[k]$
* Interest rate, $r$

Difference equation for current balance, 
$$y[k]=u[k]+y[k-1](1+r)$$

Differential (continuous-time) vs Difference (discrete-time) equations.

General form of difference equations:
$$y(k+n)=f\left[y(k+n-1), y(k+n-2), ..., y(k+1), y(k), u(k+n), u(k+n-1), ..., u(k+1), u(k)\right]$$

### Linear difference equation

$$y(k+n)+a_{n-1}y(k+n-1)+...+a_{1}y(k+1)+a_{0}y(k)=b_{n}u(k+n)+b_{n-1}u(k+n-1)+...+b_{1}u(k+1)+b_{0}u(k)$$
Properties:
* **System order**: the difference between highest and lowest arguments of $y(.)$ and $u(.)$
* **Time invariant**: if the coefficients ($a_o, ..., a_{n-1}, b_0, ..., b_n$) are constants, then the difference is time invariant. Apple (time variant) vs goat (time invariant)
* **Homogeneous**: if $u(.)=0$, then the difference equation is homogeneous.

Examples:

$y(k+2)+0.8y(k+1)+0.07y(k)=u(k)$
* The equation linear
* The coefficients are constant: time invarient
* We have u(k) in RHS: not homogenous
* System order = $y(k+2)-y(k)$ or 2

$y(k+4)+sin(0.4k)y(k+1)+0.3y(k)=0$
* Linear (Elements have function coefficient, but they are not functions)
* Time variant
* Homogeneous
* System order is 4

$y(k+1)=-0.1y^2(k)$
* Non-linear, time invarient, homogeneous.

Practice:
$y(k+2)-y(k+1)y(k)=u(k)$
* Non-linear
* Time-variant: constant coefficients
* Non-homogeneous
* Order: 2

$y(k+3)+2y(k)=0$
* Lienar
* Time invariant
* Homogeneous
* Order 3

$y(k+4)+y(k-1)=u(k)$
* System order is 5
* Linear
* Time invarient
* Non-homogeneous

### Z-transform

Motivation: similar to Laplace transform - converting convolution (for discrete, integration for continuous) into multiplication - by transforming time domain into z domain.

Z-transform is the discrete time version of Laplace-tranform.
$z=e^{sT}$

$Z\{u_k\}=1+3.z^{-1}+2z^{-2}+0z^{-3}+4z^{-4}$

$u_k=\{0, 1, 2, 4, 0, ... \}$  
$Z\{u_k\}=0+1.z^{-1}+2.z^{-2}+4.z^{-3}$

$u_k=\{0, 0, 0, 1, 1, 1, 0, 0, 0, ... \}$  
$Z\{u_k\}=1.z^{-3}+1.z^{-4}+1.z^{-5}$

$u_k=\{0, 0, 0, 1, 1, 1, 0, 0, 0, ... \}$  
$Z\{u_k\}=1.z^{-3}+1.z^{-4}+1.z^{-5}$

$u_k=\{1, 1, 1, ... \}$  
$Z\{u_k\}=\sum_{k=0}^\infin{z^{-k}}$

$$|a|\lt1\rightarrow\sum_{k=0}^\infin{a^{k}}=\frac{1}{1-a}$$

$$|z^{-1}|\lt1\rightarrow\sum_{k=0}^\infin{z^{-k}}=\frac{1}{1-k^{-1}}=\frac{z}{z-1}$$

15:

...

---

## 3. z-Transform Inversion and Final Value Theorem

### 3.1 Motivation

### 3.2 Inversion of the Z-transform

### 3.3 Partial Fraction Expansion

### 3.4 Repeated Roots

### 3.5 Final Value Thorem

### 3.6 Z-Transform Solutions of Difference Equations

---

## 4. Time and Frequency Response of Discrete-time System

### 4.1 Time Response of Discrete-time Systems

### 4.2 The Convolution Theorem

### 4.3 Frequency Response of Discrete-time Systems

### 4.4 The Sampling Theorem

### 4.5 Selection of Sampling Frequency

---

## 5. Modeling of Digital Control Systems

### 5.1 DAC Model

### 5.2 Transfer Function of Zero Order Hold

### 5.3 Frequency Response of Zero Order Hold

### 5.4 ADC Model

### 5.5 DAC, Analog Subsystem, and ADC Combination Transfer Function

$$G_{\text{ZAS}}(z)=\frac{z-1}{z}\mathcal{Z}\left\{\frac{G(S)}{S}\right\}$$

#### Example

3 steps of finding $G_{\text{ZAS}}(z)$:  

Step 1: Find $\frac{G(s)}{s}$  

Step 2: Find $\mathcal{Z}\left\{\frac{G(s)}{s}\right\}$

Step 3: Multiply $(1-z)^{-1}$ with $\mathcal{Z}\left\{\frac{G(s)}{s}\right\}$

---

## 6. Systems with Transport Lag and Block Diagram Reduction

### 6.1 Transport Lag

### 6.2 The Modified z-Transform

### 6.3 Systems with Transport Lag

### 6.4 Closed-loop Transfer Function

---

## 7. Steady-state Error and Error Constants

### 7.1 Steady-state Error

### 7.2 Type Number

### 7.3 Steady-state Error of Step Input

### 7.4 Steady-state Error of Ramp Input

### 7.5 Steady-state Error of Parabolic Input

---

## 8. Stability of Digital Control Systems, Nyquist Criterion, Phase Margin, and Gain Margin 


### 8.1 Stability in Discrete-time Systems

### 8.2 Stable z-domain Pole Locations

### 8.3 Pole Location-based Stability Test

### 8.4 Jury Test

### 8.5 Internal Stability

### 8.6 Nyquist Criterion

### 8.7 Nyquist Curve

### 8.8 Gain Margin and Phase Margin

### 8.9 Undefined Stability Margins

## 10. Analog Control System Design

---

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
$$f(k)=\{0, 5, 0, 0, 0, 4, 0, ...\}$$

b.
$$F(z)=\frac{z-0.1}{z^2+0.04z+0.25}$$

|                    | $z^{-1}-0.14z^{-2}-0.2444z^{-3}$ |
| ------------------ | -------------------------------- |
| ${z^2+0.04z+0.25}$ | ${z-0.1}$                        |
|                    | $z+0.04+0.25z^{-1}$              |
|                    |                                  |
|                    | $-0.14-0.25z^{-1}$               |
|                    | $0.14-0.0056z^{-1}-0.035z^{-2}$  |
|                    |                                  |
|                    | $-0.2444z^{-1}+0.035z^{-2}$      |

$$F(z)=z^{-1}-0.14z^{-2}-0.2444z^{-3}$$
$$f(k)=\{0, 1, -0.14, -0.2444, ...\}$$

### 4.

### 5. Find the final value for the function: $$F(z)=\frac{z}{z^2-7z+6}$$

$$F(z)=\frac{z}{z^2-7z+6}=\frac{z}{z^2-z-6z+6}=\frac{z}{z(z-1)-6(z-1)}=\frac{z}{(z-1)(z-6)}$$

$$f(\infin)=\lim_{z\rightarrow1}\left[(z-1)F(z)\right]$$
$$=\lim_{z\rightarrow1}\left[(z-1)\frac{z}{(z-1)(z-6)}\right]$$
$$=\lim_{z\rightarrow1}\left[\frac{z}{(z-6)}\right]=\frac{1}{1-6}=-0.2$$

### 6.

### 7. Find convolution of

$\{f(k)\}=\{2, 3, 4\}$  
$\{g(k)\}=\{1, 2\}$  
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

## 2

### 1

Magnitude:
$\lvert G_{ZOH}(j\omega) \rvert = T \left| \text{sinc} \left( \frac{\omega T}{2} \right) \right| = T \frac{\sin\left(\frac{\omega T}{2}\right)}{\frac{\omega T}{2}}$

$= 0.2 \frac{\sin\left(10 \times 0.2\right)}{10 \times 0.2 / 2}$

$\lvert G_{ZOH}(j\omega) \rvert = 0.1683$

Phase:
$\angle G_{ZOH}(j\omega) = -\frac{\omega T}{2} = -10 \times \frac{0.2}{2} = -1 \, \text{rad}$

### 2

$m\ddot{x}(t) = f(t)$

Taking Laplace:

$G(s) = \frac{X(s)}{F(s)} = \frac{1}{ms^2}$

$G(s) = \frac{1}{s} \cdot \frac{1}{ms} = \frac{1}{ms^3}$

$\therefore G(z) = \frac{z(z+1)T}{2m(z-1)^3}$

Multiplying by $(z - z^{-1})$ to get $G_{ZAS}(z)$:

$G_{ZAS}(z) = (z - z^{-1}) Z \{ G(s) \}$

$G_{ZAS}(z) = (z - z^{-1}) \frac{z(z+1)T}{2m(z-1)^3}$

Simplifying:

$G_{ZAS}(z) = \frac{(z+1)T^2}{2m(z-1)^2}$

### 3

**Given:**  
$T_d = 25 \, \text{ms}, \, T = 10 \, \text{ms}$

$25 = (3 - 0.5) \times 10$

Here, $l = 3$, and $m = 0.5$.

Given:

$G(s) = \frac{\epsilon\tau s + 1}{(\tau s + 1)}$
$G_s(s) = \frac{\epsilon\tau s + 1}{s(\tau s + 1)}$

**Doing partial fraction:**

$G(s) = \frac{A}{s} + \frac{B}{\tau s + 1}$

Finding $A$ and $B$:

$A = 1$

$B = \tau(\epsilon-1)$

$\therefore G(s) = \frac{1}{s} + \frac{\tau(\epsilon-1)}{\tau s + 1}$

Taking the Z-transform:

$G_{ZAS}(z) = z^{-3}\left(1 + (\epsilon-1)\frac{(z - 1)(e^{-5/\tau})}{(z - e^{-T/\tau})} \right)$ 

### 4

**From the figure:**

$E(S) = R(S) - H(S)Y^*(S)$

Again, 

$Y(S) = G(S)C(S)E^*(S)$

$Y^*(S) = (G_C^*(S)C^*(S))E^*(S)$

Now, 

$E^*(S) = R^*(S) - H^*(S)(GC)^*(S)E^*(S)$

$\therefore E^*(S) = \frac{R^*(S)}{1 + ((HGC)^*)(S)}$

The analog $Y(S) $ is then:

$
Y(S) = G(S)C(S)E^*(S)
$

$
\therefore Y(S) = G(S)C(S) \frac{R^*(S)}{1 + (HGC)^*(S)} \quad \text{(ANS)}
$

Sampled $ Y^*(S) $ is the sample of $ Y(S) $. We can write:

$
Y^*(S) = (GC)^*(S)E^*(S)
$

$
\therefore Y^*(S) = \frac{(GCR)^*(S)}{1 + (HGC)^*(S)} \quad \text{(ANS)}
$

### 5

For the following system with unity feedback, find:

1. The position error constant $ K_p $ (C(E) = 1).  
2. The velocity error constant $ K_v $.  
3. The steady-state error due to a unit step input.  
4. The steady-state error due to a unit ramp input.

The system transfer function is given as:

$$
G(z) = \frac{0.5z + 0.2}{(z - 0.1)(z - 0.8)}
$$

From the figure, the system is **Type-0**, as it does not have any unity poles.  
Thus, $ n = 0 $.

1. Position Error Constant ($ K_p $):

For a Type-0 system, $ n = 0 $, so:

$$
K_p = \frac{N(1)}{D(1)} = \text{constant}
$$

Substituting the values:

$$
K_p = G(1) = \frac{0.5 \times 1 + 0.2}{(1 - 0.1)(1 - 0.8)} = \frac{0.7}{0.9 \times 0.2} = 3.3333
$$

2. Steady-State Error Due to a Unit Step Input:

$$
\text{Steady-state error} = \frac{1}{1 + K_p}
$$

$$
\text{Steady-state error} = \frac{1}{1 + 3.3333} = 0.231 \quad \text{(ANS)}
$$

3. Velocity Error Constant ($ K_v $):

For a Type-0 system, $ n = 0 $, so:

$$
K_v = \lim_{z \to 1} (z - 1) \cdot G(z) = 0
$$

$$
\text{So, steady-state error due to ramp input: } e(\infty) = \frac{1}{K_v} = \infty
$$

4. Steady-State Error Due to a Unit Ramp Input:

$$
e(\infty) = \frac{1}{K_v} = \frac{1}{0} = \infty
$$

### 6

$y(k+2) - 0.8y(k+1) + 0.07y(k) = 2u(k+1) + 0.2u(k), \quad k = 0, 1, 2, \dots$

Step 1: Derive the Transfer Function
Using the Z-transform of the system:

$z^2 Y(z) - 0.8z Y(z) + 0.07 Y(z) = 2z U(z) + 0.2 U(z)$

Simplify:

$(z^2 - 0.8z + 0.07) Y(z) = (2z + 0.2) U(z)$

$\therefore G(z) = \frac{Y(z)}{U(z)} = \frac{2z + 0.2}{z^2 - 0.8z + 0.07}$

Step 2: Check the Roots of the Denominator

$z^2 - 0.8z + 0.07$

Factoring gives:

$z^2 - 0.8z + 0.07 = (z - 0.7)(z - 0.1)$

The roots are$ z = 0.7$ and$ z = 0.1$.

Step 3: Stability Check
For BIBO stability, all poles of$ G(z)$ must lie inside the unit circle $|z| < 1$:

* $ |0.7| < 1$
* $ |0.1| < 1$

Since both roots satisfy$ |z| < 1$, the system is **BIBO stable**.

### 7

Determine 
$$G_{\text{ZAS}}(z)=\frac{z-1}{z}\mathcal{Z}\left\{\frac{G(S)}{S}\right\}$$

3 steps of finding $G_{\text{ZAS}}(z)$:  

Step 1: Find $\frac{G(s)}{s}$  
$$\frac{G(s)}{s}=\frac{5.8644}{s(-5.888s+1)}=\frac{A}{s}+\frac{B}{1-5.888s}$$
$$5.8644=A(-5.888s+1)+Bs$$
For $s=0$, $5.8644=A(1-0)+B\times0\Rightarrow A=5.8644$
For $s=\frac{1}{5.888}$, $5.8644=A(1-5.888\times\frac{1}{5.888})+B\times\frac{1}{5.888}\Rightarrow B=34.52$
$$\frac{G(s)}{s}=\frac{5.8644}{s(-5.888s+1)}=\frac{5.8644}{s}+\frac{34.52}{1-5.888s}$$

Step 2: Find $\mathcal{Z}\left\{\frac{G(s)}{s}\right\}$
$$\frac{5.8644}{s}\rightarrow5.8644\times\frac{z}{z-1}$$
$$\frac{34.52}{1-5.888s}\Rightarrow -5.8644\times\frac{1}{s+\frac{1}{-5.888}} \rightarrow -5.8644\times\frac{z}{z-e^{-0.17\times0.1}}$$

$$\mathcal{Z}\frac{G(s)}{s}=5.8644\times\frac{z}{z-1}-5.8644\times\frac{z}{z-e^{-0.17\times0.1}}$$

Step 3: Multiply $(1-z)^{-1}$ with $\mathcal{Z}\left\{\frac{G(s)}{s}\right\}$
$$G_{\text{ZAS}}(z)=(1-z)^{-1}\mathcal{Z}\frac{G(s)}{s}=\frac{z-1}{z}\times5.8644\times\frac{z}{z-1}+\frac{z-1}{z}\times-5.8644\times\frac{z}{z-e^{-0.17\times0.1}}=5.8644-5.8644\times\frac{z-1}{z-1.017}$$

$$G_{\text{ZAS}}(z)=5.8644-5.8644\times\frac{z-1}{z-1.017}=5.8644\left(1-\frac{z-1}{z-1.017}\right)=\frac{5.8644\times-0.017}{z-1.017}=\frac{-0.1}{z-1.017}$$
$$C(z)=\frac{z-1.017}{z-1}$$

Due to the pole-zero cancellation on 1.017 in the loop gain, the system is not internally stable.

### 8

$$F(z)=z^5-0.25Z^4+0.1z^3+0.4z^2+0.3z-0.1=0$$

The system order $n=5$, thus, we need to verify 6 conditions in Jury test.
1. $F(1)\gt0$
2. $(-1)^5F(-1=)\gt0$
3. $|a_0|\lt a_5$
4. $|b_0|\lt b_4$
5. $|c_0|\lt c_3$
6. $|d_0|\lt d_2$

Following the steps:

1. $F(1)\gt0$

$F(1) = 1 - 0.25(1) + 0.1(1) + 0.4(1) + 0.3(1) - 0.1 = 1 - 0.25 + 0.1 + 0.4 + 0.3 - 0.1 = 1.45$

2. $(-1)^5F(-1=)\gt0$

$F(-1) = (-1)^5 - 0.25(-1)^4 + 0.1(-1)^3 + 0.4(-1)^2 + 0.3(-1) - 0.1 = -1 - 0.25 - 0.1 + 0.4 - 0.3 - 0.1 = -1.3$

$(-1)^5 F(-1) = (-1) \times (-1.35) = 1.35 > 0$

3. $|a_0|\lt a_5$

$|a_0| = |-0.1| = 0.1 < 1 = a_5$

4. $|b_0|\lt b_4$  

$F^*(z) = z^5 F\left(\frac{1}{z}\right) = 1 - 0.25z + 0.1z^2 + 0.4z^3 + 0.3z^4 - 0.1z^5$

$F(z) - F^*(z) = (z^5 - 0.25z^4 + 0.1z^3 + 0.4z^2 + 0.3z - 0.1) - (1 - 0.25z + 0.1z^2 + 0.4z^3 + 0.3z^4 - 0.1z^5)$

$= 1.1z^5 - 0.55z^4 - 0.3z^3 + 0.3z^2 + 0.55z - 1.1$

$F_1(z) = \frac{F(z) - F^*(z)}{1 - |a_0|^2} = \frac{1.1z^5 - 0.55z^4 - 0.3z^3 + 0.3z^2 + 0.55z - 1.1}{0.99} \approx 1.1111z^5 - 0.5556z^4 - 0.3030z^3 + 0.3030z^2 + 0.5556z - 1.1111$

$F_1(z) = 1.1111z^5 - 0.5556z^4 - 0.3030z^3 + 0.3030z^2 + 0.5556z - 1.1111$

$b_5 = 1.1111, \quad b_4 = -0.5556, \quad b_3 = -0.3030, \quad b_2 = 0.3030, \quad b_1 = 0.5556, \quad b_0 = -1.1111$

$|b_0| = |-1.1111| = 1.1111 \quad \text{and} \quad |b_4| = |-0.5556| = 0.5556$

$1.1111 > 0.5556 \implies |b_0| > |b_4|$

5. $|c_0|\lt c_3$

$F_1^*(z) = -1.1111z^5 + 0.5556z^4 + 0.3030z^3 - 0.3030z^2 - 0.5556z + 1.1111$

$F_1(z) - F_1^*(z) = 1.1111z^5 - (-1.1111z^5) + (-0.5556z^4 - 0.5556z^4) + (-0.3030z^3 - 0.3030z^3) + (0.3030z^2 + 0.3030z^2) + (0.5556z + 0.5556z) + (-1.1111 - 1.1111)$

$= 2.2222z^5 - 1.1112z^4 - 0.6060z^3 + 0.6060z^2 + 1.1112z - 2.2222$

$F_2(z) = \frac{2.2222z^5 - 1.1112z^4 - 0.6060z^3 + 0.6060z^2 + 1.1112z - 2.2222}{1 - |b_0|^2} = \frac{2.2222z^5 - 1.1112z^4 - 0.6060z^3 + 0.6060z^2 + 1.1112z - 2.2222}{1 - (1.1111)^2} = \frac{2.2222z^5 - 1.1112z^4 - 0.6060z^3 + 0.6060z^2 + 1.1112z - 2.2222}{-0.2345}$

$\approx -9.48z^5 + 4.735z^4 + 2.583z^3 - 2.583z^2 - 4.735z + 9.48$

$F_2(z) = c_5z^5 + c_4z^4 + c_3z^3 + c_2z^2 + c_1z + c_0$

$\Rightarrow c_5 = -9.48, \quad c_4 = 4.735, \quad c_3 = 2.583, \quad c_2 = -2.583, \quad c_1 = -4.735, \quad c_0 = 9.48$

$|c_0| = |9.48| = 9.48 \quad \text{and} \quad |c_3| = |2.583| = 2.583$

Condition 5 fails, the system is not stable.


## HW 4
### HW 4.1
a. A single-input, single-ouput, linear time-varying system.

b. A single-input, single-output, linear, time-invariant.

c. Single-input, single-output, non-linear, time-invariant.

### HW 4.2
Linearizing at the equilibrium point (1,0,0):
$\frac{\delta f_1}{\delta x_1}=2x_1$, $\frac{\delta f_1}{\delta x_2}=\cos{x_2}$, $\frac{\delta f_1}{\delta u}=0$.  

$\frac{\delta f_2}{\delta x_1}=0$, $\frac{\delta f_2}{\delta x_2}=-3x_2^2$, $\frac{\delta f_2}{\delta u}=1$.  

Evaluating at (1,0,0)
$\frac{\delta f_1}{\delta x_1}=2$, $\frac{\delta f_1}{\delta x_2}=1$, $\frac{\delta f_1}{\delta u}=0$.  

$\frac{\delta f_2}{\delta x_1}=0$, $\frac{\delta f_2}{\delta x_2}=0$, $\frac{\delta f_2}{\delta u}=1$.  

$\frac{f(x,u)}{\delta x|\{x_0u_0\}}=A=\left[\begin{array}{cc}2&1\\0&0\\\end{array}\right]$  
$\frac{f(x,u)}{\delta x|\{x_0u_0\}}=B=\left[\begin{array}{c}0\\1\\\end{array}\right]$

### HW 4.3
a. State transition matrix:
$e^{At}=\left[\begin{array}{ccc}
e^{-3t} & 0 & 0\\
0 & e^{-5t} & 0\\
0 & 0 & e^{-7t}\\
\end{array}\right]$

b. State transition matrix:
$\left[\begin{array}{ccc}
\cos{\sqrt{6}t} & 0 & \frac{\sqrt{6}\sin{\sqrt{6}t}}{6}\\
0 & e^{-t} & 0\\
\sqrt{6}\sin{\sqrt{6}t} & 0 & \cos{\sqrt{6}t}
\end{array}\right]$

### HW 4.4
Discrete A matrix,  
$A_d=\left[\begin{array}{ccc}
0.993187 & -0.03434 & 0\\
-0.009456 & 0.997766 & 0\\
-0.000237 & 0.049943 & 1\\
\end{array}\right]$

$B_d=\left[\begin{array}{c}
0.002988\\
-0.0115\\
-0.000287\\
\end{array}\right]$

$C_d=\left[\begin{array}{ccc}
1 & 0 & 0\\
0 & 1 & 0\\
\end{array}\right]$

$D_d=\left[\begin{array}{c}
0\\
0\\
\end{array}\right]$

### HW 4.5
$\left[\begin{array}{c}
x_1(k+1)\\
x_2(k+1)\\
\end{array}\right]=
\left[\begin{array}{cc}
0 & 1\\
-0.5 & -0.1\\
\end{array}\right]=
\left[\begin{array}{c}
x_1(k)\\
x_2(k)\\
\end{array}\right]$

$\left[\begin{array}{c}
x_1e\\
x_2e\\
\end{array}\right]=
\left[\begin{array}{cc}
0 & 1\\
-0.5 & -0.1\\
\end{array}\right]=
\left[\begin{array}{c}
x_1e\\
x_2e\\
\end{array}\right]$

Rearranging with $(I-A)xe=0$
$\left[\begin{array}{cc}
1-0 & -1\\
0.5 & 1+0.1\\
\end{array}\right]=
\left[\begin{array}{c}
x_1e\\
x_2e\\
\end{array}\right]$

$\left[\begin{array}{cc}
1 & -1\\
0.5 & 1.1\\
\end{array}\right]=
\left[\begin{array}{c}
x_1e\\
x_2e\\
\end{array}\right]=
\left[\begin{array}{c}
0\\
0\\
\end{array}\right]$

$x_1e-x_2e=0\Rightarrow x_1e=x_2e$

$0.5x_1e+1.1x_2e=0\Rightarrow x_2e = 0 = x_1e$

$x_e=
\left[\begin{array}{c}
x_1e\\
x_2e\\
\end{array}\right]=
\left[\begin{array}{c}
0\\
0\\
\end{array}\right]$

The equlibrium state is 
$x_e=
\left[\begin{array}{cc}
0 & 0\\
\end{array}\right]^T$

### HW 4.6
a.
Eigenvalues are obtained by solving 
$\det{(A-\lambda I)}=0$

$\left[\begin{array}{cc}
0.1-\lambda & 0\\
1 & 0.2-\lambda\\
\end{array}\right]$

$\lambda_1=0.1\lt1$,
$\lambda_2=0.2\lt1$

All eigenvalues lie inside the unit circle, the system is asymptotically stable.

b.
$\left[\begin{array}{ccc}
\lambda+0.2 & 0.2 & 0\\
0 & \lambda-1 & 0.1\\
0 & 0 & \lambda+1\\
\end{array}\right]$  
$\Rightarrow (\lambda+0.2)\{(\lambda-1)(\lambda+1)-0\}\Rightarrow \lambda=\pm1,-0.2$

Not asymptotically stable.

### HW 4.7
a.
$e=[B_d| A_dB_d]$
$e=\left[\begin{array}{cc}
0 & | & 0\\
0.2 & | & 0.04
\end{array}\right]$

Rank $1\lt2$, system is not controllable.
$O=\left[\begin{array}{c}
c\\
cA_d\\
\end{array}\right]
=\left[\begin{array}{cc}
1 & 1\\
1.1 & 0.2\\
\end{array}\right]$

Full rank, system is observable.

b. c
$C =
\left[\begin{array}{ccccc}
B_d & | & A_dB_d & | & A_d^2B_d\\
\end{array}\right]=
\left[\begin{array}{cccccccc}
1 & 0 & | & -0.2 & 0 & | & 0.06 & 0.02\\
0 & 0 & | & 0.1 & 0.1 & | & 0 & 0\\
1 & 1 & | & -1 & -1 & | & 1 & 1\\
\end{array}\right]$
The rank is 3, the system is controllable.

$C=
\left[\begin{array}{ccc}
1 & 0 & 0\\
\end{array}\right]$

$A=
\left[\begin{array}{ccc}
-0.2 & 0.2 & 0\\
0 & 1 & 0.1\\
0 & 0 & -1\\
\end{array}\right]$

$O=\left[\begin{array}{c}
C\\
CA_d\\
CA_d^2\\
\end{array}\right]=
\left[\begin{array}{ccc}
1 & 0 & 0\\
-0.2 & 0.2 & 0\\
0.04 & 0.16 & 0.02\\
\end{array}\right]$

The rank is 3, the system is fully observable.

### HW 4.8
$A=
\left[\begin{array}{cc}
-1 & 0\\
1 & -2\\
\end{array}\right]$

$B=
\left[\begin{array}{c}
1\\
0\\
\end{array}\right]$

First, we check the controllability of the system
$P_c=
\left[\begin{array}{c}
B, AB\\
\end{array}\right]=
\left[\begin{array}{cc}
1 & -1\\
0 & 1\\
\end{array}\right]$

Since P_c is full rank, the system is controllable. We can use pole placement.

Step 1:The desired characteristic equation  
$(\lambda+2+2j)(\lambda+2-2j)=\lambda^2+4\lambda+8$

Step 2: the closed-loop characteristic equation is  
$(A-B_k)=
\left[\begin{array}{cc}
-1 & 0\\
1 & -2\\
\end{array}\right]-
\left[\begin{array}{cc}
k_1 & k_2\\
0 & 0\\
\end{array}\right]=
\left[\begin{array}{cc}
-1-k_1 & -k_2\\
1 & -2\\
\end{array}\right]$

Det $\lambda I_n - (A-B_k) = \lambda^2+\lambda(3+k_1)+(2+2k_1+K_2)$

Step 3: equating coefficients of eqn(1) and eqn(2) -
$k = [k_1, k_2] = [1, 4]$

### HW 4.9
$A =
\left[\begin{array}{cc}
-1 & 0\\
1 & -2\\
\end{array}\right]$

$c=
\left[\begin{array}{cc}
0 & 1\\
\end{array}\right]$

Step 1: check observability

$P_0=
\left[\begin{array}{c}
C\\
CA\\
\end{array}\right]=
\left[\begin{array}{cc}
0 & 1\\
1 & -2\\
\end{array}\right]$
$P_0$ is full rank, system is observable.

Step 2: compute $\Delta(\lambda)$
$\Delta(\lambda)=
(\lambda+8)(\lambda+10)=\lambda^2+18\lambda+80$

Step 3: compute det$(\lambda I-(A-LC))$
$A-LC =
\left[\begin{array}{cc}
-1 & 0\\
1 & -2\\
\end{array}\right]-
\left[\begin{array}{c}
L_1\\
L_2\\
\end{array}\right]
\left[\begin{array}{c}
0 & 1\\
\end{array}\right]=
\left[\begin{array}{cc}
-1 & -L_1\\
1 & (-2-L_2)\\
\end{array}\right]$

$\lambda I-(A-LC)=
\left[\begin{array}{cc}
\lambda & 0\\
0 & \lambda\\
\end{array}\right]-
\left[\begin{array}{cc}
-1 & -L_1\\
1 & (-2-L_2)\\
\end{array}\right]=
\left[\begin{array}{cc}
\lambda+1 & L_1\\
-1 & \lambda+2+L_2\\
\end{array}\right]
$

$
\det(\lambda I-(A-LC))=
(\lambda+1)(\lambda+2+L_2)+L_1=
\lambda^2+\lambda(3+L_2)+(2+L_1+L_2)
$

Step 4: equating the coefficient
$L_2=15$  
$L_1=63$

$\left[\begin{array}{c}
63\\
15\\
\end{array}\right]$