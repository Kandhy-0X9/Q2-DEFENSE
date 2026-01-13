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
            {'q': 'What is the primary color of flamingos?', 'a': 'pink'},
            {'q': 'How do flamingos feed?', 'a': 'filter feed upside-down'},
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
            {'q': 'What is the casque on a cassowary?', 'a': 'a bony helmet'},
            {'q': 'Are cassowaries flightless?', 'a': 'yes'},
            {'q': 'What do cassowaries primarily eat?', 'a': 'fruit'}
        ]
    },
    'crane': {
        'file': 'crane.txt',
        'questions': [
            {'q': 'What do cranes perform for bonding?', 'a': 'dances'},
            {'q': 'Are cranes monogamous?', 'a': 'yes'},
            {'q': 'What is the primary habitat of cranes?', 'a': 'wetlands'}
        ]
    },
    'albatross': {
        'file': 'albatross.txt',
        'questions': [
            {'q': 'What is the largest wingspan of any bird?', 'a': 'wandering albatross'},
            {'q': 'How do albatrosses fly long distances?', 'a': 'dynamic soaring'},
            {'q': 'What is a major threat to albatrosses?', 'a': 'fishing bycatch'}
        ]
    },
    'swift': {
        'file': 'swift.txt',
        'questions': [
            {'q': 'What is the fastest bird in level flight?', 'a': 'common swift'},
            {'q': 'How long can swifts stay airborne?', 'a': 'up to 10 months'},
            {'q': 'What do swifts eat?', 'a': 'insects'}
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
    print("Flamingo Columbidae Cassowaries Cranes Albatross")
    
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
                # Pseudocode: Prompt user for answer to the current question, strip and lowercase.
                ans = input(q['q'] + " ").strip().lower()
                # Check if the user's answer matches the correct answer (case-insensitive).
                if ans == q['a'].lower():
                    #If correct, print success message.
                    print("Correct!\n")
                else:
                    # If wrong, print the correct answer.
                    print(f"Wrong. The correct answer is: {q['a']}\n")
            # Ask user if they want to try another bird.
            again = input("Do you want to try another bird? (y/n): ").strip().lower()
            # If not 'y', break the loop and end the program.
            if again != 'y':
                # Print a thank you message.
                print("Thank you for playing!")
                break
        else:
            # If choice is invalid, print an error message with valid options.
            print("Invalid choice. Please choose from: Flamingo, Columbidae, Cassowaries, Cranes, Albatross")

# If this script is run directly (not imported), call the main function to start the program.
if __name__ == "__main__":
    main()