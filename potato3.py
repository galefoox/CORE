
from math import sin, cos, acos

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import time
from mpl_toolkits.mplot3d import axes3d
from itertools import product, combinations

plt.style.use('dark_background')


# Fixing random state for reproducibility
np.random.seed(int(time.time()))
# This random seed will change based on time

# rules for R(phi,theta):
# - R cannot be less than zero
# - must be periodic in phi:  0.. 2*Pi   --  so  1+sin(n*phi + phase)  is ok
# - must be periodic in theta:  0..Pi  --  so   1+sin(2*n*theta + phase)  is good
# - if theta=0 or theta=PI then R should not depend on phi, otherwise you get sharp "axis" -- see e.g. 1+sin(phi).
#                       But  1+sin(phi)*sin(theta)  is fine, because it makes R=0 for theta=0,Pi!


def generate_R(theta, phi):
    # prints number between 0 and 1
    # could do int(random * some integer)
    rnd1 = np.random.rand()
    rnd2 = np.random.rand()
    rnd3 = np.random.rand()
    rnd4 = np.random.rand()

    # return 1 + 1+sin(2*theta)*sin(2*phi) + 1+0.7*sin(phi)*sin(theta)**2;
    # try something that depends on theta
    asteroid1 = 1 + rnd1*sin(theta)*sin(phi) + rnd2 * \
        sin(phi) * rnd3*sin(3*theta)**2 + rnd4

    return asteroid1


# - Write each point to file
# - open file
file1 = open("asteroid_points.txt", "w")
file2 = open("cube_points.txt", "r")

# - gets a random R generated above (random because R depends on rand and rand depends on time)
# - also random because cos(theta), sin(theta), and phi are all randomly generated


def get_random_point():

    PI = 3.1416

    cos_theta = 2*np.random.rand() - 1
    theta = acos(cos_theta)  # arccos
    sin_theta = sin(theta)

    phi = 2*PI*np.random.rand()
    cos_phi = cos(phi)
    sin_phi = sin(phi)

    R = generate_R(theta, phi)

    x = R * cos_phi * sin_theta
    y = R * sin_phi * sin_theta
    z = R * cos_theta

# - formatted print to file
    file1.write("{0:10.3f} {1:10.3f} {2:10.3f}\n".format(x, y, z))

    return (x, y, z)


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# - generate 10,000 points
data = [get_random_point() for i in range(10000)]


# Setting the axes properties
ax.set_xlim3d([-5.0, 5.0])
ax.set_xlabel('X')

ax.set_ylim3d([-5.0, 5.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-5.0, 5.0])
ax.set_zlabel('Z')

ax.set_title('Asteroid or Potato?')


xs = [data[i][0] for i in range(len(data))]
ys = [data[i][1] for i in range(len(data))]
zs = [data[i][2] for i in range(len(data))]


# THIS SCATTER PRINTS BLACK AND GREY DOTS
# visualization purposes: dramatic effect
# ax.scatter(xs, ys, zs, marker='.', color="black")
# ax.scatter(xs, ys, zs, marker='.', color='#6D6D64')

# THIS SCATTER PRINTS COLOR CODED DOTS (YELLOW FOR FARTHEST AWAY FROM THE CENTER)
ax.scatter(xs, ys, zs, c=np.linalg.norm([xs, ys, zs], axis=0))

# draw cube
# formula in email (-a,b,c) ...
# corners = [(-3, 4, 3), (3, 4, 3),  (-3, -4, 3), (3, -4, 3),
#            (-3, 4, -3), (3, 4, -3), (-3, -4, -3), (3, -4, -3)]
# x = [p[0] for p in corners]
# y = [p[1] for p in corners]
# z = [p[2] for p in corners]
# ax.scatter(x, y, z, color="r")


# blue blob for spacecraft ADD IMAGE LATER
x = 5
y = 5
z = 5
plt.plot(x, y, z, 'bo')

plt.show()
