#reaction_time_v1
import turtle as trtl
import random as rand
import datetime as datetime
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
timer = rand.randint(2,10)
#functions
def change_color():
  global timer, timer_up
  if timer_up == True:
    react.color("red")

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
  change_color()  
def position_counter():
  counter.penup()
  counter.goto(-200,200)


#events
position_counter()

wn.ontimer(countdown, counter_interval) 
#wn.onkeypress(GoUp,"w")


wn.listen()
wn.mainloop()