import pygame
import math

pygame.init()


# todo list

# battlepass
# more upgrades
# show passive cookies
# saving system


# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


# money
cookies = 0


# upgrades
cookie_click = 1
babushkas = 99990
passive_cookie = 0


# upgrade costs
upgradecost = 20
babushka_cost = 100



# buttons
upgradeSurface = pygame.Surface ((100, 50))
upgradeRect = pygame.Rect(20, 50, 100, 100)
font = pygame.font.Font(None, 30)

# text_render(250, 120, f"babushkas: {babushkas}")
babushkaSurface = pygame.Surface ((100, 50))
babushkaRect = pygame.Rect(250, 50, 100, 100)



# passive cookie
BABUSKA_MAKE_COOKIE_EVENT_TYPE = pygame.USEREVENT + 1

pygame.time.set_timer(pygame.event.Event(BABUSKA_MAKE_COOKIE_EVENT_TYPE), 1000)



# transaction shop function
def transaction(cost, product, ffk):
    global cookies
    if cookies >= cost:
        product += 1
        cookies -= cost
        cost*=ffk
        math.ceil(cost)
        cost = int(cost)
    return cost, product
    

# text function
def text_render(left, top, text):
    text_rect = pygame.Rect(left, top, 0, 0)
    text_render = font.render(str(text), True, pygame.Color(0, 0, 0))
    screen.blit(text_render, text_rect)



running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # passive cookie addition
        if event.type == BABUSKA_MAKE_COOKIE_EVENT_TYPE:
            cookies += babushkas

        # COOKIE TRANSACTION
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if upgradeRect.collidepoint(pos):
                upgradecost, cookie_click = transaction(upgradecost, cookie_click, 1.4)
                
                
            # BABUSHKA TRANSACTION
            if babushkaRect.collidepoint(pos):
                babushka_cost, babushkas = transaction(babushka_cost, babushkas, 1.5)


        # listen for keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cookies += cookie_click
       


    # Fill the background with white
    screen.fill((255, 255, 255))


    # display cookies
    text_render(20, 20, f"cookies: {cookies}")

    # display cookies/click
    text_render(20, 120, f"cookies / click: {cookie_click}")

    # display cost of cookies/click
    text_render(20, 140, f"baker cost: {upgradecost}")

    # display babushkas
    text_render(250, 120, f"babushkas: {babushkas}")

    #display babushka cost
    text_render(250, 140, f"cost of babushka: {babushka_cost}")
    
        

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