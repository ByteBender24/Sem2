from polynomial_maker import polynomial_maker

count = 0


def polynomial_calc(degree, coeff_list, value):
    global count
    final_val = 0
    for num in range(degree, -1, -1):
        count += 1
        final_val += coeff_list[degree - num] * power(value, num)
    return final_val, count


def power(base, exponent):
    global count
    count += 1
    if exponent == 0:
        return 1
    else:
        if exponent % 2 == 0:
            t = power(base, exponent//2)
            return t * t
        else:
            t = power(base, exponent//2)
            return base * t


if __name__ == "__main__":

    degree = 10000  # int(input("Enter the degree of polynomial: "))
    expression, coeff_list = polynomial_maker(degree)
    value = 1  # eval(input("Enter value of x: "))

    # print()

    # print(expression)
    # print(coeff_list)

    # print("\n\n")

    print("count is:", polynomial_calc(degree, coeff_list, value)[1])
