VecStart_x = [0,1,3,5]
VecStart_y = [2,2,5,5]
VecStart_z = [0,1,1,5]
VecEnd_x = [1,2,-1,6]
VecEnd_y = [3,1,-2,7]
VecEnd_z  =[1,0,4,9]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#taking k as 1 and -1
d="abc"
ax.plot(1,2,3,label='Given Point',marker = 'o')


ax.plot([-2, 4], # x
        [0, 4], # y
        [5, 1],label="Output Line") # z
ax.plot([0, 3], # x
        [0, 2], # y
        [0, -2],label="Given Line") # z
ax.legend()
plt.show()
Axes3D.plot()