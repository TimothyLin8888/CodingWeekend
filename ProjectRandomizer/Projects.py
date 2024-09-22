import random
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
        text_file.write(add_project.title() + "\n")
        projects.append(add_project.title())
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
    try:
        with open("ProjectRandomizer/ProjectLists.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i.strip("\n") != remove_line:
                    f.write(i)
                    continue
                try:
                    projects.remove(remove_line.title())
                except:
                    print("It isn't removed for a reason")
            f.truncate()
    except:
        print("Can't read the file")
def display_random_project(projects):
    '''
    Displays the random project so I can code a random coding project every weekend

    Parameters:
        projects - the list of projects to choose from

    Returns:
        None
    '''
    print(random.choice(projects))

def main():
    projects = []
    generate_list(projects)
    while True:
        print("1) Add to the list of projects\n2) Remove from list of projects\n3) Choosing random project\n4) Displays the projects\n5) Break the loop")
        try:
            num = int(input("Enter the number: "))
        except:
            print("Enter a number please")
            continue
        match num:
            case 1:
                print(projects)
                add(projects)
            case 2:
                print(projects)
                remove_line = input("Enter what you want to remove: ")
                removes(remove_line, projects)
            case 3:
                display_random_project(projects)
            case 4:
                print(projects)
            case 5:
                break

main()