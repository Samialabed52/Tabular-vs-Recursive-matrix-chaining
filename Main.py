import time
import numpy as np
from TabularMatrixChaining import TabularMatrixChaining
import RecursiveMatrixChaining


d1 = np.array([30, 1, 40, 10, 25])
d2 = np.array([80, 96, 66, 4, 85, 94, 68, 76, 75])


print("Tabular matrix chaining with d1")
tic = time.perf_counter()
x = TabularMatrixChaining.matrixChainTab(d1)
toc = time.perf_counter()
total1 = toc - tic
print(x)
print("The total time to run array d1 with tabular Matrix Chaining =",total1," seconds")


print("Recursive matrix chaining with d1")
tic = time.perf_counter()
x = RecursiveMatrixChaining.matrixChainRec(d1)
toc = time.perf_counter()
total1rec = toc - tic
print(x)
print("The total time to run array d1 with recursive Matrix Chaining =",total1rec,"seconds")


print("Tabular matrix chaining with d2")
tic = time.perf_counter()
x = TabularMatrixChaining.matrixChainTab(d2)
toc = time.perf_counter()
total2 = toc - tic
print(x)
print("The total time to run array d2 with tabular Matrix Chaining =",total2," seconds")


print("Recursive matrix chaining with d2")
tic = time.perf_counter()
x = RecursiveMatrixChaining.matrixChainRec(d2)
toc = time.perf_counter()
total2rec = toc - tic
print(x)
print("The total time to run array d2 with recursive Matrix Chaining =",total2rec,"seconds")












