#!/usr/bin/python3

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
#ax = p3.Axes3D(fig)
ax = fig.add_subplot(111, projection='3d', box_aspect=(4, 4, 4))


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


# TODO -- distance space ship to asteroid (some random number)
dist_spsh_ast = 0.5*R

spsh_z = dist_spsh_ast + (cz+R)  # cz+R = highest point of asteroid

# PART 1: going straight down from space ship   d = down

Np_d = 10   # number of points for part 1
tmax_d = 2.0  # time needed for going down

t_d = np.linspace(0, tmax_d, Np_d)   # 0..2  with "Np_d" points in total

x1d = [cx] * Np_d
y1d = [cy] * Np_d
# array of z values  -- t_d/tmax_d = array [0,1]   and   dist1/tmax_d * t_d = array [0,dist_spsh_ast]
z1d = spsh_z - (dist_spsh_ast/tmax_d) * t_d

x2d = x1d
y2d = y1d
z2d = z1d


# PART 2: arcs   a = arc

Np_a = 20   # number of points for part 2
tmax_a = 3.0  # time needed for arc

PI = 3.14159

# np.arange(0, 0.5 * 3.14159, 0.5 * 3.14159 / 100)  # list points between 0 and 1
t_a = np.linspace(0, tmax_a, Np_a)

# parametric equation of straight line in 3D
# Parametric equations are a set of equations that express a set of quantities as explicit
# functions of a number of independent variables, known as "parameters.

# an array of points dependent on time
x1a = cx + R*np.sin(t_a * 0.5*PI/tmax_a)
y1a = [cy] * Np_a  # array[100] of cy
z1a = cz + R*np.cos(t_a * 0.5*PI/tmax_a)

x2a = cx - R*np.sin(t_a * 0.5*PI/tmax_a)
y2a = [cy] * Np_a
z2a = cz + R*np.cos(t_a * 0.5*PI/tmax_a)


# PART 3: spiral

Np_s = 100
tmax_s = 4.0

t_s = np.linspace(0, tmax_s, Np_s)

# x1s = (cx + R) - R/tmax_s * t_s    # start at  cx + R*np.sin(0.5*PI) = cx + R  and  we need to go to  cx
# y1s = [cy] * Np_s  # TODO
# z1s = [cz] * Np_s  # TODO

# PI/2 because we'll only do half a sphere
theta = np.linspace(0, PI/2, Np_s)

c = 16  # see wiki

x1s = cx + R * np.cos(theta)
y1s = cy + R * np.sin(theta) * np.cos(c * theta)
z1s = cz + R * np.sin(theta) * np.sin(c * theta)

# wikipedia -- Spiral/Spherical_spirals

x2s = cx - R * np.cos(theta)
y2s = cy + R * np.sin(theta) * np.cos(c * theta)
z2s = cz + R * np.sin(theta) * np.sin(c * theta)


# ADD PARTS TOGETHER

x1 = np.concatenate((x1d, x1a, x1s))
y1 = np.concatenate((y1d, y1a, y1s))  # list(np.concatenate( (y1d, y1a) )
z1 = np.concatenate((z1d, z1a, z1s))  # np.concatenate( (z1d, z1a) )

x2 = np.concatenate((x2d, x2a, x2s))
y2 = np.concatenate((y2d, y2a, y2s))
z2 = np.concatenate((z2d, z2a, z2s))


point1, = ax.plot([x1[0]], [y1[0]], [z1[0]], 'ro')
line1, = ax.plot(x1, y1, z1, label='parametric curve')

point2, = ax.plot([x2[0]], [y2[0]], [z2[0]], 'bo')
line2, = ax.plot(x2, y2, z2, label='parametric curve')


def update_points(n):  # , x, y, z, point):
    point1.set_data(np.array([x1[n], y1[n]]))
    point1.set_3d_properties(z1[n], 'z')

    point2.set_data(np.array([x2[n], y2[n]]))
    point2.set_3d_properties(z2[n], 'z')

    return (point1, point2)


# =========================================
# create the parametric curve
# t = np.arange(0, 2*np.pi, 2*np.pi/100)  # list points
# p1 = 4 * np.cos(t)  # list of all x so cos(t) at all times
# q1 = 4 * np.sin(t)
# r1 = t/(2.*np.pi)

# p = point1

# point, = ax.plot([x[0]], [y[0]], [z[0]], 'o')
# line, = ax.plot(x, y, z, label='parametric curve')


# def update_point(n, x, y, z, point):
#     point.set_data(np.array([x[n], y[n]]))
#     point.set_3d_properties(z[n], 'z')
#     return point


# =========================================

Nmax = Np_d + Np_a + Np_s

ani1 = animation.FuncAnimation(
    fig, update_points, Nmax)  # , fargs=(x1, y1, z1, point1))

# ani2 = animation.FuncAnimation(
#    fig, update_point, 99, fargs=(x2, y2, z2, point2))


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
# file1.close()
# file2.close()


# --------------------------------------------------------------
