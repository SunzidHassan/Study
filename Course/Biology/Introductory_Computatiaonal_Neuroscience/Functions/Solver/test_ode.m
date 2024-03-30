%integrate_sinx Used to demonstrate ODE solvers

function [ dydt ] = test_ode(t, y)

dydt = 2*sin(0.1*t*t);end