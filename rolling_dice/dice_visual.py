from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create 2 x D6 dice
die_1 = Die()
die_2 = Die()

# Make some rolls, and store the results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides 
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result','dtick':1}
y_axis_config = {'title':'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 dice', 
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')