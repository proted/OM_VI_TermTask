import numpy as np


def euclidean_norm(vec: list):
    norm = 0.0
    for i in range(0, len(vec)):
        norm = norm + vec[i] ** 2
    return np.sqrt(norm)


def generate_random_vector(n: int):
    random_vector = list()
    for i in range(0, n):
        random_vector.append(np.random.rand())
    norm = euclidean_norm(random_vector)
    for i in range(0, n):
        random_vector[i] = random_vector[i] / norm
    return random_vector


def vector_add(vec1: list, vec2: list):
    if len(vec1) != len(vec2):
        return None
    vec_res = list()
    for i in range(0, len(vec1)):
        vec_res.append(vec1[i] + vec2[i])
    return vec_res


def vector_mul(vec: list, val: float):
    res = list()
    for i in range(0, len(vec)):
        res.append(vec[i] * val)
    return res