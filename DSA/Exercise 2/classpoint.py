class Point :
    
    
    def __init__ (self, a=0 , b=0):

        #instance attributes = a,b (x & y co-ordinates in space)

        self.x = a
        self.y = b
    
    def distance (self, p):

        #distance is calculated by two point formul

        dist = ((self.x - p.x)**2 + (self.y - p.y)**2)**(1/2)

        return dist
    