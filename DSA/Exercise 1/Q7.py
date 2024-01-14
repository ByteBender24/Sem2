'''
Write a Python program that can “make change.” Your program should take two numbers as input, one
that is a monetary amount charged and the other that is a monetary amount given. It should then return
the number of each kind of bill and coin to give back as change for the difference between the amount
given and the amount charged. The values assigned to the bills and coins can be based on the monetary
system of any current or former government. For example, if we consider the current Indian rupee notes
and coins, and the input is (68, 100), then one answer could be “Three 10 rupee notes and two one rupee
coins”. Try to design your program so that it returns as few bills and coins as possible.
'''

#CREATOR INFO
#ROLL NO :3122225002042
#NAME    : Harishraj S
#SECTION : IT A

#DATE CREATED : 13-04-2023


def make_change(charged = 0 , given = 0):

    '''
    make_change(charged, given) is a function that finds the bills and coins 
    that are needed to be returned to the customer as change
    
    arguments:
        charged = amount charged by the shop to customer (maybe float, but here I assumed they are integer)
        given = amount given by customer to shop in return to bill (maybe float, but here I assumed they are integer)
        
        charged and given are default arguments with value 0, if no arguments are passed
        
    returns:
        returns the number of 10 rupee bills, 5,2,1 rupee coins
        
    Assumptions:
        Assumed INR 
        The money given and charged is obviously lesser than 100
        The denominations used are mostly 10 rupee bills, 5,2,1 rupee coins
        The money given and charged are not floating points, but integers (no paise is taken in order here)
    '''

    difference = given - charged

    count10 = 0
    while True:
        count10 += 1
        difference = difference - 10
        if difference < 10:
            break
        elif difference == 10:
            count10 += 1
            break

    if difference < 10 and difference >=5:
        count5 = 1
        difference = difference - 5
    elif difference < 10 and difference <5:
        count5 = 0

    count2 = 0
    while True:
        count2 += 1
        difference = difference - 2
        if difference != 2:
            break

    count1 = difference

    return (f"{count10} 'ten' rupee notes, {count5} 'five' rupee coins, {count2} 'two' rupee coins, {count1} 'one' rupee coins")

if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    charged = int(input("Enter charged amount by shop: "))
    given = int(input("Enter given amount by customer: "))
    print (make_change(charged,given))

'''
This code only works for denominations lesser than 100
This code is more of a prototype, and with sufficient time, it can be a beautiful code
So please give denominations lesser than 100
'''