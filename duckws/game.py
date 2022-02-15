import pygame,sys,os,random
os.chdir('c:\\duckws')
pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
Crosshair = pygame.image.load('crosshair.png')
wood_bg = pygame.image.load('Wood_BG.png')
lnd_bg = pygame.image.load('Land_BG.png') 
wtr_bg = pygame.image.load('Water_BG.png')
cloud = pygame.image.load('Cloud1.png')
cloud2 = pygame.image.load('Cloud2.png')
duck = pygame.image.load('duck.png') 
mouse = pygame.mouse.get_pos()
duck_x = 300
duck_y = 300
land_pos_y = 450 
land_sped = 1 
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos == duck_x:
                print('click')
    screen.blit(wood_bg,(0,0))
    land_pos_y -= land_sped
    if land_pos_y > 700 or land_pos_y < 500:
        land_sped *= -1
    screen.blit(lnd_bg,(0,land_pos_y))
    screen.blit(wtr_bg,(0,530))

    screen.blit(cloud2,(50,100))
    screen.blit(cloud,(600,100))
    screen.blit(cloud2,(1100,100))
    
    screen.blit(duck, (300,300))
    screen.blit( Crosshair, ( pygame.mouse.get_pos() ) )


    pygame.display.update()
    clock.tick(120)