import pygal


#Make an instance of the Worldmap class.
wm = pygal.maps.world.World()#mK
wm.title = 'North, Central, and South America'

#'wm.add' Takes in a label and a list of countries which we want to focus on.
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America',['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file ('americas.svg')
