import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Направления движения
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

def random_food():
    return [random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
            random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE]

# Инициализация змейки
snake = [[100, 100], [80, 100], [60, 100]]
direction = RIGHT
food = random_food()
clock = pygame.time.Clock()
game_over = False

while not game_over:
    screen.fill(BLACK)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
    
    # Движение змейки
    new_head = [snake[0][0] + direction[0] * CELL_SIZE, snake[0][1] + direction[1] * CELL_SIZE]
    
    # Проверка на столкновение с границами или собой
    if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        game_over = True
        break
    
    snake.insert(0, new_head)
    
    # Проверка, съела ли змейка еду
    if new_head == food:
        food = random_food()
    else:
        snake.pop()
    
    # Рисуем еду
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Рисуем змейку
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(10)

pygame.quit()
