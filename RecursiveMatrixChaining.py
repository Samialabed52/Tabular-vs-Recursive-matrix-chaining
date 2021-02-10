import numpy as np

def matrixChainRec(d):
    n = len(d) - 1
    if n <= 0:
        return np.zeros(shape = (1,1), dtype= int), np.zeros(shape = (1,1), dtype= int)
    M = np.zeros(shape = (n,n), dtype= int)
    K = np.zeros(shape = (n,n), dtype= int)
    M[:n-1,:n-1], K[:n-1,:n-1] = matrixChainRec(d[:n])
    for i in range(n-2,-1,-1):
        minimum = M[i,i]+M[i+1,n-1]+d[i]*d[i+1]*d[n]
        for j in range(i,n-1):
            count = M[i,j]+M[j+1,n-1]+d[i]*d[j+1]*d[n]
            if count <= minimum:
                minimum = count
                K[i,n-1] = j+1
        M[i,n-1] = minimum
    return M, K




