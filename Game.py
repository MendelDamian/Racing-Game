import pygame
import time
import functions


class Game:

    def __init__(self):

        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.car_x = self.screen_width * 0.45
        self.car_y = self.screen_height * 0.8
        self.car_width = 59
        self.car_height = 66
        self.exit = False
        self.x_change = 0
        self.dodged = 0
        self.speed = 4
        self.max_speed = 7
        self.bool_menu = True
        self.mouse = pygame.mouse.get_pos()
        self.pressed = pygame.mouse.get_pressed()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Racing game!")
        self.clock = pygame.time.Clock()
        self.car_img = pygame.image.load('player.png')
        self.menu_img = pygame.image.load('menu.png')
        self.menu()

    def quit(self):
        pygame.quit()
        quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_change = -self.speed
                elif event.key == pygame.K_RIGHT:
                    self.x_change = self.speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.x_change = 0

        self.car_x += self.x_change
        self.screen.fill((211, 211, 211))

    def car(self):
        self.screen.blit(self.car_img, (self.car_x, self.car_y))
        if self.car_x >= (self.screen_width - self.car_width) or self.car_x <= 0:
            self.crash()

    def message_display(self, text):
            font = pygame.font.SysFont('freesansbold', 115)
            text_surf, text_rect = functions.text_objects(text, font, (0, 0, 0))
            text_rect.center = (self.screen_width / 2, self.screen_height / 2)
            self.screen.blit(text_surf, text_rect)

            pygame.display.update()

            time.sleep(1)
            functions.game_loop()

    def draw_rect(self, color, x1, y1, x2, y2, text, event):
        if self.check(x1=x1, y1=y1, x2=x2, y2=y2):
            for i in range(0, 2):
                color[i] += 22
                if self.pressed[0] == 1:
                    self.menu_events(event)

        pygame.draw.rect(self.screen, color, (x1, y1, x2, y2))

        font = pygame.font.SysFont('Showcard Gothic', 30)
        text_surf, text_rect = functions.text_objects(text, font, (0, 0, 0))
        text_rect.center = (x1+x2 / 2, y1+y2 / 1.8)
        self.screen.blit(text_surf, text_rect)

    def check(self, x1, y1, x2, y2):
        if x1+x2 > self.mouse[0] > x1 and y1+y2 > self.mouse[1] > y1:
            return True

    def menu_events(self, event):
        if event == "play":
            self.bool_menu = False
        elif event == 'quit':
            self.quit()

    def crash(self):
        self.message_display('You crashed!')

    def menu(self):
        while self.bool_menu:
            self.mouse = pygame.mouse.get_pos()
            self.pressed = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.menu_img, (0, 0))

            self.draw_rect(color=[0, 200, 0],
                           x1=self.screen_width/3, y1=self.screen_height/2,
                           x2=100, y2=50, text="Race!", event="play")

            self.draw_rect(color=[200, 0, 0],
                           x1=self.screen_width*2/3-100, y1=self.screen_height/2,
                           x2=100, y2=50, text="Quit!", event="quit")

            font = pygame.font.SysFont('Ravie', 80)
            text_surf, text_rect = functions.text_objects("Racing Game", font, (220, 160, 0))
            text_rect.center = (self.screen_width / 2, self.screen_height / 4)
            self.screen.blit(text_surf, text_rect)
            pygame.display.update()
            self.clock.tick(30)
