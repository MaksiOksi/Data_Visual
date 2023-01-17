import matplotlib.pyplot as plt

x_value = range(1, 5001)
y_value = [x**3 for x in x_value]

fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, s=15)

plt.show()
