import pygame

class Waz():
    #konstruktor klasy
    #tworzy podstawowe elementy klast podczas wywolania jej
    def __init__(self):
        self.__pozycja=[(100,100)]
        self.dlugoscWeza=1
        self.punkty=0

    def ruch(self,x,y):
         #sprawdzenie czy waz nie zjada siebie
        for location in self.__pozycja [::]:
             if x==location[0] and y==location[1]:
                    self.__pozycja=[(x,y)]
                    self.dlugoscWeza=1
                    self.punkty=0
        #dodanie nowej pozycji weza
        self.__pozycja.append((x,y))
    #funkcja rysujaca weza
    #jako parametry wywolania uzywa self - samej siebie oraz OknoGry- tam gdzie bedziemy rysowac weza
    def rysowanie(self, OknoGry):
        #rysowanie weza z pozycji
         for poz in self.__pozycja[::-1]:
            r=pygame.Rect((poz[0],poz[1]),(20,20))
            pygame.draw.rect(OknoGry,(0,255,0),r)