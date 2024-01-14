''' 
Write a program to model a real-time online shopping system using
inheritance. The base class should be called Product, and it should have 
attributes for the name, price, and quantity of the product. The derived 
classes should be ElectronicProduct and ClothingProduct, which inherit from 
Product. Each derived class should have additional attributes specific to that
type of product, such as the brand and model for ElectronicProduct, and the 
size and color for ClothingProduct. Implement methods in each class to 
display the product information. Additionally, override the display_information() method 
in the derived classes to include the specific attributes of each product type. 
Also, implement a function in the derived classes to calculate the total price 
based on the quantity of the product. Finally, overload the '+' operator in 
the derived classes to allow adding two products together offering a combo 
pack with the summed-up price tag. 

Created by : Harishraj S
             IT A
             3122 22 5002 042

Contact    : <harishraj2210713@ssn.edu.in>
             
Date created : 24-05-2023

'''


class Product:

    def __init__(self, name, price):
        '''Initializes the Product class with parameters : name, price'''

        self.name = name
        self.price = price

    def display_information(self):
        '''prints all the data attributes of Product object '''

        print(f"Product : {self.name}")
        print(f"Price : ₹{self.price}")

    def __str__(self):
        '''Returns the string format of this object, ready to be printed'''

        return f"Product : {self.name} \nPrice : ₹{self.price}"

    def __add__(self, other):
        '''overrides the (+) operator for this product'''

        return (self.price) + (other.price)

    def __mul__(self, quantity: int):
        '''overrides the (*) operator for this product'''

        return self.price * quantity


class Electronic_product(Product):

    def __init__(self, name, price, brand, model):
        '''
        Initializes the Electronic_product class with parameters from:
        Base class : name, price
        Derived class (Electronic_product) : brand, model
        '''

        super().__init__(name, price)  # inherited from base class "Product"

        self.brand = brand
        self.model = model

    def display_information(self):
        '''Overrides the base class "display_information()'''

        super().display_information()  # inherited from base class "Product"
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")

    def __str__(self):
        '''returns the string ready to be printed, with string derived from base class'''

        # inherited from base class "Product"
        return super().__str__() + f"\nBrand : {self.brand} \nModel : {self.model}"

    def __add__(self, other):
        '''overrides the (+) operator and returns from base class'''

        return super().__add__(other)  # inherited from base class "Product"

    def __mul__(self, quantity: int):
        '''overrides the (*) operator and returns from base class'''

        return super().__mul__(quantity)  # inherited from base class "Product"


class Clothing_product(Product):

    def __init__(self, name, price, Colour, Size):
        '''
        Initializes the Clothing_product class with parameters from:
        Base class : name, price
        Derived class (Clothing_product) : Colour, Size
        '''

        super().__init__(name, price)  # inherited from base class "Product"

        self.Colour = Colour
        self.Size = Size

    def display_information(self):
        '''Overrides the base class "display_information()'''

        super().display_information()  # inherited from base class "Product"
        print(f"Colour : {self.Colour}")
        print(f"Size : {self.Size}")

    def __str__(self):
        '''returns the string ready to be printed, with string derived from base class'''

        return super().__str__() + f"\nColour : {self.Colour} \nSize : {self.Size}"

    def __add__(self, other):
        '''overrides the (+) operator and returns from base class'''

        return super().__add__(other)  # inherited from base class "Product"

    def __mul__(self, quantity: int):
        '''overrides the (*) operator and returns from base class'''

        return super().__mul__(quantity)  # inherited from base class "Product"


def grocery_list(prod_list):
    '''
        grocery_list(prod_list) returns the combo price after taking in a grocery list

        Arguments:
            prod_list = list/tuple of lists/tuples with each sublist or subtuple, contains:
                            [ ( Product, Quantity, Discount(if any) ) ........]
                      = can be also a dictionary with Product as key
                            and (Quantity, Discount(if any))

        Returns:
            returns the combo price by calculating the price, quantity and discount for each product

    '''

    combo_price = 0
    if isinstance(prod_list, dict):  # if given argument is a list
        for elt in prod_list:
            if (type(prod_list[elt]) is int):  # if only quantity is given
                combo_price += elt.price * prod_list[elt]
            else:  # if quantity and discount is given
                combo_price += (elt.price - (elt.price *
                                prod_list[elt][1]/100)) * prod_list[elt][0]
    else:
        for elt in prod_list:  # if given argument is a list/tuple/set of tuples
            if len(elt) != 3:  # if quantity and discount not given
                combo_price += elt[0].price * elt[1]
            else:
                combo_price += (elt[0].price -
                                (elt[0].price * elt[2]/100)) * elt[1]
    return combo_price


if __name__ == "__main__":

    x1 = Product("Colgate Paste", 20)
    x2 = Electronic_product("Pendrive", 200, "sandisk", "22123x")
    x3 = Clothing_product("T-Shirt", 120, "red", "L")

    prod_list = [(x1, 5), (x2, 2, 5), (x3, 1, 25)]
    prod_list2 = {x1: 5, x2: (2, 5), x3: (1, 25)}

    print(x1 + x2)
    print(x1 + x3)
    print(x2 + x3)

    print(grocery_list(prod_list))
    print(grocery_list(prod_list2))

    print(x3 * 10)
