import pygal
wm = pygal.maps.world.World()

wm.title = "Population of countries in North America."

#Pygal will automatically use the inputted numbers to shade the countries from light
#(less populated) to dark (more populated)
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
