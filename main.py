#imports

from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
from wallbricks import WallBricks
from scoreboard import Scoreboard
import time

#-------------------------Setting up classes--------------------------#

screen=Screen()
paddle=Paddle((0,-220))
ball=Ball()
bricks=WallBricks()
scoreboard=Scoreboard()


#-------------------------Creating the bricks and preparing the setup -----------------------------------------#

#-------------------------Setting up the Screen--------------------------#


screen.setup(width=500,height=500)
screen.bgcolor("black")
screen.tracer(0)


bricks.create_brick()




#----------------------------starting the game--------------------------------------------------------------------------#

#----------------------------moving paddle and ball module while listening-----------------------#


screen.listen()
screen.onkey(paddle.go_right,"Right")
screen.onkey(paddle.go_left,"Left")


game_is_on=True
while game_is_on:

  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

#--------------Check the different collision's while moving ! -------------------#
  

  #if it hits the paddle , let it bounce up !
  if ball.distance(paddle)<45  and ball.ycor()<-200 : 
     ball.bounce_y()
     if scoreboard.score%10==0:
       ball.increase_speed()

  

  #if it hits ground , gameover , restart the game !
  if  ball.ycor()<-230 :
      ball.reset()
      scoreboard.reset()

  

  #if it hits the top , let it go down 
  if  ball.ycor()>220 :
      ball.bounce_y()

  

  #if it hits left side , let it go rightdown , if it hits right , let it it go leftdown
  if  ball.xcor()>550 or ball.xcor()<-550 :
      ball.bounce_x()

  

  #checking the collision with the bricks , in addition to providing the color to update the score depending on it ,
  #and updating the status of the brick and if its destroyed or not. 
  
  for brick in bricks.all_bricks:
    if ball.distance(brick)<50  :
      ball.bounce_y()
      brick_color=brick.color()
      bricks.update(brick)
      scoreboard.increase_score(brick_color)
      
      
      

  

screen.exitonclick()

#---------------------------------#

  
  

  













# Notes:
#1) game_is_on=True
# while game_is_on:

#   time.sleep(ball.move_speed)
#   screen.update()
#   ball.move()
#what we are doing with the ball is instead of going straightly towards the position , we will make take steps while going , instead of going in a flash way , and we will stop the screen wrt to its speed , where if its speed is 10 , then we wait 10 seconds then let it move at every step , and we increase the speed but the effect will be the saame ! 

# 2) #if it hits the paddle , let it bounce up !
# if ball.distance(paddle)<25  and ball.ycor()<-160  :
#    ball.bounce_y()
#what we are doing here is that the paddle is at -190 , the height is 25 , so the coordinates of the top of the paddle is 
#165 , and we give a buffer = to 5 , so when its less then 160 and have a distance equal to 25 between paddle and ball , let it bounce ! distance is equal to the top of the paddle to the bottom of it ! 