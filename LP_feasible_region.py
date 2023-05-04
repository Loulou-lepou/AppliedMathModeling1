# LP prob: f = # fruit cakes, c = # chocolate cakes
# maximise P = 3.5 * f + 5 * c
# s.t:   f + 2c <= 36, f + c <= 28, 2f + 3c <= 60, f, c >= 0

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker  # add grid on minor tick marks


def plot_constraints(x, y1, y2, y3):
    plt.plot(x, y1, label=r'$f + 2c = 36$')
    plt.plot(x, y2, label=r'$f + c = 28$')
    plt.plot(x, y3, label=r'$2f + 3c = 60$')
    plt.fill_between(x,
                     np.minimum(np.minimum(y1, y2), y3),
                     color='gray', alpha=0.5)


# set running configuration parameters to render Latex
plt.rcParams['text.usetex'] = True

c = np.linspace(0, 36, 1000)
f1 = 36 - 2 * c
f2 = 28 - c
f3 = (60 - 3 * c) / 2
# visualize linear constraints
plot_constraints(c, f1, f2, f3)

# Plot lattice points
lattice_points = []
# 0 <= c, f <= 28
for i in range(29):
    for j in range(37):
        if 2 * i + j <= 36 and i + j <= 28 and 3 * i + 2 * j <= 60:
            lattice_points.append((i, j))
            plt.scatter(i, j,
                        color='red', marker='o',
                        s=10, edgecolors='black')

plt.xticks(np.arange(0, 37, 4))
plt.yticks(np.arange(0, 37, 4))
plt.gca().set_aspect('equal', adjustable='box')

# Objective function line
z = 100  # Arbitrary revenue value for plotting
y_obj = (z - 3.5 * c) / 5
plt.plot(c, y_obj,
         'k--',
         label=r'Objective function $3.5x + 5y = Z$')
plt.arrow(10, 5, 2, 1,
          head_width=0.5, head_length=0.5,
          color='green', linestyle='--',
          label='Increasing direction')
# corners
corners = [(0, 0), (0, 18), (12, 12), (20, 0)]
optimal_solution = (12, 12)
plt.scatter(12, 12,
            color='red', marker='*', s=100,
            edgecolors='black',
            label='Optimal solution (12, 12)')
# Set minor ticks and grid
ax = plt.gca()
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.grid(which='minor', linestyle=':', linewidth=0.5)

plt.xlim(-0.2, 37)
plt.ylim(-0.2, 37)
plt.xlabel('Chocolate cakes (c)')
plt.ylabel('Fruit cakes (f)')
plt.title(f'Feasible Region ({len(lattice_points)} lattice Points)')
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()
