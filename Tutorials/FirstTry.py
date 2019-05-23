import turtle #native already
import random

def RacamanSequence(current, joe, size, maxScale): #creating a function
    seen = set() #starting!
    
    for step_size in range(1,size):

        scale = random.randrange(0, maxScale+1) #creating random scale
        backwards = current - step_size #renewing backwards with the actual step and old value
        
        if backwards > 0 and backwards not in seen:
            joe.setheading(90) #head point up
            joe.circle(scale*step_size/2, 180) #drawing semicirles this why 180
            current = backwards
            seen.add(current) #adding value to a set so we can see if we saw already
        
    # Otherwise, go forwards
        else:
            joe.setheading(270) #head point down
            joe.circle(scale*step_size/2, 180) #semicircle again
            current += step_size
            seen.add(current) #adding value to a set so we can see if we saw already


window = turtle.Screen() #creates the Screen
window.setup(width=1280, height=720, startx=10, starty=0.5) #set screen size

joe = turtle.Turtle() #creates joe
joe.shape('circle')#cute trick
joe.penup()
joe.setpos(-390, 0)
joe.pendown()

stepSize = 100 #maxStepSize
maxScale = 10 #max Multiply Scale

#Creating the Racáman sequence

currentNumber = 0 #start from zero (less than zero is not possible)

RacamanSequence(currentNumber,joe, stepSize, maxScale)

turtle.done() #keeps the window from closing