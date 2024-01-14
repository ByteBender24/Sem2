#CREATOR INFO:
    #REG. NO : 3122225002042
    #NAME : HARISHRAJ S
    #SEC : IT A

#DATE CREATED: 24/04/2023

'''
This module consists of functions
    1) suggestion_maker(histogram_path , word) - returns the top 5(num) suggestions for given word based on frequency

The main module of this questions, works only when the first question is run.    
The main module for testing this functions for 2nd question are also here
'''

def suggestion_maker(histogram_path , word):
    
    '''
    suggestion_maker(histogram_path, word) returns the top 5 suggestions of given word,
    based on the frequency of histogram in the file path given as histogram_path
    
    arguments:
        histogram_path - path of txt file containing the histogram
        word - word that needs suggestions
    
    returns:
        returns the top 5 suggestions[list] for given word based on histogram
    '''


    with open (histogram_path) as fh:       #fh is file handle
        histogram = eval(fh.read())         #fh.read() is a string of dictionary, which is then evaluated and assigned to histogram
                                            #histogram is of dictionary class

    #histogram is sorted in descending order based on frequency of words 
    #occured in a given number of files (which was done in question 1)

    histogram_sorted = dict(sorted(histogram.items() , key = lambda x: x[1] , reverse = True))  
    
    num = 5         #can be changed (No.of suggestions)

    suggestions = []

    for key in histogram_sorted.keys():
        if key.startswith(word):
            suggestions.append((key , histogram_sorted[key]))       #if the keys starts with the 'word', then they are added in suggestions(list)
            num = num - 1
        if num == 0:        #this is to make sure that only the 'num' no of suggestions are added
            break
        
    return  suggestions

if __name__ == "__main__":


    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    try:
        #HISTOGRAM_PATH MUST BE MANUALLY GIVEN BY USER HERE IN THIS PROGRAM
        #There was no way for me to convert a string to raw string without using 'r'

        histogram_path = r"D:\Python\words-histogram.txt"

        old_word = "SEARCH: "
        search_word = ""

        while True:
            

            '''
            This loop is designed for replicating the dynamic finish of google search
            This is not dynamic like google search, but an attempt to achieve this
            
            The ontime typing and suggestions cannot be replicated, but it can be done by pressing ENTER

            Press TAB and then ENTER to intimate that the word you want to search is finally typed.
            
            old_word and search_word are also present for this dynamic finish (so don't get confused)

            #ncurses - for dynamic usage in linux           (a suggestion for further development)
            '''
        

            print ("Press TAB & then ENTER key to finish your word finally")
            print()        

            word = input(f"{old_word}")
            print()
            search_word += word
            suggestions = suggestion_maker(histogram_path , search_word)
            for words , count in suggestions:
                print (words , count)
            old_word += word
            
            print ()
            if word.endswith("\t"):         #for stopping loop, press TAB and ENTER, so that the string is ended with escape character "\t"
                suggestions = suggestion_maker(histogram_path , search_word)
                for words , count in suggestions:
                    print (words , count)
                break
    except FileNotFoundError:
        print ('''HISTOGRAM_PATH MUST BE MANUALLY GIVEN BY USER HERE IN THIS PROGRAM
        There was no way for me to convert a string to raw string without using 'r' ''')