from pygame import *
from time import time as tim

wind = display.set_mode((600,500))
background = transform.scale(image.load('back.png'), (600, 500))
display.set_caption('Pin pong "Kidney death" ver.')
font.init()

mixer.init()
hit = mixer.Sound('hit.wav')

font1 = font.SysFont("Montserrat-Blod.ttf", 50)
end_font = font.SysFont("Montserrat-Blod.ttf", 35)
end_txt = font1.render("The game ended", True, (224, 128, 40))
bottom_loose = end_font.render("You loose, bro", True, (224, 128, 40))
bottom_win = end_font.render("You win, bro", True, (224, 128, 40))


clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))  # (68, 100)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def reset(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def moving1(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 338:
            self.rect.y += self.speed

    def moving2(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 338:
            self.rect.y += self.speed

        
# mixer.init()
# mixer.music.load("space.ogg")
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')

player1 = Player("platform.png", 550, 169, 5, 40, 162)
player2 = Player("platform.png", 20, 169, 5, 40, 162)

ball = GameSprite("ball.png", 250, 250, 2, 80,80)
speed_y = 3
speed_x = 3

start_time = tim()
true_time = None

follow = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    print(ball.rect.x)
    clock.tick(60)

        # update location of sprites
    # print(game)
    player1.moving1()
    player2.moving2()
    
    #ball's phisycs
    if ball.rect.y >= 0 and ball.rect.bottom <= 500 and ball.rect.x >= 0 and ball.rect.x < 600 - 80:
        if ball.colliderect(player1.rect):
            speed_x *= -1
            speed_y *= 1
            hit.play()

        if ball.colliderect(player2.rect):
            speed_y *= 1
            speed_x *= -1
            hit.play()
    else:
        if ball.rect.y < 0 or ball.rect.y > 418:
            speed_y *= -1
        if ball.rect.x < -3 or ball.rect.x > 530:
            follow = True
            print(ball.rect.x)
            print(follow)
            game = False

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    # update time
    end_time = tim()
    true_time = round(end_time - start_time)
    # text of time 
    txt = f'Time:{str(true_time)}'
    time_txt = font1.render(txt, True, (224, 128, 40))
    # check, if game must end (win)
    if true_time >= 100:
        game = False 
        follow = True
        # print(follow)
        #update/draw sprites

    wind.blit(background, (0,0))
    ball.reset()
    player1.reset()
    player2.reset()
    wind.blit(time_txt, (10, 30))
    display.update()

#if game ended(loose)
while follow:
    for e in event.get():
        if e.type == QUIT:
            follow = False
    if ball.rect.x < -3 or ball.rect.x > 530:
        wind.blit(end_txt, (160, 200))
        wind.blit(bottom_loose, (250, 250))
    
    if true_time > 120:
        wind.blit(end_txt, (160, 200))
        wind.blit(bottom_win, (250, 220))
    display.update()
