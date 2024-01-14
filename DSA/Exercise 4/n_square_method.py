from polynomial_maker import polynomial_maker

# O(quadratic)
count = 0


def quad_evaluate_polynomial(degree, coeff_list, value):

    global count
    eval_poly = 0
    for coeff in coeff_list:
        deg_eval = 1
        count += 1
        for num in range(degree, 0, -1):
            count += 1
            deg_eval *= value
        deg_eval = deg_eval * coeff
        eval_poly += deg_eval
        degree -= 1
        count += 3
    return eval_poly, count


if __name__ == "__main__":

    degree = 10000  # int(input("Enter the degree of polynomial: "))
    expression, coeff_list = polynomial_maker(degree)
    value = 1  # eval(input("Enter value of x: "))

    # print()

    # print(expression)
    # print(coeff_list)

    # print("\n\n")

    print("count is:", quad_evaluate_polynomial(degree, coeff_list, value)[1])
