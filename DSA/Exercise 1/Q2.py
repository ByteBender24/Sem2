'''Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns
the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions
min or max in implementing your solution. Suppose there are n elements in the input sequence, how
many comparisons are done by your function? Run your function for increasing values of n and observe
how the number of comparisons is increasing. What can you conclude from this experiment?'''

#CREATOR INFO:
#ROLL NO :3122225002042
#NAME    : Harishraj S
#SECTION : IT A

#DATE CREATED : 06-04-2023

import random
import datetime


def minmax(data):

    '''
    defining a function minmax(data) for finding the largest and smallest 
    numbers and return them in a tuple of length two
    '''
    try :
        comp=0                                                  #variable for number of comparisons made in this sorting algorithm
        for i in range(len(data) - 1):                          #used bubble sort algorithm to sort 
            for j in range(0,len(data)-i-1):
                comp=comp+1
                if data[j] > data[j+1]:
                    data[j+1] , data[j] = data[j] , data[j+1]
        return (data[0],data[len(data)-1]) , comp               #first element(minimum) & last element(maximum) in sorted array & number of comparisons are returned as a tuple pair like ((min,max),comparisons)
    except IndexError:
        return ("There are no elements in the given list")

if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    #for randomized sequence of data
    data =[]                                       #this variable has the randomized unsorted array
    num_elt = abs(int(input("Enter no.of elements in randomized data: ")))                                #number of elements in the unsorted randomized array (can be changed))
    
    for num in range(num_elt):
        data.append(random.randrange(-999,1000))
    

    #for calculation of run time
    start_time = str(datetime.datetime.now())       #start time calculated with datetime module
    start_time = start_time[17:]                    #sliced from 17: denotes "seconds.microseconds"
    
    print (f"start_time:{start_time}")
    minmax(data)

    end_time = str(datetime.datetime.now())         #end time calculated with datetime module
    end_time = end_time[17:]                        #sliced from 17: denotes "seconds.microseconds"

    print (f"end_time:{end_time}")   
    diff = float(end_time) - float(start_time)      #difference between the start and end time gives the time duration for this function of program to run (runtime)
    print (f"Runtime: {diff}")                                    #converted earlier 'str class' which was earlier 'datetime class' to 'float class'

    #Results:
    if type(minmax(data)) is tuple:
        print (f"Sequence : {data}")                                                  #Input for function minmax(data)
        print (f"maximum & minimum:\n{minmax(data)[0]}")                                #Miminum and maximum in a tuple of length 2
        print (f"number of comparisons for {num_elt} elements: {minmax(data)[1]}")      #number of comparisons in the bubble sort algorithm used above
    else:
        pass

    print ()

    #Relation between the number of elements and number of comparisons took place:
    print ("sum of numbers from n-1 to 0 is the relation between the number of elements and number of comparisons")
    