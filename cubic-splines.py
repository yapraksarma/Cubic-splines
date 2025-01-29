import matplotlib.pyplot as plt
import numpy as np


#first cubic spline for 0
a = np.arange(1, 2, 0.001)
a1 = 3 + (3)*(a - 1) + (-1)*((a - 1)**3)

b = np.arange(2, 3, 0.001)
b1 = 5 + (-3)*((b - 2)**2) + (1)*((b - 2)**3)

#second cubic spline for 0
c = np.arange(1, 2, 0.001)
c1 = 3 + (-3)*(c - 1) + (1)*((c - 1)**3)

d = np.arange(2, 3, 0.001)
d1 = 1 + (3)*((d - 2)**2) + (-1)*((d - 2)**3)




# first linear spline for 1
e = np.arange(5.9, 6, 0.001)
e1 = 5 + 40*(e - 6)

#second linear spline for 1
f = np.arange(4, 6, 0.001)
f1 = 3 + 1*(f - 4)



#cubic spline for 2
g = np.arange(7, 8, 0.001)
g1 = 4 + (3/2)*(g - 7) + (-1/2)*((g - 7)**3)

h = np.arange(8, 9, 0.001)
h1 = (5) + (-3/2)*((h - 8)**2) + (1/2)*((h - 8)**3)

#first linear spline for 2
i = np.arange(7, 9, 0.001)
i1 = 1 + 0*(i - 9)

#second linear spline  for 2
j = np.arange(7, 9, 0.001)
j1 = 4 + (3/2)*(j - 9)



# first linear spline for 7
k = np.arange(10, 12, 0.001)
k1 = 5 + 2*(k - 12)

#second linear spline for 7
l= np.arange(10, 12, 0.001)
l1 = 5 + 0*(l - 12)


# plotting 0
plt.plot(a, a1)
plt.plot(b, b1)
plt.plot(c, c1)
plt.plot(d, d1)

# plotting 1
plt.plot(e, e1)
plt.plot(f, f1)

# plotting 2
plt.plot(g, g1)
plt.plot(h, h1)
plt.plot(i, i1)
plt.plot(j, j1)

# plotting 7
plt.plot(k, k1)
plt.plot(l, l1)


plt.axis((0,15,0,15))
plt.show()