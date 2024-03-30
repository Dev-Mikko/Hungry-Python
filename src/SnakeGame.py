import pygame
import random
from Snake import Snake
from utils import Direction, Point

class SnakeGame:
    def __init__(self, block_size = 20, speed = 20):
        self.block_size = block_size
        self.speed = speed

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w, self.h = self.screen.get_size()
        self.screen.fill("chartreuse3")

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Hungry Python")

        self.snake = Snake(Point(self.w / 2, self.h / 2), self.block_size)

        # Environment settings
        self.score = 0
        self.food = None
        self._place_food()

    def play_game(self):
        # Event handler
        for event in pygame.event.get():
            # Snake movements handler
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        if self.snake.direction != Direction.DOWN:
                            self.snake.direction = Direction.UP
                    case pygame.K_LEFT:
                        if self.snake.direction != Direction.RIGHT:
                            self.snake.direction = Direction.LEFT
                    case pygame.K_DOWN:
                        if self.snake.direction != Direction.UP:
                            self.snake.direction = Direction.DOWN
                    case pygame.K_RIGHT:
                        if self.snake.direction != Direction.LEFT:
                            self.snake.direction = Direction.RIGHT

        self.snake.move(self.snake.direction)
        self.snake.grow()

        game_over = False
        if self._check_collision():
            game_over = True
            return game_over, self.score

        if self.snake.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.body.pop()

        self._update_ui()
        self.clock.tick(self.speed)

        return game_over, self.score

    def _place_food(self):
        # Generate randomly the food position
        x = random.randint(0, (self.w - self.block_size) // self.block_size) * self.block_size
        y = random.randint(0, (self.h - self.block_size) // self.block_size) * self.block_size
        self.food = Point(x, y)

        # Avoid to generate food where the snake is located
        if self.food in self.snake.body:
            self._place_food()

    def _update_ui(self):
        self.screen.fill("chartreuse3")

        for point in self.snake.body:
            pygame.draw.rect(self.screen, "yellow3", pygame.Rect(point.x, point.y, self.block_size, self.block_size))
            pygame.draw.rect(self.screen, "yellow", pygame.Rect(point.x + 4, point.y + 4, 12, 12))

        pygame.draw.rect(self.screen, "red", pygame.Rect(self.food.x, self.food.y, self.block_size, self.block_size))

        pygame.display.flip()

    def _check_collision(self):
        if self.snake.head.x > self.w - self.block_size or self.snake.head.x < 0 or self.snake.head.y > self.h - self.block_size or self.snake.head.y < 0:
            return True

        if self.snake.head in self.snake.body[1:]:
            return True

        return False

