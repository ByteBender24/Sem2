'''Write a short program that takes as input three integers, a, b, and c, from the console and determines if
they can be used in a correct arithmetic formula (in the given order), like “a + b = c”, “a = b - c”, or
“a * b = c”. List different types of test cases to verify the correctness of your program'''

#NAME : MOHANAKRISHNAA R
#DATE CREATED : 13-04-2023

def add_exp(a,b,c):

    '''
    add_exp(a,b,c) evaluates the expression 'a + b = c' and returns the appropriate answer
    
    arguments:
        a,b,c = numbers (floats, integers, complex numbers)
    
    returns:
        Returns True if the expression is correct
        Returns False if the expression is incorrect
    '''

    if a + b == c :
        return True
    else:
        return False

def sub_exp(a,b,c):

    
    '''
    sub_exp(a,b,c) evaluates the expression 'a = b - c' and returns the appropriate answer
    
    arguments:
        a,b,c = numbers (floats, integers, complex numbers)
    
    returns:
        Returns True if the expression is correct
        Returns False if the expression is incorrect
    '''

    if a == b - c :
        return True
    else:
        return False

def mul_exp(a,b,c):

    
    '''
    mul_exp(a,b,c) evaluates the expression 'a * b = c' and returns the appropriate answer
    
    arguments:
        a,b,c = numbers (floats, integers, complex numbers)
    
    returns:
        Returns True if the expression is correct
        Returns False if the expression is incorrect
    '''

    if a * b == c :
        return True
    else:
        return False

if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    #inputs can be floats, integers, complex numbers

    a = eval(input("Enter the first number 'a': "))
    b = eval(input("Enter the first number 'b': "))
    c = eval(input("Enter the first number 'c': "))

    print ()

    #Based on the given expression, it returns the expression 
    #if the function for that is true

    if add_exp(a,b,c) == True:
        print ("Expression a + b = c is satisfied")

    if mul_exp(a,b,c) == True:
        print ("Expression a * b = c is satisfied")

    if sub_exp(a,b,c) == True:
        print ("Expression a - b = c is satisfied")
        
    if add_exp(a,b,c) == False and mul_exp(a,b,c) == False and sub_exp(a,b,c) == False :
        print ("No satisfied expressions")
        