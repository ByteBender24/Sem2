#CREATOR INFO:
#REG. NO : 3122225002042
#NAME : HARISHRAJ S
#SEC : IT A

#DATE CREATED: 07/05/2023

from typing import Iterable
# import numpy


class Matrix:

    def __init__(self, *args):

        '''
        initializes a matrix object with the suitable arguments given
        
        can be rows and cols given as two arguments
        or the matrix itself as list of lists
        or the order of matrix as a tuple (rows, cols)
        '''

        __slots__ = "rows", "cols", "matrix", "order"           #only data attributes in this class

        if len(args) == 1:
            if isinstance(args[0], list) and all(isinstance(row, list) for row in args[0]):
                #if one argument is given, and that is a matrix represented as a list

                self.rows = len(args[0])
                self.cols = len(args[0][0])
                self.order = (self.rows , self.cols)
                self.matrix = args[0]

                if any([len(self.matrix[x]) != self.cols for x in range(self.rows)]) == True:
                    #if matrix in the list is given with wrong number of columns in any row, it raises an error

                    raise TypeError(
                        "Enter proper matrix with same number of columns")

            elif isinstance(args[0], list) and all(isinstance(row, int) for row in args[0]):
                #if a row of elements is given mistakenly not as a list of lists, then also it takes it as a argument
                self.cols = 0
                self.rows = len(args[0])
                self.order = (self.rows , self.cols)
                self.matrix = [[x for x in args[0]]]
            
            elif isinstance(args[0], tuple) and len(args[0]) == 2:
                #if order of matrix is given as a tuple
                self.rows = args[0][0]
                self.cols = args[0][1]
                self.order = args[0]
                self.matrix = [
                    [0 for c in range(self.cols)] for r in range(self.rows)]

        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            #if two arguments are given, as number of cols and number of rows, automatically it assumes zeros as elements
            self.rows, self.cols = args
            self.order = (self.rows , self.cols)
            self.matrix = [
                [0 for c in range(self.cols)] for r in range(self.rows)]
        
        elif len(args) == 0:
            #if no arguments are given, it assumes a 1x1 matrix with element as 0
            self.rows , self.cols = 1 , 1
            self.order = (1,1)
            self.matrix = [0]

    def display(self):

        '''returns the matrix as a list of lists format'''

        return str(self.matrix)

    def __str__(self):
        
        '''returns the string format of how we see normal matrices as we see'''
        if self.rows == 0 and self.cols == 0:
            str_matrix = ""
        else:
            str_matrix = ""
            for rows in self.matrix:
                row = ""
                for cols in rows:
                    row += str(cols)
                    row += " "
                str_matrix += row
                str_matrix += "\n"

        return str_matrix

    def __len__(self):

        '''for making the Matrix object iterable'''

        return self.rows

    def __getitem__(self, idx):

        '''for making the Matrix object iterable'''

        return self.matrix[idx]

    def __setitem__(self, idx, val):

        '''for making the Matrix object iterable'''

        self.matrix[idx] = val

    def matorder(self):

        '''returns the order of matrix object as a tuple (rows, cols)'''

        return self.order
    
    def elt(self, r , c):

        '''Given rows and column, the element is returned'''

        return self[r-1][c-1]
    
    def determinant(self):
        

        '''
        can find determinant of a square matrix. Used numpy modules determinant function
        
        If the below code is used, it raises few errors, and time complexity is more
        '''

        if self.rows != self.cols:
            return "Determinant can only be found for square matrices"

        else:
            # return numpy.linalg.det(self.matrix)
            pass            #for faster time complexity

        '''

        we can use this code also, but the time complexity is high for this algorithm:

        def determinant(mat : Matrix, total=0):
            index = list(range(len(mat)))
            
            if mat.matorder() == (2,2):
                val = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
            
            elif mat.matorder() == (1, 1):
                mat[0][0]
        
            for fc in index: 
                newmat = Matrix(mat.matrix) 
                newmat = newmat[1:] 
                row_height = len(newmat) 
        
                for i in range(row_height):
                    newmat[i] = newmat[i][0:fc] + newmat[i][fc+1:] 
        
                sign = (-1) ** (fc % 2) 
                sub_det = determinant(newmat)
                total += sign * mat[0][fc] * sub_det 
        
            return total
        '''          

    def __add__(self, other):

        '''
        addition of each element of corresponding row and column is added
        
        Using (+) operator

        Syntax:
            m1 + m2
        '''

        if self.rows != other.rows and self.cols != other.cols:
            return "Enter matrices of same order(rows x columns)"

        else:
            add_matrix = Matrix(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    add_matrix[r][c] += self[r][c] + other[r][c]

            return add_matrix

    def __sub__(self, other):
        
        '''
        subtraction of each element of corresponding row and column is added
        
        Using (-) operator

        Syntax:
            m1 - m2
        '''

        if self.rows != other.rows and self.cols != other.cols:
            return "Enter matrices of same order(rows x columns)"

        else:
            add_matrix = Matrix(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    add_matrix[r][c] += self[r][c] - other[r][c]

            return add_matrix

    def __mul__(self, other):

        '''
        matrix multiplication of two matrices
        
        Using (*) operator

        Syntax:
            m1 * m2
        '''

        if isinstance(other, Matrix):
            if self.cols != other.rows:
                return "Enter matrices of suitable order!"

            else:
                mul_matrix = Matrix(self.rows, other.cols)

                for rs in range(self.rows):
                    for co in range(other.cols):
                        for ro in range(other.rows):
                            mul_matrix[rs][co] += self[rs][ro] * other[ro][co]

                return mul_matrix
        elif isinstance(other, int):

            mul_matrix = Matrix (self.rows,self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    mul_matrix[r][c] = other * self[r][c]
            
            return mul_matrix

    def __truediv__ (self, other):
        
        '''division is not possible with matrices, if want to find inverse, it is unavailable'''

        return f"{self} / {other} is not available. In case if you are trying to find inverse, inverse method is not available for this 'Matrix' class"
    
    def __ne__ (self, other):

        '''
        Syntax:
            self != other
        
        overloads the not equal to operator
        '''

        return self.matrix != other.matrix
    
    def __eq__ (self, other):

        '''
        Syntax:
            self == other
        
        overloads the equal to operator
        '''

        return self.matrix == other.matrix
    