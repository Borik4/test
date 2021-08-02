import random
import time
import pygame
import math
ker_time = 0

def generate_ker():
    global ker_time
    if ker_time + 0.5 < time.process_time():
        ker.append({})
        ker[-1]['x'] = random.randint(50, 700)
        ker[-1]['y'] = random.randint(50, 700)
        ker_time = time.process_time()
pygame.init()
ker = [{'x': 484, 'y': 638}, {'x': 730, 'y': 282}, {'x': 681, 'y': 103}, {'x': 541, 'y': 789}, {'x': 370, 'y': 153}, {'x': 153, 'y': 784}, {'x': 438, 'y': 792}, {'x': 691, 'y': 176}, {'x': 565, 'y': 70}, {'x': 696, 'y': 86}, {'x': 685, 'y': 697}, {'x': 675, 'y': 88}, {'x': 35, 'y': 43}, {'x': 833, 'y': 275}, {'x': 827, 'y': 133}, {'x': 437, 'y': 32}, {'x': 481, 'y': 636}, {'x': 286, 'y': 435}, {'x': 781, 'y': 814}, {'x': 657, 'y': 68}, {'x': 428, 'y': 505}, {'x': 411, 'y': 562}, {'x': 207, 'y': 384}, {'x': 623, 'y': 712}, {'x': 191, 'y': 724}, {'x': 506, 'y': 283}, {'x': 877, 'y': 706}, {'x': 451, 'y': 21}, {'x': 86, 'y': 284}, {'x': 227, 'y': 490}, {'x': 567, 'y': 228}, {'x': 228, 'y': 720}, {'x': 282, 'y': 170}, {'x': 211, 'y': 79}, {'x': 332, 'y': 701}, {'x': 544, 'y': 623}, {'x': 421, 'y': 797}, {'x': 558, 'y': 63}, {'x': 36, 'y': 54}, {'x': 440, 'y': 225}, {'x': 366, 'y': 215}, {'x': 513, 'y': 203}, {'x': 259, 'y': 237}, {'x': 110, 'y': 421}, {'x': 663, 'y': 440}, {'x': 310, 'y': 190}, {'x': 179, 'y': 715}, {'x': 337, 'y': 497}, {'x': 184, 'y': 742}, {'x': 637, 'y': 232}, {'x': 375, 'y': 305}, {'x': 188, 'y': 314}, {'x': 398, 'y': 643}, {'x': 36, 'y': 326}, {'x': 716, 'y': 739}, {'x': 79, 'y': 126}, {'x': 557, 'y': 584}, {'x': 174, 'y': 330}, {'x': 750, 'y': 530}, {'x': 321, 'y': 804}, {'x': 648, 'y': 469}, {'x': 326, 'y': 259}, {'x': 518, 'y': 46}, {'x': 148, 'y': 751}, {'x': 250, 'y': 150}, {'x': 295, 'y': 9}, {'x': 574, 'y': 98}, {'x': 847, 'y': 694}, {'x': 801, 'y': 667}, {'x': 267, 'y': 782}, {'x': 723, 'y': 359}, {'x': 592, 'y': 191}, {'x': 26, 'y': 363}, {'x': 223, 'y': 93}, {'x': 791, 'y': 347}, {'x': 379, 'y': 776}, {'x': 529, 'y': 25}, {'x': 335, 'y': 817}, {'x': 506, 'y': 290}, {'x': 45, 'y': 298}, {'x': 767, 'y': 633}, {'x': 473, 'y': 131}, {'x': 577, 'y': 712}, {'x': 29, 'y': 576}, {'x': 712, 'y': 268}, {'x': 358, 'y': 559}, {'x': 115, 'y': 22}, {'x': 861, 'y': 768}, {'x': 627, 'y': 322}, {'x': 226, 'y': 290}, {'x': 574, 'y': 26}, {'x': 491, 'y': 501}, {'x': 633, 'y': 500}, {'x': 641, 'y': 525}, {'x': 431, 'y': 685}, {'x': 253, 'y': 46}, {'x': 15, 'y': 505}, {'x': 168, 'y': 494}, {'x': 678, 'y': 540}, {'x': 737, 'y': 496}]

