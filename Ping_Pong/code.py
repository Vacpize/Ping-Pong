from pygame import *

wind = display.set_mode((600,500))
background = transform.scale(image.load('back.png'), (600, 500))
display.set_caption('Pin pong "Kidney death" ver.')
font.init()

mixer.init()
hit = mixer.Sound('hit.wav')

font1 = font.SysFont("Montserrat-Blod.ttf", 50)
end_font = font.SysFont("Montserrat-Blod.ttf", 20)
end_txt = font1.render("The game ended", True, (224, 128, 40))
bottom_txt = end_font.render("good job", True, (224, 128, 40))

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

ball = GameSprite("ball.png", 300, 250, 2, 80,80)
speed_y = 2
speed_x = 2
follow = False

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)

        # update location of sprites

    player1.moving1()
    player2.moving2()
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
            game = False

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    #update/draw sprites

    wind.blit(background, (0,0))
    ball.reset()
    player1.reset()
    player2.reset()

    display.update()

while follow:
    for e in event.get():
        if e.type == QUIT:
            follow = False
    wind.blit(end_txt, (160, 200))
    wind.blit(bottom_txt, (270, 250))
    display.update()