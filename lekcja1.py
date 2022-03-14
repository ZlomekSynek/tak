import pygame
import random
import waz
import jablko

#zmianne globalne
obiektWaz1=waz.Waz()
obiektWaz2=waz.Waz()
def zmianaKolorWaz1(self,kolor):
    obiektWaz1.ustawKolor(kolor)
def zmianaKolorWaz2(self,kolor):
    obiektWaz2.ustawKolor(kolor)


def main():
    pygame.init()
    OknoGry=pygame.display.set_mode((440,440),0,32)
    pygame.display.set_caption("3tieg")
    run=True
    iloscJablek=3
    #tworzenoe kilku jablek
    obiektJablko=[]
    for nrJablko in range(0,iloscJablek):
        obiektJablko.append(jablko.Jablko())
    
    #losowanie pozycji jablka
    apleX=random.randint(0,21)*20+10
    apleY=random.randint(0,21)*20+10

    while(run):
        OknoGry.fill((0,0,0))

        for obiektApple in obiektJablko[::]:
            obiektApple.rysujJablko(OknoGry)
        #obiektJablko.rysujJablko(OknoGry)
        pygame.time.delay(150)
        #obsługa ruchu węża obiektu obiekt waz
        for zdarzenie in pygame.event.get():
            if zdarzenie.type==pygame.QUIT:
                run=False
            elif zdarzenie.type==pygame.KEYDOWN:
                if zdarzenie.key==pygame.K_LEFT:
                    obiektWaz1.setKierunek((-1,0))
                elif zdarzenie.key==pygame.K_RIGHT:
                    obiektWaz1.setKierunek((1,0))
                elif zdarzenie.key==pygame.K_UP:
                    obiektWaz1.setKierunek((0,-1))
                elif zdarzenie.key==pygame.K_DOWN:
                    obiektWaz1.setKierunek((0,1))
                elif zdarzenie.key==pygame.K_a:
                    obiektWaz2.setKierunek((-1,0))
                elif zdarzenie.key==pygame.K_d:
                    obiektWaz2.setKierunek((1,0))
                elif zdarzenie.key==pygame.K_w:
                    obiektWaz2.setKierunek((0,-1))
                elif zdarzenie.key==pygame.K_s:
                    obiektWaz2.setKierunek((0,1))
        #wykonanie ruchu za każdym razem wykonania pętli
        obiektWaz1.ruch()
        obiektWaz1.rysowanie(OknoGry)
        obiektWaz2.ruch()
        obiektWaz2.rysowanie(OknoGry)

        #tworzenie jablka za pomoca kola
        #pygame.draw.circle(OknoGry,(255,0,0),(apleX,apleY),10)

        #sprawdzanie czy waz zjada jablko
        poz1=obiektWaz1.getPosition()
        poz2=obiektWaz2.getPosition()
        for obiektApple in obiektJablko[::]:
            pozJablko=obiektApple.getPozycja()
            if(poz1[1]+10==pozJablko[1] and poz1[0]+10==pozJablko[0]):
                obiektWaz1.zjadanie()
                #wylosowanie nowej pozycji jablka
                obiektApple.losujPozycje()
            if(poz2[1]+10==pozJablko[1] and poz2[0]+10==pozJablko[0]):
                obiektWaz2.zjadanie()
            #wtlosowanie nowej pozycji jablka
                obiektApple.losujPozycje()
            #apleX=random.randint(0,21)*20+10
            #apleY=random.randint(0,21)*20+10
            #pygame.draw.circle(OknoGry,(128,128,128),(apleX,apleY),10)
        #zjadanie się węży nawzajem
        obiektWaz1.czyKtosMnieUgryzl(poz2)
        obiektWaz2.czyKtosMnieUgryzl(poz1)
        #wypisanie punktow na ekran
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty gracz 1: {0}".format(obiektWaz1.punkty),1,(255,160,0))
        tekst2=czcionka.render("Punkty gracz 2: {0}".format(obiektWaz2.punkty),1,(0,160,255))
        OknoGry.blit(tekst, (10,10))
        OknoGry.blit(tekst2, (250,10))
        
        #pobieranie pozycji glowy
        glowa1=obiektWaz1.getPosition()
        glowa2=obiektWaz2.getPosition()
        #sprawdzanie przejścia przez krawędź okna
        #prawa czesc okna
        if glowa1[0]>420:
            obiektWaz1.setPosition(0,glowa1[1])
        #lewa czesc okna
        if glowa1[0]<0:
            obiektWaz1.setPosition(420,glowa1[1])
        #dol ekranu
        if glowa1[1]>420:
            obiektWaz1.setPosition(glowa1[0],0)
        #gora ekranu
        if glowa1[1]<0:
            obiektWaz1.setPosition(glowa1[0],420)
        #prawa czesc okna
        if glowa2[0]>420:
            obiektWaz2.setPosition(0,glowa2[1])
        #lewa czesc okna
        if glowa2[0]<0:
            obiektWaz2.setPosition(420,glowa2[1])
        #dol ekranu
        if glowa2[1]>420:
            obiektWaz2.setPosition(glowa2[0],0)
        #gora ekranu
        if glowa2[1]<0:
            obiektWaz2.setPosition(glowa2[0],420)
        
        
        pygame.display.update()

#main()