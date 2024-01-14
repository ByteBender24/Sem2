#CREATOR INFO:
    #REG. NO : 3122225002042
    #NAME : HARISHRAJ S
    #SEC : IT A

#DATE CREATED: 24/04/2023

'''
This module contains functions that
    1)word_histogram_maker(file) - makes a histogram when a path of a file is given
    
    2)create_file() - makes two file handles in write mode, returns two file handles
    one for unique words and another for histogram
    
    3)write_txt_file(uniq_words, histogram, f1, f2) writes the histogram as string and uniq words into the filehandles
'''


histogram_final = {}            #this stores all the words with frequency from all files

def word_histogram_maker(file):
    
    '''
    word_histogram_maker(file) returns all the unique words and 
    stores the words with frequency in a global variable "histogram_final"

    arguments:
        file - path of the file is given
    
    returns:
        returns the histogram and stores the words with frequency in a global variable "histogram_final"
    '''

    f = open(f"{file}", 'r', errors="ignore")           #errors are ignored, even with encoding = utf-8,there will be errors due to files made in linux OS

    global histogram_final          #global varible (stores all the words and frequency from all files)

    histogram = {}      

    for word in f.read().split():       #f.read().split() returns a list of words split by 'space'
        if word.isalpha():              #only returns alphabetic words (not symbols & numbers) reduces the runtime by 1 sec roughly
            if word in histogram:       #for finding frequency
                histogram[word] += 1
            elif word not in histogram:
                histogram[word] = 1      

    #for storing the words with frequency or increasing frequency if the word has already been there from another file
    for key in histogram.keys():
        if key in histogram_final.keys():
            histogram_final[key] += histogram[key]
        elif key not in histogram_final.keys():
            histogram_final[key] = histogram[key]
    
    f.close()
    
    return histogram_final , histogram  #retuns a tuple of two dictionaries (not efficient)

uniq_words = histogram_final.keys()     #unique words are the keys of dictionary histogram_final

def create_file():

    '''
    create_file() creates new files for writing and returns the file handles
    
    returns:
        fw - file handle of file 'words.txt' 
        fh - file handle of file 'words-histogram.txt  
    '''

    fw = open("words.txt", 'w' , errors = "ignore" )
    fh = open("words-histogram.txt", 'w' , errors = "ignore")

    return fw, fh


def write_txt_file(uniq_words, histogram_final , fw, fh):

    '''
    write_txt_file function writes the given unique words and histogram_final into the file handles fw & fh
    
    arguments:
        uniq_words - keys of histogram_final [list of words]
        histogram_final - dictionary with words and frequency
        fw, fh - file handles returned from create_file function
        
    returns:
        no returns, but write in the file handles fw & fh
    '''

    fh.write(str(histogram_final))      #writes the dictionary as a string, so that it can be evaluated for future use.

    for word in uniq_words:
        fw.write(word)
        fw.write("\n")

if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    file = r"C:\Users\HARI\Desktop\Visual Studio Code\Python\Semester 2\PSP0\bugs.txt"
    print (word_histogram_maker(file))
    fw, fh = create_file()
    write_txt_file(uniq_words, histogram_final ,fw , fh)
