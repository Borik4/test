import pygame
import time
import random


def snake_blit():
    if direction == 1:
        win.blit(head_down, (snake[-1]['x'], snake[-1]['y']))
    elif direction == -1:
        win.blit(head_up, (snake[-1]['x'], snake[-1]['y']))
    elif direction == 2:
        win.blit(head_right, (snake[-1]['x'], snake[-1]['y']))
    elif direction == -2:
        win.blit(head_left, (snake[-1]['x'], snake[-1]['y']))

    for pl in range(len(snake) - 1):
        win.blit(snake_img, (snake[pl]['x'], snake[pl]['y']))


def snake_go():
    snake.append({})
    if direction % 2 == 0 and direction > 0:
        snake[-1]['x'] = snake[-2]['x'] + 35
        snake[-1]['y'] = snake[-2]['y']
    elif direction % 2 == 0 and direction < 0:
        snake[-1]['x'] = snake[-2]['x'] - 35
        snake[-1]['y'] = snake[-2]['y']
    elif direction < 0:
        snake[-1]['x'] = snake[-2]['x']
        snake[-1]['y'] = snake[-2]['y'] - 35
    elif direction > 0:
        snake[-1]['x'] = snake[-2]['x']
        snake[-1]['y'] = snake[-2]['y'] + 35
    if len(snake) > p:
        del snake[0]


def ker_blit():
    win.blit(ker_img, (ker['x'], ker['y']))


def dead():
    global run
    for df in range(len(red)):
        if snake[-1]['x'] == red[df]['x'] and snake[-1]['y'] == red[df]['y']:
            print('red')
            run = False
            print()
            print(red)
            print(snake[-1])
    if 670 < snake[-1]['x'] or snake[-1]['x'] < 0 or 670 < snake[-1]['y'] or snake[-1]['y'] < 0:
        print('durs')
        run = False
    for wer in range(len(snake) - 1):
        if snake[wer]['x'] == snake[-1]['x'] and snake[wer]['y'] == snake[-1]['y']:
            print('git')
            run = False


def ker_stugum():
    global p, a
    if ker['x'] == snake[-1]['x'] and ker['y'] == snake[-1]['y']:
        t = True
        while t:
            t = False
            ker['x'] = random.randrange(25, 671, 35)
            ker['y'] = random.randrange(25, 671, 35)
            for fgh in range(len(snake)):
                if snake[fgh]['x'] == ker['x'] and snake[fgh]['y'] == ker['y']:
                    t = True
                    break
            if t is False:
                for vbn in range(len(red)):
                    if red[vbn]['x'] == ker['x'] and red[vbn]['x'] == ker['y']:
                        t = True
                        break
        p += 1
        a -= a/40
        print(a)


def blit_red():
    for asd in range(len(red)):
        win.blit(red_img, (red[asd]['x'], red[asd]['y']))


pygame.init()
win = pygame.display.set_mode((705, 705))
pygame.display.set_caption("Game")
snake_img = pygame.image.load("img/black.jpg")
ker_img = pygame.image.load("img/green.jpg")
red_img = pygame.image.load("img/red.jpg")
head_left = pygame.image.load('img/head_left.jpg')
head_up = pygame.image.load('img/head_up.jpg')
head_right = pygame.image.load('img/head_right.jpg')
head_down = pygame.image.load('img/head_down.jpg')
run = True
clock = pygame.time.Clock()

direction = -2
red = []
for i in range(20):
    red.append({})
    while True:
        red[-1]['x'] = random.randrange(25, 671, 35)
        if red[-1]['x'] != 305 and red[-1]['x'] != 340 and red[-1]['x'] != 270 and red[-1]['x'] != 235:
            break
    red[-1]['y'] = random.randrange(25, 671, 35)
snake = [{'x': 305, 'y': 305}]
ker = {'x': 340, 'y': 340}
last_time = 0
p = 1
a = 0.4
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('quit')
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = -2
    if keys[pygame.K_RIGHT]:
        direction = 2
    if keys[pygame.K_UP]:
        direction = -1
    if keys[pygame.K_DOWN]:
        direction = 1

    if time.process_time() - a > last_time:
        dead()
        win.fill((250, 250, 250))
        blit_red()
        ker_blit()
        snake_go()
        snake_blit()
        pygame.display.update()
        last_time = time.process_time()
        ker_stugum()
