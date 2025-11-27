from fractions import Fraction
import copy
from app.utils.formatter import format_fraction_matrix

def ref_with_steps(A_input):
    A = copy.deepcopy(A_input)
    rows = len(A)
    columns = len(A[0]) if rows>0 else 0
    steps = []
    r = 0
    for c in range(columns):
        pivot = None
        for i in range(r, rows):
            if A[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        if pivot != r:
            A[r], A[pivot] = A[pivot], A[r]
            steps.append(f"Swap row {pivot+1} with row {r+1}\n" + format_fraction_matrix(A))
        pv = A[r][c]
        if pv != 1:
            A[r] = [x / pv for x in A[r]]
            steps.append(f"Divide row {r+1} by {pv}\n" + format_fraction_matrix(A))
        for i in range(r+1, rows):
            factor = A[i][c]
            if factor != 0:
                A[i] = [A[i][j] - factor * A[r][j] for j in range(columns)]
                steps.append(f"R{i+1} = R{i+1} - ({factor}) * R{r+1}\n" + format_fraction_matrix(A))
        r += 1
        if r == rows:
            break
    return A, steps
