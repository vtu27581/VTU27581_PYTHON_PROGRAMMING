import game

import random

import sys

pygame. init()

width, height = 500,600

Screen = pygame display.set_mode (width, height))

pygame display set caption ("car Dodging hame")

WHITE = (255,255, 255)

RED=(200,0,0)

BLUE= (0,0,200)

car = pygame Rect (230, 500, 40,60)

obstacle =pygame. React (random randint(0, width_40)

0,40,60)

speed = 5

Obstacle-speed = 5

Clock = pygame. time clock()

nunning: True

while running:

Screen.fill(WHITE)

for event in pygame event.get():

If event.type == pygame. QUIT:

running=faise

keys=Pygame. key-get-pressed()

if keys [Pygame.K-LEFT] and car-left>0:

car.move-ip (-speed, 0).

iF keys (pygame.k-RIGHT] and car. right <width:

car. move-ip (speed, 10)

obstrale move-ip (0. obstacle-speed)

it obstacle top > heigt:

obstacle top=0

obstacle-left-random.randint (0, width=40)

pygame draw rect (screen, BLUE, POT)

pygame draw.rect (screen, RED, Obstacie)

it com collide erect (obstacle):

front= pygame front sys front (None, 50)

text = front render(" GAME OVER!", True, REO)

screen. blit (text, (150,250))

pygame. display flip()

pygame-time.wait (2000)

running = false

pygame display flip()

clock tick (60)

pygame.quit()

Sys.exit()
