from random_walk import RandomWalk
import matplotlib.pyplot as plt

rw = RandomWalk()
rw.fill_walk()

plt.plot(rw.x_values, rw.y_values, linewidth = 0.5, color = 'black')
plt.scatter(0,0, c = 'red', s = 30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'green', s = 30)
plt.show()
