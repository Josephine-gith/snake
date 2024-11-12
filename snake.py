import pygame as pg
from random import randint
from collections import deque, namedtuple

# constantes utiles
NB_PIXELS =30
T_PIXELS =20
T_ECRAN = NB_PIXELS*T_PIXELS
RED = (255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
EPS=2

# état initial du jeu
Cell=namedtuple("Cell", ["x","y"])
snake = deque([Cell(x=10,y=15),Cell(x=11,y=15),Cell(x=12,y=15)])
fruit=Cell(x=randint(0,NB_PIXELS-1),y=randint(0,NB_PIXELS-1))
direction=Cell(x=-1,y=0)
acc=2

# sous-fonctions utiles
def draw_damier():
    screen.fill(BLACK)
    for i in range(NB_PIXELS):
        for j in range(NB_PIXELS):
            if (i+j)%2==0:
                rect = pg.Rect(i*T_PIXELS, j*T_PIXELS, T_PIXELS, T_PIXELS)
                pg.draw.rect(screen, WHITE, rect)

def handle_event(event, running, direction):
    if event.type == pg.QUIT:
        running = False
    # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
    elif event.type == pg.KEYDOWN:
        # si la touche est "Q" on veut quitter le programme
        if event.key == pg.K_q:
            running = False
        if event.key == pg.K_UP and direction!=Cell(x=0,y=1):
            direction=Cell(x=0,y=-1)
        if event.key == pg.K_DOWN and direction!=Cell(x=0,y=-1):
            direction=Cell(x=0,y=1)
        if event.key == pg.K_LEFT and direction!=Cell(x=1,y=0):
            direction=Cell(x=-1,y=0)
        if event.key == pg.K_RIGHT and direction!=Cell(x=-1,y=0):
            direction=Cell(x=1,y=0)
    return running, direction

def move_snake(snake, direction):
    for i in range(1,len(snake)):
        snake[-i]=snake[-i-1]
    snake[0]=Cell(x=snake[0][0]+direction[0],y=snake[0][1]+direction[1])
    return snake

def draw_snake(snake):
    for c in snake:
        rect_c = pg.Rect(c[0]*T_PIXELS, c[1]*T_PIXELS, T_PIXELS, T_PIXELS)
        pg.draw.rect(screen, GREEN, rect_c)

def game_over(snake, running):
    if snake[-1] in list(snake)[:-2]:
        running = False
    elif snake[0][0] in [-1,NB_PIXELS] or snake[0][-1] in [-1,NB_PIXELS]:
        running = False
    return running


if __name__ == "__main__":
    #initialisation de l'écran
    pg.init()
    screen = pg.display.set_mode((T_ECRAN, T_ECRAN))
    clock = pg.time.Clock()

    running = True
    while running:
        clock.tick(acc*EPS)
        for event in pg.event.get():
            running, direction= handle_event(event, running, direction)

        draw_damier()

        move_snake(snake,direction)
        draw_snake(snake)
        
        #création du nouveau fruit, si le précédent a été mangé
        if fruit in snake:
            fruit=(randint(0,NB_PIXELS-1), randint(0,NB_PIXELS-1))
            snake.append(snake[-1])
            acc=acc+1
        #affichage du fruit
        rect_f = pg.Rect(fruit[0]*T_PIXELS, fruit[1]*T_PIXELS, T_PIXELS, T_PIXELS)
        pg.draw.rect(screen, RED, rect_f)

        running = game_over(snake,running)

        pg.display.update()

    pg.quit()