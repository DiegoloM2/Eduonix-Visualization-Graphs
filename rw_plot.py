from random_walk import RandomWalk
import matplotlib.pyplot as plt
while True:

    rw = RandomWalk(10000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))

    #Set the size of the plotting window
    plt.figure(figsize=(10,6))

    #Create a cmap which gives color according to the index of the data point in the list.
    plt.scatter(rw.x_values, rw.y_values, s = 10, c = point_numbers,
    cmap = plt.cm.Reds)

    #Emphasize the first and last points:
    plt.scatter(0,0,c = 'green', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'yellow', s = 100)

    #Remove the axes:
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n)")

    if keep_running == 'n':
        break
