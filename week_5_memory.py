# implementation of card game - Memory
# before you run this game, please load this image http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg

import simplegui
import random

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')
# helper function to initialize globals
turns = 0
def new_game():
    global card_list, exposed_list, state, turns
    exposed_list = []
    card_list = range(8) + range(8)
    random.shuffle(card_list)
    for i in  range(len(card_list)):
        exposed_list.append(False)
    state = 0
    turns = 0
    label.set_text("Turns = 0")
    #print card_list, exposed_list

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, state1_inx, state2_inx, turns
    inx = pos[0] // 50
    if exposed_list[inx] != True:
        exposed_list[inx] = True
        if state == 0:
            state = 1
            state1_inx = inx
        elif state == 1:
            state = 2
            state2_inx = inx
        else:
            if card_list[state1_inx] == card_list[state2_inx]:
                exposed_list[state1_inx] = True
                exposed_list[state2_inx] = True
            else:
                exposed_list[state1_inx] = False
                exposed_list[state2_inx] = False
            state1_inx = inx
            state = 1
        turns += 1
        label.set_text("Turns = " + str(turns))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(card_list)):
        if exposed_list[i]:
            canvas.draw_text(str(card_list[i]), (i * 50 +15, 75), 50, "White")
        else:
            canvas.draw_image(image, (1521 / 2, 1818 / 2), (1521, 1818), (i * 50 + 25, 50), (50, 100))
        canvas.draw_line((i * 50, 0), (i * 50, 100), 5, 'Red')
            


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric