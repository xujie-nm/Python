#The week 1

import random

#0 - rock
#1 - Spock
#2 - paper
#3 - lizard
#4 - scissors

# helper functions

def number_to_name(number):
    """
    convert number to player's name
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print "invaild number"
        return 'null'
    
#test number_to_name

#print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)
#print number_to_name(5)

def name_to_number(name):
    """
    convert player's number
    """
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print "invaild name"
        return -1
    
#test name_to_numbers
    
#print name_to_number('rock')
#print name_to_number('Spock')
#print name_to_number('paper')
#print name_to_number('lizard')
#print name_to_number('scissors')
#print name_to_number('spock')

#main function

def rpsls(name):
    """
    player and computer fight!!
    """
    player_choice = name_to_number(name)
    comp_number = random.randrange(0, 5)
    comp_name = number_to_name(comp_number)
    print "Player chooses " + name
    print "Computer chooses " + comp_name
    if player_choice == -1:
        print "error player"
        
    fight_num = player_choice - comp_number
    if fight_num < 0:
        fight_num += 5
    if fight_num == 0:
        print "Player and Computer tie!"
        print ""
    elif fight_num <= 2 and fight_num > 0:
        print "Player wins!" 
        print ""
    elif fight_num >= 3 and fight_num <= 4:
        print "Computer wins!"
        print ""
    else:
        print "error input"
        print ""

        
#test main function

rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')
