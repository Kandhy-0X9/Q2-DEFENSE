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
            {'q': 'What is a group of flamingos called?', 'a': ['flamboyance']}
        ]
    },
    'columbidae': {
        'file': 'columbidae.txt',
        'questions': [
            {'q': 'What is the family name for pigeons and doves?', 'a': ['columbidae']},
            {'q': 'What do pigeons and doves feed their young?', 'a': ['crop milk']},
            {'q': 'How do pigeons and doves navigate?', 'a': ['using the earth\'s magnetic field and sun', 'magnetic field', 'sun']}
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
            {'q': 'What is the primary habitat of cranes?', 'a': ['wetlands', 'shallow swamps', 'marshes']}
        ]
    },
    'albatross': {
        'file': 'albatross.txt',
        'questions': [
            {'q': 'What bird has the largest wing span?', 'a': ['wandering albatross','albatross']},
            {'q': 'How do albatrosses fly long distances?', 'a': ['dynamic soaring','by dynamic flying']},
            {'q': 'What is a major threat to albatrosses?', 'a': ['fishing bycatch', 'bycatch','fishing nets','fishing']}
        ]
    },
    'swift': {
        'file': 'swift.txt',
        'questions': [
            {'q': 'Why do swifts rarely landing?', 'a': ['spend nearly entire life in the air', 'spend life in air','they spend 10 months in the air','they live in the air']},
            {'q': 'What do swifts eat?', 'a': ['insects caught in the air', 'insects']},
            {'q': 'What is the swift\'s name derived from?', 'a': ['Greek apous, meaning "footless"','apous','footless']}
        ]
    },
    'hoopoe': {
        'file': 'hoopoe.txt',
        'questions': [
            {'q': 'What is distinctive about the hoopoe\'s crest?', 'a': ['erectile crest of cinnamon feathers', 'crest of cinnamon feathers','cinnamon feathers']},
            {'q': 'How does the hoopoe feed?', 'a': ['probing soil with its bill', 'probing with bill']},
            {'q': 'What is the hoopoe the national bird of?', 'a': ['Israel']}
        ]
    },
    'owls': {
        'file': 'owls.txt',
        'questions': [
            {'q': 'What allows owls to have excellent binocular vision?', 'a': ['large, fixed, tube-shaped eyes', 'tube-shaped eyes', 'large fixed eyes']},
            {'q': 'How do owls pinpoint sounds?', 'a': ['asymmetrical ears','different ears']},
            {'q': 'What do owls regurgitate as indigestible parts?', 'a': ['pellets']}
        ]
    },
    'loon': {
        'file': 'loon.txt',
        'questions': [
            {'q': 'What are loons known for in terms of calls?', 'a': ['haunting calls', 'calls']},
            {'q': 'Why are loons awkward on land?', 'a': ['legs set far back for swimming', 'legs far back']},
            {'q': 'What do loons primarily eat?', 'a': ['fish', 'sea animals', 'marine life']}
        ]
    },
    'eagle': {
        'file': 'eagle.txt',
        'questions': [
            {'q': 'What are eagles known for in terms of eyesight?', 'a': ['incredible eyesight','good eyesight', 'best eyesight']},
            {'q': 'What do eagles use to catch prey?', 'a': ['strong talons','talons',]},
            {'q': 'What is the national emblem of the United States?', 'a': ['bald eagle', 'eagle']}
        ]    },
    'heron': {
        'file': 'heron.txt',
        'questions': [
            {'q': 'What does a heron use to catch fish?', 'a': ['sharp beak', 'dagger-like bill', 'spear']},
            {'q': 'What is the name of a group of nesting herons?', 'a': ['heronries', 'heronry']},
            {'q': 'What are the main habitats of herons?', 'a': ['marshes', 'ponds', 'rivers', 'coastlines', 'wet habitats']}
        ]
    },
    'osprey': {
        'file': 'osprey.txt',
        'questions': [
            {'q': 'What is the osprey also known as?', 'a': ['fish hawk']},
            {'q': 'What is unique about the osprey\'s wing shape when soaring?', 'a': ['m shape', 'crooked bend']},
            {'q': 'What do ospreys eat exclusively?', 'a': ['fish']}
        ]
    },
    'blackbird': {
        'file': 'blackbird.txt',
        'questions': [
            {'q': 'What is the primary color of male European Common Blackbirds?', 'a': ['black', 'all black']},
            {'q': 'What do blackbirds primarily eat?', 'a': ['insects', 'worms', 'fruits', 'berries']},
            {'q': 'What family do North American blackbirds belong to?', 'a': ['icterids', 'icteridae']}
        ]
    },
    'chicken': {
        'file': 'chicken.txt',
        'questions': [
            {'q': 'What are chickens descended from?', 'a': ['red junglefowl', 'junglefowl']},
            {'q': 'What do chickens eat?', 'a': ['seeds', 'insects', 'fruits', 'omnivores']},
            {'q': 'What is the social structure of chickens called?', 'a': ['pecking order', 'hierarchy']}
        ]
    },
    'cuckoos': {
        'file': 'cuckoos.txt',
        'questions': [
            {'q': 'What is the defining behavior of cuckoos?', 'a': ['brood parasitism', 'lay eggs in other nests']},
            {'q': 'What do cuckoos primarily eat?', 'a': ['insects', 'caterpillars', 'bugs']},
            {'q': 'What is the famous call of the male cuckoo?', 'a': ['cuckoo']}
        ]
    },
    'passerines': {
        'file': 'passerines.txt',
        'questions': [
            {'q': 'What is another name for passerines?', 'a': ['perching birds', 'songbirds']},
            {'q': 'What is unique about passerine feet?', 'a': ['three toes forward, one back', 'anisodactyl feet']},
            {'q': 'What organ allows passerines to sing complex songs?', 'a': ['syrinx', 'voice box']}
        ]
    },
    'peafowls': {
        'file': 'peafowls.txt',
        'questions': [
            {'q': 'What is the male peafowl called?', 'a': ['peacock']},
            {'q': 'What do peafowls use their train for?', 'a': ['courtship displays', 'mating']},
            {'q': 'What is the diet of peafowls?', 'a': ['seeds', 'insects', 'reptiles', 'omnivores']}
        ]
    },
    'pelican': {
        'file': 'pelican.txt',
        'questions': [
            {'q': 'What do pelicans use their throat pouch for?', 'a': ['scoop fish', 'catching prey']},
            {'q': 'How do pelicans catch fish?', 'a': ['diving', 'herding fish']},
            {'q': 'What is the habitat of pelicans?', 'a': ['lakes', 'coasts', 'water bodies']}
        ]
    },
    'plover': {
        'file': 'plover.txt',
        'questions': [
            {'q': 'What is the feeding style of plovers?', 'a': ['run-pause-peck', 'foot-trembling']},
            {'q': 'What do plovers use to distract predators?', 'a': ['distraction displays', 'feigning injury']},
            {'q': 'What is the primary habitat of plovers?', 'a': ['beaches', 'mudflats', 'grasslands']}
        ]
    },
    'skimmer': {
        'file': 'skimmer.txt',
        'questions': [
            {'q': 'How do skimmers catch their food?', 'a': ['skimming the water', 'slicing the surface']},
            {'q': 'What is unique about the skimmer\'s bill?', 'a': ['elongated lower bill', 'lower mandible longer']},
            {'q': 'What is the habitat of skimmers?', 'a': ['coasts', 'estuaries', 'beaches']}
        ]
    },
    'starling': {
        'file': 'starling.txt',
        'questions': [
            {'q': 'What is the starling known for in terms of vocalization?', 'a': ['mimicry', 'complex whistles']},
            {'q': 'What do starlings eat?', 'a': ['insects', 'worms', 'fruits', 'omnivores']},
            {'q': 'What is a group of starlings called?', 'a': ['murmuration']}
        ]
    },
    'toucan': {
        'file': 'toucan.txt',
        'questions': [
            {'q': 'What is the most striking feature of toucans?', 'a': ['large bill', 'oversized bill']},
            {'q': 'What do toucans primarily eat?', 'a': ['fruit', 'insects', 'small vertebrates']},
            {'q': 'What is the habitat of toucans?', 'a': ['rainforests', 'tropical forests']}
        ]    },
    'turkey': {
        'file': 'turkey.txt',
        'questions': [
            {'q': 'What is the fleshy growth that hangs over a turkey\'s beak called?', 'a': ['snood']},
            {'q': 'How fast can wild turkeys run?', 'a': ['up to 25 mph', '25 mph', '25 miles per hour']},
            {'q': 'What is a group of turkeys called?', 'a': ['flock']}
        ]
    },
    'woodpecker': {
        'file': 'woodpecker.txt',
        'questions': [
            {'q': 'What is the foot arrangement of woodpeckers called?', 'a': ['zygodactyl', 'zygodactyl feet']},
            {'q': 'What do woodpeckers use their stiff tail feathers for?', 'a': ['support', 'prop', 'bracing against trees']},
            {'q': 'Why do woodpeckers drum on trees?', 'a': ['communication', 'mating', 'territory', 'attract mates']}
        ]
    },
    'aves': {
        'file': 'aves.txt',
        'questions': [
            {'q': 'What is the scientific class for birds?', 'a': ['aves']},
            {'q': 'What are the key characteristics that define birds?', 'a': ['feathers', 'beaked jaws', 'hard-shelled eggs', 'warm-blooded', 'lightweight skeletons']},
            {'q': 'How many bird species are estimated to exist worldwide?', 'a': ['around 10,000', '10,000', 'roughly 10,000']}
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
    print("\nAvailable Birds:\n")
    for bird in sorted(birds):
        print(f"- {bird.title()}")


    
    # Start an infinite loop to allow multiple attempts.
    while True:
        # Get user input for bird choice, convert to lowercase and strip whitespace.
        choice = input("\nChoose a bird to read about(type the name): ").strip().lower()
        # Check if the choice is a valid bird in the dictionary.
        if choice in birds:
            # Open the corresponding file, read its content, and store in 'passage'.
            with open(birds[choice]['file'], 'r') as f:
                passage = f.read()
            # Print separators and the passage title.
            print("\n" + "="*50)
            print("PASSAGE:", bird.title())
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