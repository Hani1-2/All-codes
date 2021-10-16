name = input("enter your name \n>>>")
print (f'hey {name} there is a game for you')
print('you have 3 guesses and 3 warnings')
guesses = 6
warnings = 3

import random
l=['cat','dog' ,'tie','goat','king','hall']
secret_word=random.choice(l)
main = ''
word_revealed = ""



    for letter in secret_word:
        if letter in letters_guessed:
            word_revealed += letter
        else:
            word_revealed += "_ "


while True:
    if guesses == 0 and warnings == 0:
        print ("you lost the game ")
        break
    letter = input("enter a letter\n>>>")
    if len (letter)>1:
        print ('enter an alphabet at a time ')
    if letter.isalpha() == False:
        print ('enter only alphabets')

    if letter in secret_word:
        print("Right guess:", get_guessed_word(secret_word, letters_guessed))
    else:
        print("Oops! That letter isn't in my word:",get_guessed_word(secret_word, letters_guessed))

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
second_integer = int(input())
double = int(input())
string_variable = input()
# Read and save an integer, double, and String to your variables.
print(i + second_integer)
# Print the sum of both integer variables on a new line.
print(d + double)
# Print the sum of the double variables on a new line.
print (s + string_variable)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.


# l=[]
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     l+=[[name,score]]
# print(l)
