import pygame

class Waz():
    #konstruktor klasy
    #tworzy podstawowe elementy klast podczas wywolania jej
    def __init__(self):
        self.__pozycja=[(100,100)]
        self.dlugoscWeza=1
        self.punkty=0
        self.kierunek=(0,-1)
        self.kolor=(0,255,0)
    def getPosition(self):
        return self.__pozycja[-1]
    def setPosition(self,x,y):
        self.__pozycja[-1]=(x,y)
    def setKierunek(self,direction):
            self.kierunek=direction
    def ruch(self):
        #obliczanie nowej pozycji
        ostatniaPozycja=self.__pozycja[-1]
        x=ostatniaPozycja[0]+20*self.kierunek[0]
        y=ostatniaPozycja[1]+20*self.kierunek[1]
         #sprawdzenie czy waz nie zjada siebie
        for location in self.__pozycja [::]:
             if x==location[0] and y==location[1]:
                    self.__pozycja=[(x,y)]
                    self.dlugoscWeza=1
                    self.punkty=0
        #dodanie nowej pozycji weza
        self.__pozycja.append((x,y))
        #nie usuwamy pozycji gdy waz zjadl jablko
        if len(self.__pozycja)>self.dlugoscWeza:   
            del self.__pozycja[0]
        #funkcja zjadania jablka
    def zjadanie(self):
        #self.dlugoscWeza=self.dlugoscWeza+1
        self.dlugoscWeza+=1
        self.punkty+=1
    #funkcja rysujaca weza
    #jako parametry wywolania uzywa self - samej siebie oraz OknoGry- tam gdzie bedziemy rysowac weza
    def rysowanie(self, OknoGry):
        #rysowanie weza z pozycji
         for poz in self.__pozycja[::-1]:
            r=pygame.Rect((poz[0],poz[1]),(20,20))
            pygame.draw.rect(OknoGry,self.kolor,r)
    #czy ktos zjadl waz
    def czyKtosMnieUgryzl(self,pozycja):
        for czesciCiala in self.__pozycja[::]:
            if pozycja[0]==czesciCiala[0] and pozycja[1]==czesciCiala[1]:
                self.__pozycja=[(pozycja[0],pozycja[1])]
                self.dlugoscWeza=1
                self.punkty=0
    def ustawKolor(self,nowyKolor):
        self.kolor=nowyKolor