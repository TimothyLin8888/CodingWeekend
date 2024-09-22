def generate_list(projects):
    '''
    It generates a list from 'ProjectList.txt' which makes a list
    so that I can choose a random project from the list

    Parameters:
        projects - it is the list that holds the projects

    Returns:
        None
    '''
    try:
        text_file = open("ProjectRandomizer/ProjectLists.txt", "r")
        for line in text_file:
            projects.append(line.strip())
    except:
        text_file = open("ProjectLists.txt", "x")

def add(projects):
    '''
    It adds to 'ProjectsLists.txt' so that it is able to be written in without
    needing to enter the file.

    Parameters:
        None
    
    Returns:
        None
    '''
    add_project = input("What do you want to add?\n")
    try:
        text_file = open("ProjectRandomizer/ProjectLists.txt", "a")
        text_file.write(add_project + "\n")
        projects.append(add_project)
    except:
        text_file = open("ProjectLists.txt", "x")

def removes(remove_line, projects):
    '''
    It removes from project from the list and removes it from the text file
    'ProjectsLists.txt'

    Parameters:
        remove_line - the project you want to remove
        projects - the list that holds the projects

    Returns:
        None
    '''
    print("remove")
    with open("ProjectRandomizer/ProjectLists.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i.strip("\n") != remove_line:
                f.write(i)
                continue
            projects.remove(remove_line)
        f.truncate()
        
def main():
    projects = []
    generate_list(projects)
    while True:
        print("1) Add to the list of projects\n2) Remove from list of projects\n3) Choosing random project\n4) Break the loop")
        num = int(input())
        match num:
            case 1:
                print(projects)
                add(projects)
            case 2:
                print(projects)
                remove_line = input("Enter what you want to remove: ")
                removes(remove_line, projects)
            case 3:
                print(projects)
            case 4:
                break

main()