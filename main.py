import random
import time
import pygame
import math
ker_time = 0


def create_new_bjij(px, py):
    bjij.append({})
    bjij[-1]['x'] = px
    bjij[-1]['y'] = py
    bjij[-1]['speed'] = random.randint(1, 10)
    bjij[-1]['energy'] = random.randint(1, 10)
    bjij[-1]['amenamotik_x'] = None
    bjij[-1]['amenamotik_y'] = None
    bjij[-1]['distance'] = None
    bjij[-1]['amenamotik_num'] = None


def generate_ker():
    global ker_time
    if ker_time + 0.5 < time.process_time():
        ker.append({})
        ker[-1]['x'] = random.randint(50, 700)
        ker[-1]['y'] = random.randint(50, 700)
        ker[-1]['energy'] = random.randint(2, 8)
        ker_time = time.process_time()
pygame.init()
ker = []
for i in range(10):
    ker.append({})
    ker[-1]['x'] = random.randint(50, 700)
    ker[-1]['y'] = random.randint(50, 700)
    ker[-1]['energy'] = random.randint(2, 8)

bjij = []

for i in range(1):
    bjij.append({})
    bjij[-1]['x'] = random.randint(50, 700)
    bjij[-1]['y'] = random.randint(50, 700)
    bjij[-1]['speed'] = 10
    bjij[-1]['energy'] = random.randint(1, 10)
    bjij[-1]['amenamotik_x'] = None
    bjij[-1]['amenamotik_y'] = None
    bjij[-1]['distance'] = None
    bjij[-1]['amenamotik_num'] = None

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Game")
background = pygame.image.load("img/background.jpg")
bjij_img =pygame.image.load("img/bjij.png")
ker_img = pygame.image.load("img/ker.png")
run = True
clock = pygame.time.Clock()
e = 0

while run:
    clock.tick(10)
    generate_ker()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(background, (0, 0))
    for i in range(len(ker)):
        win.blit(ker_img, (ker[i]['x'], ker[i]['y']))

    s = True
    for i in range(len(bjij)):
        bjij[i]['energy'] -= 0.1
        if bjij[i]['energy'] >= 30:
            bjij[i]['energy'] /= 2
            create_new_bjij(bjij[i]['x']+10, bjij[i]['y']+10)
        if bjij[i]['energy'] <= 0:
            s = i
            continue



        h = False
        if bjij[i]['amenamotik_x'] is None:
            distance = 100000
            number = 0
            for d in range(len(ker)):
                o = math.sqrt((bjij[i]['x'] - ker[d]['x']) ** 2 + (bjij[i]['y'] - ker[d]['y']) ** 2)
                if o < distance:
                    distance = o
                    sin = (bjij[i]['x'] - ker[d]['x']) / distance
                    cos = (bjij[i]['y'] - ker[d]['y']) / distance
                    bjij[i]["amenamotik_x"] = sin
                    bjij[i]["amenamotik_y"] = cos
                    bjij[i]["distance"] = distance
                    number = d
                    bjij[i]['amenamotik_num'] = number
            if distance <= 5:
                h = True
                bjij[i]['energy'] += ker[d]['energy']
                bjij[i]['amenamotik_x'] = None
                bjij[i]['amenamotik_y'] = None
                bjij[i]["distance"] = None
                delet = number
            if bjij[i]['y'] > 0 and bjij[i]['y'] < 900:
                bjij[i]['y'] -= bjij[i]["amenamotik_y"] * bjij[i]['speed']
            else:
                if bjij[i]['y'] > 900:
                    bjij[i]['y'] = 899
                else:
                    bjij[i]['y'] = 1
            if bjij[i]['x'] > 0 and bjij[i]['x'] < 900:
                bjij[i]['x'] -= bjij[i]["amenamotik_x"] * bjij[i]['speed']
            else:
                if bjij[i]['x'] > 900:
                    bjij[i]['x'] = 899
                else:
                    bjij[i]['x'] = 1
        else:
            bjij[i]['distance'] -= bjij[i]['speed']

            if bjij[i]['y'] > 0 and bjij[i]['y'] < 900:
                bjij[i]['y'] -= bjij[i]['amenamotik_y'] * bjij[i]['speed']
            else:
                if bjij[i]['y'] > 900:
                    bjij[i]['y'] = 899
                else:
                    bjij[i]['y'] = 1
            if bjij[i]['x'] > 0 and bjij[i]['x'] < 900:
                bjij[i]['x'] -= bjij[i]['amenamotik_x'] * bjij[i]['speed']
            else:
                if bjij[i]['x'] > 900:
                    bjij[i]['x'] = 899
                else:
                    bjij[i]['x'] = 1
            if bjij[i]['distance'] <= 5:
                h = True
                bjij[i]['energy'] += bjij[i]['amenamotik_num']
                delet = bjij[i]['amenamotik_num']



        win.blit(bjij_img, (bjij[i]['x'], bjij[i]['y']))
    if h is True:
        bjij[i]['amenamotik_x'] = None
        bjij[i]['amenamotik_y'] = None
        del ker[delet]






    if s is not True:
        e += 1
        print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo', e)
        del bjij[s]
    pygame.display.update()