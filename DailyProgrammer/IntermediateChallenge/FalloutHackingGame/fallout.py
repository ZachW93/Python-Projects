'''
Problem:
The popular video games Fallout 3 and Fallout: New Vegas have a computer 
"hacking" minigame where the player must correctly guess the correct password 
from a list of same-length words. Your challenge is to implement this game 
yourself.

The game operates similarly to the classic board game Mastermind. The player 
has only 4 guesses and on each incorrect guess the computer will indicate how 
many letter positions are correct.

For example, if the password is MIND and the player guesses MEND, the game 
will indicate that 3 out of 4 positions are correct (M_ND). If the password 
is COMPUTE and the player guesses PLAYFUL, the game will report 0/7. While some 
of the letters match, they're in the wrong position.

Ask the player for a difficulty (very easy, easy, average, hard, very hard), 
then present the player with 5 to 15 words of the same length. The length can 
be 4 to 15 letters. More words and letters make for a harder puzzle. The player
then has 4 guesses, and on each incorrect guess indicate the number of correct 
positions.
'''

import random

def fallout():

    #This section initializes the difficulty that the user chooses and selects the correct word

    difficulty = input("Please Enter a Difficulty Between 1-5: ")
    difficulty_dict = {'1': (4,5), '2': (6,7,8), '3': (9,10), '4': (11,12), '5': (13,14,15)}
    size = random.randint(3, random.choice(difficulty_dict[difficulty]))
    length = random.choice(difficulty_dict[difficulty])
    word_list = get_WordList(length, size)

    correct_word = word_list[random.randint(0, len(word_list) - 1)]
    correct_word_list = list(correct_word)

    #end section

    #This section will create the 408 character grid when finding the correct word

    output_str = ""
    characters = 408
    last_placement = 0
    counter = 0
    output_list = [None] * characters

    for word in word_list:
        output_list, last_placement, counter = place_word_firsthalf(output_list, word, length,
                                                                    last_placement, counter)

    output_list = fillListRandom(output_list)
    output_str = output_str.join(output_list)
    print(output_str)

    #end section
'''
    #This section will allow the user to input one of the words, if correct the user wins, else it will inform
    #the user how many characters were right and in the right spot. After 4 guesses, the player will lose if
    #they have not guessed correctly.

    user_input = ""
    counter = 0
    remainingGuesses = 4
    
    for word in word_list:
        print(word)
    while user_input != correct_word:
        score = 0
        counter += 1
        if counter == 5:
            print("You have failed!")
            break
        else:
            print("%i Guesses Left!" % remainingGuesses)
            user_input = input("Please enter a word from the list: ").upper()
            user_input_list = list(user_input)
            for i in range(len(correct_word)):
                if correct_word_list[i] == user_input_list[i]:
                    score += 1
                else:
                    continue
            print("%i/%i correct" % (score, len(correct_word)))
            remainingGuesses -= 1
        
    if user_input == correct_word:
        print("Congratulations, you guessed it!")

    #end section
'''
def get_WordList(wordListSize, lengthOfWords):
    
    with open("enable1.txt") as f:
        words = list(map(lambda s: s.strip().lower(), f.readlines()))
    
    word_list = []
    
    while len(word_list) != wordListSize:
            
        x = random.randint(0,172820)
        if len(words[x]) == lengthOfWords:
            word_list.append(words[x].upper())
        else:
            continue
    
    return word_list


def place_word_firsthalf(current_list: list, word: str, length: int,last_placement: int, counter: int):


    word_chars = [x for x in word]

    isPlaced = False
    while isPlaced != True:

        placement = random.randint(0, len(current_list))

        if current_list[placement + (len(word)-1)] == None and (placement + len(word) - 1 < len(current_list)):
            isPlaced = True

    for letter in word_chars:
        current_list[placement] = letter
        placement += 1

    counter += 1

    return current_list, placement, counter

def fillListRandom(current_list):

    randomChar_hash = {1: "!", 2: '"', 3: "#", 4: "$", 5: "%", 6: "&", 7: "'", 8: "(", 9: ")", 10: "*", 11: "+",
                       12: "-", 13: ".", 14: "/", 15: ":", 16: ";", 17: "<", 18: "=", 19: ">", 20: "?", 21: "@",
                       22: "[", 23: '\\', 24: '{', 25: ']', 26: '^', 27: "_", 28: "|", 29: "}", 30: "~"}

    for i in range(0, len(current_list)):
        if current_list[i] == None:

            randomChar = random.randint(1, 30)
            current_list[i] = randomChar_hash[randomChar]

    return current_list

fallout()
