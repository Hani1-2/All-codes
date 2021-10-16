import random
import string



###########################################################################

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter in letters_guessed:
            continue
        else:
            return False

    return True


#########################################################################

def get_guessed_word(secret_word, letters_guessed):
    word_revealed = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_revealed += letter
        else:
            word_revealed += "_ "
    return word_revealed


##############################################################


def get_available_letters(letters_guessed):
    alphabet_remaining = list(string.ascii_lowercase)
    for letter in letters_guessed:
        alphabet_remaining.remove(letter)
    return "".join(alphabet_remaining)


def loading_words():
    print("Loading word list from file...")
    File = open('D:words.txt', 'r')
    line = File.readline()
    word_list = line.split()
    print("  ", len(word_list), "words loaded...\n")
    return word_list


#######################################################

def choose_word(word_list):
    return random.choice(word_list)


def hangman_with_hints(secret_word):
    length = len(secret_word)
    guesses = 6
    warnings = 3
    letters_guessed = []

    vowels = ["a", "e", "i", "o", "u"]
    print("Hello and welcome to Hangman!")
    print("I am thinking of a word that is", str(length), "letters long.\n")
    print("You have", warnings, "warnings.")
    print("You have", guesses, "guesses.")
    while guesses > 0:

        print(" \n            *-------*                 ")
        print("You have", guesses, "guesses remaining.")
        print("Available letters are:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if len(letter) != 1:
            print('please enter a valid or a single value')
        else:
            letter = str.lower(letter)
            if str.isalpha(letter) == False:
                warnings -= 1
                if warnings < 0:
                    print("No, no, my friend, that is not a letter. There are no warnings left, so you lose one guess.",
                          get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
                else:
                    print("That is not a letter.", "\n", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed))
                    continue
            elif letter in letters_guessed:
                warnings -= 1
                if warnings < 0:
                    print(
                        "Yikes! You've guessed that letter already. There are no warnings left, so you lose one guess.",
                        get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
                    continue

                else:
                    print("Aah! you've already guessed that letter.", "\n", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed))
                    continue
            else:
                letters_guessed.append(letter)
            if letter in secret_word:
                print("Right guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter isn't in my word:",
                      get_guessed_word(secret_word, letters_guessed))
                if letter in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
            if is_word_guessed(secret_word, letters_guessed):
                s = secret_word
                s = s.lower()
                s = sum(1 for c in string.ascii_lowercase if s.count(c) == 1)

                total_score = guesses * s
                print("Congratulations dear. You won!\nYour total score for this game is:", total_score)
                break
            else:
                continue

    if guesses <= 0:
        print("------- \nSorry, you've run out of guesses.So you lost. The word was", "\"", secret_word, "\"")

    ############################################################################
##########################################################################
word_list = loading_words()

if __name__ == "__main__":
    secret_word = choose_word(word_list)
    hangman_with_hints(secret_word)