from plotly.graph_objs import Bar, Layout
from plotly import offline

from gambling_cube import GamblingCube

# Create GC6
gamb_cube = GamblingCube()

# Make a throw
results = []
for roll_num in range(1000):
    result = gamb_cube.roll()
    results.append(result)

# Analyze
frequencies = []
for value in range(1, gamb_cube.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization of results
x_values = list(range(1, gamb_cube.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results pf rolling GC6 1000 times',
                   xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='gc6.html')