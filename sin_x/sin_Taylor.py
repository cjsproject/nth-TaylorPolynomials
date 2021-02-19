from matplotlib import pyplot as plt
import numpy as np
#import pandas as pd
import math

"""
* find linear and quadratic
* taylor polynomials for
* f(x)=sin(x) where a=(pi/4)
"""

x = np.arange(-2., 2., 0.01)
a=(math.pi/4)

# f(x)=sin(x)
def f(n):
  return math.sin(n)

# generates derivatives of sin(x)
def deriv(n=1):
  h = math.exp(-10)
  prime = [(f(j) - f(j-h))/(h) for j in x]
  if n == 1:
    return prime
  elif n % 2 == 0:
    if n % 4 == 0:
      return [f(i) for i in x]
    else:
      return [-1.0*f(i) for i in x]
  else:
    if n % 3 == 0:
      return [-1.0*math.cos(i) for i in x]
    else:
      return [math.cos(i) for i in x]

# generalized derivative: (dy/dx)^n?
def dydx(v, degree):
  h = math.exp(-6)
  if degree > 1:
    return dydx((f(v) - f(v-h))/(h), degree-1)
  else:
    return (f(v) - f(v-h))/(h)


fx = [f(i) for i in x]
fp = [dydx(a, 1) for i in x]
fpp = [dydx(a, 2) for i in x]
fp3 = [dydx(a, 3) for i in x]
"""
fp = deriv()
fpp = deriv(n=2)
"""
# set a = 1 and keep derivative fcn sqrt(x)
# for hilarious approximations
a = math.pi/4
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
ax.plot(x, fx, 'k', label='f(x) = sin(x)')
ax.plot(x, p1, 'r--', label='linear P1(x)')
ax.plot(x, p2, 'g--', label='quadratic P2(x)')
ax.plot(x, p3, 'b--', label='cubic P3(x)')

ax.legend()

ax.set_ylim(ymin=-1.5, ymax = 1.5)

plt.show()