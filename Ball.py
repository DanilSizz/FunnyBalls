import random
import pygame
import physics

class Ball():

    def __init__(self, x: int, y: int):
        
        size = self.setSize(50, 20)

        self.rect_zone = pygame.rect.Rect(x - size // 2, y - size // 2, size, size)
        self.phys_engine = physics.Physics(0.1, 1)

        #super().__init__(x - size // 2, y - size // 2, size, size)
        self.color = self.setRandomColor()
        self.setVelocity(3, 3, 1)

    def setRandomColor(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def setSize(self, size, randomness):
        return size + random.randint(-1 * randomness, randomness)

    def setVelocity(self, vx, vy, randomness):
        self.vx = vx * random.randint(-1, 1) + random.randint(-1 * randomness, randomness)
        self.vy = vy * random.randint(-1, 1) + random.randint(-1 * randomness, randomness)
        
    def updatePosition(self):
        self.rect_zone.x += self.vx
        self.rect_zone.y += self.vy

    def checkBounds(self, width, height):
        if self.rect_zone.left < 0 or self.rect_zone.right > width:
            self.vx = -1 * self.vx 
        if self.rect_zone.top < 0 or self.rect_zone.bottom > height:
            self.vy = -1 * self.vy

    def checkCollision(self, balls):

        for ball in balls:
            if ball != self:
                if self.rect_zone.colliderect(ball):
                    self.vx = -1 * (self.vx + ball.vx) / 2 
                    self.vy = -1 * (self.vy + ball.vy) / 2
