from pygame  import *

main_weight = 700
main_height = 500
window = display.set_mode((main_weight, main_height))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("горы.png"), (main_weight, main_height))
sprite1 = transform.scale(image.load("доги.png"), (50, 50))
sprite2 = transform.scale(image.load("пикачу.png"), (50, 50))
ball = transform.scale(image.load("Мячик.png"), (50, 50))

clock = time.Clock()

mixer.init()
mixer.music.load("звуки дождя.ogg")
mixer.music.play()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_weight, player_height, player_speed):
        super().__init__()
        self.player_image = transform.scale(image.load(player_image), (player_weight, player_height))
        self.speed = player_speed
        self.rect = self.player_image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.player_image, (self.rect.x, self.rect.y))


class Dog(GameSprite):
    def dog_update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys[K_DOWN] and self.rect.y < 445:
            self.rect.y += 10


class Pikachu(GameSprite):
    def pikachu_update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys[K_s] and self.rect.y < 445:
            self.rect.y += 10


player1 = Dog("доги.png", 605, 250, 50, 50, 5)
player2 = Pikachu("пикачу.png", 45, 250, 50, 50, 5)
mach = GameSprite("Мячик.png", 350, 250, 50, 50, 5)

speed_x = 3
speed_y = 3
finish = False
game = True
while game:
    window.blit(background, (0, 0))


    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        mach.rect.x += speed_x
        mach.rect.y += speed_y
        if mach.rect.y >= 450:
            mach.rect.x += speed_x
            mach.rect.y -= speed_y
        if mach.rect.y <= 0:
            mach.rect.x -= speed_x
            mach.rect.y += speed_y

        player1.reset()
        player2.reset()
        mach.reset()

        player1.dog_update()
        player2.pikachu_update()

        if mach.rect.x <= 0:
            finish = True
            font.init()
            font1 = font.Font(None, 70)
            loser1 = font1.render("Player_1  is lose!", True, (0, 0, 255))
            window.blit(loser1, (200, 200))
        if mach.rect.x >= 650:
            finish = True
            font.init()
            font2 = font.Font(None, 70)
            loser2 = font2.render("Player_2 is lose!", True, (0, 0, 255))
            window.blit(loser2, (200, 200))

        display.update()
        clock.tick(60)
