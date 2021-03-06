import numpy as np
from typing import Callable


def boltzmann_step(k: int):
    return 1 / np.log(1 + k)


def hyperbolic_step(k: int):
    return 1 / k


def constant_step(k: int):
    return 1


def square_step(k: int):
    return k**2


def paired_sample_method(function: Callable, dim: int, initial_vec: np.ndarray, work_step_initial: float,
                         test_step_initial: float, work_step: Callable, test_step: Callable, iteration_count: int,
                         descent: np.ndarray = None, test_descent: np.ndarray = None):
    x = initial_vec.copy()
    if descent is not None:
        descent[0] = x
    for i in range(1, iteration_count):
        direction = np.random.uniform(-1, 1, dim)
        direction /= np.linalg.norm(direction, 2)
        t_step = test_step_initial*test_step(i)
        x1, x2 = x - t_step * direction, x + t_step * direction
        if test_descent is not None:
            test_descent[i-1][0] = x1
            test_descent[i-1][1] = x2
        x = x + work_step_initial * work_step(i) * direction * np.sign(function(x1) - function(x2))
        if descent is not None:
            descent[i] = x
    return x
