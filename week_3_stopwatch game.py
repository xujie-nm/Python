# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
run = False
time = 0
player_win = 0#player win times
stop_times = 0#you press the stop button times

# define helper function format that converts time
def convert():
    global time
    return format(time)

# in tenths of seconds into formatted string A:BC.D
def format(t):
    second = float((float(t % 600)) / 10)
    minute = t / 600
    if second < 10:
        return str(minute) + ":" + "0" + str(second)
    else:
        return str(minute) + ":" + str(second)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global run
    run = True
    timer.start()
    
    
def stop_handler():
    global run, player_win, stop_times, time
    if time % 10 == 0:
        player_win += 1
    stop_times += 1
    run = False
    timer.stop()
    

def reset_handler():
    global time, run, player_win, stop_times
    run = False
    time = 0
    player_win = 0
    stop_times = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    #if run == False:
    canvas.draw_text(str(player_win) + "/" + str(stop_times), (250,20), 25, "green")
    canvas.draw_text(format(time), (80, 100), 36, "Red")
    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 200)
timer = simplegui.create_timer(interval, timer_handler)

# register event handlers
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()


# Please remember to review the grading rubric
