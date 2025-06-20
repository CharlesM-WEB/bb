import pygame
import random
import ball 
import time
import paddle

pygame.init()



startball = ball.Ball([400,400])
startball.velocity = [0, 4]
screen = pygame.display.set_mode((800,800))
p1 = paddle.Paddle()

while True:
    time.sleep(0.01)
    pygame.display.update()
    screen.fill("black")
    
    if startball.shape().colliderect(p1.shape()):
        startball.velocity[1] *= -1
        
        diff = startball.pos[0] - p1.pos[0]
        startball.velocity[0] += diff // 20
    
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        p1.pos[0] += 5
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        p1.pos[0] -= 5
        
    
    startball.draw()
    p1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    
            
            
