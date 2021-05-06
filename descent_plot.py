import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# if __name__ == '__main__':
#     dim = 2
#     iterations = 7
#     func = function1
#     xy = np.ndarray((iterations, dim))
#     xy_test = np.ndarray((iterations, 2, dim))
#     init = np.array([-1.7, -0.6])
#     paired_sample_method(func, dim, init, 0.25, 0.25, boltzmann_step, boltzmann_step, iterations, xy, xy_test)
#     x = xy[:, 0]
#     y = xy[:, 1]
#     z = x.copy()
#     for i in range(len(x)):
#         z[i] = func(np.array([x[i], y[i]]))
#     for i in range(iterations):
#         f = True
#         if i == iterations - 1:
#             f = False
#         plot_descent(-3, 0, -2, 0.5, 0.01, func, x[:i+1], y[:i+1], z[:i+1], xy_test[i][0], xy_test[i][1], 35, f)


def plot_descent(x_min, x_max, y_min, y_max, step, func, descent_x, descent_y, descent_z, test1, test2, contours, flag):
    x = np.arange(x_min, x_max, step)
    y = np.arange(y_min, y_max, step)
    z = np.ndarray((len(y), len(x)))
    for i in range(len(y)):
        for j in range(len(x)):
            z[i][j] = func(np.array([x[j], y[i]]))
    x, y = np.meshgrid(x, y)
    fig = plt.figure(figsize=(15, 15), dpi=120)
    ax = fig.add_subplot(projection='3d')
    ax.plot(descent_x, descent_y, descent_z, color='black', linewidth=2)
    if flag:
        ax.plot(np.array([descent_x[descent_x.size - 1], test1[0]]),
                np.array([descent_y[descent_y.size - 1], test1[1]]),
                np.array([descent_z[descent_z.size - 1], func(test1)]), color='red', linewidth=2)
        ax.plot(np.array([descent_x[descent_x.size - 1], test2[0]]),
                np.array([descent_y[descent_y.size - 1], test2[1]]),
                np.array([descent_z[descent_z.size - 1], func(test2)]), color='orange', linewidth=2)
    surf = ax.contour(x, y, z, contours, cmap=cm.coolwarm, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.view_init(elev=35., azim=100.)
    plt.show()
