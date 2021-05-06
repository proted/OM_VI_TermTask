import numpy as np
from typing import Callable


def boltzmann_annealing(dim: int, function: Callable, t_0: float, iteration_count: int,
                        initial_vec: np.ndarray = None,
                        descent: np.ndarray = None, temperature_descent: np.ndarray = None,
                        test_descent: np.ndarray = None):
    if initial_vec is None:
        global_minimum_point = np.random.normal(0, t_0, dim)
    else:
        global_minimum_point = initial_vec
    global_minimum_energy = function(global_minimum_point)
    if descent is not None:
        descent[0] = global_minimum_point
    if temperature_descent is not None:
        temperature_descent[0] = t_0
    for k in range(1, iteration_count):
        temperature = t_0 / np.log(1 + k)
        if temperature_descent is not None:
            temperature_descent[k] = temperature
        current_point = np.random.normal(global_minimum_point, temperature, dim)
        if test_descent is not None:
            test_descent[k-1] = current_point
        current_energy = function(current_point)
        if current_energy < global_minimum_energy:
            global_minimum_energy = current_energy
            global_minimum_point = current_point
            if descent is not None:
                descent[k] = global_minimum_point
            continue
        alpha = np.random.uniform(0, 1, 1)
        if alpha < np.exp(- (current_energy - global_minimum_energy) / temperature):
            global_minimum_energy = current_energy
            global_minimum_point = current_point
        if descent is not None:
            descent[k] = global_minimum_point
    return global_minimum_point
