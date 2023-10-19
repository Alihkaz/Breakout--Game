#

from turtle import Turtle







class WallBricks(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.first_row=75
        self.x=-50
        self.color()
       

  
    def create_brick(self):

      # creating all the bricks and positioning all the breakes !
      
      for n in range(0,88):


            
        
            
        
            brick = Turtle("square")
            brick.shapesize(stretch_wid=1,stretch_len=2)
            self.tilt(90)
            brick.penup()
          


          # going up every 100 bricks and restarting from the begining! ! 
            if n%22==0:
              self.first_row+=30
              self.x=-530

           #giving each row a seperate color ! 
            if  0<=n<=22:
              brick.color('yellow')
  
            if  21<n<=44:
                brick.color('red')
              
            if  43<n<=66:
               brick.color('blue')
                
            if 65<n<=88 :             
                brick.color('purple')
                

           
        
            #to remove the starting bug
            brick.goto(self.x,self.first_row)
            
            # print(self.x) (just for test)
            self.x+=50
            self.all_bricks.append(brick)
   


  
#when the ball collides with the brick , the brick will be destroyed ! 
    def update(self,brick):

  
      for bricks in self.all_bricks:
        
        if bricks==brick:
            pass
        else:
          brick.goto(bricks.xcor(),bricks.ycor())
          
          


  #what we are doing here is rearranging all the bricks , we start with checking if the brick in the brick list is 
  #the hitted brick by the wall , if so , then ignore it and check the next one , if its not hitted , then go to the your previous coordinate (may be here , and I dont know how this happened , I will search through it , the stranger thing is that brick each brick is going to xcor and ycor related to its corresponding item , and taking its color also ! )
     