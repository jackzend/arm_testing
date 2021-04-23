import numpy as np
from itertools import product
from sklearn.neighbors import KDTree
import pickle

data = {}
dynamixel_range = 300.0
gear_ratio = 1
l_1 = 10.81
l_2 = 10.31
x_offset = 0
y_offset = 0
#
theta_prime_1 = np.deg2rad(-111.14)
theta_prime_2 = np.deg2rad(237.35)

def f_with_theta(s):
    theta_1 = ((1023.0-s[:,1])/1023.0) * np.deg2rad(dynamixel_range / gear_ratio) + theta_prime_1
    theta_2 = theta_prime_2 - ((1023.0-s[:,0])/1023.0) * np.deg2rad(dynamixel_range / gear_ratio)
    x = np.sin(theta_1) * l_1 + np.sin(theta_1 + theta_2) * l_2
    z = np.cos(theta_1) * l_1 + np.cos(theta_1 + theta_2) * l_2
    #ret = np.array([x, y]).T
    return np.array([x, z]).T

srange = np.array(list(product(range(1024), range(1024))))

pts = f_with_theta(srange)

tree = KDTree(pts, metric='euclidean')

def g(pts):
    return np.array(srange[tree.query(pts, return_distance=False)]).reshape(-1, 2)

print(g((17.3739,0.3801))) ## spits out elbow shoulder

path = 'arm_movement_engine_pts.npy'
np.save(path, pts)

with open('arm_movement_engine.kdtree', 'wb') as f:
    pickle.dump(tree, f)

print("sdjfhsfj") # subtract the x add the z
