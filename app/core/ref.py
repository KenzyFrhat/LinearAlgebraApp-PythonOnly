from fractions import Fraction
import copy
from app.utils.formatter import format_fraction_matrix

def ref_with_steps(A_input):
    A = copy.deepcopy(A_input)
    rows = len(A)
    columns = len(A[0]) if rows>0 else 0
    steps = [] # to store each step of the transformation
    r = 0
    for c in range(columns):
        pivot_row_index = None # to store the row index of the pivot element in column c
        for i in range(r, rows): # find pivot in column c, starting from row r #!<vertically down search>
            if A[i][c] != 0:
                pivot_row_index = i
                break
        if pivot_row_index is None:
            continue
        if pivot_row_index != r:
            A[r], A[pivot_row_index] = A[pivot_row_index], A[r]
            steps.append(f"Swap row {pivot_row_index+1} with row {r+1}\n" + format_fraction_matrix(A))
        pv = A[r][c] # pivot value , which is now at row r #!after any swap
        if pv != 1:
            A[r] = [x / pv for x in A[r]]
            steps.append(f"Divide row {r+1} by {pv}\n" + format_fraction_matrix(A))

        #The elimination process to create zeros below the pivot
        #?The difference between REF and RREF is that in REF we only eliminate entries below the pivot
        for i in range(r+1, rows): # eliminate entries below the pivot, force the rest of the column to be 0
            factor = A[i][c]
            if factor != 0:
                #?<goal>
                #make good use of the pivot row to
                #!<subracted the the rest columns values from itself>

                #?<steps>
                 #* go through the entire row <horizontally>,
                 #* multiplying it by the current row <r>
                 #* subtracting it from the current row 
                 #!in order to force the current column entry to be 0 <subracted from itself> using the pivot value which is always 1

                A[i] = [A[i][j] - factor * A[r][j] for j in range(columns)] 
                steps.append(f"R{i+1} = R{i+1} - ({factor}) * R{r+1}\n" + format_fraction_matrix(A)) #record each step

        r += 1
        if r == rows:
            break
    return A, steps
