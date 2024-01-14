'''The p-norm of a vector v = (v1, v2, · · · , vn) in n-dimensional space is defined as
For the special case of p = 2, this results in the traditional Euclidean Norm, which represents the length
of the vector. Give an implementation of a function named 'norm' such that norm(v, p) returns the
p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a tuple of
numbers.'''

#CREATOR INFO:
#ROLL NO :3122225002042
#NAME    : Harishraj S
#SECTION : IT A

#DATE CREATED : 09-04-2023


def norm(v,p=2):

    '''
    This norm function takes two arguments, v and p. p is a default argument
    and equals to 2 when value of p is not given
    
    v - vector notation of elements in n dimensional space
    p - p value of norm
    
    returns : p norm of vector given
    '''
    
    sum = 0
    for elt in v:
        sum = sum + elt**p
    try:
        p_norm = sum ** (1/p)
    except OverflowError:
        try:
            p_norm = round (sum ** (1/p))

        #OverflowError shows up, when the integer is too large to convert to a float.
        #So exception handling is used here, but this is not accurate

        except OverflowError:
            #the value might not be true for this error
            sum = 0
            for elt in v:
                sum = sum + round (elt**p)
            p_norm = round (sum ** round(1/p))
    return p_norm


if __name__ == "__main__" :

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.
    
    v = eval(input("Enter a tuple of all dimensional elements of a vector v: "))        #v is given as a tuple
    p = int(input("Enter the p value for p-norm: "))
   
    if p == 1:
        print ("Manhattan norm",end ="\t")                  #when p=1, it's called 'Manhattan norm'
        print (norm(v,p))
        print ("However the Euclidean norm for the given vector is: ",end = "")
        print (norm(v))
    elif p == 2:
        print ("Euclidean norm",end ="\t")                  #when p=2, it's called 'Euclidean norm'
        print (norm(v,p))
    elif p == 3:
        print ("Cubic norm",end ="\t")                      #when p=3, it's called 'Cubic norm'
        print (norm(v,p))
        print ("However the Euclidean norm for the given vector is: ",end = "")
        print (norm(v))
    else:
        print (norm(v,p))
        print ("However the Euclidean norm for the given vector is: ",end = "")
        print (norm(v))
    