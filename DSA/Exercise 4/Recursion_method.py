from polynomial_maker import polynomial_maker
import sys 

idx = -1
def recursion_method(degree , coeff_list, value):
    global idx
    
    if degree == 0:
        return coeff_list[degree-1]
    else:
        def power(count ,value):
            if count == 1:
                return value
            else:
                return value * power(count-1, value)
        
        val = power(degree, value)

        idx = idx + 1
        coeff = coeff_list[idx]

        return (coeff_list[idx] * val) + recursion_method(degree-1, coeff_list, value)


if __name__ == "__main__":
    
    degree = 1000 #int(input("Enter the degree of polynomial: "))
    expression, coeff_list = polynomial_maker(degree)
    value = 1000 #eval(input("Enter value of x: "))

    # print ()

    # print (expression)
    # print (coeff_list)

    # print ("\n\n")

    sys.setrecursionlimit(10000)

    print (recursion_method(degree, coeff_list ,value))
