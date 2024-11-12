import pygame as pg
from random import randint

# constantes utiles
NB_PIXELS =30
T_PIXELS =20
T_ECRAN = NB_PIXELS*T_PIXELS
RED = (255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)

# état initial du jeu
snake = [(10, 15),(11, 15),(12, 15)]
fruit=(randint(0,NB_PIXELS-1),randint(0,NB_PIXELS-1))
direction=(-1,0)

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
        if event.key == pg.K_UP:
            direction=(0,-1)
        if event.key == pg.K_DOWN:
            direction=(0,1)
        if event.key == pg.K_LEFT:
            direction=(-1,0)
        if event.key == pg.K_RIGHT:
            direction=(1,0)
    return running, direction

def move_snake(snake, direction):
    for i in range(1,len(snake)):
        snake[-i]=snake[-i-1]
    snake[0]=(snake[0][0]+direction[0],snake[0][1]+direction[1])
    return snake

def draw_snake(snake):
    for c in snake:
        rect_c = pg.Rect(c[0]*T_PIXELS, c[1]*T_PIXELS, T_PIXELS, T_PIXELS)
        pg.draw.rect(screen, GREEN, rect_c)


if __name__ == "__main__":
    #initialisation de l'écran
    pg.init()
    screen = pg.display.set_mode((T_ECRAN, T_ECRAN))
    clock = pg.time.Clock()

    running = True
    while running:
        clock.tick(8)
        for event in pg.event.get():
            running, direction= handle_event(event, running, direction)

        draw_damier()

        move_snake(snake,direction)
        draw_snake(snake)
        
        #création du nouveau fruit, si le précédent a été mangé
        if snake[0]==fruit:
            fruit=(randint(0,NB_PIXELS-1), randint(0,NB_PIXELS-1))
            snake=snake+[snake[-1]]
        #affichage du fruit
        rect_f = pg.Rect(fruit[0]*T_PIXELS, fruit[1]*T_PIXELS, T_PIXELS, T_PIXELS)
        pg.draw.rect(screen, RED, rect_f)

        pg.display.update()

    pg.quit()