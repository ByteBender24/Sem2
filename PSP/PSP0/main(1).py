#CREATOR INFO:
    #REG. NO : 3122225002042
    #NAME : HARISHRAJ S
    #SEC : IT A

#DATE CREATED: 24/04/2023

#All necessary files are imported from modules

from histogram_words import uniq_words
from histogram_words import histogram_final
from histogram_words import word_histogram_maker

from histogram_words import write_txt_file
from histogram_words import create_file

from runtime import starttimer
from runtime import endtimer

from access_dir_file import filetaker
from access_dir_file import list_file


'''
This is the main module of the program for creating histogram and unique words from a set of files
This program takes in the path of homefolder, and two files are created
The histogram and unique words are written in those text files

homepath is given as input from user
'''

try:
    starttimer()    #from runtime module (created by me), starttimer is called, to start the time 


    #HOMEPATH SHOULD BE GIVEN MANUALLY BY USER IN THIS PROGRAM
    #there was no way for me convert a string to a raw string without using 'r'

    homepath = r"C:\Users\HARI\Desktop\New_folder"

    filetaker(homepath)         #stores all the file paths in list_file which is a global variable 
                                #list_file imported from access_dir_file module

    f1, f2 = create_file()

    #for each file, path is taken from list_file and 
    #each file is inserted into word_histogram maker, to return histogram
    #histogram for each file is finally stored in histogram_final with words and their frequency in all files

    for path in list_file:
        word_histogram_maker(path)
        
    write_txt_file(uniq_words, histogram_final, f1, f2)   #writes the histogram & unique words in file handles

    f1.close()
    f2.close()

    #from runtime module (created by me), endtimer is called, to calculate the runtime from starttime and printed

    print("RUNTIME:",endtimer())

except FileNotFoundError:
        print ('''HISTOGRAM_PATH MUST BE MANUALLY GIVEN BY USER HERE IN THIS PROGRAM
        There was no way for me to convert a string to raw string without using 'r' ''')