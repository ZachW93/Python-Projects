import turtle
import random


def random_word(filehandle):  # creating the function
    WordDictionary = []  # takes in the list of words and
    input_filehandle = open(filehandle, "r")  # strips \n
    for line in input_filehandle:  # then chooses a random word from list
        Word = line.strip("\n")
        WordDictionary.append(Word)
    RI = random.randint(0, len(WordDictionary)-1)
    return WordDictionary[RI]


def Hangman(Word):  # takes in the word
    t = 0  # used to spread out the letters in turtle
    y = 0  # also used to spread letters
    turtle.bgpic('CBBG.gif')  # creates the actual hangman
    turtle.setup(1024, 682)
    turtle.title("Hangman Game")
    turtle.tracer(0)
    turtle.up()
    turtle.setposition(-150, 20)
    turtle.down()
    turtle.forward(300)
    turtle.up()
    turtle.setposition(0, 20)
    turtle.down()
    turtle.setposition(0, 300)
    turtle.forward(100)
    turtle.setposition(100, 250)
    WWL = Word
    Fails = 0
    AG = []
    Blank = ""
    LOW = len(Word)  # creates blank marks for turtle
    for i in range(0, LOW):  # takes in the range of length
        Blank += str('_')  # to give me exact number of blanks
    Blank = list(Blank)
    i = 0
    x = -100
    turtle.up()
    turtle.setposition(-100, -100)
    turtle.down()
    while i < len(Blank) + 1:
        turtle.write("__", font=('Arial', 16, "normal"))
        turtle.up()
        turtle.setposition(x, -100)
        turtle.down()
        i += 1
        x += 40
    print(Blank)
    while len(WWL) > 0:  # creates the guess a letter format
        letter = turtle.textinput("Hangman", "Guess a Letter")
        if letter in WWL:  # checks to see if letter is in word
            x = -100
            print("There is a(n) " + letter)
            for i, c in enumerate(Word):  # if yes, rights the letter in
                if letter == c:  # appropriate spot
                    Blank[i] = letter
                    y = i*40
                    x = x + y
                    turtle.up()
                    turtle.setposition(x, -100)
                    turtle.write(letter, font=('Arial', 30, "normal"))
            print(''.join(Blank))
            WWL = WWL.replace(letter, '')
            AG.append(letter)
        else:
            if letter in AG:  # checks to see if letter is already in
                print("Already Guessed!")
            else:
                turtle.up()  # writes letter below if wrong
                turtle.setposition(t, -200)
                turtle.down()
                turtle.write(letter, font=('Arial', 30, "normal"))
                t += 50
                AG.append(letter)
                Fails = Fails + 1
                if Fails == 1:  # draws the hangman figure dependent on fails
                    turtle.up()
                    turtle.setposition(100, 200)
                    turtle.down()
                    turtle.circle(25)
                elif Fails == 2:
                    turtle.up()
                    turtle.setposition(100, 200)
                    turtle.down()
                    turtle.setposition(100, 75)
                    turtle.setposition(100, 200)
                elif Fails == 3:
                    turtle.up()
                    turtle.setposition(100, 75)
                    turtle.down()
                    turtle.setposition(60, 35)
                elif Fails == 4:
                    turtle.up()
                    turtle.setposition(100, 75)
                    turtle.down()
                    turtle.setposition(140, 45)
                elif Fails == 5:
                    turtle.up()
                    turtle.setposition(100, 175)
                    turtle.down()
                    turtle.setposition(50, 175)
                elif Fails == 6:
                    turtle.up()
                    turtle.setposition(50, 175)
                    turtle.down()
                    turtle.setposition(0, 175)
                    turtle.write("YOU LOSE!!", font=('Arial', 40, "normal"))
    if len(WWL) == 0:  # displays WIN
        turtle.up()
        turtle.setposition(-200, -200)
        turtle.down()
        turtle.write("YOU WIN!!", font=('Arial', 40, "normal"))
    turtle.done()
    again = turtle.textinput("Play Again?")  # if they want to play again
    return

Word = random_word('word_list.txt')
Hangman(Word)
