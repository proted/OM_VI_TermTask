import numpy as np
import miscellaneous as misc

def paired_sample_method(function, initial_value: list, step_count: int):
    dim = len(initial_value)
    width_space = 1.0
    current_value = initial_value.copy()
    for i in range(0, step_count):
        random_vector = misc.generate_random_vector(dim)
        first = misc.vector_add(current_value, misc.vector_mul(random_vector, width_space))
        second = misc.vector_add(current_value, misc.vector_mul(random_vector, -width_space))
        
