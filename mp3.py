import pygame

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
W, H = 500, 700
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("PLAYLIST")

WHITE = (255, 255, 255)
FPS = 60

sc.fill(WHITE)

music_files = [
    r"C:\Users\Acer\Desktop\PP2\tabyldy-dosymov-ak-didaryn-aj_(kmuzon.com).mp3",
    r"C:\Users\Acer\Desktop\PP2\tabyldy-dosymov-zhalgan-dunie_(kmuzon.com).mp3"
]
current_track_index = 0

akdidarym = pygame.image.load(r"C:\Users\Acer\Desktop\PP2\1605770036_hqdefault.jpg").convert_alpha()
akdidarym = pygame.transform.scale(akdidarym, (500, 200))

zhalgandunie = pygame.image.load(r"C:\Users\Acer\Desktop\PP2\1605770036_hqdefault.jpg").convert_alpha()
zhalgandunie = pygame.transform.scale(zhalgandunie, (500, 200))

myfont = pygame.font.SysFont('arial', 40)
text_surface = myfont.render('MY PLAYLIST', True, 'Black')

pygame.mixer.music.load(music_files[current_track_index])
pygame.mixer.music.play()

def next_song():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()

def last_song():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                last_song()

    sc.fill(WHITE)
    sc.blit(akdidarym, (0, 100))
    sc.blit(zhalgandunie, (0, 300))
    sc.blit(text_surface, (20, 30))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
