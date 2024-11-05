import pygame as pg
from random import randint

np =30
tp =20

pg.init()
screen = pg.display.set_mode((np*tp,np*tp ))
clock = pg.time.Clock()

# initialisation
snake = [(10, 15),(11, 15),(12, 15)]
fruit=(randint(0,np-1),randint(0,np-1))
d=(-1,0)

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:
    clock.tick(10)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_UP:
                d=(0,-1)
            if event.key == pg.K_DOWN:
                d=(0,1)
            if event.key == pg.K_LEFT:
                d=(-1,0)
            if event.key == pg.K_RIGHT:
                d=(1,0)

    #dessin du damier
    screen.fill((0,0,0))
    for i in range(np):
        for j in range(np):
            if (i+j)%2==0:
                x = i*tp # coordonnée x (colonnes) en pixels
                y = j*tp # coordonnée y (lignes) en pixels
            rect = pg.Rect(x, y, tp, tp)
            pg.draw.rect(screen, (255, 255, 255), rect)

    #mouvement du snake
    for i in range(1,len(snake)):
        snake[-i]=snake[-i-1]
    snake[0]=(snake[0][0]+d[0],snake[0][1]+d[1])
    #affichage du snake déplacé
    for c in snake:
        rect_c=rect = pg.Rect(c[0]*tp, c[1]*tp, tp, tp)
        pg.draw.rect(screen, (0,255,0), rect_c)
    
    #création du nouveau fruit, si le précédent a été mangé
    if snake[0]==fruit:
        fruit=(randint(0,np), randint(0,np))
        snake=snake+[snake[-1]]
    #affichage du fruit
    rect_f = pg.Rect(fruit[0]*tp, fruit[1]*tp, tp, tp)
    pg.draw.rect(screen, (255, 0, 0), rect_f)

    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()