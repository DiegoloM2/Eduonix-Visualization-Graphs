from die import Die
import matplotlib.pyplot as plt
from random import randint
die = Die()

results = []
for j in range(1000):
    results.append(die.roll())
frequencies = [results.count(i) for i in range(1, die.num_sides)]#this is not necessary when using
                                                    #matplotlib as count is calculated automatically
x = list(range(1, 7))

plt.hist(results,bins = x,edgecolor = 'black',rwidth = 10)
plt.xlabel("Result")
plt.ylabel("Num of appearances")
plt.show()
