#CREATOR INFO:
#REG. NO : 3122225002042
#NAME : HARISHRAJ S
#SEC : IT A

#DATE CREATED: 07/05/2023


from typing import Iterable

class Vector:

    def __init__ (self, val = 0):

        '''
        Using this constructor function, we initialize the values of dimensions of vector 
        or vector itself in the Vector object
        '''

        __slots__ = "__dim" , "__coord"         #only data attributes of this class

        if isinstance (val , int):  #if val is integer (dimension), then a list of zeros as Vector object are produced for given dimension

            self.__coord = ([0]*val)
            self.__dim = val
        
        elif isinstance (val , Iterable): #if val is list(vector), then the list(vector) is initialized as Vector object

            self.__coord = val
            self.__dim = len(val)
        
        else:  #if the entered argument is not of list or integer datatype, an error    is induced

            raise TypeError ("Enter correct vector or dimensions!")

        
    def display(self):

        '''this function is similar to __str__, but it displays as such the object,
        not the space where it is stored'''

        return self.__coord

    def __str__ (self):
        
        '''
        returns string format ready to print
        
        Syntax : print (self)
        '''

        return str(self.__coord)

    def __len__ (self):

        '''returns the length of self Object, makes the object iterable'''

        return self.__dim
    
    def __getitem__ (self, index : int):

        '''returns the item at a particular index, makes the object iterable'''

        return self.__coord[index]

    def __setitem__ (self, index : int, value : (int or float)):

        '''assigns the value in a particular index, makes the object iterable'''

        self.__coord [index] = value
    
    def __add__ (self , other):      

        '''
        addition of each space coordinate of self vector and other vector
        
        Using (+) operator

        Syntax:
            v1 + v2
        '''

        if self.__dim != other.__dim:
            return ("Vectors are not of equal dimensions!")

        else:
            v = Vector(self.__dim)          #as addition of two vectors in space gives rise to a new vector

            for idx in range(self.__dim):
                v.__coord[idx] = (self.__coord[idx] + other.__coord[idx])   #each co-ordinate is added to it's equivalent space co-ordinate
        
            return (v)
    
    def __sub__ (self , other):

        '''
        subtraction of each space coordinate of self and other vector

        Using (-) operator

        Syntax:
            v1 - v2
        '''

        if self.__dim != other.__dim:
            return ("Vectors are not of equal dimensions!")

        else:
            v = Vector(self.__dim)          #as subtraction of two vectors in space gives rise to a new vector

            for idx in range(self.__dim):
                v.__coord[idx] = (self.__coord[idx] - other.__coord[idx])   #each co-ordinate is added to it's equivalent space co-ordinate
        
            return (v)
    
    def __mul__ (self , other):

        '''
        multiplication between a scalar and a vector - 
                returns new multiplied vector with each element multiplied by scalar
        
        multiplication between a vector and vector - scalar product is returned (scalar)
        
        Argument should be vector or scalar (not a list or any other data type)
        
        Using (*) operator

        Syntax:
            v1 * v2
        '''


        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return Vector([other*x for x in self.__coord])      #vector is returned
    
        elif isinstance(other , Vector):        #Vector object is given as argument
            if self.__dim != other.__dim:
                return "The vectors are not in same dimensions"
            else:
                dot = 0
                for i in range(other.__dim):
                    dot += self.__coord[i] * other.__coord[i]
                return dot
        else:
            raise TypeError("Enter correct type of argument")
    
    def scalprod(self, other):

        '''
        returns the scalar product of two matrices, it does mat1 * mat2
        and calls the __mul__ operator

        Syntax:
            self.scalprod(other)            
        '''

        return self.__mul__(other)              
    
    def vectprod(self, other):
        
        '''
        returns the vector product of two matrices

        vector product is actually applicable for two matrices of 3 space co-ordinates
        
        Syntax:
            self.vectprod(other)
        '''

        if isinstance(other , Vector):        #it should be vector 
            
            if self.__dim != other.__dim:
                return "The vectors are not in same dimensions"
            
            elif self.__dim != 3 or other.__dim != 3:               
                return "Vector product is only applicable for 3D vectors"
            
            else:
                a = self.__coord
                b = other.__coord
                v = Vector([a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]])                            
                return v
        else:
            raise TypeError("Enter correct type of argument")

    def __truediv__ (self, other):

        '''
        division of each space coordinate of self and other vector
        '''

        return ("This operation doesn't occur on vectors")

    '''
    cmp is not widely used now, use other methods such as 
    __eq__ and __gt__....
    cmp has the same syntax as __eq__
    '''
  
    def __ne__ (self , other):

        '''returns True or False for (self != other) Matrix objects'''

        return self.__coord != other.__coord
    
    def __eq__ (self , other):

        '''returns True or False for (self == other) Matrix objects'''

        return self.__coord == other.__coord        #not self = other (as this is assignment)
    
    '''
    Cannot use dot product as v1.v2 as (.)dot operator is "__getattribute__" 
    This special method, is responsible for assigning methods and data members of a class
    If I override this, everything within this class don't work
    
    It arises a "AttributeError", when v1.v2 is called.

    # def __getattribute__(self, other):
    #     if isinstance(other, Vector or int):
    #         return self.__mul__(other)
    '''
