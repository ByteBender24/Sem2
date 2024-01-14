'''Write a short Python function that takes a sequence of integer values and determines if there is a distinct
pair of numbers in the sequence whose product is odd. How many pairs do you need to consider, in the
worst case, to find the answer?'''

#CREATOR INFO:
#ROLL NO :3122225002042
#NAME    : Harishraj S
#SECTION : IT A

#DATE CREATED : 09-04-2023


def random_seq_generator():

    '''Function random_seq_generator() generates a random sequence based on 
    no.of elements in sequence given as input.
    The output is a list of elements in a sequence.'''  

    import random
    seq = []
    num = abs(int(input("Enter no. of elements in sequence: ")))
    for times in range(num):
        seq.append(random.randint(-99,99))
    return seq

def odd_multiple_pair_maker(seq):
    
    '''
    Function odd_multiple_pair_maker(seq) takes a sequence (list) as argument
    Returns all pairs of elements whose product is a odd number'''

    pair_list = []
    for num1 in seq:
        for num2 in seq[(seq.index(num1)+1):]:
            if (num1 * num2) % 2 != 0:
                pair_list.append((num1,num2))
    return pair_list

if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    seq = random_seq_generator()        #returned value of this function (list/sequence) is set in variable 'seq'
    print (f"Sequence:\n{seq}")

    print ("The pairs whose multiple is odd are given below: ")
    print (odd_multiple_pair_maker(seq))    #'seq' is given as argument and returned value is printed.


'''The worst case possible scenario is that all pairs are giving the output as even, 
that all elements are even.
hence no pair that gives us the odd value when multiplied.'''


'''Also to find how many pairs we can find for each array of elements, we use 
To find the number of possible pairs in the worst case, we need to use the formula for the number of combinations. The formula is:
C(n, r) = n! / (r! * (n-r)!)
where n is the total number of objects, and r is the number of objects we want to select from the total. In this case, we want to select 2 integers from the sequence, so r=2.
The total number of possible pairs we can form from the sequence is equal to C(n, 2). Substituting n=2, we get:
C(n, 2) = n! / (2! * (n-2)!) = n * (n-1) / 2
Therefore, in the worst case where all the integers are even, we need to consider (n * (n-1)) / 2 pairs of integers to determine if there is a distinct pair whose product is odd.'''
