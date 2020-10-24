from math import sin, cos, acos

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import time
from mpl_toolkits.mplot3d import axes3d
from itertools import product, combinations


# ===========================================================================================
# create the parametric curve

count = 0
# next_initial = (5, 5, 5)


corners = [(-3, 4, 3), (3, 4, 3),  (-3, -4, 3), (3, -4, 3),
           (-3, 4, -3), (3, 4, -3), (-3, -4, -3), (3, -4, -3)]

R = 1
cx = 0.5
cy = 0.5
cz = 0


r0x, r0y, r0z = (5, 5, 5)  # start point
px, py, pz = corners[0]  # end point


t = np.arange(0, 1.0, 1.0 / 100)  # list points between 0 and 1

# parametric equation of straight line in 3D
# Parametric equations are a set of equations that express a set of quantities as explicit
# functions of a number of independent variables, known as "parameters.
x = r0x + (px - r0x)*t  # array of points
y = r0y + (py - r0y)*t
z = r0z + (pz - r0z)*t

# while count < len(corners):
#         r0x, r0y, r0z = px, py, pz
#         px, py, pz = corners[count]
#         count += 1
#         plt.plot(r0x, r0y, r0z, 'bo')


point, = ax.plot([x[0]], [y[0]], [z[0]], 'o')
line, = ax.plot(x, y, z, label='parametric curve')


def update_point(n, x, y, z, point):
    point.set_data(np.array([x[n], y[n]]))
    point.set_3d_properties(z[n], 'z')

    # while count < len(corners):
    #     r0x, r0y, r0z = px, py, pz
    #     px, py, pz = corners[count]
    #     count += 1
    #     plt.plot(r0x, r0y, r0z, 'bo')

    return point


ani = animation.FuncAnimation(fig, update_point, 99, fargs=(x, y, z, point))
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
