# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

# The fastest way to multiply two matrices that I can think of is to use numpy

# NxN matrix
X = np.random.randint(0, 101, size=(N, N))

# Nx(N+1) matrix
Y = np.random.randint(0, 101, size=(N, N + 1))

# result is Nx(N+1)
result = X @ Y

# for r in result:
#     print(r)
