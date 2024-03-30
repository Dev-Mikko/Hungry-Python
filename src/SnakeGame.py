import pygame
import random
from collections import namedtuple
from enum import Enum

class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4


Point = namedtuple("Point", "x, y")


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

        # Snake state
        self.direction = Direction.UP
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - self.block_size, self.head.y),
                      Point(self.head.x - (2 * self.block_size), self.head.y)]
        
        # Environment settings
        self.score = 0
        self.food = None
        self._place_food()
    
    def _place_food(self):
        # Generate randomly the food position
        x = random.randint(0, (self.w - self.block_size) // self.block_size) * self.block_size
        y = random.randint(0, (self.h - self.block_size) // self.block_size) * self.block_size
        self.food = Point(x, y)

        # Avoid to generate food where the snake is located
        if self.food in self.snake:
            self._place_food()
    
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        
        match direction:
            case Direction.UP:
                y -= self.block_size
            case Direction.LEFT:
                x -= self.block_size
            case Direction.DOWN:
                y += self.block_size
            case Direction.RIGHT:
                x += self.block_size
        
        self.head = Point(x, y)
    
    def _update_ui(self):
        self.screen.fill("chartreuse3")

        for point in self.snake:
            pygame.draw.rect(self.screen, "yellow3", pygame.Rect(point.x, point.y, self.block_size, self.block_size))
            pygame.draw.rect(self.screen, "yellow", pygame.Rect(point.x + 4, point.y + 4, 12, 12))

        pygame.draw.rect(self.screen, "red", pygame.Rect(self.food.x, self.food.y, self.block_size, self.block_size))

        pygame.display.flip()
    
    def _check_collision(self):
        if self.head.x > self.w - self.block_size or self.head.x < 0 or self.head.y > self.h - self.block_size or self.head.y < 0:
            return True
        
        if self.head in self.snake[1:]:
            return True
        
        return False

