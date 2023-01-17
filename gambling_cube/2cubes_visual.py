from plotly.graph_objs import Bar, Layout
from plotly import offline

from gambling_cube import GamblingCube

# Create GC6
gamb_cube_1 = GamblingCube()
gamb_cube_2 = GamblingCube()

# Make a throw
results = []
for roll_num in range(5000):
    result = gamb_cube_2.roll() + gamb_cube_1.roll()
    results.append(result)

# Analyze
frequencies = []
max_result = gamb_cube_1.num_sides + gamb_cube_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization of results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results pf rolling 2 gc6 5000 times',
                   xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='gc2x6.html')