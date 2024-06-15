import time
import numpy as np
import matplotlib.pyplot as plt
# from numpy.polynomial import Polynomial as P
from random import shuffle

def function_1(n: int) -> None:
    """
    compute the time complexity of running
    this function as a function of n.
    """
    temp_list = list()
    for i in range(n**2):
        temp = 0
        for j in range(i):
            temp += j
        temp_list.append(temp)
    sum(temp_list)
    

def function_2(n: int) -> None:
    """
    compute the time complexity of running
    this function as a function of n.

    do not hesitate to do some reseach about the
    complexity of the functions used and to average
    the measured times over a number of trials if necessary.
    """
    print(n)
    for i in range(n):
        temp_list = [j+i for j in range(n)]
        shuffle(temp_list)
        max(temp_list)

# Temps d'exécution function_1
n_values = [10, 20, 30, 40, 50]
times_function_1 = []

for n in n_values:
    start_time = time.time()
    function_1(n)
    end_time = time.time()
    times_function_1.append(end_time - start_time)

# Temps d'exécution funciton_2
times_function_2 = []

for n in n_values:
    start_time = time.time()
    function_2(n)
    end_time = time.time()
    times_function_2.append(end_time - start_time)

# polynomial function for function_1
vector_coeff_function_1 = np.polyfit(n_values, times_function_1, deg=4)
polynomial_function_1 = np.poly1d(vector_coeff_function_1)

# polynomial function for function_2
vector_coeff_function_2 = np.polyfit(n_values, times_function_2,  deg=2)
polynomial_function_2 = np.poly1d(vector_coeff_function_2)

# Draw graph
n_fit = np.linspace(min(n_values), max(n_values), 100)

plt.figure(figsize=(12, 6))

# function_1
plt.subplot(1, 2, 1)
plt.plot(n_values, times_function_1, 'o', label='Measures')
plt.plot(n_fit, polynomial_function_1(n_fit), '-', label='Polynomial Adjustment')
plt.title('Elapsed time computing function_1')
plt.xlabel('n')
plt.ylabel('Time in seconds')
plt.legend()

# function_2
plt.subplot(1, 2, 2)
plt.plot(n_values, times_function_2, 'o', label='Measures')
plt.plot(n_fit, polynomial_function_2(n_fit), '-', label='Polynomial Adjustment')
plt.title('Elapsed time computing function_2')
plt.xlabel('n')
plt.ylabel('Time in seconds')
plt.legend()

plt.savefig("complexity.pdf")
