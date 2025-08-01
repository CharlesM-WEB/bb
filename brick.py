import pygame
import math

class Brick:
    def __init__(self, pos = [0, 0]):
        self.color = "green"
        self.pos = pos
        self.size = [15,15]
        self.health = 1
        
    def shape(self):
        return pygame.Rect(self.pos[0] - self.size[0]/2, self.pos[1] - self.size[1]/2, self.size[0], self.size[1])
    
    def draw(self):
        if self.health < 1:
            return 
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.shape())
    
    def destroy(self):
        pass
    
    def collide(self,other):
        if self.helth < 1:
            return
        self.health -= 1
        return self.shape().colliderect(other.shape())
        
           

class Unbreakable_Brick(Brick):
    def __init__(self, pos = [0,0]):
        super().__init__(pos)
        self.color = "red"
        self.health = math.inf
    
    def destroy(self):
        pass   