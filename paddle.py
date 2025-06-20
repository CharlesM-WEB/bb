import pygame

class Paddle:
    def __init__(self):
        self.color = "salmon"
        self.pos = [400,700]
        self.size = [60,10]

    def shape(self):
        return pygame.Rect(self.pos[0] - self.size[0]/2, self.pos[1] - self.size[1]/2, self.size[0], self.size[1])
    
    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.shape())
        
    def collide(self,other):
        return self.shape().colliderect(other.shape())