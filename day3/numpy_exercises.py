import numpy as np

# a)
vector_a = np.zeros(10)
vector_a[4] = 1 # The fifth value has index four
print(vector_a)

# b)
vector_b = np.arange(10, 50, 1)
print(vector_b)

# c)
vector_c = vector_b[::-1]
print(vector_c)

# d)
matrix_d = np.arange(0, 9, 1).reshape(3, 3)
print(matrix_d)

# e)
vector_e = np.array([1, 2, 0, 0, 4, 0])
nonzero_e = np.nonzero(vector_e)
print(vector_e)
print(nonzero_e)

# f)
vector_f = np.random.rand(30)
mean_f = np.mean(vector_f)
print(vector_f)
print(mean_f)

# g)
size_g = 7
matrix_g = np.ones((size_g, size_g))
matrix_g[1:-1, 1:-1] = 0
print(matrix_g)

# h)
matrix_h = np.zeros((8, 8), dtype=np.uint64)
matrix_h[::2, ::2] = 1
matrix_h[1::2, 1::2] = 1
print(matrix_h)

# i)
matrix_i = np.tile(np.array([[1, 0], [0, 1]]), (4, 4))
print(matrix_i)

# j)
Z_j = np.arange(11)
Z_j = Z_j[np.logical_or(Z_j <= 3, Z_j >= 8)]
print(Z_j)

# k)
Z_k = np.random.random(10)
Z_k = np.sort(Z_k)
print(Z_k)

# l)
A_l = np.random.randint(0,2,5)
B_l = np.random.randint(0,2,5)
equal = np.array_equal(A_l, B_l)
print(equal)

# m)
Z_m = np.arange(10, dtype=np.int32)
print(Z_m.dtype)
Z_m = np.square(Z_m, out=Z_m)
print(Z_m.dtype)

# n)
A_n = np.arange(9).reshape(3,3)
B_n = A_n + 1
C_n = np.dot(A_n, B_n)
print(C_n)
D_n = np.diag(C_n)
print(D_n)
