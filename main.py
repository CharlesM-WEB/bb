# DO: add the bricks to the balls as a parameter when cronstructing a ball\
# so we can check for collisions in the substeps5

import pygame
import random
import ball 
import time
import paddle
import math
import os
import brick 

os.system("git config user.name CharlesM-WEB")
os.system("git config user.email ctmarchant11@gmail.com")

pygame.init()

ticks = 0
bricks = []
startball = ball.Ball([400,400], bricks)
startball.velocity = [0, 4]
screen = pygame.display.set_mode((800,800))
p1 = paddle.Paddle()
balls = [startball]

file = open("layout.txt")
layout = file.readlines()

for row in range(len(layout)):
    for col in range(len(layout[row])):
        cell = layout[row][col]
        if cell == "b":
            bricks.append(brick.Brick([col * 20 + 10, row * 20 + 10]))
        if cell == "u":
            bricks.append(brick.Unbreakable_Brick([col * 20 + 10, row * 20 + 10]))

#game loop
while True:
    time.sleep(0.01)
    pygame.display.update()
    screen.fill("black")

    ticks += 1
    if ticks >= 500:
        ticks = 0
        newballs = []
        for b in balls:
            newball = ball.Ball(b.pos, bricks)
            newball.velocity = b.velocity
            newball.velocity += [random.randint(-5, 5), random.randint(-5, 5)]
            newballs.append(newball)
        balls += newballs
            
    
    #Detects colisions between ball and paddle
    for b in balls:
        if b.shape().colliderect(p1.shape()):
            b.velocity[1] *= -1
        
            diff = b.pos[0] - p1.pos[0]
            b.velocity[0] += diff // 20
    
    #Handeling player inputs
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        p1.pos[0] += 5
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        p1.pos[0] -= 5
        
    #draw
    p1.draw()
    
    for b in balls:
        b.draw()
    
    for b in bricks:
        b.draw()
    
    #event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    
            
            
