import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def plot_descent_paired_sample(x_min, x_max, y_min, y_max, step, func, descent_x, descent_y, descent_z, test1, test2,
                               contours, flag):
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
    title = f'Текущее приближение = {descent_x[descent_x.size - 1], descent_y[descent_y.size - 1]}\n'
    if flag:
        title += f'Значение функции в красном пробном шаге = {func(test1)}\n' \
                 f'Значение функции в оранжевом пробном шаге = {func(test2)}'
    ax.set_title(title)
    plt.savefig(f'../../Documents/MetOpt/termtask/showcase_pair_samples/pic{len(descent_x)}.pmg', format='png')
    plt.show()
