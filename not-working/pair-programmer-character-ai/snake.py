import pygame

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set up the game timer
clock = pygame.time.Clock()

# Define the snake's starting position and speed
x = width / 2
y = height / 2
dt = 0.01  # Delay in seconds
d = 3  # Speed in pixels per second

# Define the snake's body
snake = []
for segment in range(10):
    rect = pygame.Rect(x, y, 10, 10)
    snake.append(rect)

# Define a game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    # Update the screen
    screen.fill('black')
    pygame.draw.ellipse(screen, 'white', snake[0])
    for i in range(1, len(snake)):
        pygame.draw.ellipse(screen, 'white', snake[i])

    # Move the snake body
    for i in range(len(snake) - 1, 0, -1):
        head = snake[i][0]
        if i > 0:
            tail = pygame.Rect(snake[i - 1][0] - d * dt, snake[i - 1][1] + d * dt, 10, 10)
        else:
            tail = pygame.Rect(snake[0][0] + d * dt, snake[0][1] - d * dt, 10, 10)

        if head.colliderect(tail):
            game_over = True
            
    # Move the head
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake[0].top < height:
        x = x - d * dt
    if keys[pygame.K_DOWN] and snake[0].bottom > 0:
        x = x + d * dt
    if keys[pygame.K_LEFT] and snake[0].left > 0:
        y = y - d * dt
    if keys[pygame.K_RIGHT] and snake[0].right < width:
        y = y + d * dt
            
    # Check if the game is over
    if game_over:
        pygame.quit()
        quit()

