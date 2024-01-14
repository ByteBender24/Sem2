from polynomial_maker import polynomial_maker
count = 0
# n


def Horners_method(degree, coeff_list, value):
    global count
    for num in range(degree):
        count += 1
        coeff_list[num+1] = (coeff_list[num] * value) + coeff_list[num+1]
    return coeff_list[degree], count


if __name__ == "__main__":

    degree = int(input("Enter the degree of polynomial: "))
    expression, coeff_list = polynomial_maker(degree)
    value = eval(input("Enter value of x: "))

    # print ()

    # print (expression)
    # print (coeff_list)

    # print ("\n\n")

    print("count is:", Horners_method(degree, coeff_list, value)[1])
