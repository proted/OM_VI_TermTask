import numpy as np
from typing import Callable


def paired_sample_method(function: Callable, dim: int, work_step: Callable, test_step: Callable, iteration_count: int):
    x = np.random.normal(0, 100, dim)
    for i in range(iteration_count):
        direction = np.random.uniform(-1, 1, dim)
        x = x + work_step(i) * direction * np.sign(
            function(x - test_step(i) * direction) - function(x + test_step(i) * direction))
    return x
        
