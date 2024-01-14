# Author        : Singaram PL
# Date          : 15/4/23
# Register      : 3122 22 5002 130
# Exercise      : PSP0.1
# Objective     : To read every py file in the given zip file and
# to count the number of modules, sub modules, etc.. and their loc
# without including comment lines, doc string.


def is_comment_line(line):
    """
    This function checks if a given line is a comment line.
    :param line: str
    :return: bool
    """
    hash = line.find('#')
    single3, double3 = line.find("\'\'\'"), line.find("\"\"\"")
    single, double = line.find("\'"), line.find("\"")
    rsingle3, rdouble3 = line.rfind("\'\'\'"), line.rfind("\"\"\"")
    rsingle, rdouble = line.rfind("\'"), line.rfind("\"")
    
    # Check if the line starts with a hash symbol
    hash_cond = ((line.count(' ', 0, hash) == len(line[0:hash])) and hash != -1)
    
    # Check if the line is empty or contains only spaces
    space_cond = (line.count(' ') == len(line))
    
    # Check if the line is a new line character
    new_line_cond = ((line == "\n") or (line == '\n'))
    
    # Check if the line starts and ends with single quotes
    single_quote_cond = ((line.count(' ', 0, single) == 
                          len(line[0:single])) and
                         (line.count(' ', rsingle + 1) == 
                          len(line[rsingle + 2:])) and (rsingle != -1))
    
    # Check if the line starts and ends with double quotes
    double_quote_cond = ((line.count(' ', 0, double) == 
                          len(line[0:double])) and 
                         (line.count(' ', rdouble + 1) == 
                          len(line[rdouble + 2:])) and (rdouble != -1))
    
    # Check if the line starts and ends with triple single quotes
    single3_quote_cond = ((line.count(' ', 0, single3) == 
                           len(line[0:single3])) and
                          (line.count(' ', rsingle3 + 3) == 
                           len(line[rsingle3 + 4:])) and (rsingle3 != -1))
    
    # Check if the line starts and ends with triple double quotes
    double3_quote_cond = ((line.count(' ', 0, double3) == 
                           len(line[0:double3])) and 
                          (line.count(' ', rdouble3 + 3) == 
                           len(line[rdouble3 + 4:])) and (rdouble3 != -1))
    
    # Return True if any of the conditions are met
    if (hash_cond or single_quote_cond or double_quote_cond or
        single3_quote_cond or double3_quote_cond or 
        space_cond or new_line_cond):
        return True
    
    # Return False otherwise
    else:
        return False


def end_of_multiline_comment(line_ind, lines):
    """
    This function checks if a given line is the 
    end of a multiline comment.

    :param line_ind: int
    :param lines: list of str
    :return: int or bool
    """
    single3 = lines[line_ind].find("\'\'\'")
    double3 = lines[line_ind].find("\"\"\"")
    rsingle3 = lines[line_ind].rfind("\'\'\'")
    rdouble3 = lines[line_ind].rfind("\"\"\"")
    
    # Check if the line starts with triple single or triple double quotes
    if (((lines[line_ind].count(' ', 0, single3) == 
          len(lines[line_ind][0:single3]) and single3 != -1) and
        not(lines[line_ind].count(' ', rsingle3 + 3) == 
            len(lines[line_ind][rsingle3 + 4:])) and rsingle3 != -1) or
        ((lines[line_ind].count(' ', 0, double3) == 
          len(lines[line_ind][0:double3]) and double3 != -1) and
        not(lines[line_ind].count(' ', rdouble3 + 3) == 
            len(lines[line_ind][rdouble3 + 4:]) and rdouble3 != -1))):
        
        # Check for the end of the multiline comment in the following lines
        for line in lines[line_ind + 1:]:
            rsingle3_end = line.rfind("\'\'\'")
            rdouble3_end = line.rfind("\"\"\"")
            
            # Check if the line ends with triple single or
            #  triple double quotes
            if (((line.count(' ', rsingle3_end + 3) == 
                len(line[rsingle3_end + 4:])) and rsingle3_end != -1) or
                ((line.count(' ', rdouble3_end + 3) == 
                len(line[rdouble3_end + 4:]))) and rdouble3_end != -1):
                
                # Return the index of the line that ends the 
                # multiline comment
                end = lines.index(line, line_ind + 1)
                return end
    
    # Return False if no multiline comment is found
    else:
        return False


def loc_of_block(lines, tup):
    """
    This function counts the number of non-comment
    lines in a block of code.
    :param lines: list of str
    :param tup: tuple of int
    :return: int
    """
    start, end = tup
    loc = 0
    end_multi_ind = -1
    
    # Iterate over the lines in the given range
    for line in lines[start:end + 1]:
        ind = lines.index(line, start)
        
        # Skip lines that are part of a multiline comment
        if ind <= end_multi_ind:
            continue
        
        # Check for the end of a multiline comment
        end_2 = end_of_multiline_comment(ind, lines)
        if end_2 == False:
            end_multi_ind = -1
        else:
            end_multi_ind = end_2
            continue
        
        # Increment the count if the line is not a comment line
        if not(is_comment_line(line)):
            loc += 1
    
    # Return the count of non-comment lines
    return loc


