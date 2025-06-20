import pygame


class Ball: 
    def __init__(self, pos =[0,0]):
        self.color = "white"
        self.size = 5
        self.pos = pos
        self.velocity = [0, 0]
        
    def draw(self):
        pygame.draw.circle(pygame.display.get_surface(),
                            self.color,self.pos, self.size)
        
        self.pos = [self.pos[0] + self.velocity[0],
                    self.pos[1] +self.velocity[1]]
        
        if self.pos[1] > 800 or self.pos[1] < 0:
            self.velocity[1] *= -1
            
        if self.pos[0] > 800 or self.pos[0] < 0:
            self.velocity[0] *= -1
        
    def shape(self):
        return pygame.Rect(self.pos[0] -self.size, self.pos[1] -self.size, 10,10)
        