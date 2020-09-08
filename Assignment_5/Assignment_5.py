import matplotlib.pyplot as plt
import math
circle1 = plt.Circle((0, 0), math.sqrt(2),fill=False)
circle2 = plt.Circle((2, 0), 2,fill=False,color='b')
fig, ax = plt.subplots()
plt.xlim(-7,7)
plt.ylim(-7,7)
ax.add_artist(circle1)
ax.add_artist(circle2)
plt.show()