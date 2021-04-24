import numpy as np
from typing import Callable


def boltzmann_annealing(dim: int, function: Callable, t_0: float, iteration_count: int):
    global_minimum_point = np.random.normal(0, t_0, dim)
    global_minimum_energy = function(global_minimum_point)
    for k in range(1, iteration_count):
        temperature = t_0 / np.log(1 + k)
        current_point = np.random.normal(global_minimum_point, temperature, dim)
        current_energy = function(current_point)
        if current_energy < global_minimum_energy:
            global_minimum_energy = current_energy
            global_minimum_point = current_point
            continue
        alpha = np.random.uniform(0, 1, 1)
        if alpha < np.exp(- (current_energy - global_minimum_energy) / temperature):
            global_minimum_energy = current_energy
            global_minimum_point = current_point
    return global_minimum_point
