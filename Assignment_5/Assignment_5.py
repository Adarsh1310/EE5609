import matplotlib.pyplot as plt
import math

circle1 = plt.Circle((0, 0), 2,fill=False)
circle2 = plt.Circle((2, 0), 2,fill=False,color='b')

fig, ax = plt.subplots()

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.scatter(1,math.sqrt(3))
plt.scatter(1,-math.sqrt(3))


plt.annotate("A", (1,math.sqrt(3)))
plt.annotate("B", (1,-math.sqrt(3)))
plt.annotate("C", (1,0))
plt.annotate("D", (0,0))
plt.annotate("E", (2,0))
x1 = [0, 1]
y1 = [0, math.sqrt(3)]
x2 = [1,2]
y2 = [math.sqrt(3),0]
x3=[0,2]
y3=[0,0]
x4=[1,1]
y4=[-math.sqrt(3),math.sqrt(3)]
plt.plot(x1, y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)

ax.set_aspect(1)

ax.add_artist(circle1)
ax.add_artist(circle2)



plt.savefig("plot_circle_matplotlib_02.png", bbox_inches='tight')

plt.show()