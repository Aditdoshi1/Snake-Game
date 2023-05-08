import pygame
import random
import sys
import pygame.mixer


# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Window size
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 600

# Snake size
SNAKE_SIZE = 10

# Initialize the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adit's Snake Game")

# Initialize the clock
clock = pygame.time.Clock()


# Create the Snake class
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = SNAKE_SIZE
        self.dy = 0
        self.body = [(self.x, self.y)]

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Check if the snake hits the boundaries
        if self.x >= WINDOW_WIDTH or self.x < 0 or self.y >= WINDOW_HEIGHT or self.y < 0:
            return False

        # Check if the snake hits its body
        if (self.x, self.y) in self.body[:-1]:
            return False

        # Add the new position to the snake's body
        self.body.insert(0, (self.x, self.y))

        # If the snake eats the food, generate a new one and increase the length of the snake
        if self.x == food.x and self.y == food.y:
            food.generate()
            score.increase()
        else:
            self.body.pop()

        return True

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, GREEN, (x, y, SNAKE_SIZE, SNAKE_SIZE))



    def reset(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.dx = SNAKE_SIZE
        self.dy = 0
        self.body = [(self.x, self.y)]


# Create the Food class
class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.generate()

    def generate(self):
        self.x = random.randint(0, WINDOW_WIDTH // SNAKE_SIZE - 1) * SNAKE_SIZE
        self.y = random.randint(0, WINDOW_HEIGHT // SNAKE_SIZE - 1) * SNAKE_SIZE

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, SNAKE_SIZE, SNAKE_SIZE))


# Create the Score class
class Score:
    def __init__(self):
        self.value = 0
        self.highscore = 0
        self.font = pygame.font.Font(None, 30)

    def increase(self):
        self.value += 1

    def draw(self, surface):
        text = self.font.render("Score: " + str(self.value) + " Highscore: " + str(self.highscore), True, WHITE)
        surface.blit(text, (10, 10))

    def reset(self):
        if self.value > self.highscore:
            self.highscore = self.value
        self.value = 0

    def game_over_text(self, surface):
        font = pygame.font.Font(None, 60)
        text = font.render("Game Over! Press Space to Restart", True, WHITE)
        surface.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))

#Initialize the game

pygame.init()
pygame.display.set_caption("Adit's Snake Game")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
snake = Snake(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
food = Food()
score = Score()

# Game loop
game_over = False

# Game loop
while True:
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.dy != SNAKE_SIZE:
                    snake.dx = 0
                    snake.dy = -SNAKE_SIZE
                elif event.key == pygame.K_DOWN and snake.dy != -SNAKE_SIZE:
                    snake.dx = 0
                    snake.dy = SNAKE_SIZE
                elif event.key == pygame.K_LEFT and snake.dx != SNAKE_SIZE:
                    snake.dx = -SNAKE_SIZE
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT and snake.dx != -SNAKE_SIZE:
                    snake.dx = SNAKE_SIZE
                    snake.dy = 0

        # Move the snake
        if not snake.move():
            game_over = True

        # Draw the screen
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        score.draw(screen)
        pygame.display.update()

        # Tick the clock
        clock.tick(10 + score.value // 10)

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snake.reset()
                    food.generate()
                    score.reset()
                    game_over = False

        # Show game over screen
        screen.fill(BLACK)
        score.game_over_text(screen)
        pygame.display.update()
        clock.tick(10)
