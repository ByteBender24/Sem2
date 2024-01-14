from classmatrix import Matrix

matrix = Matrix([[1, 2, 3], [1, 3, 4], [1, 6, 0]])
matrix2 = Matrix([[1, 2], [9, 2]])

def determinant_recursive(mat : Matrix):
    if mat.matorder() == (2, 2):
        det = ((mat[0][0] * mat[1][1]) - (mat[1][0] * mat[0][1]))
        return det
    
    else:
        mat.matrix.remove(matrix[0])
        for j in range(mat.rows):
            mat[j].remove(mat[j][0])
        determinant_recursive
        print (mat)                

def determinant_recursive(mat : Matrix, total=0):
    indices = list(range(len(mat)))
     
    if mat.matorder() == (2,2):
        val = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
    
    elif mat.matorder() == (1, 1):
        mat[0][0]
  
    for fc in indices: 
        As = Matrix(mat.matrix) 
        As = As[1:] 
        height = len(As) 
 
        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2) 
        sub_det = determinant_recursive(As)
        total += sign * mat[0][fc] * sub_det 
 
    return total

print(determinant_recursive(matrix))
print(determinant_recursive(matrix2))
