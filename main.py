#tutorial series followed https://www.youtube.com/playlist?list=PLjcN1EyupaQlBSrfP4_9SdpJIcfnSJgzL

#import libraries
import pygame

#initialise pygame
pygame.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Super Cool Platformer')

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#colour
WHITE = (255, 255, 255)

#load images
bg_image = pygame.image.load('assets/bg.png').convert_alpha()
player_image = pygame.image.load('assets/player.png').convert_alpha()


#player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(player_image, (40, 80))
        self.width = 40
        self.height = 80
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.flip = False

    def move(self):
        #reset variables
        dx = 0
        dy = 0

        #process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
            self.flip = True
        if key[pygame.K_d]:
            dx = 10
            self.flip = False

        #ensure player doesn't go off the edge of the screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, WHITE, self.rect, 2)


player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

#game loop
run = True
while run:

    clock.tick(FPS)

    player.move()

    #draw background
    screen.blit(bg_image, (0, 0))

    #draw sprites
    player.draw()

    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()

pygame.quit()