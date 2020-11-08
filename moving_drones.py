from math import sin, cos, acos

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import time
from mpl_toolkits.mplot3d import axes3d
from itertools import product, combinations
# for read image #
import matplotlib.image as mpimg


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

# Add image as a background #
#img = mpimg.imread('https://i.imgur.com/XR1J92C.png')
# plt.imshow(img)


# ===========================================================================================
# create the parametric curve
R = 5  # radius of sphere
cx = 0  # center of sphere
cy = 3.5
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
x1 = cx + R*np.sin(t)  # an array of points dependent on time
y1 = [cy] * 100  # array[100] of cy
z1 = cz + R*np.cos(t)

x2 = cx - R*np.sin(t)
y2 = [cy] * 100
z2 = cz + R*np.cos(t)


point1, = ax.plot([x1[0]], [y1[0]], [z1[0]], 'ro')
line1, = ax.plot(x1, y1, z1, label='parametric curve')

point2, = ax.plot([x2[0]], [y2[0]], [z2[0]], 'bo')
line2, = ax.plot(x2, y2, z2, label='parametric curve')


def update_point(n, x, y, z, point):
    point1.set_data(np.array([x1[n], y1[n]]))
    point1.set_3d_properties(z1[n], 'z')

    point2.set_data(np.array([x2[n], y2[n]]))
    point2.set_3d_properties(z2[n], 'z')

    return (point1, point2)


ani1 = animation.FuncAnimation(
    fig, update_point, 99, fargs=(x1, y1, z1, point1))
ani2 = animation.FuncAnimation(
    fig, update_point, 99, fargs=(x2, y2, z2, point2))
# ========================================================================================
# =========================/////////////////////////////////////////======================

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
# ax.imshow(img)
plt.show()

# - close file
file1.close()
file2.close()
