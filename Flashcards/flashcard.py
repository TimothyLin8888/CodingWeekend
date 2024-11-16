import random
def load_flashcards(file_path):
    '''
    Loads the flashcards into the flashcards list.

    Parameters:
        file_path - the file path that it accesses.
        flashcards - the list of flashcards it loads.

    Returns:
        flashcards - so it can load it into the list.
    '''
    flashcards = []
    with open(file_path, "r") as file:
        for line in file:
            question, answer = line.strip().split('->', 1)  # Split by arrow, only once
            flashcards.append({"question": question, "answer": answer})
    return flashcards

def create_flashcards(file_path):
    '''
    Creates the flashcards into a file.

    Parameters:
        file_path - the file path that it writes into
    
    Returns:
        None
    '''
    with open(file_path, "w") as file:
        while True:
            question = input("Enter your question or Quit: ")
            if question.title() == "Quit":
                break
            answer = input("Enter the answer: ")
            file.write(f"{question}->{answer}\n")


def add_flashcards(file_path):
    '''
    Adds the flashcards into the speicfied file.

    Parameters:
        file_path - the file path that it writes into
    
    Returns:
        None
    '''
    with open(file_path, "a") as file:
        while True:
            question = input("Enter your question or Quit: ")
            if question.title() == "Quit":
                break
            answer = input("Enter the answer: ")
            file.write(f"{question}->{answer}\n")

def edit_flashcards(file_path):
    '''
    Edits the flashcards in case of mistakes in typing.

    Parameters:
        file_path - the file path that it writes into
    
    Returns:
        None
    '''
    flashcards = []
    load_flashcards(file_path, flashcards)
    for i, flashcard in enumerate(flashcards):
        print(f"{i + 1}: {flashcard['question']} -> {flashcard['answer']}")
    try:
        index = int(input("Enter the number of the flashcard to edit: ")) - 1
        if 0 <= index < len(flashcards):
            new_question = input("Enter new question (leave blank to keep current): ")
            new_answer = input("Enter new answer (leave blank to keep current): ")
            
            if new_question:
                flashcards[index]["question"] = new_question
            if new_answer:
                flashcards[index]["answer"] = new_answer
            
            with open(file_path, "w") as file:
                for card in flashcards:
                    file.write(f"{card['question']}->{card['answer']}\n")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def start_flashcards(file_path):
    '''
    It starts the flashcards to review. You can do it in order or random

    Parameters:
        file_path - the file path that it writes into
    
    Returns:
        None
    '''
    flashcards = load_flashcards(file_path)
    choice = input("In order or random: order/rand: ")
    if choice == "order":
        for card in flashcards:
            print(f"Question: {card['question']}")
            quit = input("Press Enter to see the answer or quit: ")
            # Display the answer
            if quit == "quit":
                break
            print(f"Answer: {card['answer']}\n")
    elif choice == "rand":
        random.shuffle(flashcards)
        for card in flashcards:
            print(f"Question: {card['question']}")
            quit = input("Press Enter to see the answer or quit: ")
            # Display the answer
            if quit == "quit":
                break
            print(f"Answer: {card['answer']}\n")
def reverse_questions_and_answers(file_path):
    '''
    This reverses the questions and answers in case
    you put it into quizlet in the other way like I did.
    Quizlet has a feature to review by term or definition
    so if you want to review a way, you will reverse the txt file
    here.

    Parameters:
        file_path - the file path that it writes into
    
    Returns:
        None
    '''
    reversed_flashcards = []

    # Load and reverse the flashcards
    with open(file_path, "r") as file:
        for line in file:
            # Split the line by the delimiter
            answer, question = line.strip().split('->', 1)
            reversed_flashcards.append(f"{question.strip()}->{answer.strip()}")  # Reverse the order

    # Write the reversed flashcards to the output file
    with open(file_path, "w") as file:
        for flashcard in reversed_flashcards:
            file.write(f"{flashcard}\n")

def main():
    while True:
        print("1) Create Flashcards\n2) Add Flashcards\n3) Edit Flashcards\n4) Start Flashcards\n5) Reverse the Flashcard's terms and definitions\n6) Break")
        try:
            num = int(input("Enter the number: "))
        except:
            print("Enter a number please")
            continue
        match num:
            case 1: # Create Flashcards
                file = input("What file do you want to create: ")
                file_path = f"Flashcards/{file}"
                create_flashcards(file_path)
                continue
            case 2: # Add Flashcards
                file = input("What file do you want to go into: ")
                file_path = f"Flashcards/{file}"
                add_flashcards(file_path)
                continue
            case 3: # Edit Flashcards
                file = input("What file do you want to go into: ")
                file_path = f"Flashcards/{file}"
                edit_flashcards(file_path)
                continue
            case 4: # Start Flashcards
                file = input("What file do you want to go into: ")
                file_path = f"Flashcards/{file}"
                start_flashcards(file_path)
                continue
            case 5:
                file = input("What file would you like to reverse or type 'quit' to cancel: ")
                if file.lower() == 'quit':
                    continue
                file_path = f"Flashcards/{file}"
                reverse_questions_and_answers(file_path)
            case 6:
                break


main()