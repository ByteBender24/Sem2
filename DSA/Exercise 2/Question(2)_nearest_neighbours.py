'''
Write a Python code to generate a random sequence of n Points. Define a function
that, given an integer k and a new Point Pnew, returns k-nearest neighbours of Pnew
in the given sequence of n Points.
'''

#CREATOR INFO:
#REG. NO : 3122225002042
#NAME : HARISHRAJ S
#SEC : IT A

#DATE CREATED: 12/04/2023


from classpoint import Point        #Imported "Point" class from module "classpoint"
import random                       #Imported "Random" module

    
def random_pts_dist_generator(point=Point(0,0)):
    
    '''
    random_pts_dist_generator() function generates random 'Point' objects
    and stores it in a list of tuples, each tuple with (Point object, point, distance)

    arguments:
        point = Reference point object to find distance, can give, 
        or be taken as default argument which equals to Point(0,0)
    
    variables:
        n = number of 'Point' objects in list

    returns:
        seq = sequence/list of tuples, each tuple with (Point object, point, distance)
    '''

    seq = []            #list of tuple ((Point object, point, distance))
    seq_uniq = []       #to filter out point objects with attributes that are unique 
                        #and not same as given point in argument

    n = int(input("Enter number of points in this sequence: "))     #number of points are taken as input

    for times in range(n):          #iterated over n times to produce n Point objects
        x = random.randint(-10,10)
        y = random.randint(-10,10)
        p = Point(x,y)              #random point 'p'
        
        if ((p.x,p.y) not in seq_uniq) and point.distance(p) != 0:      #unique ones and not rememble the given point (argument)
            seq.append((p,(p.x,p.y),point.distance(p)))
            seq_uniq.append((p.x,p.y))
        else:
            continue
    
    del (seq_uniq)          #for space efficiency

    return (seq)
        
def nearest_neighbours(Pnew,k,seq):

    '''
    nearest_neighbours(Pnew,k,seq) takes three arguments
    It sorts the sequence of points(seq) and returns the first 'k' points
    
    arguments:
        Pnew = Point
        k = number of nearest neighbours to be returned
        seq = sequence/list of 'Point' objects
    
    returns:
        seq = list of nearest neighbours as 'Point' objects
    '''
    
    seq.sort(key = lambda x : x[2]) #Can use bubble sort algorithm also, but inefficient
                                    #x[2] is the distance, sorting using distance between Pnew and points

    seq = seq[0:k]      #first 'k' nearest neighbours (for space efficiency)

    if len(seq) != 0:           #if no random points generated, nothing is printed
        print (f"The {k} nearest neighbours of point {(Pnew.x,Pnew.y)} are: ")

        for idx in range(k):
            print (f"Point : {seq[idx][1]}  Distance : {Pnew.distance(seq[idx][0])}")
    
    return seq 


if __name__ == "__main__": 

    '''
    Following code will be executed only when this Python
    file is run directly.  Code will be ignored if this
    file is imported by another Python source.
    '''

    Pnew = Point(1,1)       #Reference point object
    k = 2                #number of point objects

    seq = random_pts_dist_generator()   #seq has returned list from this function

    if len(seq) == 0:
        print ("No random points generated.")
    else:       
        print ("Random points generated: ")     #all the random points produced are printed
        for elt in seq:
            # print (elt[1])
            pass

    nearest_neighbours(Pnew , k , seq)        
