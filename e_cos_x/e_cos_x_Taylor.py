from matplotlib import pyplot as plt
import numpy as np
#import pandas as pd
import math

"""
* find linear and quadratic
* taylor polynomials for
* f(x) = e^(cos(x)) where a=0
* f(a) = e
* f'(x) = cos(x)*e^(cos(x)-1)
* f'(a) = 1
* f''(x) = cos(x)*(cos(x)-1)*e^(cos(x)-2) + -sin(x)*e^(cos(x)-1)
* f''(a) = 0
"""

x = np.arange(-1.5, 1.5, 0.01)
a = 0

# f(x)= e^(cos(x))
def f(n):
  return math.exp(math.cos(n))

# derivatives of f(x)
def deriv(n=1):
  h = math.exp(-6)
  prime = [(f(j) - f(j-h))/(h) for j in x]
  if n == 1:
    return prime
  elif n == 2:
    d2 = [
      math.cos(i)*(math.cos(i)-1)*(math.exp(math.cos(i)-2)) + 
      -math.sin(i)*math.exp(math.cos(i)-1) for i in x]
    return d2

# generalized derivative: (dy/dx)^n?
def dydx(v, degree):
  h = math.exp(-1)
  if degree > 1:
    return dydx((f(v) - f(v-h))/(h), degree-1)
  else:
    return (f(v) - f(v-h))/(h)


fx = [f(i) for i in x]
fp = [dydx(a, 1) for i in x]
fpp = [dydx(a, 2) for i in x]
fp3 = [dydx(a, 3) for i in x]


p1 = [f(a) + (i-a)*j for i, j in zip(x,fp)]
p2 = [f(a) + (i-a)*j + (0.5)*((i-a)**2)*k for i,j,k in zip(x,fp,fpp)]

p3 = [f(a) + (i-a)*j + (0.5)*((i-a)**2)*k + (1/6)*((i-a)**3)*l for i,j,k,l in zip(x,fp,fpp, fp3)]


#grab subplots
fig, ax = plt.subplots()

# fix aspect ratios
ax.set_aspect('equal')
ax.grid(True, which='both')

# horiz and vert axis colors
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# plot f(x), P1(x), P2(x)
ax.plot(x, fx, 'k', label='f(x) = e^(cos(x))')
ax.plot(x, p1, 'r--', label='linear P1(x)')
ax.plot(x, p2, 'g--', label='quadratic P2(x)')
ax.plot(x, p3, 'b--', label='cubic P3(x)')


ax.legend()

#ax.set_ylim(ymin=-1.5, ymax = 1.5)

plt.show()