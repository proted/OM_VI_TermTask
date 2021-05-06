import os

from simulated_annealing import boltzmann_annealing
from paired_sample import *
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import glob
import moviepy.editor as mpy
from descent_plot import plot_descent_paired_sample, plot_descent_boltzmann_annealing


def hist_mean(data: np.ndarray):
    (n, bins, patches) = plt.hist(data, bins=100)
    n_copy = n.copy()
    n_copy.sort()
    n_copy = np.flip(n_copy)
    top_count_values = n_copy[0: 3]
    top_value_values = list()
    sum_n = 0
    for i in top_count_values:
        index_in_n = list(n).index(i)
        sum_n += n[index_in_n]
        val = list(bins)[index_in_n] * n[index_in_n]
        top_value_values.append(val)
    return np.array(top_value_values).mean() / sum_n


def do_accuracy_distribution_research():
    pass


def do_avg_dist_to_sln_against_iter_count_research():
    exact_solution_for_1_4 = np.array([0, 0])
    exact_solution_for_5 = np.array([1, 1, 1, 1, 1])
    x_value = range(1, 200)
    y_value = list()
    for iteration_count in x_value:
        one_step_data = list()
        for experiment in range(1, 300):
            solution = boltzmann_annealing(5, function5, 1, iteration_count)
            distance = np.linalg.norm(solution - exact_solution_for_5)
            # if not distance > 10:
            #    one_step_data.append(distance)
            one_step_data.append(distance)
        y_value.append(hist_mean(one_step_data))
    ax = plt.figure().add_subplot()
    # ax.set_yscale('log')
    # ax.set_xscale('log')
    ax.plot(x_value, y_value)
    plt.show()


if __name__ == '__main__':
    dim = 2
    iterations = 10
    func = function1
    xy = np.ndarray((iterations, dim))
    xy_test = np.ndarray((iterations, dim))
    temp = np.ndarray((iterations,))
    init = np.array([-1.7, -0.6])
    boltzmann_annealing(2, func, 0.5, iterations, init, xy, temp, xy_test)
    x = xy[:, 0]
    y = xy[:, 1]
    z = x.copy()
    for i in range(len(x)):
        z[i] = func(np.array([x[i], y[i]]))
    for i in range(iterations):
        f = True
        if i == iterations - 1:
            f = False
        plot_descent_boltzmann_annealing(-3, 0.5, -2, 0.5, 0.01, func, x[:i + 1], y[:i + 1], z[:i + 1], xy_test[i],
                                         temp[i], 35, f)
    gif_name = 'b'
    fps = 0.33
    file_list = sorted(glob.glob('../../Documents/MetOpt/termtask/showcase_boltzmann/*'), key=os.path.getmtime)
    clip = mpy.ImageSequenceClip(file_list, fps=fps)
    clip.write_gif('../../Documents/MetOpt/termtask/{}.gif'.format(gif_name), fps=fps)

# dim = 2
# iterations = 10
# func = function1
# xy = np.ndarray((iterations, dim))
# xy_test = np.ndarray((iterations, 2, dim))
# init = np.array([-1.7, -0.6])
# paired_sample_method(func, dim, init, 0.25, 0.25, boltzmann_step, boltzmann_step, iterations, xy, xy_test)
# x = xy[:, 0]
# y = xy[:, 1]
# z = x.copy()
# for i in range(len(x)):
#     z[i] = func(np.array([x[i], y[i]]))
# for i in range(iterations):
#     f = True
#     if i == iterations - 1:
#         f = False
#     plot_descent_paired_sample(-3, 0.5, -2, 0.5, 0.01, func, x[:i + 1], y[:i + 1], z[:i + 1], xy_test[i][0],
#                                xy_test[i][1], 35, f)
# gif_name = 'ps'
# fps = 0.33
# file_list = sorted(glob.glob('../../Documents/MetOpt/termtask/showcase_pair_samples/*'), key=os.path.getmtime)
# clip = mpy.ImageSequenceClip(file_list, fps=fps)
# clip.write_gif('../../Documents/MetOpt/termtask/{}.gif'.format(gif_name), fps=fps)

# data = list()
# exact_solution = np.array([1, 1, 1, 1, 1])
# for i in range(0, 1000):
#   solution = boltzmann_annealing(5, function5, 0.5, 400)
#   solution = paired_sample_method(function5, 5, 1, 3, boltzmann_step, boltzmann_step, 1000)
#    data.append(np.linalg.norm(solution - exact_solution))

# bins=[7 + i*0.01 for i in range(0, 500)]
# plt.hist(data, bins=50)
# plt.show()

# a = array.array('f', [1, 2, 3, 4])
# print(a)
# with open("data.bin", "wb") as f:
#     a.tofile(f)
# f.close()
# b = array.array('f')
# with open("data.bin", "rb") as f:
#     b.fromfile(f, 4)
# f.close()
# print(b)


