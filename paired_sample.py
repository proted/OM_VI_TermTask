import numpy as np
from typing import Callable


def boltzmann_step(k: int):
    return 1 / np.log(2 + k)


def hyperbolic_step(k: int):
    return 1 / k


def constant_step(k: int):
    return 1


def paired_sample_method(function: Callable, dim: int, work_step: Callable, test_step: Callable, iteration_count: int):
    x = np.random.normal(0, 100, dim)
    for i in range(iteration_count):
        direction = np.random.uniform(-1, 1, dim)
        direction /= np.linalg.norm(direction, 2)
        t_step = test_step(i)
        x1, x2 = x - t_step * direction, x + t_step * direction
        x = x + work_step(i) * direction * np.sign(function(x1) - function(x2))
    return x
