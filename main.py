from simulated_annealing import boltzmann_annealing
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import math

data = list()
exact_solution = np.array([0, 0])
for i in range(0, 5000):
    solution = boltzmann_annealing(2, function4, 0.5, 100)
    data.append(np.linalg.norm(solution - exact_solution))

# bins=[7 + i*0.01 for i in range(0, 500)]
plt.hist(data, bins=100)
plt.show()