# def do_avg_dist_to_sln_against_iter_count_research1():
#     exact_solution_for_1_4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     x_value = range(30, 300, 10)
#     y_value = list()
#     for iteration_count in x_value:
#         one_step_data = list()
#         for experiment in range(1, 1000):
#             init = np.random.normal(0, 1, 10)
#             solution = paired_sample_method(function1, 10, init, 0.5, 0.5, boltzmann_step, boltzmann_step,
#                                             iteration_count)
#             distance = np.linalg.norm(solution - exact_solution_for_1_4)
#             # if not distance > 10:
#             #    one_step_data.append(distance)
#             one_step_data.append(distance)
#         y_value.append(hist_mean(one_step_data))
#     ax = plt.figure().add_subplot()
#     ax.plot(x_value, y_value)
#     ax.set_ylabel('Усредненённое расстояние до экстремума')
#     ax.set_xlabel('Количество итераций')
#     plt.show()
# 
# 
# def do_avg_dist_to_sln_against_iter_count_research3():
#     exact_solution_for_1_4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     x_value = range(30, 300, 10)
#     y_value = list()
#     for iteration_count in x_value:
#         one_step_data = list()
#         for experiment in range(1, 1000):
#             init = np.random.normal(0, 1, 10)
#             solution = paired_sample_method(function3, 10, init, 0.25, 0.25, boltzmann_step, boltzmann_step,
#                                             iteration_count)
#             distance = np.linalg.norm(solution - exact_solution_for_1_4)
#             # if not distance > 10:
#             #    one_step_data.append(distance)
#             one_step_data.append(distance)
#         y_value.append(hist_mean(one_step_data))
#     ax = plt.figure().add_subplot()
#     ax.plot(x_value, y_value)
#     ax.set_ylabel('Усредненённое расстояние до экстремума')
#     ax.set_xlabel('Количество итераций')
#     plt.show()
# 
# 
# def do_avg_dist_to_sln_against_iter_count_research4():
#     exact_solution_for_1_4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     x_value = range(30, 300, 10)
#     y_value = list()
#     for iteration_count in x_value:
#         one_step_data = list()
#         for experiment in range(1, 1000):
#             init = np.random.normal(0, 1, 10)
#             solution = paired_sample_method(function4, 10, init, 0.25, 0.25, boltzmann_step, boltzmann_step,
#                                             iteration_count)
#             distance = np.linalg.norm(solution - exact_solution_for_1_4)
#             # if not distance > 10:
#             #    one_step_data.append(distance)
#             one_step_data.append(distance)
#         y_value.append(hist_mean(one_step_data))
#     ax = plt.figure().add_subplot()
#     ax.plot(x_value, y_value)
#     ax.set_ylabel('Усредненённое расстояние до экстремума')
#     ax.set_xlabel('Количество итераций')
#     plt.show()
# 
# 
# def do_relative_frequency_against_iter_count_research4_3():
#     exact_solution_for_1_4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     accuracy = [1e0, 1e-1]
#     x_value = range(30, 300, 10)
#     y_value = list()
#     for k in range(2):
#         for iteration_count in x_value:
#             count = 0
#             for experiment in range(1, 1000):
#                 init = np.random.normal(0, 1, 10)
#                 solution = paired_sample_method(function4, 10, init, 0.25, 0.25, boltzmann_step, boltzmann_step,
#                                                 iteration_count)
#                 distance = np.linalg.norm(solution - exact_solution_for_1_4)
#                 if distance <= accuracy[k]:
#                     count += 1
#             y_value.append(count / 1000)
#         ax = plt.figure().add_subplot()
#         ax.plot(x_value, y_value)
#         ax.set_ylabel(f'Относительная частота получения точности eps = {accuracy[k]}')
#         ax.set_xlabel('Количество итераций')
#         plt.show()
# 
# 
# def do_relative_frequency_against_iter_count_research1():
#     exact_solution_for_1_4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     accuracy = [1e0, 1e-1]
#     x_value = range(30, 1500, 50)
#     y_value = list()
#     for iteration_count in x_value:
#         count = 0
#         for experiment in range(1, 1000):
#             init = np.random.normal(0, 1, 10)
#             solution = paired_sample_method(function1, 10, init, 0.5, 0.5, boltzmann_step, boltzmann_step,
#                                             iteration_count)
#             distance = np.linalg.norm(solution - exact_solution_for_1_4)
#             if distance <= accuracy[0]:
#                 count += 1
#         y_value.append(count / 1000)
#     ax = plt.figure().add_subplot()
#     ax.plot(x_value, y_value)
#     ax.set_ylabel(f'Относительная частота получения точности eps = {accuracy[0]}')
#     ax.set_xlabel('Количество итераций')
#     plt.show()
# 
# 
# def do_accuracy_distribution_research():
#     iterations = [1000, 2000, 4000, 7500]
#     funcs = [function1, function3, function4]
#     exact_solution = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     for f in funcs:
#         data = [list() for _ in range(len(iterations))]
#         for i in range(len(iterations)):
#             for _ in range(2500):
#                 init = np.random.normal(0, 1, 10)
#                 solution = paired_sample_method(f, 10, init, 0.25, 0.25, boltzmann_step, boltzmann_step,
#                                                 iterations[i])
#                 data[i].append(np.linalg.norm(solution - exact_solution))
#             plt.hist(data[i], bins=100)
#             plt.xlabel('Расстояние до глобального минимума')
#             plt.ylabel('Число экспериментов с достигнутым расстоянием')
#             plt.title(f'Распределение расстояний, число итераций = {iterations[i]}')
#             plt.show()
