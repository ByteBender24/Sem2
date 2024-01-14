'''Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns
the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions
min or max in implementing your solution. Suppose there are n elements in the input sequence, how
many comparisons are done by your function? Run your function for increasing values of n and observe
how the number of comparisons is increasing. What can you conclude from this experiment?'''

#3122225002042
#Harishraj S

import random
import datetime
import time

def minmax(data):
    comp=0
    for i in range(len(data) - 1):
        for j in range(0,len(data)-i-1):
            comp=comp+1
            if data[j] > data[j+1]:
                data[j+1] , data[j] = data[j] , data[j+1]
    return (data[0],data[len(data)-1]) , comp

if __name__ == "__main__":

    #for randomized sequence of data
    data =[]
    num_elt = 10

    for num in range(num_elt):
        data.append(random.randrange(-999,1000))

    #for calculation of run time
    start_time = time.time_ns()
    minmax(data)
    end_time = time.time_ns()
    print (end_time - start_time)

    #Results:
    # print (f"Sequence : {data}")                                                  #Input for function minmax(data)
    print (f"maximum & minimum:\n{minmax(data)[0]}")                                #Miminum and maximum in a tuple of length 2
    print (f"number of comparisons for {num_elt} elements: {minmax(data)[1]}")      #number of comparisons in the bubble sort algorithm used above

    print ()

'''
    #Relation between the number of elements and number of comparisons took place:
    print ("sum of numbers from n-1 to 0 is the relation between the number of elements and number of comparisons")
    next_num = num_elt-1

    def comparison(next_num):
        if next_num == 0:
            return 0
        else:
            return (next_num) + comparison(next_num - 1)
        
    print (comparison(next_num))
'''

