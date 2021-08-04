import random
import time
import pygame
import math
ker_time = 0


def go_to(ia):
    bjij[ia]['distance'] -= bjij[ia]['speed']
    if bjij[ia]['y'] > 0 and bjij[ia]['y'] < 900:
        bjij[ia]['y'] -= bjij[ia]['amenamotik_y'] * bjij[ia]['speed']
    elif bjij[ia]['y'] > 0:
        bjij[ia]['y'] = 899
    else:
        bjij[ia]['y'] = 1
    if bjij[ia]['x'] > 0 and bjij[ia]['x'] < 900:
        bjij[ia]['x'] -= bjij[ia]['amenamotik_x'] * bjij[ia]['speed']
    elif bjij[ia]['x'] > 0:
        bjij[ia]['x'] = 899
    else:
        bjij[ia]['x'] = 1


def ker_utel(ui, kl):
    bjij[ui]['energy'] += ker[kl]['energy']
    bjij[ui]['amenamotik_x'] = None
    bjij[ui]['amenamotik_y'] = None
    bjij[ui]["distance"] = None
    bjij[ui]['amenamotik_num'] = None


def bjij_energy(qwert):
    bjij[qwert]['energy'] -= 0.1
    if bjij[qwert]['energy'] >= 30:
        print(bjij[qwert]['energy'])
        bjij[qwert]['energy'] /= 2
        print(bjij[qwert]['energy'])
        create_new_bjij(bjij[qwert]['x'] + 10, bjij[qwert]['y'] + 10)
        bjij[qwert]['amenamotik_x'] = None
        bjij[qwert]['amenamotik_y'] = None
        bjij[qwert]['distance'] = None
        bjij[qwert]['amenamotik_num'] = None
        print(bjij[0]['energy'])


def blit_ker():
    for i in range(len(ker)):
        win.blit(ker_img, (ker[i]['x'], ker[i]['y']))


def create_new_bjij(px, py):
    bjij.append({})
    bjij[-1]['x'] = px
    bjij[-1]['y'] = py
    bjij[-1]['speed'] = random.randint(1, 10)
    bjij[-1]['energy'] = random.randint(3, 4)
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
for i in range(15):
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
    blit_ker()
    s = True

    if len(bjij) > 1:
        has = 'o'



    for i in range(len(bjij)):
        win.blit(bjij_img, (bjij[i]['x'], bjij[i]['y']))
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
        go_to(i)
        if bjij[i]['distance'] <= 5:
            h = True
            bjij[i]['energy'] += ker[bjij[i]['amenamotik_num']]['energy']


            for j in range(len(bjij)):
                if bjij[j]['amenamotik_num'] == bjij[i]['amenamotik_num']:
                    if j != i:
                        bjij[-1]['amenamotik_x'] = None
                        bjij[-1]['amenamotik_y'] = None
                        bjij[-1]['distance'] = None
                        bjij[-1]['amenamotik_num'] = None

            delet = bjij[i]['amenamotik_num']



        bjij_energy(i)
        if bjij[i]['energy'] <= 0:
            s = i



    if h is True:
        bjij[i]['amenamotik_x'] = None
        bjij[i]['amenamotik_y'] = None
        bjij[i]['distance'] = None
        bjij[i]['amenamotik_num'] = None
        del ker[delet]

    if s is not True:
        e += 1
        print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo', e)
        del bjij[s]
    pygame.display.update()