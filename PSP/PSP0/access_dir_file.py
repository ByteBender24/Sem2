#CREATOR INFO:
    #REG. NO : 3122225002042
    #NAME : HARISHRAJ S
    #SEC : IT A

#DATE CREATED: 24/04/2023

'''
This module has the methods and functions to access directories and files 
inside of a extracted zip file
'''

import os  # os module is imported

list_file = []      #contains all the paths of all files inside all directories


def filetaker(homepath):

    '''
    filetaker(homepath) takes in path and collects all the text files from path and 
    stores in a global variable 'list_file'
    
    global variable :
        list_file - list of paths of text files

    arguments:
        homepath of all files (mother folder path)
    returns:
        no returns
    '''

    global list_file            #list_file is made global as it is changed for every path

    for elt in os.listdir(homepath):
        if elt.endswith(".txt"):            #only returns paths of text files, can be changed by preference
            list_file.append(os.path.join(homepath, elt))
        else:
            filetaker(os.path.join(homepath, elt))



'''
for avoiding recursion error:

for root, folders, files in os.walk(homepath):
    for file in files:
        if file.endswith(".txt"):
            list_file.append(os.path().join(roots , files))

or use:

import sys 
sys.setrecursionlimit(10000)
'''

if __name__ == "__main__":
    
    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    
    homepath = r"C:\Users\HARI\Desktop\python-3.11.3-docs-text"

    filetaker(homepath)