bjij = [{'x': 22, 'y': 463, 'speed': 4, 'time': 7.932637097581722, 'new_time': 2.0853737877235714}, {'x': 844, 'y': 344, 'speed': 10, 'time': 3.7853535585099216, 'new_time': 1.2277775076009545}, {'x': 862, 'y': 514, 'speed': 5, 'time': 3.2935996467732975, 'new_time': 8.169167866205186}, {'x': 221, 'y': 10, 'speed': 5, 'time': 8.282134683751794, 'new_time': 7.945940377751228}, {'x': 15, 'y': 598, 'speed': 4, 'time': 2.7050573229681465, 'new_time': 5.829470007713998}, {'x': 553, 'y': 39, 'speed': 6, 'time': 7.868227278990302, 'new_time': 8.983896763522738}, {'x': 77, 'y': 845, 'speed': 2, 'time': 7.855842372937362, 'new_time': 7.37948957962058}, {'x': 416, 'y': 447, 'speed': 9, 'time': 6.505293191434342, 'new_time': 4.036384253705529}, {'x': 162, 'y': 489, 'speed': 8, 'time': 0.24516125513798226, 'new_time': 7.474410177170784}, {'x': 306, 'y': 542, 'speed': 2, 'time': 0.06295681578924794, 'new_time': 9.980683411684591}]
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Game")
background = pygame.image.load("img/background.jpg")
bjij_img =pygame.image.load("img/bjij.png")
ker_img = pygame.image.load("img/ker.png")
run = True
clock = pygame.time.Clock()
e = 0

while run:

    generate_ker()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(30)
    win.blit(background, (0, 0))
    for i in range(len(ker)):
        win.blit(ker_img, (ker[i]['x'], ker[i]['y']))

    s = True
    for i in range(len(bjij)):
        if bjij[i]['new_time'] + 15 < time.process_time():
            bjij.append({})
            bjij[-1]['x'] = bjij[i]['x'] + 20
            bjij[-1]['y'] = bjij[i]['y'] + 20
            bjij[-1]['speed'] = random.randint(0, 10)
            bjij[-1]['new_time'] = time.process_time()
            bjij[-1]['time'] = time.process_time()
            bjij[i]['new_time'] = time.process_time()
        if bjij[i]['time'] + 10 < time.process_time():
            s = i
            continue
        h = False
        distance = 100000
        number = 0
        for d in range(len(ker)):
            o = math.sqrt((bjij[i]['x'] - ker[d]['x']) ** 2 + (bjij[i]['y'] - ker[d]['y']) ** 2)
            if o < distance:
                distance = o
                sin = (bjij[i]['x'] - ker[d]['x']) / distance
                cos = (bjij[i]['y'] - ker[d]['y']) / distance
                number = d
                if distance <= 5:
                    h = True
                    bjij[i]['time'] = time.process_time()
                    delet = d
        if bjij[i]['y'] > 0 and bjij[i]['y'] < 900:
            bjij[i]['y'] -= cos * bjij[i]['speed']
        else:
            if bjij[i]['y'] > 900:
                bjij[i]['y'] = 899
            else:
                bjij[i]['y'] = 1
        if bjij[i]['x'] > 0 and bjij[i]['x'] < 900:
            bjij[i]['x'] -= sin * bjij[i]['speed']
        else:
            if bjij[i]['x'] > 900:
                bjij[i]['x'] = 899
            else:
                bjij[i]['x'] = 1
        win.blit(bjij_img, (bjij[i]['x'], bjij[i]['y']))
        if h is True:
            del ker[delet]
    if s is not True:
        e += 1
        print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo', e)
        del bjij[s]
    pygame.display.update()