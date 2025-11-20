from fractions import Fraction
import copy
from app.utils.formatter import format_fraction_matrix

def inverse_with_steps(A_input):
    A = copy.deepcopy(A_input)
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError('Inverse requires a square matrix')
    steps = []
    # augment with identity
    Aug = [row[:] + [Fraction(1 if i==j else 0) for j in range(n)] for i,row in enumerate(A)]
    total_cols = 2*n
    # forward elimination / Gauss-Jordan
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, n):
            if Aug[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        if pivot != r:
            Aug[r], Aug[pivot] = Aug[pivot], Aug[r]
            steps.append(f"Swap row {pivot+1} with row {r+1}\n" + format_fraction_matrix(Aug))
        pv = Aug[r][c]
        if pv != 1:
            Aug[r] = [x / pv for x in Aug[r]]
            steps.append(f"Divide row {r+1} by {pv}\n" + format_fraction_matrix(Aug))
        for i in range(n):
            if i == r: continue
            factor = Aug[i][c]
            if factor != 0:
                Aug[i] = [Aug[i][j] - factor * Aug[r][j] for j in range(total_cols)]
                steps.append(f"R{i+1} = R{i+1} - ({factor}) * R{r+1}\n" + format_fraction_matrix(Aug))
        r += 1
        if r == n:
            break
    # check left side is identity
    left = [[Aug[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i==j and left[i][j] != 1) or (i!=j and left[i][j] != 0):
                raise ValueError('Matrix is singular and not invertible')
    Inv = [[Aug[i][j] for j in range(n, total_cols)] for i in range(n)]
    return Inv, steps
