import pygame
class Keyhandler:

    def __init__(self):
        pass

    def handle_keyboard(self, BallGame):

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    BallGame.gameState = False
                case pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    BallGame.spawnBall(x, y)
