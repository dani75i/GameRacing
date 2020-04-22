import pygame
import random
from car import Car
from obstacle import Obstacle
from text import Text

pygame.init()

# Constantes
SIZE_FENETRE_X = 540
SIZE_FENETRE_Y = 800
NUMBER_OBSTACLE = 1
TIME_GAME = 50000

# Variables
continuer = True
start = False
x = 0
y = 0
y2 = - SIZE_FENETRE_Y
list_obstacles = []

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((SIZE_FENETRE_X, SIZE_FENETRE_Y))

# Définition du background
background = pygame.image.load("images/street.PNG")
background = pygame.transform.scale(background, (SIZE_FENETRE_X, SIZE_FENETRE_Y))

# Définition de la voiture
voiture = pygame.image.load("images/voiture.jpg")
voiture = pygame.transform.scale(voiture, (100, 50))
voiture = pygame.transform.rotate(voiture, -90)

# Instanciation class Text
texte = Text()

# Instanciation class Car
car = Car()


# Fonction pour créer des obstacles
def create_obstacles(number_obstacle):
    for obstacle in range(number_obstacle):
        obstacle_one = Obstacle(random.randint(300, 340), random.randint(100, 150))
        obstacle_two = Obstacle(random.randint(200, 240), random.randint(200, 250))
        list_obstacles.append(obstacle_one)
        list_obstacles.append(obstacle_two)


# Instanciation class Obstacle
create_obstacles(NUMBER_OBSTACLE)

# Intanciation Timer
time_elapsed_since_last_action = TIME_GAME
clock = pygame.time.Clock()

while continuer:

    # Afficher et animer le background
    y += 5
    y2 += 5

    fenetre.blit(background, (x, y))
    fenetre.blit(background, (x, y2))

    if y > SIZE_FENETRE_Y:
        y = -SIZE_FENETRE_Y
    if y2 > SIZE_FENETRE_Y:
        y2 = -SIZE_FENETRE_Y

    # Afficher le text
    if not start:
        fenetre.blit(texte.start_message(), texte.textRect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            continuer = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True

    # Commenrcer le jeu
    if start:

        # Decrement timer
        dt = clock.tick()
        time_elapsed_since_last_action -= dt
        time = int(time_elapsed_since_last_action / 1000)

        if time_elapsed_since_last_action <= 0:
            fenetre.blit(texte.win_message(), texte.textRect)

        else:
            fenetre.blit(texte.time_message(str(time)), texte.textRect)
            fenetre.blit(car.image, (car.rect.x, car.rect.y))

            if len(list_obstacles) == 0:
                create_obstacles(1)

            for obstacle in list_obstacles:
                if obstacle.rect.y >= 800:
                    list_obstacles.remove(obstacle)
                else:
                    fenetre.blit(obstacle.image, (obstacle.rect.x, obstacle.rect.y))
                    obstacle.move_down()

            # print(list_obstacles)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT] and car.rect.x + car.rect.width < SIZE_FENETRE_X:
                if car.rect.x <= 345:
                    car.move_right()

            elif keys[pygame.K_LEFT] and car.rect.x > 0:
                if car.rect.x > 155:
                    car.move_left()

            elif keys[pygame.K_UP] and car.rect.y > 0:
                car.move_up()

            elif keys[pygame.K_DOWN] and car.rect.y + car.rect.height < SIZE_FENETRE_Y:
                car.move_down()

    # Rafraichissement
    pygame.display.flip()
