
from mpl_toolkits.mplot3d import axes3d
from itertools import product, combinations
from math import sin, cos, acos

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import time
# ===============================CREATE ASTEROID=============================#

# Setting black background
plt.style.use('dark_background')


# This random seed will change based on time
np.random.seed(int(time.time()))
PI = 3.141159

# - Rules for R(phi,theta):
# - R cannot be less than zero
# - Must be periodic in phi:  0.. 2*Pi   --  so  1+sin(n*phi + phase)  is ok
# - Must be periodic in theta:  0..Pi  --  so   1+sin(2*n*theta + phase)  is good
# - If theta=0 or theta=PI then R should not depend on phi, otherwise you get sharp "axis" -- see e.g. 1+sin(phi).
# - But  1+sin(phi)*sin(theta)  is fine, because it makes R=0 for theta=0,Pi!


def generate_R(theta, phi):
    # prints number between 0 and 1
    # could do int(random * some integer)
    rnd1 = np.random.rand()
    rnd2 = np.random.rand()
    rnd3 = np.random.rand()
    rnd4 = np.random.rand()

    # Depends on theta
    asteroid1 = 1 + rnd1*sin(theta)*sin(phi) + rnd2 * \
        sin(phi) * rnd3*sin(3*theta)**2 + rnd4

    return asteroid1


# - Write each point to file
# - open file
file1 = open("asteroid_points.txt", "w")
file2 = open("cube_points.txt", "r")


# - Gets a random R generated above (random because R depends on rand and rand depends on time)
# - Also random because cos(theta), sin(theta), and phi are all randomly generated
def get_random_point():

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

# Formatted print to file
    file1.write("{0:10.3f} {1:10.3f} {2:10.3f}\n".format(x, y, z))
    return (x, y, z)


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)


# Generate 10,000 points
data = [get_random_point() for i in range(10000)]


# Setting the axes properties
ax.set_xlim3d([-6.0, 6.0])
ax.set_xlabel('X')

ax.set_ylim3d([-6.0, 6.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-6.0, 6.0])
ax.set_zlabel('Z')

ax.set_title('Asteroid or Potato?')

# =====================================DESIGN====================================
# Get rid of colored axes planes
# First remove fill
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Now set color to grey
ax.xaxis.pane.set_edgecolor('grey')
ax.yaxis.pane.set_edgecolor('grey')
ax.zaxis.pane.set_edgecolor('grey')

# To get rid of the grid as well:
ax.grid(False)
# =====================================DESIGN====================================

xs = [data[i][0] for i in range(len(data))]
ys = [data[i][1] for i in range(len(data))]
zs = [data[i][2] for i in range(len(data))]


# THIS SCATTER PRINTS BLACK AND GREY DOTS
# visualization purposes: dramatic effect
ax.scatter(xs, ys, zs, marker='.', color="black")
ax.scatter(xs, ys, zs, marker='.', color='#6D6D64')

# THIS SCATTER PRINTS COLOR CODED DOTS (YELLOW FOR FARTHEST AWAY FROM THE CENTER)
#ax.scatter(xs, ys, zs, c=np.linalg.norm([xs, ys, zs], axis=0))


# ===============================DRONE ENCAPSULATION=============================#
# Create the parametric curve
R = 5  # radius of sphere
cx = 0  # center of sphere
cy = 0
cz = 0


# 2 End points because 2 drones
px1, py1, pz1 = (cx+R, cy, cz)
px2, py2, pz2 = (cx-R, cy, cz)


# Distance space ship to asteroid
dist_spsh_ast = 0.5*R

# cz+R = Highest point of asteroid
spsh_z = dist_spsh_ast + (cz+R)

# PART 1: Going straight down from space ship  |  d = down

# Number of points for part 1
Np_d = 10
# Time needed for going down
tmax_d = 2.0

# 0..2  with "Np_d" points in total -> 10 points between 0 and 2
t_d = np.linspace(0, tmax_d, Np_d)

x1d = [cx] * Np_d
y1d = [cy] * Np_d
z1d = spsh_z - (dist_spsh_ast/tmax_d) * t_d
# Array of z values  -- t_d/tmax_d = array [0,1]   and   dist1/tmax_d * t_d = array [0,dist_spsh_ast]


# For two points lines
x2d = x1d
y2d = y1d
z2d = z1d


# PART 2: Arcs  |  a = arc

# Number of points for part 2
Np_a = 20

# Time needed for arc
tmax_a = 3.0
t_a = np.linspace(0, tmax_a, Np_a)

# Parametric equation of straight line in 3D
# Parametric equations are a set of equations that express a set of quantities as explicit functions of a number of independent variables, known as "parameters.

# An array of points dependent on time
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

# PI/2 because we'll only do half a sphere
theta = np.linspace(0, PI/2, Np_s)

# See wiki
c = 16

x1s = cx + R * np.cos(theta)
y1s = cy + R * np.sin(theta) * np.cos(c * theta)
z1s = cz + R * np.sin(theta) * np.sin(c * theta)

# wikipedia -- Spiral/Spherical_spirals

x2s = cx - R * np.cos(theta)
y2s = cy + R * np.sin(theta) * np.cos(c * theta)
z2s = cz + R * np.sin(theta) * np.sin(c * theta)


# ADD PARTS TOGETHER

x1 = np.concatenate((x1d, x1a, x1s))
y1 = np.concatenate((y1d, y1a, y1s))
z1 = np.concatenate((z1d, z1a, z1s))

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


Nmax = Np_d + Np_a + Np_s

ani1 = animation.FuncAnimation(
    fig, update_points, Nmax)


plt.show()

# Close file
file1.close()
file2.close()
