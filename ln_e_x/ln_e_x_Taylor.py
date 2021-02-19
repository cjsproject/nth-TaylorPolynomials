from matplotlib import pyplot as plt
import numpy as np
#import pandas as pd
import math

"""
* find linear and quadratic
* taylor polynomials for
* f(x) = ln(1 + e^x), where a = 0
"""

# all functions share this domain
x = np.arange(-1.5, 1.5, 0.01)
a = 0

# f(x)= e^(cos(x))
def f(n):
  return math.log(1 + math.exp(n))

# creates a list of range values for (dy/dx)^n, 
# i think this finds gradient, as in derivative at each point?
def deriv(n=1):
  return [dydx(j, degree=n) for j in x]
  
# generalized derivative: (dy/dx)^n?
def dydx(v, degree):
  h = math.exp(-6)
  if degree > 1:
    return dydx((f(v) - f(v-h))/(h), degree-1)
  else:
    return (f(v) - f(v-h))/(h)


# generalized Taylor Polynomial attempt
def nth_taylor_poly(n):
  poly = []
  for j in x:
    sum_poly = 0
    
    for i in range(n+1):
      if i == 0:
        sum_poly += f(j)
      else:
        sum_poly += ((j - a)**i)*dydx(j, degree=i)/(math.factorial(i))
    
    poly.append(sum_poly)
  return poly
  


fx = [f(i) for i in x]
fp = [dydx(a, 1) for i in x]
fpp = [dydx(a, 2) for i in x]
fp3 = [dydx(a, 3) for i in x]
"""
p1 = nth_taylor_poly(1)
p2 = nth_taylor_poly(2)
p3 = nth_taylor_poly(3)
"""
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
ax.plot(x, fx, 'k', label='f(x) = ln(1 + e^x)')
ax.plot(x, p1, 'r--', label='linear P1(x)')
ax.plot(x, p2, 'g--', label='quadratic P2(x)')
ax.plot(x, p3, 'b--', label='cubic P3(x)')

ax.legend()

#ax.set_ylim(ymin=-1.5, ymax = 1.5)
plt.savefig('ln_table.png')

plt.show()