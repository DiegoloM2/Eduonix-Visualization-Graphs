from random_walk import RandomWalk
import pygal

#Create the random walk.

rw = RandomWalk()
rw.fill_pygal()
scat = pygal.XY()
scat.title = "Random Walk"
scat.add('Values',rw.vals)
scat.add('Start', rw.vals[0])
scat.add('End', rw.vals[-1])
scat.xtitle = "X"
scat.ylabel = "Y"
scat.render_to_file("rw_wpygal.svg")
