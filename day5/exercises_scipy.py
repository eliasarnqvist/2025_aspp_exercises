import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# %% 1

# a)
A = np.array([[1, -2, 3], [4, 5, 6], [7, 1, 9]])

# b)
b = np.array([1, 2, 3])

# c)
x = sp.linalg.solve(A, b)
print(x)

# d)
b_d = A @ x
print(b_d)

# e)
B = np.random.rand(3, 3) * 10
x_e = sp.linalg.solve(A, B)
print(x_e)
b_e = A @ x_e
print(b_e)
print(B)

# f)
eigvals, eigvecs = sp.linalg.eig(A)
print(eigvals, eigvecs)

# g)
inv_A = sp.linalg.inv(A)
print(inv_A)
det_A = sp.linalg.det(A)
print(det_A)

# h)
norm_A = sp.linalg.norm(A)
print(norm_A)
norm_A_1 = sp.linalg.norm(A, ord=1)
norm_A_2 = sp.linalg.norm(A, ord=2)
# norm_A_3 = sp.linalg.norm(A, ord=3)
print(norm_A_1, norm_A_2)

# %% 2

# a)
lambda_param = 4
number_of_samples = 1000
x = np.arange(0, 20)

poisson_dist = sp.stats.poisson(lambda_param)

pmf_p = poisson_dist.pmf(x)
cdf_p = poisson_dist.cdf(x)
samples_p = poisson_dist.rvs(size=number_of_samples)

fig, ax = plt.subplots(1, 3, figsize=(12, 4))

ax[0].stem(x, pmf_p, label='PMF')
ax[0].set_title('Probability mass function')
ax[0].set_xlabel('k')
ax[0].set_ylabel('P(X = k)')

ax[1].step(x, cdf_p, where='post', label='CDF')
ax[1].set_title('Cumulative distribution function')
ax[1].set_xlabel('k')
ax[1].set_ylabel('P(X ≤ k)')

ax[2].hist(samples_p, bins=range(max(samples_p)+2), density=True, alpha=0.7, label='Samples')
ax[2].set_title('Histogram of ' + str(number_of_samples) + ' samples')
ax[2].set_xlabel('k')
ax[2].set_ylabel('Frequency')
ax[2].legend()

plt.tight_layout()

# b)
number_of_samples = 1000
x = np.arange(-5, 6)

normal_dist = sp.stats.norm(loc=0, scale=1)

pmf_n = normal_dist.pdf(x)
cdf_n = normal_dist.cdf(x)
samples_n = normal_dist.rvs(size=number_of_samples)

fig, ax = plt.subplots(1, 3, figsize=(12, 4))

ax[0].stem(x, pmf_n, label='PMF')
ax[0].set_title('Probability mass function')
ax[0].set_xlabel('k')
ax[0].set_ylabel('P(X = k)')

ax[1].step(x, cdf_n, where='post', label='CDF')
ax[1].set_title('Cumulative distribution function')
ax[1].set_xlabel('k')
ax[1].set_ylabel('P(X ≤ k)')

ax[2].hist(samples_n, bins=40, density=True, alpha=0.7, label='Samples')
ax[2].set_title('Histogram of ' + str(number_of_samples) + ' samples')
ax[2].set_xlabel('k')
ax[2].set_ylabel('Frequency')
ax[2].legend()

plt.tight_layout()

# c)

t_statistic, t_pvalue = sp.stats.ttest_ind(samples_p, samples_n)
print(t_statistic, t_pvalue)

plt.show()
