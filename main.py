from simulated_annealing import boltzmann_annealing
from paired_sample import *
from functions import *
import numpy as np
import matplotlib.pyplot as plt

data = list()
exact_solution = np.array([0, 0])
for i in range(0, 300):
    # solution = boltzmann_annealing(2, function2, 0.5, 100)
    solution = paired_sample_method(function2, 2, 1, 3, boltzmann_step, boltzmann_step, 2500)
    data.append(np.linalg.norm(solution - exact_solution))

# bins=[7 + i*0.01 for i in range(0, 500)]
plt.hist(data, bins=50)
plt.show()
