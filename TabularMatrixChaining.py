import numpy as np
import math

class TabularMatrixChaining:
    def matrixChainTab(d):
        n = len(d)-1
        M = np.zeros(shape = (n,n), dtype= int)
        K = np.zeros(shape = (n,n), dtype= int)
        for i in range(1, n):
            for j in range(0, n - i):
                k = j + i
                minimum = math.inf
                for l in range(j, k):
                    count = M[j, l] + M[l + 1, k] + d[j] * d[l + 1] * d[k + 1]
                    if count < minimum:
                        minimum = count
                        M[j, k] = minimum
                        K[j, k] = l + 1
        return M, K


