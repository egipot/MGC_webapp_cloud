FILEPATH = 'tasks.txt'


#custom function to avoid redundant code
def get_tasks(filepath_r=FILEPATH):
    """
    Read a text file and return the list of to do items.
    """
    with open(filepath_r,'r') as getfile_local:
        gettasks_local = getfile_local.readlines()
    return gettasks_local 


def write_tasks(tasks_arg, filepath_w=FILEPATH):
    """
    Write the new/updated list of to do items
    into the existing text file.
    """
    with open(filepath_w,'w') as writefile_local:
        writefile_local.writelines(tasks_arg)
 

#print(__name__) #prints "function" when the main.py is run (due to import function command)

#conditional block
#But when you run functions.py directly, the value of that variable is __main__.
#And that allows us to have this condition here.
if __name__ == '__main__':
    print('Hello')
    print(get_tasks())