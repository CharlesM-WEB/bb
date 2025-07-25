import pygame
import math

class Ball: 
    def __init__(self, pos =[0,0], bricks=[]):
        self.color = "white"
        self.size = 5
        self.pos = pos
        self.velocity = [0, 0]
        self.speed = 3
        self.bricks = bricks

    def draw(self):
        direction = math.atan2(self.velocity[1], self.velocity[0])
        x = math.cos(direction)
        y = math.sin(direction)
        self.velocity = [x * self.speed, y * self.speed]

        pygame.draw.circle(pygame.display.get_surface(),
                            self.color,self.pos, self.size)
        for i in range(10):
            self.pos = [self.pos[0] + self.velocity[0]/10,
                        self.pos[1] + self.velocity[1]/10]
            
            if self.pos[1] > 800 or self.pos[1] < 0:
                self.velocity[1] *= -1
                
            if self.pos[0] > 800 or self.pos[0] < 0:
                self.velocity[0] *= -1
        
    def shape(self):
        return pygame.Rect(self.pos[0] -self.size, self.pos[1] -self.size, 10,10)
        
    def collide(self,other):
        return self.shape().colliderect(other.shape())