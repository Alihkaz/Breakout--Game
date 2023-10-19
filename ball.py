
#again , we are inheriting from the turtle class , where we are assigning many attributes related to the turtle class towards Ball class through super().__init__(), and here we are creating a new turtle object but with the shape of a circle ! 

from turtle import Turtle

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.shapesize(1.2, 1.2)
    self.penup()
    
    self.x_move = 7
    self.y_move = 7
    self.move_speed=0.1


  
  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def bounce_y(self):
    self.y_move *= -1
    
    
  def bounce_x(self):
    self.x_move *= -1
    # self.move_speed*=0.9



  def reset(self):
    self.goto(0,-180)
    self.move_speed=0.1
    self.bounce_y()
    

  def increase_speed(self):
    self.move_speed+=0.2



# so whats happening here is thaat we created different functions , the ball is moving with incremental x and y each time
#, when it hits the paddle , we say to bounce y , that is instead of going upward , it have to go downword ! 

#bouncey means reverse the direction from upward to down ward 
