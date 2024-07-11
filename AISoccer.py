import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("AI Soccer")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define game objects
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, team):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.team = team
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # Keep the player within the game window
        self.rect.clamp_ip(game_window.get_rect())

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce the ball off the walls
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.speed_y *= -1

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the players
    player1 = Player(100, 300, "Team 1")
    player2 = Player(700, 300, "Team 2")

    # Move the ball
    ball = Ball(400, 300)
    ball.move()

    # Clear the game window
    game_window.fill(GREEN)

    # Draw the players and ball
    game_window.blit(player1.image, player1.rect)
    game_window.blit(player2.image, player2.rect)
    game_window.blit(ball.image, ball.rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()