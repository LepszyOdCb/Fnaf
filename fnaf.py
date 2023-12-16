import pygame
import sys

def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Aplikacja pełnoekranowa")

    screen_width = screen.get_width()
    screen_height = screen.get_height()
    
    main_back = pygame.image.load("main_back.png")
    left_back = pygame.image.load("left_side_back.png")
    right_back = pygame.image.load("right_side_back.png")
    left_back_closed = pygame.image.load("left_side_back_closed.png")
    right_back_closed = pygame.image.load("right_side_back_closed.png")
    left_back_light = pygame.image.load("left_side_back_light.png")
    right_back_light = pygame.image.load("right_side_back_light.png")
    
    cam_1 = pygame.image.load("cam_1.png")
    cam_2 = pygame.image.load("cam_2.png")
    cam_3 = pygame.image.load("cam_3a.png")
    cam_4 = pygame.image.load("cam_4.png")
    cam_5 = pygame.image.load("cam_5.png")
    cam_6 = pygame.image.load("cam_6.png")
    cam_7 = pygame.image.load("cam_7.png")
    cam_8 = pygame.image.load("cam_8.png")
    cam_9 = pygame.image.load("cam_9.png")

    scaled_main_back = pygame.transform.scale(main_back, (screen.get_width(), screen.get_height()))
    scaled_left_back = pygame.transform.scale(left_back, (screen.get_width(), screen.get_height()))
    scaled_right_back = pygame.transform.scale(right_back, (screen.get_width(), screen.get_height()))
    scaled_left_back_closed = pygame.transform.scale(left_back_closed, (screen.get_width(), screen.get_height()))
    scaled_right_back_closed = pygame.transform.scale(right_back_closed, (screen.get_width(), screen.get_height()))
    scaled_left_back_light = pygame.transform.scale(left_back_light, (screen.get_width(), screen.get_height()))
    scaled_right_back_light = pygame.transform.scale(right_back_light, (screen.get_width(), screen.get_height()))

    scaled_cam_1 = pygame.transform.scale(cam_1, (screen.get_width(), screen.get_height()))
    scaled_cam_2 = pygame.transform.scale(cam_2, (screen.get_width(), screen.get_height()))
    scaled_cam_3 = pygame.transform.scale(cam_3, (screen.get_width(), screen.get_height()))
    scaled_cam_4 = pygame.transform.scale(cam_4, (screen.get_width(), screen.get_height()))
    scaled_cam_5 = pygame.transform.scale(cam_5, (screen.get_width(), screen.get_height()))
    scaled_cam_6 = pygame.transform.scale(cam_6, (screen.get_width(), screen.get_height()))
    scaled_cam_7 = pygame.transform.scale(cam_7, (screen.get_width(), screen.get_height()))
    scaled_cam_8 = pygame.transform.scale(cam_8, (screen.get_width(), screen.get_height()))
    scaled_cam_9 = pygame.transform.scale(cam_9, (screen.get_width(), screen.get_height()))

    fan_sound = pygame.mixer.Sound("fan_sound.mp3")    

    viev = 1
    vievs = [scaled_left_back, scaled_main_back, scaled_right_back]

    show_cam_select = False
    cttvs = [[scaled_cam_1, scaled_cam_2, scaled_cam_3, scaled_cam_4, scaled_cam_9], [scaled_cam_5, scaled_cam_6, scaled_cam_7, scaled_cam_8, scaled_cam_9]]
    row = 1
    col = 4

    locations = {
    'main_stage': [0, 0, 0],
    'dining_room': [0, 0, 0],
    'service_room': [0, 0, 0],
    'foxy_hideout': [0, 0, 0],
    'kitchen': [0, 0, 0],
    'corridor_left': [0, 0, 0],
    'corridor_right': [0, 0, 0],
    'close_corridor_left': [0, 0, 0],
    'close_corridor_right': [0, 0, 0],
    'door_left': [0, 0, 0],
    'door_right': [0, 0, 0]
    }

    black = (0, 0, 0)
    green = (0, 128, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_a and viev != 0 and not show_cam_select:
                    viev -= 1
                    show_cam_select = False
                elif event.key == pygame.K_d and viev != 2 and not show_cam_select:
                    viev += 1
                    show_cam_select = False
                elif event.key == pygame.K_e and viev != 1:
                    if vievs[viev] in [scaled_right_back, scaled_right_back_closed]:
                        vievs[viev] = scaled_right_back_closed if vievs[viev] == scaled_right_back else scaled_right_back
                    elif vievs[viev] in [scaled_left_back, scaled_left_back_closed]:
                        vievs[viev] = scaled_left_back_closed if vievs[viev] == scaled_left_back else scaled_left_back
                elif event.key == pygame.K_q and viev != 1:
                    if vievs[viev] in [scaled_right_back, scaled_right_back_light]:
                        vievs[viev] = scaled_right_back_light if vievs[viev] == scaled_right_back else scaled_right_back
                    elif vievs[viev] in [scaled_left_back, scaled_left_back_light]:
                        vievs[viev] = scaled_left_back_light if vievs[viev] == scaled_left_back else scaled_left_back
                elif event.key == pygame.K_SPACE and viev == 1:
                    show_cam_select = not show_cam_select
                elif event.key == pygame.K_w and show_cam_select:
                    if col != 4:
                        col += 1
                elif event.key == pygame.K_s and show_cam_select:
                    if col != 0:
                        col -= 1
                elif event.key == pygame.K_a and show_cam_select:
                    if row != 0:
                        row -= 1
                elif event.key == pygame.K_d and show_cam_select:
                    if row != 1:
                        row += 1

        fan_sound.play(-1)  

        screen.blit(vievs[viev], (0, 0))
        pygame.draw.rect(screen, black, (50, 50, 100, 200), border_radius=10)

        if show_cam_select: 
                screen.blit(cttvs[row][col], (0, 0))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
