from random import choice

class RandomWalk():
    """A class to generate random walks"""
    def __init__(self, num_points = 5000):
        """Initialize attributes of a walk"""

        self.num_points = num_points

        #All walks start at 0,0
        self.x_values = [0]
        self.y_values = [0]
        self.vals = [[0,0]]
    def fill_walk(self):
        """Calculate all the steps in the walk"""

        #Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()
            #Reject moves that go nowhere:
            if y_step == 0 and x_step == 0:
                continue
            #calculate the next x and y values:
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
    def get_step(self):
        """Decide what direction to go and how far to go in that direction"""
        x_direction = choice([1, -1])
        x_distance = choice([0,1,2,3,4])
        x_step = x_direction * x_distance

        y_direction = choice([1,-1])
        y_distance = choice(list(range(5)))
        y_step = y_direction * y_distance
        return x_step, y_step

    def fill_pygal(self):
        """Calculate steps for pygal"""
        while len(self.vals) < int(self.num_points/2):
            x_step, y_step = self.get_step()
            if y_step == 0 and x_step == 0:
                continue
            next_x = self.vals[-1][0] + x_step
            next_y = self.vals[-1][1] + y_step

            self.vals.append([next_x, next_y])