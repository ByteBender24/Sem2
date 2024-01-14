import random

def polynomial_maker(degree):
    coeff_list = []
    expression = ""
    deg = degree
    for exp in range(deg,-1,-1):
        coeff = random.randint(0,9)
        coeff_list.append(coeff)    
        if exp == 0:
            expression += f"{coeff}"
        elif exp == 1:
            expression += f"{coeff}x + "
        elif coeff == 0:
            continue
        elif coeff == 1:
            expression += f"x**{exp} + "
        else:
            expression += f"{coeff}x**{exp} + "
    return expression , coeff_list 


if __name__ == "__main__":
    exp = polynomial_maker(3)[0]
    x = 1
    exp = "8*(x**3) + 4*(x**2) + 4*(x) + 10"
    print (eval(exp))