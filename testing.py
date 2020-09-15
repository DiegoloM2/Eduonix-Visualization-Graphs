import matplotlib.pyplot as plt

squares = [0,1,4,9,16,25,36]
inp = [0,1,2,3,4,5,6]
plt.plot(inp,squares, linewidth = 4)#

#Set chart title and label axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Squared Value", fontsize = 14)

#Set size of tick labels:
plt.tick_params(axis = 'both', labelsize = 14)

#Open the viewer and display the plot
plt.show()
