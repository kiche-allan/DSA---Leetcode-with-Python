def set_zeros(matrix): 
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = False
    first_col_has_zero = False
    
    #check if the first row has zero
    
    for j in range (n):
        if matrix [0][j] == 0:
            first_row_has_zero = True
            break
        
    #check if the first column has zero
    
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break
        
    #check for zeos in the rest of the matrix
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0]= 0
                matrix[0][j] = 0
                
   #set the zeros in the rest of the matrix
   
   for i in range(1, m):
       for j in range(1, n):
           if matrix[i][0] == 0 or matrix[0][j] ==0:
               matrix[i]{j} = 0
               
    #set the zeros in the first roww and column if needed
    
    if first_row_has-zero:
        for j in range(n):
            matrix[0][j] = 0
    
   