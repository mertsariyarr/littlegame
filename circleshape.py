import pygame

#Base class for game objects (visible objects)

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
        self.x = x
        self.y = y
        #we will be using this later

    def draw(self, screen):
        #sub-classes must override
        pass

    def update(self, dt):
        #sub-classes must override
        pass
    
    def collisions(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= self.radius + other.radius:
            return True
        return False