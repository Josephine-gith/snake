import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)

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

    #dessin du damier
    screen.fill((0,0,0))
    width = 20 # largeur du rectangle en pixels
    height = 20 # hauteur du rectangle en pixels
    for i in range(30):
        for j in range(30):
            if (i+j)%2==0:
                x = i*20 # coordonnée x (colonnes) en pixels
                y = j*20 # coordonnée y (lignes) en pixels
            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, (255, 255, 255), rect)

    # dessin du snake
    snake = [(10, 15),(11, 15),(12, 15),]
    for c in snake:
        rect_c=rect = pg.Rect(c[0]*20, c[1]*20, width, height)
        pg.draw.rect(screen, (255,0,0), rect_c)
    
    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()