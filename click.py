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
babushkas = 0
passive_cookie = 0


# upgrade costs
upgradecost = 20
babushka_cost = 100


# buttons
upgradeSurface = pygame.Surface ((100, 50))
upgradeRect = pygame.Rect(20, 50, 100, 100)
font = pygame.font.Font(None, 30)
"""
Upgrade_button
    .rect
    .surface
"""


# text_render(250, 120, f"babushkas: {babushkas}")
babushkaSurface = pygame.Surface ((100, 50))
babushkaRect = pygame.Rect(250, 50, 100, 100)



# passive cookie
BABUSKA_MAKE_COOKIE_EVENT_TYPE = pygame.USEREVENT + 1

pygame.time.set_timer(pygame.event.Event(BABUSKA_MAKE_COOKIE_EVENT_TYPE), 1000)

# animated message setup
class AnimatedMessage:
    def __init__(self, text: str, color: pygame.Color):
        self.animation_factor = 0
        self.text = text
        self.color = color
        x, y = pygame.mouse.get_pos()

        self.origin_x = x
        self.origin_y = y 

animated_messages = []


# transaction shop function
def transaction(cost, product, ffk):
    global cookies
    if cookies >= cost:
        product += 1
        cookies -= cost
        cost *= ffk
        math.ceil(cost)
        cost = int(cost)
        animated_messages.append(
            AnimatedMessage("you are so rich $$$", pygame.Color(0, 255, 0))
        )
    else: # if we are poor bozos and dont have enugh money (lol)
        animated_messages.append(
            AnimatedMessage("du är så fattig (xd)", pygame.Color(255, 0, 0))
        )

    return cost, product
    

# text function
def text_render(left, top, text, color=pygame.Color(0, 0, 0), center_text=False):
    text_rect = pygame.Rect(left, top, 0, 0)
    text_render = font.render(str(text), True, color)
    if center_text == True:
        text_rect.left -= int(text_render.get_width()/2)
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

    # render animated messages and advance the animation by one step
    for message in animated_messages.copy():
        message: AnimatedMessage
        message.animation_factor += 0.01
        y_offset = message.animation_factor * 10
        x_offset = math.sin(message.animation_factor) * 10

        text_render(
            message.origin_x + x_offset,
            message.origin_y - y_offset,
            message.text,
            color=message.color,
            center_text=True
        )

        if message.animation_factor >= 10:
            animated_messages.remove(message)
   


    # Flip the display
    pygame.display.update ()
    pygame.display.flip()



# Done! Time to quit.
pygame.quit()