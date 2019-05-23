import turtle #native already

def RacamanSequence(current, joe): #creating a function
    seen = set() #starting!
    for step_size in range(1,100):

        backwards = current - step_size #renewing backwards with the actual step and old value
        
        if backwards > 0 and backwards not in seen:
            joe.backward(step_size)
            current = backwards
            seen.add(current) #adding value to a set so we can see if we saw already
        
    # Otherwise, go forwards
        else:
            joe.forward(step_size)
            current += step_size
            seen.add(current) #adding value to a set so we can see if we saw already


window = turtle.Screen() #creates the Screen

joe = turtle.Turtle() #creates joe
joe.shape('turtle')#cute trick

#Creating the Racáman sequence

currentNumber = 0 #start from zero (less than zero is not possible)

RacamanSequence(currentNumber,joe)

turtle.done() #keeps the window from closing