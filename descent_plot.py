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
    ax.view_init(elev=15., azim=100.)
    title = f'Текущее приближение = ({descent_x[descent_x.size - 1]:.5f}, {descent_y[descent_y.size - 1]:.5f})\n'
    if flag:
        title += f'Значение функции в красном пробном шаге = {func(test1):.5f}\n' \
                 f'Значение функции в оранжевом пробном шаге = {func(test2):.5f}'
    ax.set_title(title)
    plt.savefig(f'../../Documents/MetOpt/termtask/showcase_pair_samples/pic{len(descent_x)}.png', format='png')
    plt.show()


def plot_descent_boltzmann_annealing(x_min, x_max, y_min, y_max, step, func, descent_x, descent_y, descent_z, test,
                                     tempr, contours, flag):
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
        ax.plot(np.array([descent_x[descent_x.size - 1], test[0]]),
                np.array([descent_y[descent_y.size - 1], test[1]]),
                np.array([descent_z[descent_z.size - 1], func(test)]), color='red', linewidth=2)
    surf = ax.contour(x, y, z, contours, cmap=cm.coolwarm, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.view_init(elev=15., azim=100.)
    cur_energy = func(np.array([descent_x[descent_x.size - 1], descent_y[descent_y.size - 1]]))
    title = f'Текущее приближение = ({descent_x[descent_x.size - 1]:.5f}, {descent_y[descent_y.size - 1]:.5f})\n' \
            f'Текущее энергия = {cur_energy:.5f}\n' \
            f'Текущая температура = {tempr:.5f}\n'
    if flag:
        prob = np.exp(- (func(test) - cur_energy) / tempr)
        if prob >= 1:
            prob = 1.
        title += f'Энергия пробного шага = {func(test):.5f}\n' \
                 f'Вероятность перемещения в пробный шаг = {prob:.5f}'
    ax.set_title(title)
    plt.savefig(f'../../Documents/MetOpt/termtask/showcase_boltzmann/pic{len(descent_x)}.png', format='png')
    plt.show()
