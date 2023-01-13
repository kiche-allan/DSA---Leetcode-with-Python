class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
            #  This is a Python class called "Solution" that contains a method called "setZeroes" that takes in a 2D matrix (List of Lists) as its parameter. The method modifies the input matrix in place to set all the elements in the rows and columns that have at least one element with a value of 0 to 0. The method first uses two sets, "rows" and "cols", to store the rows and columns that need to be set to 0 respectively. It then iterates through the matrix and marks the rows and columns with elements that have a value of 0. Finally, it iterates through the matrix again and using the "rows" and "cols" sets, updates the elements accordingly.       
    