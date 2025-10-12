import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "cointainers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.velocity = pygame.Vector2(0,0)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        
    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass