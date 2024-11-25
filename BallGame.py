import pygame
<<<<<<< Updated upstream
import Ball
=======
import ball
import keyHandler
>>>>>>> Stashed changes
class BallGame():

    def __init__(self, screen_size, fps = 60, gameState = True):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.framesPerSecond = fps
        self.gameState = gameState
        self.clock = pygame.time.Clock()
        self.balls = []
<<<<<<< Updated upstream
=======
        self.keyHandler = keyHandler.KeyHandler()
>>>>>>> Stashed changes
        
    def run(self):

        while self.gameState != False:
            self.clock.tick(self.framesPerSecond)

<<<<<<< Updated upstream
            self.keyboardEvents()
=======
            self.keyHandler.handle_keyboard(self)
>>>>>>> Stashed changes

            self.render()

            pygame.display.update()

    def setBackground(self, imagePath):
        self.background = pygame.image.load(imagePath)
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
            
    def keyboardEvents(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.gameState = False
                case pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.spawnBall(x, y)
                    
    def spawnBall(self, x, y):
        ball_var = ball.Ball(x, y)
        self.balls.append(ball_var)

    def render(self):
        self.screen.fill((0, 0, 0))
        for ball_var in self.balls:
            ball_var.updatePosition()
            ball_var.checkBounds(self.screen.get_width(), self.screen.get_height())
            #ball_var.checkCollision(self.balls)
            
            pygame.draw.ellipse(self.screen, ball_var.color, ball_var.rect_zone)
            
        
newGame = BallGame((800, 600), 60, True)
newGame.run()