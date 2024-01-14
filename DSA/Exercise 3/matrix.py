#CREATOR INFO:
#REG. NO : 3122225002042
#NAME : HARISHRAJ S
#SEC : IT A

#DATE CREATED: 07/05/2023

from classmatrix import Matrix
import random
def get_matrix(r=0,c=0):
    
    '''
    this gets rows and columns as arguments 
    
    returns matrix as a list of lists
    '''

    mat=[]
    print("Enter matrix elements by row: ")
    for rows in range(r):
        temp=[]
        for cols in range(c):
            elt = random.randint(0,9)
            temp.append(elt)
        mat.append(temp)
    return mat

if __name__ == "__main__":
    
    m1 = Matrix(get_matrix(3,3))
    m2 = Matrix()
    m3 = Matrix(3,3)
    m4 = Matrix([[1,2],[0,0]])

    print (m4.matorder())

    print (m4.elt(1,2))

    print (m1 == m4)
    print (m4.determinant())

    print (m1.determinant())

    m5 = (m1 * m3)
    print (m5)

    print (m3+m1) 

