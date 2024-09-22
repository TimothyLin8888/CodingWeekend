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
        text_file = open("ProjectLists.txt", "r")
        projects = [line.strip() for line in text_file]
    except:
        text_file = open("ProjectLists.txt", "x")

def add(create_list):
    print("test")
    add_project = input("What do you want to add?\n")
    try:
        text_file = open("ProjectLists.txt", "a")
        text_file.write(add_project)
    except:
        text_file = open("ProjectLists.txt", "x")

def remove(remove_line):
    print("remove")
    with open("ProjectLists.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != remove_line:
                f.write(i)
        f.truncate()
def main():
    projects = []
    while True:
        print("1) Add to the list of projects\n2) Remove from list of projects\n3) Choosing random project\n4) Break the loop")
        num = int(input())
        match num:
            case 1:
                print(projects)
                add(projects)
            case 2:
                print(2)
                remove("Amongus")
            case 3:
                print(3)
            case 4:
                break

main()