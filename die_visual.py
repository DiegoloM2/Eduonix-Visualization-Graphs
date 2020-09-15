import pygal
from die import Die

#Create 2 Dice:

die_1 = Die(8)
die_2 = Die(8)

#Make some rolls and store the results in a list:
results = []
for i in range(200000):
    results.append(die_1.roll() + die_2.roll())

#Analyze the results:

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequencies.append(results.count(value))

hist = pygal.Bar()
hist.title = "Results of Rolling 2 D8s many times"

hist.x_labels = map(lambda x: str(x),list(range(2,13)))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("2 D8s", frequencies)

hist.render_to_file("d8s_visual.svg")
