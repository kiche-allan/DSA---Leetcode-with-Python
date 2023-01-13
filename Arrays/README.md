#th above line defines a function called called set_zeros tha takes a single argument called matrix and represents the input matrix we want to modify

def set_zeros(matrix): 
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = False
    first_col_has_zero = False
    