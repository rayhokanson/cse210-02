# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball

class Director:
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        pygame.init()

        # Define some colors
        self._BLACK = (0, 0, 0)
        self._WHITE = (255, 255, 255)

        # Open a new window
        size = (700, 500)
        self._screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Pong")

        self._paddleA = Paddle(self._WHITE, 10, 100)
        self._paddleA.rect.x = 20
        self._paddleA.rect.y = 200

        self._paddleB = Paddle(self._WHITE, 10, 100)
        self._paddleB.rect.x = 670
        self._paddleB.rect.y = 200

        self._ball = Ball(self._WHITE, 10, 10)
        self._ball.rect.x = 345
        self._ball.rect.y = 195

        #This will be a list that will contain all the sprites we intend to use in our game.
        self._all_sprites_list = pygame.sprite.Group()

        # Add the 2 paddles and the ball to the list of objects
        self._all_sprites_list.add(self._paddleA)
        self._all_sprites_list.add(self._paddleB)
        self._all_sprites_list.add(self._ball)

        # The clock will be used to control how fast the screen updates
        self._clock = pygame.time.Clock()

        self._scoreA = 0
        self._scoreB = 0

    def score(self):
        
        if self._ball.rect.x >= 690:
            self._scoreA += 1
            self._ball._velocity[0] = -self._ball._velocity[0]
        if self._ball.rect.x <= 0:
            self._scoreB += 1
            self._ball._velocity[0] = -self._ball._velocity[0]
        if self._ball.rect.y > 490:
            self._ball._velocity[1] = -self._ball._velocity[1]
        if self._ball.rect.y < 0:
            self._ball._velocity[1] = -self._ball._velocity[1]

    def displayScore(self):
        font = pygame.font.Font(None, 74)
        text = font.render(str(self._scoreA), 1, self._WHITE)
        self._screen.blit(text, (250, 10))
        text = font.render(str(self._scoreB), 1, self._WHITE)
        self._screen.blit(text, (420, 10))

    def start_game(self):
    # -------- Main Program Loop -----------
        carryOn = True

        while carryOn:
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False  # Flag that we are done so we exit this loop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                        carryOn = False

            #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self._paddleA.moveUp(5)
            if keys[pygame.K_s]:
                self._paddleA.moveDown(5)
            if keys[pygame.K_UP]:
                self._paddleB.moveUp(5)
            if keys[pygame.K_DOWN]:
                self._paddleB.moveDown(5)

            # --- Game logic should go here
            self._all_sprites_list.update()

            self.score()

            #Detect collisions between the ball and the paddles
            if pygame.sprite.collide_mask(self._ball, self._paddleA) or pygame.sprite.collide_mask(self._ball, self._paddleB):
                self._ball.bounce()

            # --- Drawing code should go here
            # First, clear the screen to black.
            self._screen.fill(self._BLACK)
            #Draw the net
            pygame.draw.line(self._screen, self._WHITE,
                             [349, 0], [349, 500], 5)

            #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
            self._all_sprites_list.draw(self._screen)

            self.displayScore()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self._clock.tick(60)

    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
