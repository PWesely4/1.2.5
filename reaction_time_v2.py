#reaction_time_v2.2
import turtle as trtl
import random as rand
import time
playagain = ("y")
leadernamelist = []
leaderscorelist = []
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
clicker =  trtl.Turtle()
name = input("what is your name?")
score = 0
#functions
def settimer():
  global timer
  timer = (rand.randint(1,100)/20)
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
  global score
  react.color("black")
  end_time = time.time()
  time_lapsed = end_time - start_time
  counter.write(time_lapsed, font=font_setup)
  score = time_lapsed
  return score

'''def handle_leaderboard():
  global name
  global score
  while score '''
def playgame():
  global playagain
  global timer_up

  wn.ontimer(countdown, counter_interval) 
  wn.onscreenclick(handle_click,1)
  wn.listen()
  playagain = input("Do you want to play? y or n")
  return playagain
#events
position_counter()
while playagain == ("y"):
  settimer()
  react.color("black")
  playgame()
  
wn.mainloop()
