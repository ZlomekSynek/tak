import pygame

def main():
    pygame.init()
    OknoGry=pygame.display.set_mode((400,400),0,32)
    pygame.display.set_caption("3tieg")
    run=True
    zmienna=100
    zmienna1=200
    zmienna2=280
    zmienna3=180
    while(run):
        OknoGry.fill((0,0,0))
        pygame.time.delay(100)
        for zdarzenie in pygame.event.get():
            if zdarzenie.type==pygame.QUIT:
                run=False
        r=pygame.Rect((80,zmienna),(50,50))
        pygame.draw.rect(OknoGry,(0,255,0),r)
        zmienna=zmienna +5
        r1=pygame.Rect((zmienna3,zmienna1),(50,50))
        pygame.draw.rect(OknoGry,(0,255,0),r1)
        zmienna1=zmienna1 +5
        r2=pygame.Rect((zmienna2,100),(50,50))
        pygame.draw.rect(OknoGry,(0,255,0),r2)
        zmienna2=zmienna2 +5
        if zmienna>440:
            zmienna=0
        if zmienna1>440:
            zmienna1=0
        if zmienna2>440:
            zmienna2=0
        if zmienna3>440:
            zmienna3=0
        pygame.display.update()

main()