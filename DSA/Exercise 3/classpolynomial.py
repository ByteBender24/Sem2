from typing import Iterable

class Polynomial:

    def __init__(self , coeff = ((0,0))):
        
        '''Initializes the polynomial object with a list of tuples with tuple (degree, coeff) pairs
        or can be a list of lists, or can be a dictionary

        it can also be string of polynomial
        
        but it should follow the order (degree, coeff) not the other way around (coeff, degree)
        '''

        __slots__ = "degree" , "poly" ,"pairs"
        if isinstance(coeff , Iterable):
            if isinstance(coeff , list):
                coeff.sort(key = lambda x:x[0] , reverse = True)
                self.degree = coeff[0][0]
                self.pairs = list(coeff)
                self.poly = ""
                for elt in coeff:
                    self.poly += f"{elt[1]}*(x**{elt[0]}) + "
                self.poly = self.poly[:-3] 

            elif isinstance(coeff , tuple):
                list(coeff).sort(key = lambda x:x[0] , reverse = True)
                self.degree = coeff[0][0]
                self.pairs = list(coeff)
                self.poly = ""
                for elt in coeff:
                    self.poly += f"{elt[1]}*(x**{elt[0]}) + "
                self.poly = self.poly[:-3] 

            elif isinstance(coeff , dict):
                coeff = dict(sorted(coeff.items() , key = lambda x:x[0]))
                self.pairs = list(coeff.items())
                self.degree = list(coeff.items())[0][0]
                self.poly = ""
                for deg, cof in coeff.items():
                    self.poly += f"{cof}*(x**{deg}) + " 
                self.poly = self.poly[:-3]     
        if isinstance(coeff , str):
            self.poly = coeff.replace("^","**").replace("(","*(")
            
            coeff = coeff.replace(" ", "").replace("(","").replace(")","").replace("*","")
            terms = coeff.split('+')

            self.pairs = []
            for term in terms:
                term = term.strip()
                if 'x' in term:
                    coeff_str, degree_str = term.split('x')
                    coeff = float(coeff_str.strip())
                    if degree_str.strip() == '':
                        degree = 1
                    else:
                        degree = int(float(degree_str.strip("^")))
                else:
                    coeff = float(term.strip())
                    degree = 0
                self.pairs.append((coeff, degree))

            self.degree = self.pairs.sort(key = lambda x:x[0] , reverse= True)

    def display(self):

        return self.poly
    
    def __str__ (self):

        return self.poly.replace("**" , "^").replace("*","")
    
    def __len__ (self):
        
        return self.degree
    
    def __getitem__(self , degree):

        for deg, cof in self.pairs:
            if deg == degree:
                return cof
            
    def __setitem__(self, idx , tup):

        self.pairs[idx] = tup

    def evaluate(self , value):
        x = value
        return eval(self.poly)

    def polydegree(self):
        return self.degree
    
    def __add__ (self , other):

        new_poly = ""
        
        for deg1 , cof1 in self.pairs:
            for deg2, cof2 in other.pairs:
                if deg1 == deg2:
                    new_poly += f"{cof1 + cof2}*(x**{deg1}) + "
        new_poly = new_poly[:-3]

        return Polynomial(new_poly)
    
    def __mul__ (self, other):

        new_poly = ""
        
        for deg1 , cof1 in self.pairs:
            for deg2, cof2 in other.pairs:
                    new_poly +=  f"{(cof1*cof2)}*x**{(deg1 + deg2)} + "
        new_poly = new_poly[:-3]

        temp_poly = Polynomial(new_poly)
        temp_dict = {}
        for deg , cof in temp_poly.pairs:
            if deg not in temp_dict.keys():
                temp_dict[deg] = cof
            elif deg in temp_dict.keys():
                temp_dict[deg] += cof

        del temp_poly

        return Polynomial(temp_dict)


p = Polynomial(((1,2),(2,3)))
q = Polynomial ("1(x^2)")
print (q)
print (type(q))
print (q.display())
print (q)
print (q.evaluate(10))

print (p*q)
