# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():#direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(-3, 3), random.randrange(-3, 3)]


# define event handlers


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2]
    paddle2_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2]
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball()
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_vel[0] < 0:
        ball_vel[0] -= 0.01
    else:
        ball_vel[0] += 0.01
    ball_vel[1] += 0.0000000001
    if(ball_pos[0] <= BALL_RADIUS + PAD_WIDTH or ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH):
        ball_vel[0] = -ball_vel[0]
        if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and(ball_pos[1] < (paddle1_pos[1] - 40) or ball_pos[1] > (paddle1_pos[1] + 40)):
            score2 += 1
        elif ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH and (ball_pos[1] < (paddle2_pos[1] - 40) or ball_pos[1] > (paddle2_pos[1] + 40)):
            score1 += 1
    elif(ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]  
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, 'White')
    
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] > (PAD_HEIGHT / 2) and paddle1_pos[1] < (HEIGHT - PAD_HEIGHT / 2):
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] < (PAD_HELGHT / 2):
        paddle1_pos[1] = PAD_HEIGHT / 2
    elif paddle1_pos[1] > (HEIGHT - PAD_HEIGHT) / 2:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT / 2
        
    if paddle2_pos[1] > (PAD_HEIGHT / 2) and paddle2_pos[1] < (HEIGHT - PAD_HEIGHT / 2):
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] < 40:
        paddle2_pos[1] = 50
    elif paddle2_pos[1] > 360:
        paddle2_pos[1] = 360
    # draw paddles
    #canvas.draw_line([paddle1_pos[0] - PAD_WIDTH / 2, paddle2_pos[1] - PAD_HEIGHT / 2 - 40],[paddle1_pos[0] + PAD_WIDTH / 2, paddle2_pos[1] - PAD_HEIGHT / 2 - 40], 1, "White")
    #canvas.draw_line([paddle1_pos[0] - PAD_WIDTH / 2, paddle2_pos[1] + PAD_HEIGHT / 2 - 40],[paddle1_pos[0] + PAD_WIDTH / 2, paddle2_pos[1] + PAD_HEIGHT / 2 - 40], 1, "White")
    canvas.draw_polygon([[paddle1_pos[0] - PAD_WIDTH / 2, paddle1_pos[1] - PAD_HEIGHT / 2], [paddle1_pos[0] + PAD_WIDTH / 2, paddle1_pos[1] - PAD_HEIGHT / 2], [paddle1_pos[0] - PAD_WIDTH / 2, paddle1_pos[1] + PAD_HEIGHT / 2], [paddle1_pos[0] + PAD_WIDTH / 2, paddle1_pos[1] + PAD_HEIGHT / 2]], 7, 'White')
    canvas.draw_polygon([[paddle2_pos[0] - PAD_WIDTH / 2, paddle2_pos[1] - PAD_HEIGHT / 2], [paddle2_pos[0] + PAD_WIDTH / 2, paddle2_pos[1] - PAD_HEIGHT / 2], [paddle2_pos[0] - PAD_WIDTH / 2, paddle2_pos[1] + PAD_HEIGHT / 2], [paddle2_pos[0] + PAD_WIDTH / 2, paddle2_pos[1] + PAD_HEIGHT / 2]], 7, 'White')
    # draw scores
    canvas.draw_text(str(score1), (250, 20), 24, 'White')
    canvas.draw_text(str(score2), (320, 20), 24, 'White')
    

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle_vel1 = -5
    elif key == simplegui.KEY_MAP['s']:
        paddle_vel1 = 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    print paddle1_vel
    print paddle1_pos
    print paddle2_vel
    print paddle2_pos
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0



# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', new_game)


# start frame
new_game()
frame.start()
