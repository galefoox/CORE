from math import sin, cos, acos

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import time
from mpl_toolkits.mplot3d import axes3d
from itertools import product, combinations

fig = plt.figure()
ax = p3.Axes3D(fig)

# Setting the axes properties
# TODO: change limits to size of asteroid
ax.set_xlim3d([-5.0, 5.0])
ax.set_xlabel('X')

ax.set_ylim3d([-5.0, 5.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-5.0, 5.0])
ax.set_zlabel('Z')
# ===========================================================================================
# create the parametric curve
R = 1  # radius of sphere
cx = 0.5  # center of sphere
cy = 0.5
cz = 0

# TODO LATER: move spaceship up a bit higher so its not caught in weaving of two drones -> start at higher point and then move in a straight line down and then split and do the arcs
# spaceship location = top of sphere
spaceship_point = (cx, cy, cz+R)


r0x, r0y, r0z = spaceship_point  # start point

# 2 end points because 2 drones
px1, py1, pz1 = (cx+R, cy, cz)
px2, py2, pz2 = (cx-R, cy, cz)

t = np.arange(0, 0.5 * 3.14159, 0.5 * 3.14159 /
              100)  # list points between 0 and 1

# parametric equation of straight line in 3D
# Parametric equations are a set of equations that express a set of quantities as explicit
# functions of a number of independent variables, known as "parameters.

# TODO: SAME THING FOR X2, Y2, Z2 - this is just for one drone
x1 = cx + R*np.sin(t)
y1 = [cy] * 100  # array[100] of cy
z1 = cz + R*np.cos(t)

x2 = cx + R*np.sin(t)
y2 = [cy] * 100
z2 = cz + R*np.cos(t)


point, = ax.plot([x1[0]], [y1[0]], [z1[0]], 'ro')
line, = ax.plot(x1, y1, z1, label='parametric curve')

point, = ax.plot([x2[0]], [y2[0]], [z2[0]], 'bo')
line, = ax.plot(x2, y2, z2, label='parametric curve')


def update_point(n, x, y, z, point):
    point.set_data(np.array([x1[n], y1[n]]))
    point.set_3d_properties(z1[n], 'z')

    point.set_data(np.array([x2[n], y2[n]]))
    point.set_3d_properties(z2[n], 'z')

    return point


ani = animation.FuncAnimation(fig, update_point, 99, fargs=(x1, y1, z1, point))
ani = animation.FuncAnimation(fig, update_point, 99, fargs=(x2, y2, z2, point))
# ========================================================================================
# =========================/////////////////////////////////////////================================
# q = [[5.00, 4.91, -0.27, -4.07, -0.65, -1.95],
#      [5.00, 0.71,  4.05, 5.66, -4.49,  -5.46], [5.00, 5.14, 2.80, 1.75, 6.24, 4.0267]]
# v = [[0.0068, 0.024, -0.014, -0.013, -0.0068, -0.04], [0.012,
#                                                        0.056, -0.022, 0.016,  0.0045, 0.039],
#      [-0.0045,  0.031,  0.077, 0.0016, -0.015, -0.00012]]

# x = np.array(q[0])
# y = np.array(q[1])
# z = np.array(q[2])
# s = np.array(v[0])
# u = np.array(v[1])
# w = np.array(v[2])

# point, = ax.plot(x, y, z, '*')


# def update_points(t, x, y, z, points):

#     new_x = x + s * t
#     new_y = y + u * t
#     new_z = z + w * t
#     print('t:', t)

#     # update properties
#     point.set_data(new_x, new_y)
#     point.set_3d_properties(new_z, 'z')

#     # return modified artists
#     return point


# ani = animation.FuncAnimation(
#     fig, update_points, frames=30, fargs=(x, y, z, point))
# =========================/////////////////////////////////////////================================
plt.show()

# - close file
file1.close()
file2.close()
