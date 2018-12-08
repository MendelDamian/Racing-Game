import pygame
import random


class Log:
    def __init__(self, screen_width, speed):
        self.log_img = pygame.image.load('log.png')
        self.log_width = 94
        self.log_height = 45
        self.log_y = random.randrange(-600, -100)
        self.log_x = random.randrange(0, screen_width - self.log_width)
        self.speed = speed

    def move_down(self, screen_width, screen_height):
        if self.log_y > screen_height:
            self.resize()
            self.log_y = 0 - self.log_height - random.randrange(0, 50)
            self.log_x = random.randrange(10, screen_width - self.log_width - 10)
            if self.speed < 8:
                self.speed *= 1.1
            else:
                self.speed = 8
            print('Log has fallen')
            print('Log speed: ', round(self.speed, 3))
            return True
        else:
            self.log_y += self.speed

    def check(self, cy, cx, cw, ch):
        if self.log_y + self.log_height > cy > self.log_y or \
           self.log_y + self.log_height > cy + ch > self.log_y:
            if self.log_x + self.log_width > cx > self.log_x or\
               cx+cw > self.log_x and cx + cw < self.log_x + self.log_width:
                return True

    def resize(self):
        if self.log_width < 130:
            width = int(self.log_width * 1.05)
            height = int(self.log_height * 1.05)
            self.log_img = pygame.image.load('log.png')
            self.log_img = pygame.transform.scale(self.log_img, (width, height))
            self.log_width = width
            self.log_height = height
            print("log width: ", self.log_width)
            print("log height: ", self.log_height)
