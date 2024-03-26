import random
import time
from mnemonic import Mnemonic
from colorama import Fore, Style

# Initialize colorama for colored output
import colorama
colorama.init()

# Function to read words from file and return a list of words
def read_words_from_file(word_file):
    with open(word_file, 'r') as file:
        words = file.read().split()
        return words

# Function to generate a random recovery phrase
def generate_recovery_phrase(word_list):
    return ' '.join(random.choices(word_list, k=12))  # Select 12 random words from the list and join them with spaces

# Function to validate a recovery phrase using Mnemonic library
def validate_recovery_phrase(phrase):
    mnemo = Mnemonic("english")
    return mnemo.check(phrase)

# Main function
def main():
    # Path for the word file
    word_file = "word_list.txt"

    # Read words from file
    word_list = read_words_from_file(word_file)

    # User input for the number of phrases to generate
    while True:
        try:
            num_phrases = int(input('How many phrases would you like to generate? (1-100000): '))
            if 1 <= num_phrases <= 100000:
                break
            else:
                print('Error! Number of phrases must be between 1 and 100000.')
        except ValueError:
            print('Error! Please enter a valid number.')

    valid_phrases = []

    start_time = time.time()  # Record start time

    # Generate random recovery phrases
    for _ in range(num_phrases):
        recovery_phrase = generate_recovery_phrase(word_list)
        print(recovery_phrase)
        if validate_recovery_phrase(recovery_phrase):
            valid_phrases.append(recovery_phrase)
            print(Fore.GREEN + "VALID")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "INVALID")
            print(Style.RESET_ALL)
            time.sleep(.01)

    end_time = time.time()  # Record end time

    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f'Elapsed Time: {elapsed_time:.2f} seconds to generate', num_phrases, 'phrases. Valid Phrases:', valid_phrases)

    # Write valid recovery phrases to file
    with open("phrases.txt", "w+") as f:
        for phrase in valid_phrases:
            f.write(phrase + '\n')

if __name__ == "__main__":
    main()

#end of program