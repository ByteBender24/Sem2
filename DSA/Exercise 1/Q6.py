'''The birthday paradox says that the probability that two people in a room will have the same birthday
is more than half, provided n, the number of people in the room, is more than 23. This property is
not really a paradox, but many people find it surprising. Design a Python program that can test this
paradox by a series of experiments on randomly generated birthdays, which test this paradox for n =
5,10,15,20,...,100.'''

#CREATOR INFO:
#ROLL NO :3122225002042
#NAME    : Harishraj S
#SECTION : IT A

#DATE CREATED : 13-04-2023


import random

def leapyear(year):

    '''
    leapyear(year) finds if the year is a leap year or not by Gregorian method
    
    arguments:
        year = year as integer
        
    returns: 
        True or False Boolean value based on whether it is leapyear or not    
    '''

    if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
        return True
    else :
        return False

def birthday_generator():

    '''
    birthday_generator() makes a random birthday out of randint function/method

    data values:
        year = year
        month = month 
        day = based on whether it is leapyear or not and based on month
        
    returns: 
        a birthday string in format DD-MM-YYYY   
    '''

    year = random.randint(1990,2023)
    
    month = random.randint(1,12)
    
    if month in [1,3,5,7,8,10,12]:
        date = random.randint(1,31)
    elif month == 2:
        if leapyear(year) is True :
            date = random.randint(1,29)
        if leapyear(year) is False:
            date = random.randint(1,28)
    else:
        date = random.randint(1,30)

    birthday = str(date) + "-" + str(month) + "-" + str(year)
    return birthday


def birthday_paradox_counter(people):

    '''
    birthday_paradox_counter(people) counts how many times there are people with same birthdays 
    in a group of people
    
    arguments:
        people = number of people in a group
        
    returns: 
        count value as integer value    
    '''

    birthdays = []
    for num in range(people):
        birthday = birthday_generator()
        birthdays.append(birthday)

    uniq_bday = []
    bday_histogram = {}

    for day in birthdays:
        if day not in uniq_bday:
            uniq_bday.append(day)
            bday_histogram[day] = 1
        elif day in uniq_bday:
            bday_histogram[day] += 1

    count = 0
    for value in bday_histogram.values():
        if value != 1:
            count += 1
    return count

def bday_probability_finder(people):

    '''
    bday_probability_finder(people) finds the probability of having people in a group with same birthday
    
    arguments:
        people = number of people
        used to pass in another function inside which is defined before (birthday_paradox_counter(people))

    returns:
        returns the probability value as a float    
    '''
    
    prob = []

    for i in range(10000):
        prob.append(birthday_paradox_counter(people))

    probability = (len(prob)-prob.count(0))/len(prob)   

    return probability

if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    people = int(input("Enter number of people (preferably less than 200): "))

    probability = bday_probability_finder(people)

    print (f"Probability of having a pair of people with same birthdays for a group of {people} people is {probability}")
        
