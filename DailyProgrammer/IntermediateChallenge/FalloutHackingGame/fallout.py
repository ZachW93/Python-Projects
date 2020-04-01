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
    
    difficulty = input("Please Enter a Difficulty Between 1-5: ")
    difficulty_dict = {'1': (4,5,6), '2': (7,8), '3': (9,10), '4': (11,12), '5': (13,14,15)}
    size = random.randint(4, random.choice(difficulty_dict[difficulty]))
    length = random.choice(difficulty_dict[difficulty])
    word_list = get_WordList(length, size)
    correct_word = word_list[random.randint(0, len(word_list) - 1)]
    correct_word_list = list(correct_word)
    

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
  
fallout()
