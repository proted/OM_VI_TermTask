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

#if __name__ == '__main__':
#    iterations = [2500]
#    data = [list() for _ in range(len(iterations))]
#    exact_solution = np.ndarray((10,), buffer=np.array([1.0, 4.0, -12.9, -0.33334, 7.8, 1.0, 0.1, 4, -11, 6.8]))
#    for i in range(len(iterations)):
#        for _ in range(300):
#            init = np.random.normal(np.ndarray((10,), buffer=np.array([1.0, 4.0, -12.9, -0.33334, 7.8, 1.0, 0.1, 4, -11, 6.8])), 1, 10)
#            solution = paired_sample_method(function5, 10, init, 6, 1, hyperbolic_step, hyperbolic_step, iterations[i])
#            data[i].append(np.linalg.norm(init - exact_solution, 2)/np.linalg.norm(solution - exact_solution, 2))
#        plt.hist(data[i], bins=80)
#        plt.xlabel('||x_0 - x*||/||x_k-x*||')
#        plt.title(f'Число итераций = {iterations[i]}')
#        plt.show()
