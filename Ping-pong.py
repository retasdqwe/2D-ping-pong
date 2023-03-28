#imports
from pygame import *


#window settings
window_im = "INTERWORLD.png"
w = 1000
h = 1000
window = display.set_mode((w, h))
display.set_caption("Ping-pong")
background = transform.scale(image.load(window_im), (w, h))


clock = time.Clock()
FPS = 60


#text
font.init()

font = font.SysFont(None, 30)
plr1_failed_text = font.render('Player 1 Lost', True, (250, 20, 0))
plr2_failed_text = font.render('Player 2 Lost', True, (250, 20, 0))

#character appearance

ball_im = "Ball.png"
Plr_im = "PlayerBaseplate.png"


#classes

class Plr1():
    def __init__(self, x, y, speed, p_image):

        self.image = transform.scale(image.load(p_image), (20, 85))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 995:
            self.rect.y += self.speed

class Plr2():
    def __init__(self, x, y, speed, p_image):

        self.image = transform.scale(image.load(p_image), (20, 85))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 995:
            self.rect.y += self.speed


class Ball():
    def __init__(self, x, y, speed_x, speed_y, b_image):

        self.image = transform.scale(image.load(b_image), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#classes stats

player1 = Plr1(100, 458, 10, Plr_im)
player2 = Plr2(900, 458, 10, Plr_im)
ball = Ball(180, 480, 3, 3, ball_im)


#game cycle
game = True
end = False

while game:
    for e in event.get():
        
        if e.type == QUIT:
            game = False
        
    if end != True:
        window.blit(background, (0, 0))
    

        ball.reset()
        player1.reset()
        player2.reset()

        player1.update()
        player2.update()

        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y

        display.update()

    
    if sprite.collide_rect(player1, ball):
        ball.speed_x *= -1
    
    if sprite.collide_rect(player2, ball):
        ball.speed_x *= -1
    
    
    if ball.rect.x < 5:
        window.blit(plr1_failed_text, (200, 100))
        end = True
    
    if ball.rect.x > 995:
        window.blit(plr2_failed_text, (200, 100))
        end = True
    
    if ball.rect.y < 5:
        ball.speed_y *= -1
    
    if ball.rect.y > 995:
        ball.speed_y *= -1