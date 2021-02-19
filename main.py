import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

background_color = white
(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Desen')
screen.fill(background_color)

dist = 20


def culoare(i):
    return {
        0: red,
        1: lime,
        2: blue,
        3: yellow,
        4: cyan,
        5: magenta
    }.get(i)


def desen(time):
    screen.fill(background_color)

    for i in range(200):
        if time > i*dist:
            pygame.draw.circle(screen, culoare(i % 6), (250, 250), time - i * dist)
            # if i % 2 == 0:
            #     pygame.draw.circle(screen, culoare(i/2 % 6), (250, 250), time - i*dist)
            # else:
            #     pygame.draw.circle(screen, white, (250, 250), time - i*dist)


t = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    desen(t)
    pygame.display.flip()
    t += 0.1