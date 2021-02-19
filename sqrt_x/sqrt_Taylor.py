from matplotlib import pyplot as plt
import numpy as np
#import pandas as pd
import math


"""
* find linear and quadratic
* taylor polynomials for
* f(x)=sqrt(x) where a=1
"""

x = np.arange(0.01, 1.5, 0.01)
a = 1
# f(x)=sqrt(x)
def f(n):
  return math.sqrt(n)


# first derive f(x)=sqrt(x)
def deriv(n=1):
  h = math.exp(-10)
  prime = [(f(j) - f(j-h))/(h) for j in x]
  return prime
  if n > 1:
    coeff = 1/2
    power = (1/2)-1
    for i in range(n):
      coeff *= 1/2-i
      power -= 1
    power -= 1
    return [round(coeff*(j**power), 2) for j in x]


# generalized derivative: (dy/dx)^n?
def dydx(v, degree):
  h = math.exp(-6)
  if degree > 1:
    return dydx((f(v) - f(v-h))/(h), degree-1)
  else:
    return (f(v) - f(v-h))/(h)


# arrays containing y values of
# f(x), f'(x) and f''(x)
fx = [f(i) for i in x]
fp = [dydx(a, 1) for i in x]
fpp = [dydx(a, 2) for i in x]
fp3 = [dydx(a, 3) for i in x]
"""
original derivative method, didn't use f'(a)
fp = deriv()
fpp = deriv(n=2)
"""
# create taylor polynomials using 
# previously computed derivatives.
a = 1
p1 = [f(a) + (i-a)*j for i, j in zip(x,fp)]
p2 = [f(a) + (i-a)*j + (0.5)*((i-a)**2)*k for i,j,k in zip(x,fp,fpp)]
p3 = [f(a) + (i-a)*j + (0.5)*((i-a)**2)*k + (1/6)*((i-a)**3)*l for i,j,k,l in zip(x,fp,fpp, fp3)]

# get subplots
fig, ax = plt.subplots()

# fix aspect ratios
ax.set_aspect('equal')
ax.grid(True, which='both')

# horiz and vert axis colors
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# set the y min and max vals
ax.set_ylim(ymin=0, ymax=2)

ax.plot(x, fx, 'k', label='f(x)')
ax.plot(x, p1, 'r--', label='linear P1(x)')
ax.plot(x, p2, 'g--', label='quadratic P2(x)')
ax.plot(x, p3, 'b--', label='cubic P3(x)')

ax.legend()
plt.show()