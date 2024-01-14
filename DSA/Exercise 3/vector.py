#CREATOR INFO:
#REG. NO : 3122225002042
#NAME : HARISHRAJ S
#SEC : IT A

#DATE CREATED: 07/05/2023

import random 

from classvector import Vector

def random_vector_generator(dim,num):

    '''
    random_vector_generator(dim, num) returns a list of vectors with same dimensions
    
    arguments:
        dim - dimensions (integer)
        num - number of vector objects (integer)
    
    returns:
        returns a list of Vector objects of same dimensions    
    '''

    lst_vector = []

    for i in range(num):
        v= []
        for j in range(dim):
            v.append(random.randint(1,10))
        lst_vector.append(Vector(v))
    
    return lst_vector

if __name__ == "__main__":

    '''
    Following code will be executed only when this Python
    file is run directly.  Code will be ignored if this
    file is imported by another Python source.
    '''

    v0 = Vector()
    v1 = Vector(3)
    
    v2 = Vector([1,2,3])
    v3 = Vector ([0,8,9])

    print (v0 , v1, v2, v3)

    print (v1.display())
    print (v3)

    v3[2] = 1
    print(v3)
    
    v4 = (v2 + v3)

    print (v4)

    print (v2 + v4)

    print (v2 - v3)

    print (v3 * 3)

    print (v2 * v3)    
    print (v2.scalprod(v3))
    print(v2.vectprod(v3))

    print (v2 == v3)
    print (v0 == v1)
