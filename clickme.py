from random import randint
import pygame
from sys import exit
pygame.init()


class Button:
    def __init__(self, pos):
        # rectangle
        self.pos = pos
        self.rect = pygame.Rect(self.pos, (100, 30))
        self.rect_colr = (255, 0, 0)
        self.click = False

        # text
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, 30)
        self.txt = self.font.render('click me', True, self.color)
        self.txt_rect = self.txt.get_rect(center=self.rect.center)

    def draw(self):
        #print(self.pos, end=' ')
        self.txt_rect.center = self.rect.center
        pygame.draw.rect(main_surf, self.rect_colr, self.rect, 0, 10)
        main_surf.blit(self.txt, self.txt_rect)
        self.check_mouse()

    def check_mouse(self):

        mouse_pos = pygame.mouse.get_pos()
        #print("mouse == ", mouse_pos)
        if self.rect.collidepoint(mouse_pos):
            self.rect_colr = (200, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                self.click = True
            else:
                if self.click:
                    self.click = False
                    #print(randint(100, 200), randint(0, 700))
                    self.pos = (randint(10, 800), randint(10, 500))
                    self.rect = pygame.Rect(self.pos, (100, 30))

        else:
            self.rect_colr = (255, 0, 0)


main_surf = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Infinite clicky")
clock = pygame.time.Clock()

button1 = Button((200, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()
    main_surf.fill((60, 60, 60))

    button1.draw()
    pygame.display.update()
    clock.tick(60)