def blocks_identifier(lines, start=0, end=0, class_methods=False):
    """
    This function identifies the positions of blocks of code in a list of lines.
    :param lines: list of str
    :param start: int
    :param end: int
    :param class_methods: bool
    :return: dict or list
    """
    blocks_pos_dic = {"main": (0, len(lines) - 1), "class": [], "function": []}

    def end_finder(start_1, indent=' '):
        """
        This function finds the end of a block of code.
        :param start_1: int
        :param indent: str
        :return: int
        """
        exe_lines = False
        for i in range(start_1 + 1, len(lines)):
            if lines[i].startswith(indent) and not(is_comment_line(lines[i])):
                end_1 = i
                exe_lines = True
            
            # If block has only comments.
            elif (lines[i].startswith(indent) and is_comment_line(lines[i])) and not(exe_lines):
                end_1 = start_1
            
            # To find the block end.
            elif not(lines[i].startswith(indent)) and not(is_comment_line(lines[i])):
                break
        return end_1

    if class_methods == False:
        for i in range(len(lines)):
            if lines[i].startswith('class '):
                start = i
                end = end_finder(start)
                class_lst = blocks_identifier(lines, start, end, True)
                blocks_pos_dic["class"].append(class_lst)
            if lines[i].startswith('def '):
                start = i
                end = end_finder(start)
                blocks_pos_dic["function"] += ((start, end),)
    
    elif class_methods == True:
        class_lst = [(start, end)]  # Here start, end refers to the class
        for line in lines[start + 1:end + 1]:
            if line.find('def ') != -1:
                start_pos_method = lines.index(line, start)
                nxt_line = lines[start_pos_method + 1]
                for k in range(len(nxt_line)):
                    if nxt_line[k] != ' ':
                        indent = nxt_line[:k]
                        break
                end_pos_method = end_finder(start_pos_method, indent)
                class_lst.append((start_pos_method, end_pos_method))
        return class_lst
    
    return blocks_pos_dic
            

def sub_module_reader(path):
    """
    This function reads a Python file and prints information about its structure.
    :param path: str
    :return: int
    """
    global loc_of_package
    with open(path) as file:
        lines_lst = file.readlines()
        blocks_pos_dic = blocks_identifier(lines_lst)
        main_tup = blocks_pos_dic["main"]
        loc_main = loc_of_block(lines_lst, main_tup)
        classes = len(blocks_pos_dic["class"])
        functions = len(blocks_pos_dic["function"])
        loc_of_package += loc_main
        tot_loc_others = 0
        loc_of_functions_lst = []
        
        # Calculate the LOC of each function
        for tup in blocks_pos_dic["function"]:
            loc_of_function = loc_of_block(lines_lst, tup)
            tot_loc_others += loc_of_function
            loc_of_functions_lst.append(loc_of_function)
        
        print(f"\nloc of submodule            : {loc_main}")
        print(f"no of classes               : {classes}")
        print(f"no of independent functions : {functions}, loc : {loc_of_functions_lst}\n")
        
        i = 1
        
        # Calculate the LOC of each class and its methods
        for class_x_lst in blocks_pos_dic["class"]:
            no_of_methods = len(class_x_lst[1:])
            class_tup = class_x_lst[0]
            loc_of_class = loc_of_block(lines_lst, class_tup)
            tot_loc_others += loc_of_class
            loc_of_methods_lst = []
            
            for tup in class_x_lst[1:]:
                loc_method = loc_of_block(lines_lst, tup)
                loc_of_methods_lst.append(loc_method)
            
            print(f"for class {i}: loc : {loc_of_class},\tno of methods : {no_of_methods},\tloc of methods : {loc_of_methods_lst}")
            i += 1
        
        print(f"\nno of other loc : {loc_main - tot_loc_others}")
        
        # Return the LOC of the submodule
        return loc_main


# Main program runs if it is only called inside the file.
if __name__ == "__main__":
    
    import os
    from zipfile import ZipFile
    
    # Extract the contents of the zip file
    with ZipFile(r"D:\Python\Singaram-UIT2201-psp-ex-02.zip\xml.zip") as zip:
        zip.extractall()
        print("\nExtraction is successfull.")
    
    loc_of_package = 0
    j = 1
    
    # Iterate over the directories and files in the extracted package
    for package, dirs, sub_modules in os.walk("xml", topdown=True):
        if dirs != []:
            no_of_modules = len(dirs)
        else:
            print(f"\nModule {j} : ")
            j += 1
        
        loc_module = 0
        print("\n", "-" * 95, "\n")
        
        # Iterate over the submodules in the current directory
        for sub_module in sub_modules:
            i = sub_modules.index(sub_module)
            path = package + '\\' + sub_module
            print(f"\nsub-module {i + 1} : {path}")
            
            # Calculate the LOC of the submodule
            loc_sub_module = sub_module_reader(path)
            print("-" * 95)
            loc_module += loc_sub_module
        
        print(f"no of sub-modules : {len(sub_modules)}")
        print(f"loc of module     : {loc_module}")
        print("\n", "-" * 95)
        print("-" * 95, "\n")
    
    # Print the total number of modules and LOC of the package
    print(f"\nTotal no of modules : {no_of_modules}")
    print(f"LOC of Package      : ", loc_of_package)
    # End of the program