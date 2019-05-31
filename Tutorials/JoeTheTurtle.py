import turtle #native already
import random
from datetime import datetime
from PIL import Image

def RacamanSequence(current, joe, size, maxScale): #creating a function
    seen = set() #starting!
    colors  = ["red","green","blue","orange","purple","pink","yellow"] #creating a random vector

    for step_size in range(1,size):

        color = random.choice(colors) #getting one of the colors (random)
        scale = random.randrange(0, maxScale+1) #creating random scale
        backwards = current - step_size #renewing backwards with the actual step and old value
        
        if backwards > 0 and backwards not in seen:
            joe.color(color)
            joe.setheading(90) #head point up
            joe.circle(scale*step_size, 180) #drawing semicirles this why 180
            current = backwards
            seen.add(current) #adding value to a set so we can see if we saw already
        
    # Otherwise, go forwards
        else:
            joe.color(color)
            joe.setheading(270) #head point down
            joe.circle(scale*step_size, 180) #semicircle again
            current += step_size
            seen.add(current) #adding value to a set so we can see if we saw already


stepSize = 100 #maxStepSize
maxScale = 10 #max Multiply Scale

for i in range(1, maxScale):

    window = turtle.Screen() #creates the Screen
    window.setup(width=1920, height=1080, startx=10, starty=0.5) #set screen size
    now=datetime.now()
  

    joe = turtle.Turtle() #creates joe
    screenSaving = joe.getscreen() 
    window.bgcolor('black')
    #joe.shape('turtle')#cute trick
    joe.hideturtle() #hiding joe
    joe.speed(0) #fastest drawing
    joe.width(5)
    joe.penup()
    joe.setpos(-200, 0)
    joe.pendown()



    #Creating the Racáman sequence

    currentNumber = 0 #start from zero (less than zero is not possible)

    RacamanSequence(currentNumber,joe, stepSize, i)

    myFile = "figures/Joe_" + now.strftime("%m_%d_%Y_%H_%M_%S")
#print(myFile)
    screenSaving.getcanvas().postscript(file=(myFile+'.eps'), colormode='color')
    #converting eps to png
    img= Image.open(myFile+'.eps')
    img.save(myFile+'.png', 'png')
    joe.reset()
#turtle.done() #keeps the window from closing