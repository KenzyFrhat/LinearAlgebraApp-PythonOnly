def transpose_matrix(A):
    rows = len(A) # number of rows 
    columns = len(A[0]) if rows >0 else 0  # number of coumns , the if condition is to handle empty matrix case cause len(A[0]) will give index error if A is empty
    return [[A[i][j] for i in range(rows)] for j in range(columns)]  # we went through the original matrix column by column and created new rows for the transposed matrix
     

