import pygame
import math

pygame.init()


# todo list

# battlepass
# more upgrades
# saving system
# random events


# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


# money
cookies = 200


# upgrades
cookie_click = 1
babushkas = 0
factory = 0


# upgrade costs
upgradecost = 20
babushka_cost = 60
factory_cost = 100



# buttons
upgradeSurface = pygame.Surface ((100, 50))
upgradeRect = pygame.Rect(20, 50, 100, 100)
font = pygame.font.Font(None, 30)


babushkaSurface = pygame.Surface ((100, 50))
babushkaRect = pygame.Rect(250, 50, 100, 100)

factorySurface = pygame.Surface ((100, 50))
factoryRect = pygame.Rect(20, 180, 100, 100)



# passive babushka
BABUSKA_MAKE_COOKIE_EVENT_TYPE = pygame.USEREVENT + 1

pygame.time.set_timer(pygame.event.Event(BABUSKA_MAKE_COOKIE_EVENT_TYPE), 1000)


# passive factory
PASSIVE_FACTORY = pygame.USEREVENT + 2

pygame.time.set_timer(pygame.event.Event(PASSIVE_FACTORY), 1000)


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

        # passive factory addition
        if event.type == PASSIVE_FACTORY:
            cookies += factory*5

            
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # COOKIE TRANSACTION
            if upgradeRect.collidepoint(pos):
                upgradecost, cookie_click = transaction(upgradecost, cookie_click, 1.4)
                
                
            # BABUSHKA TRANSACTION
            if babushkaRect.collidepoint(pos):
                babushka_cost, babushkas = transaction(babushka_cost, babushkas, 1.5)

            # FACTORY TRANSACTION
            if factoryRect.collidepoint(pos):
                factory_cost, factory = transaction(factory_cost, factory, 1.6)


        # listen for keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cookies += cookie_click




    # Fill the background with white
    screen.fill((255, 255, 255))

    text_render(250, 20, f"cookies / second: {babushkas+factory*5}")

    # display cookies
    text_render(20, 20, f"cookies: {cookies}")

    # display cookies/click
    text_render(20, 120, f"cookies / click: {cookie_click}")

    # display cost of cookies/click
    text_render(20, 140, f"baker cost: {upgradecost}")

    # display babushkas
    text_render(250, 120, f"babushkas: {babushkas}")

    #display babushka cost
    text_render(250, 140, f"babushka cost: {babushka_cost}")

    # display factory
    text_render(20, 250, f"factories: {factory}")

    #display factory cost
    text_render(20, 270, f"factory cost: {factory_cost}")
    
        

    # Upgrade Button
    upgradeSurface.fill ((0, 0, 0))
    screen.blit (upgradeSurface, upgradeRect)

    # babushka Button
    babushkaSurface.fill ((235, 150, 70))
    screen.blit (babushkaSurface, babushkaRect)

    # factory button
    factorySurface.fill((158, 158, 158))
    screen.blit(factorySurface, factoryRect)
    
   


    # Flip the display
    pygame.display.update ()
    pygame.display.flip()



# Done! Time to quit.
pygame.quit()