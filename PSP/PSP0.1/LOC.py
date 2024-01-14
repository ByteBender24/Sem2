homepath = r"D:\Python\Semester 2\PSP0.1\expatbuilder.py"

tot_new_line_comments = 0
tot_side_line_comments = 0
tot_blank_lines = 0
tot_docstrings = 0

def comment_blank_remover(homepath):

    global tot_new_line_comments 
    global tot_side_line_comments 
    global tot_blank_lines 
    global tot_docstrings 

    new_line_comments = 0
    side_line_comments = 0                      
    blank_lines = 0
    docstrings = 0

    f = open(homepath , 'r')
    f_temp = open('temp.txt' , 'w+')
    
    lines = f.readlines()
    lines_temp = lines.copy()
    
    try:
        for line in lines:
            if line.strip().startswith("#"):
                new_line_comments += 1
                lines_temp.remove(line)

            elif line == "\n":
                blank_lines += 1
                lines_temp.remove(line)
            
            elif line.strip().startswith("'''"):

                    if line.strip() == "'''" :
                        lines_temp.remove(line)
                        for docline in lines[lines.index(line)+1 :]:
                            lines_temp.remove(docline)
                            if docline.strip() == "'''" :
                                docstrings += 1
                                break

                    elif (line.strip() != "'''") and (line.strip().endswith("'''") == True):
                        lines_temp.remove(line)
                        docstrings += 1
    except ValueError:
        pass
        
    tot_new_line_comments += new_line_comments
    tot_side_line_comments += side_line_comments
    tot_blank_lines += blank_lines
    tot_docstrings += docstrings


    print (side_line_comments, new_line_comments , blank_lines, docstrings)
    f_temp.writelines(lines_temp)
    return f_temp.read()


codelines = comment_blank_remover(homepath)  

# def loc_finder(codelines):
    
    

# print (loc_finder(codelines))
print (tot_side_line_comments, tot_blank_lines , tot_docstrings , tot_new_line_comments)