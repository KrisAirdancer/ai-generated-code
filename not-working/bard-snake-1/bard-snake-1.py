import random
import pygame

# Create the screen
screen = pygame.display.set_mode((600, 600))

# Create the snake
snake = [pygame.Rect(0, 0, 10, 10)]

# Set the direction of the snake
direction = 'right'

# Set the speed of the snake
speed = 10

# Set the food
food = pygame.Rect(random.randint(0, 590), random.randint(0, 590), 10, 10)

# Initialize the score
score = 0

# Loop until the snake hits itself or the edge of the screen
while True:

    # Move the snake
    snake.move(speed, 0)

    # Check if the snake has hit the food
    if snake.colliderect(food):
        # Eat the food
        food = None
        # Increase the score
        score += 1
        # Grow the snake
        snake.append(pygame.Rect(snake[-1].x, snake[-1].y, 10, 10))
        # Change the direction of the snake
        direction = 'left'
        # Increase the speed of the snake
        speed += 1

    # Check if the snake has hit itself
    if snake[-1].x < 0 or snake[-1].x > 600 or snake[-1].y < 0 or snake[-1].y > 600:
        # Game over
        print('Game over! Score:', score)
        break

    # Check if the snake has hit the edge of the screen
    if snake[-1].x < 0 or snake[-1].x > 600 or snake[-1].y < 0 or snake[-1].y > 600:
        # Game over
        print('Game over! Score:', score)
        break

    # Update the screen
    screen.blit(snake[0], (snake[0].x, snake[0].y))
    screen.blit(food, (food.x, food.y))

    # Update the score
    score += 1

    # Draw the score
    screen.blit(str(score), (200, 200))

    # Update the speed of the snake
    speed -= 1

    # Update the direction of the snake
    if direction == 'right':
        snake[0].x += speed
    elif direction == 'left':
        snake[0].x -= speed

    # Input
    for event in pygame.event.pump():
        # Check if the user has quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()