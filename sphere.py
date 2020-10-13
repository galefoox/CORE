import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)


u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
##formula for creating a sphere - '(Asteroid)'
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="b")


plt.show()