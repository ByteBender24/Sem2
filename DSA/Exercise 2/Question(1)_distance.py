'''
Define a class Point, a simple class to represent 2-dimensional points (Non-mutable). Each
object has two fields: '_x' and '_y'. Methods include 'distance' that returns Euclidean
distance between 'this' object and another object.
'''

#CREATOR INFO:
#REG. NO : 3122225002042
#NAME : HARISHRAJ S
#SEC : IT A

#DATE CREATED: 12/04/2023

from classpoint import Point
import random

def random_points_generator():
    
    '''
    random_points_generator produces random point objects and stores them in a list
    
    returns:
        seq = list of random 'Point' objects
    '''

    seq = []            #stores list of random point objects

    n = int(input("Enter number of points in this sequence: "))     #number of point objects in list

    for times in range(n):              #iterated n times, random point objects are produced
        x = random.randint(-10,10)
        y = random.randint(-10,10)
        seq.append(Point(x,y))
    
    return seq          #list of random point objects is returned

if __name__ == "__main__" : 

    '''
    Following code will be executed only when this Python
    file is run directly.  Code will be ignored if this
    file is imported by another Python source.
    '''

    p1  = Point(0,0)            #reference point
    #distance is calculated by "distance" method in Class "Point"
    
    for point in random_points_generator():
        print (f"Distance from point {(p1.x,p1.y)} to point {(point.x,point.y)} is: {p1.distance(point)} units")

    try:
        p2 = Point(5.1, 0,0)
        print (p1.distance(p2))
    except TypeError:
        print ("Enter correct number of space co-ordinates")