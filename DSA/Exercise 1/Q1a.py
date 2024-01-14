'''Write a short program that takes as input three integers, a, b, and c, from the console and determines if
they can be used in a correct arithmetic formula (in the given order), like “a + b = c”, “a = b - c”, or
“a * b = c”. List different types of test cases to verify the correctness of your program'''

#CREATOR INFO:
#ROLL NO :3122225002042
#NAME    : Harishraj S
#SECTION : IT A

#DATE CREATED : 06-04-2023


def expression_creator():
    
    '''
        expression_creator() function finds all possible expressions
    for given three variables and given set of operators
    (can be changed to have different combinations)

        Can have multiple combination by changing 'symbol_lst' list

        returns : list of all possible expressions for operators in symbol_lst
    '''
    
    import random

    exp_lst = []                                #this variable contains the various expressions possible.

    for times in range(random.randrange(1000)): #created a string with random choice of operands and operators in right place to have all possibilites of expressions
        exp = ""
        operand_lst = ['a','b','c']
        symbol_lst = ['/','-','+','*']          #can include '%','//','**' and any other moderator needed
        exp = exp + random.choice(operand_lst)
        operand_lst.remove(exp)
        exp = exp + random.choice(symbol_lst)
        exp = exp + random.choice(operand_lst)
        operand_lst.remove(exp[2])
        exp = exp + "="
        exp = exp + random.choice(operand_lst) 

        exp_lst.append(exp)
    
    exp_lst_final=[]              #this variable has the unique and the maximum number of possibilities of expressions with those operators          
    for elt in exp_lst:           #this has the unrepeated expressions by removing the repeated elements of the previous list
        if elt in exp_lst_final:
            pass
        elif elt not in exp_lst_final:
            exp_lst_final.append(elt)

    return exp_lst_final

def expression_displayer(expr):
    print ("The following expressions are taken for checking: ")  

    for elt in expr:           #the possible expressions are printed for user to choose from.
        print (str(expr.index(elt) + 1) + ")" , elt)
    print ()



def expression_checker(a,b,c,exp):   
    '''
    expression_checker(a,b,c,exp) function returns the function 
    if the given expression is valid for the given set of numbers
    Takes three variables(numbers) and an expression as arguments

    a,b,c = integers or floats or complex numbers
    exp = expression to be checked (manually entered by user)

    If a expression is divided by 0, then 'ZeroDivisionError' is thrown, (exception handling)

    returns : returns if the given expression is True or False by using eval function
    ''' 

    try:
        if eval(exp) is True:
            exp = exp.replace("==","=")
            return (f"{exp} satisfied")
        elif eval(exp) is False:
            exp = exp.replace("==","=")
            return (f"{exp} not satisfied")
    except ZeroDivisionError:                           #If there is a expression, where a number is divided by zero, instead of error, it shows a message that it doesn't satisfy
        exp = exp.replace("==","=")
        return (f"Cannot divide by zero. Hence Equation {exp} doesn't satisfy")
                 

if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.
    
    expr = expression_creator()   #displays all the possible expressions for given set of variables(operators) and operators
    expression_displayer(expr)

    #inputs are taken from user
    #numbers can be positive, negative, floats, zeros, complex numbers too

    a = eval(input("Enter first number 'a': "))
    b = eval(input("Enter second number 'b': "))
    c = eval(input("Enter third number 'c': "))


    #A choice is given to user, whether to print all expression validity, or to check a individual expression validity


    choice = int(input("Enter 1 if you want all expressions that are valid\nEnter 2 for entering a particular expression and check: "))
    
    print ()

    if choice == 2:
        exp_num = int(input("Enter the expression number from the top list: "))  #Expression's place (number) in printeed  list is needed
        exp = expr[exp_num-1]
        exp = exp.replace("=","==")               #this replacement is needed for evaluating the typed expression
        print (expression_checker(a,b,c,exp))

    elif choice == 1:
        num = 0
        for itm in expr:
                num += 1
                itm = itm.replace("=","==")
                print (num, expression_checker(a,b,c,itm))
