# Numerical Integration > definite integrals
# https://personal.math.ubc.ca/~pwalls/math-python/integration/riemann-sums/

import matplotlib.pyplot as plt
import numpy as np    # used np.pi, np.linspace
# from PIL import Image    # open images to compare


# to render math equations using TeX
plt.rcParams['text.usetex'] = True


# continuous function f on [a, b]
def f(x):
    return np.sin(0.2*x) + np.sin(2 * x) + 1


if __name__ == '__main__':
    # open fig 1 to compare
    # im = Image.open('integrals_1_0.png')
    # im.show()

    # PARAMETERS
    a1 = 0
    b1 = 2 * np.pi
    a2 = np.pi / 2
    b2 = 3 * np.pi / 2
    # Partition of [a, b] with n sub-intervals
    n = 100

    # 1. Plot line graph y = f(x) over [a1, b1]
    # (n + 1) equally distributed grid pts {x_i}, x_0 = a1 <=... <= x_i <=...<= x_n = b
    # x_i = a1 + i * (b1 - a1) / n
    x1 = np.linspace(a1, b1, n)
    # corresponding values y_i = f(x_i)
    y1 = f(x1)
    # line graph y = f(x) on [a1, b1]
    plt.plot(x1, y1, 'g')   # line color = green ('g')
    plt.xlim([a1, b1])
    plt.ylim([min(y1) - 0.2, max(y1) + 0.2])
    # slow evaluation min/max of function f

    # 2. plot (net) area of y = f(x) on narrower interval [a2, b2]
    x2 = np.linspace(a2, b2, n)
    y2 = f(x2)
    plt.fill_between(x2, y2)
    # x tick marks at a2, b2
    plt.xticks([a2, b2],
               [r"$ \displaystyle a = \frac{\pi}{2} $",
                r'$ \displaystyle b = \frac{3 \pi}{2} $'],
               fontsize=14)
    plt.yticks([])
    plt.title(r'$\displaystyle y = \sin(0.2x) + \sin(2  x) + 1 $',
              fontsize=18,
              pad=16)
    plt.show()
