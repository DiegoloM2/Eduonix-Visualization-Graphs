from die import Die
import pygal
#Create a D6:
die = Die()

#Make some rolls and store them in a list:

results = []
frequencies = []
for roll_num in range(100):
    results.append(die.roll())
for value in range(1,7):
    frequencies.append(results.count(value))

#Visualize the results:
hist = pygal.Bar()#Make a bar chart

hist.title = "Results of rolling one D6 100 times"

hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_label = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')#Render a chart to an svg file.
