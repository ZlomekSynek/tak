import random
import pygame

class Jablko():
    #konstruktor klasy
    def __init__(self):
        self.pozycjaJablka=[(1,1)]
        self.losujPozycje()
    def setPozycja(self,x,y):
        self.pozycjaJablka[0]=(x,y)
    def getPozycja(self):
        return self.pozycjaJablka[-1]
    def losujPozycje(self):
        #losowanie pozycji jablka
        apleX=random.randint(0,21)*20+10
        apleY=random.randint(0,21)*20+10
        self.setPozycja(apleX,apleY)
    def rysujJablko(self,oknoGry):
         pygame.draw.circle(oknoGry,(255,0,0),(self.pozycjaJablka[0][0],self.pozycjaJablka[0][1]),10)