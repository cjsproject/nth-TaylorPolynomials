from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

x = np.arange(0.5, 1.5, 0.1)
fx = [round(math.log(i), 2) for i in x]


# sum from j=1 to n of ln(x) Taylor Polynomial
def ntaylor_ln(n, a):
    assert (n > 0), "Taylor Polynomial defined for j > 0"
    polynomials = []
    for j in range(1, n + 1):
        s = [round( ((-1)**(j - a)) * ((i - a)**j) / (j), 2 )for i in x]
        polynomials.append(s)

    temp = []
    for poly in polynomials:
        if poly == polynomials[0]:
            temp = poly
            continue
        else:
            s = []
            for i, j in zip(poly, temp):
                s.append(i + j)

            temp = s

    return temp


p1 = ntaylor_ln(n=1, a=1.0)
p2 = ntaylor_ln(n=2, a=1.0)
p3 = ntaylor_ln(n=3, a=1.0)

# grab subplots
fig, ax = plt.subplots()

#hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

#create data
df = pd.DataFrame({
    'x': x,
    'P1(x)': p1,
    'P2(x)': p2,
    'P3(x)': p3,
    'f(x)=ln(x)': fx
})

#create table
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

#display table
#ax.tight_layout()
plt.title('Taylor Approx of e^(x) on interval [-1, 1]')

#plt.savefig('ln_table.png')


plt.show()
""" Graph using matplotlib
# fix aspect ratios
ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.plot(x, fx, 'k', x, p1, 'r--', x, p2, 'b--', x, p3, 'g--')
plt.show()
#print(ntaylor_exp(2,0))
#print("p2:\n", p2)
"""
