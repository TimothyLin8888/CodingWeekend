import random
import time;
# from pydub import AudioSegment
# from pydub.playback import play
# import os
def generate_list(projects, completed_projects):
    '''
    It generates a list from 'ProjectList.txt' which makes a list
    so that I can choose a random project from the list

    Parameters:
        projects - it is the list that holds the projects
        completed_projects - it is the list that holds the completed projects

    Returns:
        None - It adds the projects to the available or completed list of projects
    '''
    try:
        with open("ProjectRandomizer/ProjectLists.txt", "r") as text_file:
            for line in text_file:
                projects.append(line.strip())
        with open("ProjectRandomizer/CompletedProjectLists.txt", "r") as text:
            for line in text:
                completed_projects.append(line.strip())
    except:
        print("File unavailable")

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
        with open("ProjectRandomizer/ProjectLists.txt", "a") as text_file:
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
    countdown = 5
    # file_path = 'ProjectRandomizer/SlotMachine.mp3'
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    print(random.choice(projects))
def completed(projects, add_project, date):
    '''
    Writes the completed project to 'CompletedProjectLists.txt'
    Also appends the completed project to the completed projects list

    Parameters:
        projects - the list of completed projects that it appends the projects and date to
        add_project - the project that gets added to the projects list
        date - the date that the project was completed

    Returns:
        None
    '''
    try:
        with open("ProjectRandomizer/CompletedProjectLists.txt", "a") as text_file:
            text_file.write(add_project.title() + " | " + date + "\n")
            projects.append(add_project.title() + " | " + date)
    except:
        with open("CompletedProjectLists.txt", "x") as text_file:
            text_file.write(add_project.title() + " | " + date + "\n")

def main():
    projects = []
    completed_projects = []
    generate_list(projects, completed_projects)
    while True:
        print("1) Add to the list of projects\n2) Remove from list of projects\n3) Choosing random project\n4) Displays the projects\n5) Complete a project\n6) Break the loop")
        try:
            num = int(input("Enter the number: "))
        except:
            print("Enter a number please")
            continue
        match num:
            case 1:
                add(projects)
            case 2:
                remove_line = input("Enter what you want to remove: ")
                removes(remove_line, projects)
            case 3:
                display_random_project(projects)
                input("Press Enter to continue: ")
            case 4:
                choice = input("Would you like to see available projects or completed projects A/C: ")
                if choice.lower() == 'a':
                    print(projects)
                elif choice.lower() == 'c':
                    print(completed_projects)
                else:
                    print("Unavailable\n")
                input("Press Enter to continue: ")
            case 5:
                print(projects)
                project = input("What project did you complete? ")
                date = input("What's today's date? ")
                completed(completed_projects, project, date)
            case 6:
                break

main()