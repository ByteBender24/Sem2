#CREATOR INFO:
    #REG. NO : 3122225002042
    #NAME : HARISHRAJ S
    #SEC : IT A

#DATE CREATED: 24/04/2023

'''
This program contains functions
    1) startimer - marks the starttime
    
    2) endtimer - marks the endtime and returns the difference
    
    this is more accurate than time module functions as this gives more precision
'''

from datetime import datetime   #from datetime module, datetime method is imported

start_time = 0      #start time is initialized as zero

def starttimer():
    global start_time

    start_time = str(datetime.now())       #start time calculated with datetime module
    start_time = start_time[17:]                    #sliced from 17: denotes "seconds.microseconds"


def endtimer():
    end_time = str(datetime.now())         #end time calculated with datetime module
    end_time = end_time[17:]                        #sliced from 17: denotes "seconds.microseconds"
    return float(end_time) - float(start_time)      #runtime is returned
