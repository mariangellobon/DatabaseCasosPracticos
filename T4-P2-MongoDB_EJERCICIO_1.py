import pygame
import time
import random
import pymongo
from datetime import datetime

###################### BLOQUE A COMPLETAR ##########################
# PALABRA CLAVE: CONEXIONES

# Conexiones con MongoDB
db_name = "practica_2_mongodb"
db_uri = ''
db_client = ''
db = ''

# Colecciones
coleccion_usuarios = ''
coleccion_partidas = ''

###################### FIN DE BLOQUE A COMPLETAR ###################

# Función para pedir datos de usuario
def get_user_data():
    username = input("Ingrese su nombre de usuario: ")
    email = input("Ingrese su correo electrónico: ")
    
    ###################### BLOQUE A COMPLETAR ##########################
    # PALABRA CLAVE: USUARIO
    
    # Buscar si el usuario ya existe y si no existe, insertalo en la BBDD

    user = {
        "username": username,
        "email": email,
        "signup_date": datetime.now()
    }

    
    ###################### FIN DE BLOQUE A COMPLETAR ###################
    
    return user

# Colores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Dimensiones de la pantalla
dis_width = 800
dis_height = 600

# Inicializar Pygame
pygame.init()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Practica 2: Snake x MongoDB')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop(user):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1
    steps = 0
    level = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    start_time = time.time()

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("¡Chocaste! Presiona C para jugar de nuevo o Q para salir", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(user)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                
            
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    steps += 1

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            if length_of_snake % 5 == 0:
                level += 1

        clock.tick(snake_speed)

    ###################### BLOQUE A COMPLETAR ##########################
    # PALABRA CLAVE: PARTIDA

    # Almacenar información de la partida en MongoDB
    game_data = {
        "user_id": user["username"],
        "score": length_of_snake - 1,
        "date": datetime.now(),
        "duration": time.time() - start_time,
        "level": level,
        "steps": steps,
        "final_position": {"x": x1, "y": y1}
    }
    
    
    ###################### FIN DE BLOQUE A COMPLETAR ###################
    

    pygame.quit()
    quit()

def main():
    user = get_user_data()
    gameLoop(user)

if __name__ == "__main__":
    main()