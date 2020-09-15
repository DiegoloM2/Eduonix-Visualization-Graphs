import matplotlib.pyplot as plt
import time
x = list(range(5000))
y = list(map(lambda x: x**3, x))

plt.scatter(x, y, c = y, cmap = plt.cm.Reds)
plt.show()
