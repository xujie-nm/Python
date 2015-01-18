# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#global variables, number is random number
num_range = 100
timers = 0
number = -1

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    """
    start a new game, and print the message
    """
    global timers, number
    if num_range == 100:
        timers = 7
        number = random.randrange(0, 100)
        print "New game, Range is from 0 to 100"
        print "Number of remaining guesses is ", timers
        print ""
    else:
        timers = 10
        number = random.randrange(0, 1000)
        print "New game, Range is from 0 to 1000"
        print "Number of remaining guesses is ", timers
        print ""

    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    if timers != 0:
        new_game()
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    if timers != 0:
        new_game()
    pass
    
def get_input(guess):
    # main game logic goes here
    global number, timers
    gue_number = int(guess)
    print "Guess was ", gue_number
    if timers != 0:#if timers is not 0, do this
        timers -= 1
        print "Number of remaining guesses is ", timers
        if number > gue_number:
            print "Higher!"
            print ""
        elif number < gue_number:
            print "Lower!"
            print ""
        else :#if guess number is right, print binggo, and start a new game
            print "Binggo!"
            print ""
            new_game()
    elif timers == 0:#if timers is 0, start a new game
        print "timers is run out, try again"
        print ""
        new_game()
        print ""
    pass

    
# create frame

frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# call new_game 
new_game()

frame.start()


# always remember to check your completed program against the grading rubric
