import pygame
import random

def main():
    pygame.init()
    OknoGry=pygame.display.set_mode((440,440),0,32)
    pygame.display.set_caption("3tieg")
    run=True
    zmienna=100
    zmienna2=100
    while(run):
        OknoGry.fill((0,0,0))
        pygame.time.delay(100)
        for zdarzenie in pygame.event.get():
            if zdarzenie.type==pygame.QUIT:
                run=False
            elif zdarzenie.type==pygame.KEYDOWN:
                if zdarzenie.key==pygame.K_LEFT:
                    zmienna2=zmienna2-20
                elif zdarzenie.key==pygame.K_RIGHT:
                    zmienna2=zmienna2+20
                elif zdarzenie.key==pygame.K_UP:
                    zmienna=zmienna-20
                elif zdarzenie.key==pygame.K_DOWN:
                    zmienna=zmienna+20
        #tworzenie kwadratu jako weza
        r=pygame.Rect((zmienna2,zmienna),(20,20))
        pygame.draw.rect(OknoGry,(0,255,0),r)
        #tworzenie jablka za pomoca kola
        apleX=random.randint(0,21)*20+10
        apleY=random.randint(0,21)*20+10
        pygame.draw.circle(OknoGry,(255,0,0),(apleX,apleY),10)

        if zmienna2<0:
            zmienna2=440
       
        if zmienna2>440:
            zmienna2=0

        if zmienna>440:
            zmienna=0

        if zmienna<0:
            zmienna=440
        pygame.display.update()

main()