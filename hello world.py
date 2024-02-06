import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Macka Clicker')

macka_img = pygame.image.load('macka.jpg').convert_alpha()
amount_of_macka = 0

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, amount_of_macka):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                pygame.time.wait(20)
                amount_of_macka += 1
                print(amount_of_macka)
        
        return amount_of_macka


start_button = Button(200, 200, macka_img, 0.2)
amount_of_macka = 0

    

run = True
while run:

    screen.fill((202, 228, 241))

    amount_of_macka = start_button.draw(amount_of_macka)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
