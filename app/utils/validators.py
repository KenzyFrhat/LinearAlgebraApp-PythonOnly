def is_square(M):
    return len(M) > 0 and all(len(row) == len(M) for row in M)
