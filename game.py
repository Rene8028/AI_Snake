import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font('arial.ttf', 25)
#font = pygame.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 20
SPEED = 40

class SnakeGameAI:

    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()


    def reset(self):
        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.reward = 20
        self.total_reward = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0


    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()


    def play_step(self, action):
        self.frame_iteration += 1
        # collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # calculate distance to food before move
        dist_before = np.linalg.norm(np.array(self.head) - np.array(self.food))

        # move
        self._move(action) # update the head
        self.snake.insert(0, self.head)
        
        self.reward = 0

        # calculate distance to food after move
        dist_after = np.linalg.norm(np.array(self.head) - np.array(self.food))

        # check if game over
        game_over = False
        if self.is_collision() or self.frame_iteration > 150:
            game_over = True
            self.reward += -20
            # 保证reward是整数
            self.reward = round(self.reward, 2)
            self.total_reward += self.reward
            return self.reward, game_over, self.score, self.total_reward

        # check if snake is closer to food
        if dist_after < dist_before:
            raw_reward = 0.5 + (self.frame_iteration * 0.005)
            self.reward += raw_reward  # 鼓励靠近食物
        else:
            raw_reward = 0.5 + (self.frame_iteration * 0.007)
            self.reward += - raw_reward # 惩罚远离食物

        # if self.frame_iteration % random.randint(30, 50) == 0:
        #     self.reward += -1  # 给予额外惩罚以防止原地踏步

        # place new food or just move
        if self.head == self.food:
            self.score += 1
            self.reward += 10
            self._place_food()
            self.frame_iteration = 0
        else:
            self.snake.pop()
        
        # 保证reward是整数
        self.reward = round(self.reward, 2)
        self.total_reward += self.reward
        self.total_reward = round(self.total_reward, 2)

        # update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # return game over and score
        return self.reward, game_over, self.score, self.total_reward


    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # hits boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # hits itself
        if pt in self.snake[1:]:
            return True

        return False


    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        score_text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(score_text, [0, 0])

        reward_text = font.render("Reward: " + str(self.reward), True, WHITE)
        self.display.blit(reward_text, [score_text.get_width() + 10, 0])

        iteration_text = font.render("Iteration: " + str(self.frame_iteration), True, WHITE)
        self.display.blit(iteration_text, [score_text.get_width() + reward_text.get_width() + 20, 0])

        pygame.display.flip()


    def _move(self, action):
        # [straight, right, left]

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)