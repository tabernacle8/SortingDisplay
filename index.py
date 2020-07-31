import pygame
import random
import time

speed = 10




pygame.init()
screen = pygame.display.set_mode((2000, 1000))
screen.fill((255,255,255))
done = False

numbers = []
listLength = 2000
currentColor = (0,255,0)


for i in range(listLength):
    numbers.append(random.randrange(0,1000))

xcounter = 0

def createLines():
    screen.fill((255,255,255))
    global numbers
    global xcounter
    xcounter = 0
    for numb in numbers:
            #print(numb)
            pygame.draw.rect(screen, (0,0,0), (xcounter,1000-numb,1,990))
            xcounter = xcounter +1
            if(xcounter==2000):
                break
    pygame.display.update()



pastindex =50
index = 0
cache = 0
while not done:
        #pygame.draw.rect(screen, currentColor, (0,0,1,990))
        #pygame.draw.rect(screen, currentColor, (0,500,2,990))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        



    n = len(numbers) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            pygame.event.get()
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if numbers[j] > numbers[j+1] : 
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        
        if(i%speed==0):
            createLines()

    #print(numbers)
    done = True
            
                