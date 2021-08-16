import random
import time
import pygame
import math

ker_time = 0


def go_to(ia):
    bjij[ia]['distance'] -= bjij[ia]['speed']
    if 0 < bjij[ia]['y'] < 900:
        bjij[ia]['y'] -= bjij[ia]['amenamotik_y'] * bjij[ia]['speed']
    elif bjij[ia]['y'] > 0:
        bjij[ia]['y'] = 899
    else:
        bjij[ia]['y'] = 1

    if 0 < bjij[ia]['x'] < 900:
        bjij[ia]['x'] -= bjij[ia]['amenamotik_x'] * bjij[ia]['speed']
    elif bjij[ia]['x'] > 0:
        bjij[ia]['x'] = 899
    else:
        bjij[ia]['x'] = 1


def bjij_energy(qwert):
    bjij[qwert]['energy'] -= 0.1
    if bjij[qwert]['energy'] >= 30:
        bjij[qwert]['energy'] /= 2
        create_new_bjij(bjij[qwert]['x'] + 10, bjij[qwert]['y'] + 10, bjij[qwert]['speed'])
        bjij[qwert]['amenamotik_x'] = None
        bjij[qwert]['amenamotik_y'] = None
        bjij[qwert]['distance'] = None
        bjij[qwert]['amenamotik_num'] = None


def blit_ker():
    for qwe in range(len(ker)):
        win.blit(ker_img, (ker[qwe]['x'], ker[qwe]['y']))


def stugum(a):
    if (ker[bjij[a]['amenamotik_num']]['x'] - bjij[a]['x']) ** 2 + (
            ker[bjij[a]['amenamotik_num']]['y'] - bjij[a]['y']) ** 2 > 5:
        return True
    return False


def create_new_bjij(px, py, pspeed):
    bjij.append({})
    bjij[-1]['x'] = px
    bjij[-1]['y'] = py
    if random.random() > 0.5:
        bjij[-1]['speed'] = pspeed + random.random()
    else:
        bjij[-1]['speed'] = pspeed - random.random()
    bjij[-1]['energy'] = random.randint(3, 4)
    bjij[-1]['amenamotik_x'] = None
    bjij[-1]['amenamotik_y'] = None
    bjij[-1]['distance'] = None
    bjij[-1]['amenamotik_num'] = None


def generate_ker():
    global ker_time, qweas
    if ker_time + 0.15 < time.process_time():
        ker.append({})
        ker[-1]['x'] = random.randint(50, 700)
        ker[-1]['y'] = random.randint(50, 700)
        ker[-1]['energy'] = random.randint(2, 8)
        ker[-1]['hert'] = qweas
        qweas += 1
        ker_time = time.process_time()


qweas = 1

pygame.init()
ker = []
for i in range(20):
    ker.append({})
    ker[-1]['x'] = random.randint(50, 700)
    ker[-1]['y'] = random.randint(50, 700)
    ker[-1]['energy'] = random.randint(2, 8)
    ker[-1]['hert'] = qweas
    qweas += 1
bjij = []

for i in range(10):
    bjij.append({})
    bjij[-1]['x'] = random.randint(50, 700)
    bjij[-1]['y'] = random.randint(50, 700)
    bjij[-1]['speed'] = random.randint(1, 10)
    bjij[-1]['energy'] = random.randint(1, 10)
    bjij[-1]['amenamotik_x'] = None
    bjij[-1]['amenamotik_y'] = None
    bjij[-1]['distance'] = None
    bjij[-1]['amenamotik_num'] = None

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Game")
bjij_img = pygame.image.load("img/bjij.png")
ker_img = pygame.image.load("img/ker.png")
run = True
clock = pygame.time.Clock()
e = 0
while run:
    joke = False
    generate_ker()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((250, 250, 250))
    blit_ker()
    s = True

    if len(bjij) > 1:
        has = 'o'

    bjij_speed = 0
    for i in range(len(bjij)):
        bjij_speed += bjij[i]['speed']
    bjij_speed /= len(bjij)
    print(bjij_speed)
    h = False
    for i in range(len(bjij)):
        if joke is True:
            win.blit(bjij_img, (bjij[i]['x'], bjij[i]['y']))

        win.blit(bjij_img, (bjij[i]['x'], bjij[i]['y']))
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
            if stugum(i):
                h = True
                b = bjij[i]['amenamotik_num']
                o = ker[b]
                bjij[i]['energy'] += o['energy']

            delet = bjij[i]['amenamotik_num']
            for j in range(len(bjij)):
                bjij[j]['amenamotik_x'] = None
                bjij[j]['amenamotik_y'] = None
                bjij[j]['distance'] = None
                bjij[j]['amenamotik_num'] = None
            joke = True

        bjij_energy(i)
        if bjij[i]['energy'] <= 0:
            s = i

    if h is True:
        bjij[i]['amenamotik_x'] = None
        bjij[i]['amenamotik_y'] = None
        bjij[i]['distance'] = None
        bjij[i]['amenamotik_num'] = None
        del ker[delet]
        h = False

    if s is not True:
        e += 1
        del bjij[s]
    pygame.display.update()
