import numpy as np


def function1(vec: np.ndarray):
    first_coords_sum = 0
    for i in range(0, len(vec) - 1):
        first_coords_sum += vec[i] ** 2
    nominator = np.sin(first_coords_sum - np.pi / 2) + np.log(1 + vec[len(vec) - 1] ** 2)
    denominator = 1 + first_coords_sum + vec[len(vec) - 1] ** 2
    return nominator / denominator


def function2(vec: np.ndarray):
    pass


def function3(vec: np.ndarray):
    pass
