import pygame
import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


cookies = 0
cookie_click = 1
upgradecost = 20



upgrade = pygame.Surface ((100, 50))
upgradeRect = pygame.Rect(20, 50, 100, 100)
#fill rect with color
font = pygame.font.Font(None, 30)

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if upgradeRect.collidepoint(pos):
                if cookies >= upgradecost:
                    cookie_click += 1
                    cookies -= upgradecost
                    upgradecost*=1.6
                    math.ceil(upgradecost)
                    upgradecost = int(upgradecost)
                    print(upgradecost)



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cookies += cookie_click
       


    # Fill the background with white
    screen.fill((255, 255, 255))

    # Display cookies
    text_rect = pygame.Rect(20, 20, 0, 0)
    text_to_render = font.render("cookies: " + str(cookies) , True, pygame.Color(0, 0, 0))
    screen.blit(text_to_render, text_rect)

    # Upgrade Button
    upgrade.fill ((0, 0, 0))
    screen.blit (upgrade, upgradeRect)
    pygame.display.update ()


    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()