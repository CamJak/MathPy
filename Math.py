import numpy as np
import matplotlib.pyplot as plt


# set range of x and function of y
x = np.arange(0, 11, 0.5)
y = np.log(x)

# print generated values for x and y
print('Values of x: ', x)
print('Values of y: ', y)

# generate plot with given values
plt.plot(x, y)

# add labels to the plot
plt.title("Identity Function")
plt.xlabel("Values of x")
plt.ylabel("Values of y")

# add grid to plot and display
plt.grid()
plt.show()
