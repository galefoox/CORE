

from math import sin, cos, acos

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import time


# Fixing random state for reproducibility
np.random.seed(int(time.time()))
# look up random seed with none and how it works
# and time


# rules for R(phi,theta):
# - R cannot be less than zero
# - must be periodic in phi:  0.. 2*Pi   --  so  1+sin(n*phi + phase)  is ok
# - must be periodic in theta:  0..Pi  --  so   1+sin(2*n*theta + phase)  is good
# - if theta=0 or theta=PI then R should not depend on phi, otherwise you get sharp "axis" -- see e.g. 1+sin(phi).
#                       But  1+sin(phi)*sin(theta)  is fine, because it makes R=0 for theta=0,Pi!
def generate_R(theta, phi):
    # print number between 0 and 1
    # could do int(random * some integer)
    rnd1 = np.random.rand()
    rnd2 = np.random.rand()
    rnd3 = np.random.rand()
    rnd4 = np.random.rand()

    # return 1 + 1+sin(2*theta)*sin(2*phi) + 1+0.7*sin(phi)*sin(theta)**2;
    # return 1 + sin(phi)
    # try something that depends on theta
    asteroid1 = 1 + (sin(theta)*sin(phi) + 0.7*sin(phi)
                     * sin(3*theta)**2) + rnd4 * rnd3

    return asteroid1

# - gets a random R generated above (random because R depends on rand and rand depends on time)
# - also random because cos(theta), sin(theta), and phi are all randomly generated


# - Write each point to file
# - open file
file = open("asteroid_points.txt", "w")


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
    file.write("{0:10.3f} {1:10.3f} {2:10.3f}\n".format(x, y, z))

    return (x, y, z)


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)


# - generate 10,000 points
data = [get_random_point() for i in range(10000)]

# - close file
file.close()


# Setting the axes properties
ax.set_xlim3d([-5.0, 5.0])
ax.set_xlabel('X')

ax.set_ylim3d([-5.0, 5.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-5.0, 5.0])
ax.set_zlabel('Z')

ax.set_title('Asteroid or Potato?')

# Creating the Animation object
# line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
#                                   interval=50, blit=False)

# print(data)

xs = [data[i][0] for i in range(len(data))]
ys = [data[i][1] for i in range(len(data))]
zs = [data[i][2] for i in range(len(data))]
# ys = [data[1][:]
# zs = [data[2][:]

# print(xs)

# google scatter and see what options i have
ax.scatter(xs, ys, zs, marker='o', color='#6D6D64')


plt.show()
