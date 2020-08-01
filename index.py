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

def createLines():
    screen.fill((255,255,255))
    xcounter = 0
    for numb in numbers:
            pygame.draw.rect(screen, (0,0,0), (xcounter,1000-numb,1,990))
            xcounter = xcounter +1
            if(xcounter==2000):
                break
    pygame.display.update()



pastindex =50
index = 0
cache = 0
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True

    n = len(numbers) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            pygame.event.get()
            if numbers[j] > numbers[j+1] : 
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        
        if(i%speed==0):
            createLines()
    done = True