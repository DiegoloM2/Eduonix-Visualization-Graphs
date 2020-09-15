import matplotlib.pyplot as plt
from random import randint
x = [12,3,5,6,22,4]
y = [13,23,5,35,9,8]
x1 = list(range(1,7))
y1 = [i**2 for i in x1 ]
#scatter the x values against the y values.
plt.scatter(x, y, s = 10, color = 'red')#'s' sets the size of the data points.

#adding more data points to the scatter plot.
plt.scatter(x1, y1, s = 20, color = 'blue')
#Adding a curve to the scatter plot
plt.plot(x1, y1, linewidth = 0.5, c = (0.5,0.6,0.8))
#Note that 'c' is the color which we set the curve to be
#Also note that it only inputs values of a range from 0 to 1.

#Create a color which assigns a color based on a data point's y-value.
x2 = list(range(1, 20))
y2 = [randint(1, i) for i in x2]
plt.scatter(x2, y2, c = y2, cmap = plt.cm.Blues)


#Set chart title and label the axes:
plt.title("Scatter")
plt.xlabel("X")
plt.ylabel("Y")


#Set the range for each axis:
plt.axis([0,22,0,36])
plt.tick_params(axis = 'both', labelsize = 10 )

#Save your plot in a png file.
plt.savefig('scatter.png', bbox_inches = 'tight')

plt.show()
