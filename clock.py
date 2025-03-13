import pygame
from datetime import datetime
pygame.init()
clock=pygame.time.Clock()
W=800
H=800
sc=pygame.display.set_mode((W,H))
pygame.display.set_caption("CLOCK")

WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
FPS=60

sc.fill(WHITE)

bg=pygame.image.load(r"C:\Users\Acer\Desktop\PP2\clock.png")
minute=pygame.image.load(r"C:\Users\Acer\Desktop\PP2\square_leftarm.png")
second=pygame.image.load(r"C:\Users\Acer\Desktop\PP2\rightarm.png")

bg = pygame.transform.scale(bg, (650, 650))
minute = pygame.transform.scale(minute, (490,490))
second = pygame.transform.scale(second, (490,490))

rect=bg.get_rect(center=(W//2,H//2))  

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()

    sc.fill(WHITE)
    sc.blit(bg, rect)  

    time=datetime.now().time()

    sang = -(time.second * 6)
    news = pygame.transform.rotate(second, sang)
    sec_rect = news.get_rect(center=rect.center)
    sc.blit(news, sec_rect.topleft)

    
    mang = -(time.minute * 6) 
    newm = pygame.transform.rotate(minute, mang)
    min_rect = newm.get_rect(center=rect.center)
    sc.blit(newm, min_rect.topleft)
    
    pygame.display.flip()

    clock.tick(FPS)