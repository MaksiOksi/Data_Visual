import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=15)

# Set the name of the graph and for each axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)

# Set the axis range
ax.axis([0, 1100, 0, 1100000])

# Set font size for types and captions
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('square_plot.png', bbox_inches='tight')

