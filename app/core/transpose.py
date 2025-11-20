def transpose_matrix(A):
    m = len(A)
    n = len(A[0]) if m>0 else 0
    return [[A[i][j] for i in range(m)] for j in range(n)]
