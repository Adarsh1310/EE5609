import matplotlib.pyplot as plt
import math

circle1 = plt.Circle((0, 0), 2,fill=False)
circle2 = plt.Circle((2, 0), 2,fill=False,color='b')

fig, ax = plt.subplots()

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.scatter(1,math.sqrt(3))
plt.scatter(1,-math.sqrt(3))
plt.annotate("Point 1", (1,math.sqrt(3)))
plt.annotate("Point 2", (1,-math.sqrt(3)))


ax.set_aspect(1)

ax.add_artist(circle1)
ax.add_artist(circle2)



plt.savefig("plot_circle_matplotlib_02.png", bbox_inches='tight')

plt.show()