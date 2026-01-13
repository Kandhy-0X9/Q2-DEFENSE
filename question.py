#Questionnaire
#imports
import os

# Import the os module to use system commands for clearing the terminal.

# Define a dictionary (birds) that maps each bird name to its data:
# - 'file': the filename of the passage text file
# - 'questions': a list of dictionaries, each with 'q' (question text) and 'a' (correct answer)
birds = {
    'flamingo': {
        'file': 'flamingo.txt',
        'questions': [
            {'q': 'What is the primary color of flamingos?', 'a': ['pink','pinkish','color pink']},
            {'q': 'How do flamingos feed?', 'a': ['filter feed upside-down', 'filter feed']},
            {'q': 'What is a group of flamingos called?', 'a': 'flamboyance'}
        ]
    },
    'columbidae': {
        'file': 'columbidae.txt',
        'questions': [
            {'q': 'What is the family name for pigeons and doves?', 'a': 'columbidae'},
            {'q': 'What do pigeons and doves feed their young?', 'a': 'crop milk'},
            {'q': 'How do pigeons and doves navigate?', 'a': 'using the earth\'s magnetic field and sun'}
        ]
    },
    'cassowaries': {
        'file': 'Cassowaries.txt',
        'questions': [
            {'q': 'What is the casque on a cassowary?', 'a': ['a bony helmet','bone helmet']},
            {'q': 'Are cassowaries flightless?', 'a': ['yes','true']},
            {'q': 'What do cassowaries primarily eat?', 'a': ['fruit', 'fruits']}
        ]
    },
    'crane': {
        'file': 'crane.txt',
        'questions': [
            {'q': 'What do cranes perform for bonding?', 'a': ['dances', 'dancing']},
            {'q': 'Are cranes monogamous?', 'a': ['yes','true']},
            {'q': 'What is the primary habitat of cranes?', 'a': ['wetlands', 'shallow swamps',]}
        ]
    },
    'albatross': {
        'file': 'albatross.txt',
        'questions': [
            {'q': 'What bird has the largest wing span?', 'a': ['wandering albatross','albatross']},
            {'q': 'How do albatrosses fly long distances?', 'a': ['dynamic soaring','by dynamic flying']},
            {'q': 'What is a major threat to albatrosses?', 'a': 'fishing bycatch'}
        ]
    },
    'swift': {
        'file': 'swift.txt',
        'questions': [
            {'q': 'Why are swifts rarely landing?', 'a': 'spend nearly entire life in the air'},
            {'q': 'What do swifts eat?', 'a': 'insects caught in the air'},
            {'q': 'What is the swift\'s name derived from?', 'a': ['Greek apous, meaning "footless"','apous','footless']}
        ]
    },
    'hoopoe': {
        'file': 'hoopoe.txt',
        'questions': [
            {'q': 'What is distinctive about the hoopoe\'s crest?', 'a': 'erectile crest of cinnamon feathers'},
            {'q': 'How does the hoopoe feed?', 'a': 'probing soil with its bill'},
            {'q': 'What is the hoopoe the national bird of?', 'a': 'Israel'}
        ]
    },
    'owls': {
        'file': 'owls.txt',
        'questions': [
            {'q': 'What allows owls to have excellent binocular vision?', 'a': 'large, fixed, tube-shaped eyes'},
            {'q': 'How do owls pinpoint sounds?', 'a': ['asymmetrical ears','different ears']},
            {'q': 'What do owls regurgitate as indigestible parts?', 'a': 'pellets'}
        ]
    },
    'loon': {
        'file': 'loon.txt',
        'questions': [
            {'q': 'What are loons known for in terms of calls?', 'a': 'haunting calls'},
            {'q': 'Why are loons awkward on land?', 'a': 'legs set far back for swimming'},
            {'q': 'What do loons primarily eat?', 'a': ['fish', 'sea animals', 'marine life']}
        ]
    },
    'eagle': {
        'file': 'eagle.txt',
        'questions': [
            {'q': 'What are eagles known for in terms of eyesight?', 'a': ['incredible eyesight','good eyesight', 'best eyesight']},
            {'q': 'What do eagles use to catch prey?', 'a': ['strong talons','talons',]},
            {'q': 'What is the national emblem of the United States?', 'a': 'Bald Eagle'}
        ]
    }
}

#  Define the main function that contains the program's logic:
# - Clear the screen
# - Display title and greeting
# - Show list of available birds
# - Enter a loop to handle user choices:
#   - Prompt user to choose a bird
#   - If choice is valid:
#     - Read and display the passage from the file
#     - Ask each question, check answer, provide feedback
#     - Ask if user wants to continue
#   - If invalid, show error message
# - Exit when user chooses not to continue
def main():
    # Call function to clear the terminal screen.
    os.system('cls||clear')
    # Print the program title.
    print("BIRDS QUESTIONNAIRE\n")
    # Print a welcome message.
    print("\nWelcome to birds questionnaire\n\n")
    # Print the list of available birds.
    print("Birds:\n")
    print("\nAvailable Birds:\n")
    for bird in sorted(birds):
        print(f"- {bird.title()}")


    
    # Start an infinite loop to allow multiple attempts.
    while True:
        # Get user input for bird choice, convert to lowercase and strip whitespace.
        choice = input("\nChoose a bird (type the name): ").strip().lower()
        # Check if the choice is a valid bird in the dictionary.
        if choice in birds:
            # Open the corresponding file, read its content, and store in 'passage'.
            with open(birds[choice]['file'], 'r') as f:
                passage = f.read()
            # Print separators and the passage title.
            print("\n" + "="*50)
            print("PASSAGE:")
            print("="*50)
            # Print the full passage content.
            print(passage)
            print("="*50)
            # Print a message introducing the questions.
            print("\nNow, answer the following questions based on the passage:\n")
            # Loop through each question for the chosen bird.
            for q in birds[choice]['questions']:
                # Prompt user for answer to the current question, strip and lowercase.
                ans = input(q['q'] + " ").strip().lower()
                # Check if the user's answer matches the correct answer (case-insensitive).
                if ans in q['a']:
                    #If correct, print success message.
                    print("Correct!\n")
                else:
                    # If wrong, print the correct answer.
                    print(f"Wrong. The correct answer is: {q['a'][0]}\n")
            # Ask user if they want to try another bird.
            again = input("Do you want to try another bird? (y/n): ").strip().lower()
            # If not 'y', break the loop and end the program.
            if again != 'y':
                # Print a thank you message.
                print("Thank you for playing! Hope you learned something new about birds!")
                break
        else:
            # If choice is invalid, print an error message with valid options.
            print("\nInvalid choice. Please choose from the following birds:\n")
            print("\nAvailable Birds:\n")
            for bird in sorted(birds):
                print(f"- {bird.title()}")



# If this script is run directly , call the main function to start the program.
if __name__ == "__main__":
    main()