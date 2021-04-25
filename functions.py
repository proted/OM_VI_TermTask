import numpy as np


def function1(vec: np.ndarray):
    first_coords_sum = 0
    for i in range(0, len(vec) - 1):
        first_coords_sum += vec[i] ** 2
    nominator = np.sin(first_coords_sum - np.pi / 2) + np.log(1 + vec[len(vec) - 1] ** 2)
    denominator = 1 + first_coords_sum + vec[len(vec) - 1] ** 2
    function_value = nominator / denominator
    return function_value


def function2(vec: np.ndarray):
    coords_sum = 0
    for i in range(0, len(vec)):
        coords_sum += vec[i] ** 2
    nominator = np.sin(coords_sum - np.pi / 2)
    denominator = 1 + coords_sum
    function_value = nominator / denominator
    return function_value


def function3(vec: np.ndarray):
    coords_sum = 0
    for i in range(0, len(vec)):
        coords_sum += vec[i] ** 2
    nominator = np.log(1 + coords_sum) - 1
    denominator = 1 + coords_sum
    function_value = nominator / denominator
    return function_value


def function4(vec: np.ndarray):
    coords_sum = 0
    for i in range(0, len(vec)):
        coords_sum += vec[i] ** 2
    function_value = - 1 / (1 + coords_sum)
    return function_value


def function5(vec: np.ndarray):
    f_value = 0.0
    shifts = np.ndarray((10,), buffer=np.array([1.0, 4.0, -12.9, -0.33334, 7.8, 1.0, 0.1, 4, -11, 6.8]))
    for i in range(len(vec)):
        f_value += (vec[i] - shifts[i]) ** 2
    return f_value
