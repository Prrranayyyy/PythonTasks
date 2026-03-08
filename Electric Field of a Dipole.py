import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5,5,30)
y = np.linspace(-5,5,30)
X, Y = np.meshgrid(x,y)

q1, q2 = 1, -1
x1, y1 = -1, 0
x2, y2 = 1, 0

r1 = np.sqrt((X-x1)**2 + (Y-y1)**2) + 0.1                                             
r2 = np.sqrt((X-x2)**2 + (Y-y2)**2) + 0.1
#+0.1 prevents division by zero near the charges


# electric field
Ex = q1*(X-x1)/r1**3 + q2*(X-x2)/r2**3
Ey = q1*(Y-y1)/r1**3 + q2*(Y-y2)/r2**3

E = np.sqrt(Ex**2 + Ey**2)
Ex = Ex/E
Ey = Ey/E

# plot
plt.figure(figsize=(6,6))
plt.quiver(X,Y,Ex,Ey)

plt.scatter([x1,x2],[y1,y2],color=['red','blue'],s=80)

plt.title("Electric Field of a Dipole")
plt.xlabel("x")
plt.ylabel("y")
plt.show()