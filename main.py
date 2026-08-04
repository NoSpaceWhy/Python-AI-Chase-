import pygame

pygame.init()

width = 1280
height = 650

screen = pygame.display.set_mode((width, height))
Clock = pygame.time.Clock()
dt = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_rect = pygame.FRect((screen.get_width() / 2, screen.get_height() / 2), (50, 100))
speed = 300

# ground
ground_offset = 80
ground_rect = pygame.FRect((0, ground_offset),(screen.get_width(), screen.get_height() - ground_offset ))

# enemy
enemy_rect =  pygame.FRect((100, 100), (50, 100))
enemy_speed = [300, 300]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("sky blue")

    # game render here
    pygame.draw.rect(screen, "#4dbf26", ground_rect)
    enemy = pygame.draw.rect(screen, "grey", enemy_rect)
    player = pygame.draw.rect(screen, "red", player_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= speed * dt
    if keys[pygame.K_s]:
        player_rect.y += speed * dt
    if keys[pygame.K_a]:
        player_rect.x -= speed * dt
    if keys[pygame.K_d]:
        player_rect.x += speed * dt

    # print(dt)
    # border colsion
    if player_rect.x <= 0:
       player_rect.x = 0 * dt
    elif player_rect.y <= 0:
       player_rect.y = 0 * dt
    elif player_rect.right >= width:
       # player_rect.right = width * dt # this has a defect this is because of dt, dt is turning it into 0
       player_rect.right = width - (player_rect.w - 5) * dt
    elif player_rect.bottom >= height:
        player_rect.bottom = height - (player_rect.h - 5) * dt # this is the defect less

    # collsion
    if player_rect.colliderect(enemy_rect):
        # running = False
        print("collided")

    # enemy_rect.x += enemy_speed[0] * dt
    # enemy_rect.y += enemy_speed[1] * dt
    # if enemy_rect.x <= 0:
    #    enemy_rect.x = 0 * dt

    #    enemy_speed[0] *= -1 # bounce back
    # elif enemy_rect.y <= 0:
    #    enemy_rect.y = 0 * dt

    #    enemy_speed[1] *= -1 # bounce back
    # elif enemy_rect.right >= width:
    #    enemy_rect.right = width - (enemy_rect.w - 5) * dt

    #    enemy_speed[0] *= -1 # bounce back
    # elif enemy_rect.bottom >= height:
    #     enemy_rect.bottom = height - (enemy_rect.h - 5) * dt # this is the defect less

    #     enemy_speed[1] *= -1 # bounce back

# AI that chses you very basic but 
    enemy_rect.x += enemy_speed[0] * dt
    enemy_rect.y += enemy_speed[1] * dt

    if player_rect.x > enemy_rect.x:
       enemy_speed[0] = 200
    elif player_rect.x < enemy_rect.x:
       enemy_speed[0] = -200
   
    if player_rect.y > enemy_rect.y:
       enemy_speed[1] = 200
    elif player_rect.y < enemy_rect.y:
       enemy_speed[1] = -200
       
    pygame.display.flip()

    dt = Clock.tick(60) / 1000

pygame.quit()
