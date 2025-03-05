#!nvidia-smi

import numpy as np
import cupy as cp
from IPython import get_ipython

sizes = [128, 256, 512, 1024, 2048]

# Default is float64
print("Using float64:")
for size in sizes:
    np_array = np.random.random((size, size))
    cp_array = cp.asarray(np_array)
    
    print(f"\Size: {size}x{size}")
    %timeit np.fft.fft2(np_array)
    %timeit cp.fft.fft2(cp_array)

# Test with float32
print("Using float32:")
for size in sizes:
    np_array = np.random.random((size, size)).astype(np.float32)
    cp_array = cp.asarray(np_array)
    
    print(f"\Size: {size}x{size}")
    %timeit np.fft.fft2(np_array)
    %timeit cp.fft.fft2(cp_array)

# Best performance with cupy for all tested cases above
# With float32, numpy does not really change, while cupy gets even better
