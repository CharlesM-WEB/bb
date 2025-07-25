# DO: add the bricks to the balls as a parameter when cronstructing a ball\
# so we can check for collisions in the substeps

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



startball = ball.Ball([400,400])
startball.velocity = [0, 4]
screen = pygame.display.set_mode((800,800))
p1 = paddle.Paddle()
bricks = []
balls = [startball]

bricks.append(brick.Brick([400,200]))
for i in range(40):
    bricks.append(brick.Brick([i * 20, 180]))

#game loop
while True:
    time.sleep(0.01)
    pygame.display.update()
    screen.fill("black")
    
    #Detects colisions between ball and paddle
    if startball.shape().colliderect(p1.shape()):
        startball.velocity[1] *= -1
        
        diff = startball.pos[0] - p1.pos[0]
        startball.velocity[0] += diff // 20
    
    #Brick and ball collisions
    for a in balls:
        for b in bricks:
            if a.collide(b):
                # find the collision angle 
                x = a.pos[0] - b.pos[0]
                y = a.pos[1] - b.pos[1]
                angle = math.degrees(math.atan2(y,x))
                
                print(angle)
                
                #horizontal bounce
                if (angle > 310 or angle < 50) or (angle > 130 and angle < 230):
                    a.velocity[0] += a.velocity[0] * -2
                    
                #Vertical bounce
                if (angle > 40 and angle < 140) or (angle > 220 and angle < 320):
                    a.velocity[1] += a.velocity[1] * -2
    
    #Handeling player inputs
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        p1.pos[0] += 5
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        p1.pos[0] -= 5
        
    #draw
    startball.draw()
    p1.draw()
    
    for b in balls:
        b.draw()
    
    for b in bricks:
        b.draw()
    
    #event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    
            
            
