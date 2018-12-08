import Game
import pygame
import Log


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def game_loop():
    game = Game.Game()
    logs = [Log.Log(screen_width=game.screen_width, speed=3)]
    length = 1
    add = True
    while game.exit is not True:
        if game.dodged != 0 and game.dodged % 10 == 0 and add and game.dodged <= 70:
            add = False
            logs.append(Log.Log(screen_width=game.screen_width, speed=logs[0].speed))
            length += 1

        if game.dodged % 10 == 1:
            add = True

        game.events()
        game.car()

        for i in range(length):
            game.screen.blit(logs[i].log_img, (logs[i].log_x, logs[i].log_y))
            if logs[i].move_down(screen_width=game.screen_width, screen_height=game.screen_height):
                if i == 0:
                    game.dodged += 1
                    if game.speed < game.max_speed:
                        game.speed *= 1.05
            if logs[i].check(cx=game.car_x, cy=game.car_y, cw=game.car_width, ch=game.car_height):
                game.crash()

        pygame.display.update()
        game.clock.tick(60)
