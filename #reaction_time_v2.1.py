#reaction_time_v2.1
import turtle as trtl
import random as rand
import time
wn = trtl.Screen()
react = trtl.Turtle()
react.turtlesize(100)
react.shape("square")
counter =  trtl.Turtle()
counter.penup()
counter_interval = 1000   #1000 represents 1 second
timer_up = False
font_setup = ("Arial", 20, "normal")
counter.pencolor("red")
timer = (rand.randint(1,100)/20)
start_time = 0
time_lapsed = 0
avar = 0
clicker =  trtl.Turtle()
#functions
def change_color():
  global start_time
  start_time = time.time()
  global timer, timer_up
  if timer_up == True:
    react.color("red")

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    #counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    #counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
  change_color()  
def position_counter():
  counter.penup()
  counter.goto(-200,200)
def handle_click(x,y):
  global start_time
  global time_lapsed
  global avar
  react.color("black")
  end_time = time.time()
  time_lapsed = end_time - start_time
  if avar == 0:
    counter.write(time_lapsed, font=font_setup)
  avar += 1

#events
position_counter()
wn.ontimer(countdown, counter_interval) 
#wn.onkeypress(GoUp,"w")
wn.onscreenclick(handle_click,1)

wn.listen()
wn.mainloop()