import pygame
import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


cookies = 100
cookie_click = 10000
babushkas = 0

upgradecost = 20
babushka_cost = 100
passive_cookie = 0


upgradeSurface = pygame.Surface ((100, 50))
upgradeRect = pygame.Rect(20, 50, 100, 100)
font = pygame.font.Font(None, 30)

babushkaSurface = pygame.Surface ((100, 50))
babushkaRect = pygame.Rect(150, 50, 100, 100)

BABUSKA_MAKE_COOKIE_EVENT_TYPE = pygame.USEREVENT + 1

pygame.time.set_timer(pygame.event.Event(BABUSKA_MAKE_COOKIE_EVENT_TYPE), 1000)




running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == BABUSKA_MAKE_COOKIE_EVENT_TYPE:
            cookies += babushkas

        # COOKIE TRANSACTION
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if upgradeRect.collidepoint(pos):
                if cookies >= upgradecost:
                    cookie_click += 1
                    cookies -= upgradecost
                    upgradecost*=1.4
                    math.ceil(upgradecost)
                    upgradecost = int(upgradecost)
                    print(upgradecost)

            # BABUSHKA TRANSACTION
            if babushkaRect.collidepoint(pos):
                if cookies >= babushka_cost:
                    babushkas += 1
                    cookies -= babushka_cost
                    babushka_cost*=1.5
                    math.ceil(babushka_cost)
                    babushka_cost = int(babushka_cost)
                    print(babushka_cost)
                    print("babushka bought " + str(babushkas) + " " + str(babushka_cost))


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
    upgradeSurface.fill ((0, 0, 0))
    screen.blit (upgradeSurface, upgradeRect)

      # babushka Button
    babushkaSurface.fill ((235, 150, 70))
    screen.blit (babushkaSurface, babushkaRect)
   


    # Flip the display
    pygame.display.update ()
    pygame.display.flip()



# Done! Time to quit.
pygame.quit()