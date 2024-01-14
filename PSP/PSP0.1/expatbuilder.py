#CREATOR INFO:
    #REG. NO : 3122225002042
    #NAME : HARISHRAJ S
    #SEC : IT A

#DATE CREATED: 24/04/2023

'''for path, copy the path of folder of all python files'''

# importing the os module to find out the python files
import os


def read_py_file(homepath):

    '''
    Opens the file passed to the function in read mode and return the data present in the file as a string

    Arguments:
        homepath (str): absolute path of the python program

    Return:
        str: source code present in the python file
    '''


    with open(homepath, "r") as filehandle:
        data = filehandle.read()
    filehandle.close()

    return data


def breakdown(filecontents, filehandle=None):


    '''
    Breaks down the source code and finds out the number of blank lines, single line comments, multi line comments,
    classes, methods and functions.

    Arguments:
        filecontents (str): source code of the python program
        filehandle (TextIOWrapper)

    return:
        dict: dictionary containing the number of blank lines, single line comments, multi line comments,
    classes, methods and functions.
    '''


    counter = {"LinesFiltered": 0,
               "Multiline": 0,
               "Comments": 0,
               "BlankLines": 0,
               "Functions": 0,
               "Classes": 0,
               "Methods": 0}
    
    isdocstring = False
    lines = filecontents.split("\n")
    print("Total LOC:", len(lines), file=filehandle)

    for line in lines:

        if isdocstring:

            if line.strip().endswith('"""') or line.strip().endswith("'''"):
                isdocstring = False
                counter["Multiline"] += 1
                continue

            counter["Multiline"] += 1
            continue

        if line.strip().startswith("#"):
            counter["Comments"] += 1
            continue

        elif line.strip() == "":
            counter["BlankLines"] += 1
            continue

        if line.strip().startswith("'''") or line.strip().startswith('"""'):
            counter["Multiline"] += 1
            isdocstring = True
            continue

        else:
            counter["LinesFiltered"] += 1

        if line.startswith("def"):
            counter["Functions"] += 1

        elif line.startswith("class"):
            counter["Classes"] += 1

        elif line.startswith("    def"):
            counter["Methods"] += 1

    return counter


def class_counter(src):


    '''
    Counts the number of lines in each class and return the name of each class along with its count.

    Arguments:
        src (str): source code of the python program

    return:
        dict: Dictionary containing the name of the class as key and number of lines in that respective class as value
    '''

    
    isdocstring = False
    classcodecounter = 0
    lines = src.split("\n")
    classcodedict = {}
    classname = None

    for line in lines:

        if line.strip().endswith('"""') or line.strip().endswith("'''"):
            isdocstring = False

        if isdocstring:
            if line.strip().endswith('"""') or line.strip().endswith("'''"):
                isdocstring = False
                continue
            continue

        if line.strip().startswith("#"):
            continue

        elif line.strip() == "":
            continue

        if line.strip().startswith("'''") or line.strip().startswith('"""'):
            isdocstring = True
            continue

        if line.strip().startswith("class"):
            classname = line.strip().split(" ")[1].split("(")[0]
            if isdocstring:
                if line.strip().endswith('"""') or line.strip().endswith("'''"):
                    isdocstring = False
                    continue
                continue

            if line.strip().startswith("#"):
                continue

            elif line.strip() == "":
                continue

            if line.strip().startswith("'''") or line.strip().startswith('"""'):
                isdocstring = True
                continue

            if line.startswith("    "):
                classcodecounter += 1

        else:
            if line.startswith("    "):
                classcodecounter += 1

            if line.split(" ")[0].isalpha():
                classcodedict[classname] = classcodecounter
                classname = None
                continue
    try:
        del classcodedict[None]

    except KeyError:
        pass

    return classcodedict


def method_counter(src):


    '''
    Counts the number of lines in each method and return the name of each method along with its count.

    Arguments:
        src (str): source code of the python program

    return:
        dict: Dictionary containing the name of the method as key and number of lines in that respective method as value
    '''


    isdocstring = False
    methodcodecounter = 0
    lines = src.split("\n")
    methodcodedict = {}
    methodname = None


    for line in lines:

        if isdocstring:
            if line.strip().endswith('"""') or line.strip().endswith("'''"):
                isdocstring = False
                continue
            continue

        if line.strip().startswith("#"):
            continue

        elif line.strip() == "":
            continue

        if line.strip().startswith("'''") or line.strip().startswith('"""'):
            isdocstring = True
            continue

        if not line.startswith("    def"):

            if line.startswith("        "):
                methodcodecounter += 1

            if line.strip().split(" ")[0].isalpha() and line.split(" ")[0] != "class" and not line.startswith("        "):
                methodcodedict[methodname] = methodcodecounter
                methodname = None
                methodcodecounter = 0
                continue

        elif line.strip().split(" ")[0].isalpha() and line.split(" ")[0] != "class" and not line.startswith("        "):
            
            methodcodedict[methodname] = methodcodecounter
            methodcodecounter = 0
            methodname = line.lstrip().split(" ")[1].split("(")[0]

            if isdocstring:
                if line.strip().endswith('"""') or line.strip().endswith("'''"):
                    isdocstring = False
                    continue
                continue

            if line.strip().startswith("#"):
                continue

            elif line.strip() == "":
                continue

            if line.strip().startswith("'''") or line.strip().startswith('"""'):
                isdocstring = True
                continue

            if line.startswith("        "):
                methodcodecounter += 1

    try:
        del methodcodedict[None]

    except KeyError:
        pass

    return methodcodedict


