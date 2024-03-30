from utils import Direction, Point

class Snake:
    def __init__(self, head: Point, block_size: int):
        self.head = head
        self.body = [self.head]
        self.direction = Direction.UP
        self.block_size = block_size

    def move(self, direction: Direction):
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

    def grow(self):
        self.body.insert(0, self.head)