def function_counter(src):
    

    '''
    Counts the number of lines in each function and return the name of each function along with its count.

    Arguments:
        src (str): source code of the python program

    return: 
    
        dict: Dictionary containing the name of the function as key and number of lines in that respective
    function as value
    '''


    isdocstring = False
    functioncodecounter = 0
    lines = src.split("\n")
    functioncodedict = {}
    functionname = None

    for line in lines:

        if isdocstring:
            if line.strip().endswith('"""') or line.strip().endswith("'''"):
                isdocstring = False
                continue
            continue
        
        if line.strip().startswith("#"):
            continue

        elif line.strip() == "":
            continue

        if line.strip().startswith("'''") or line.strip().startswith('"""'):
            isdocstring = True
            continue

        if not line.startswith("def"):

            if line.startswith("    "):
                functioncodecounter += 1

            if line.strip().split(" ")[0].isalpha() and line.split(" ")[0] != "class" and not line.startswith("    "): 
                functioncodedict[functionname] = functioncodecounter
                functionname = None
                functioncodecounter = 0
                continue

        elif line.strip().split(" ")[0].isalpha() and line.split(" ")[0] != "class" and not line.startswith("    "): 
            functioncodedict[functionname] = functioncodecounter
            functioncodecounter = 0
            functionname = line.lstrip().split(" ")[1].split("(")[0]

            if isdocstring:
                if line.strip().endswith('"""') or line.strip().endswith("'''"):
                    isdocstring = False
                    continue
                continue

            if line.strip().startswith("#"):
                continue

            elif line.strip() == "":
                continue

            if line.strip().startswith("'''") or line.strip().startswith('"""'):
                isdocstring = True
                continue
            
            if line.startswith("    "):
                functioncodecounter += 1
    try:
        del functioncodedict[None]

    except KeyError:
        pass

    return functioncodedict


def other_lines(counterdict, classdict, functiondict):


    '''
    Calculates other lines of code by removing the above calculated LOC from total LOC

    Arguments: 
    
        counterdict (dict)
        classdict (dict) 
        functiondict (dict)

    return:
        int: other lines of code
    '''


    totalfilteredlines = counterdict["LinesFiltered"]
    classlines = sum(classdict.values()) + len(classdict)
    functionlines = sum(functiondict.values()) + len(functiondict)
    otherlines = totalfilteredlines - (classlines + functionlines)
    return otherlines


def traversefolder(homepath, filehandle=None):

    
    '''
    Traverses each folder and sub-folders recursively and finds out the
    python files, and does the above operations and writes the data
    to a file.

    Arguments: 
    
        homepath (str) 
        filehandle 
    '''


    pythonfiles = []
    for root, folders, files in os.walk(homepath):
        for file in files:
            if file.endswith(".py"):
                pythonfiles.append(os.path.join(root, file))

    for file in pythonfiles:
        print("----" * 6)

        print("File:", file)

        filecontents = read_py_file(file)
        counterdict = breakdown(filecontents, filehandle)
        classdict = class_counter(filecontents)
        methoddict = method_counter(filecontents)
        functiondict = function_counter(filecontents)
        otherlines = other_lines(counterdict, classdict, functiondict)

        print(f"Filtered LOC: {counterdict['LinesFiltered']}")
        print(f"Single Line Comments: {counterdict['Comments']}")
        print(f"Multi Line Comments: {counterdict['Multiline']}")
        print(f"Number of Functions: {counterdict['Functions']}")
        print(f"Number of Classes: {counterdict['Classes']}")
        print(f"Number of Methods: {counterdict['Methods']}")

        print("-------" * 4)
        print("Classes:")

        for classname, count in classdict.items():
            print(f"{classname} - {count}")

        print("-------" * 4)
        print("Methods:")

        for methodname, count in methoddict.items():
            print(f"{methodname} - {count}")

        print("-------" * 4)
        print("Functions:")

        for functionname, count in functiondict.items():
            print(f"{functionname} - {count}")

        print("-------" * 4)
        print(f"Other Lines: {otherlines}")

        print("----" * 6)


if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.


    homedir = input("Enter the home path to search for python files: ")

    with open(os.path.join(homedir, "loc.txt"), "w") as handle:
        traversefolder(homedir, handle)

    handle.close()
