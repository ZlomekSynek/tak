import pygame
import pygame_menu
import lekcja1

def wlaczGre():
    lekcja1.main()
def zmienKolorWaz1(value):
    lekcja1.zmianaKolorWaz1(value)
def zmienKolorWaz2(value):
    lekcja1.zmianaKolorWaz2(value)
def zmienJablka(wartosc,value):
    lekcja1.iloscJablek=value
def zmienRozdzielczosc(wartosc,rozdzielczosc):
    lekcja1.rozdzielczosc=rozdzielczosc
def main():
    pygame.init()
    oknoMenu=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Wąż")
    menu=pygame_menu.Menu("Gra Snake 3TieG",500,500,theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("Włącz grę",wlaczGre,background_color=(0,0,255))
    menu.add.color_input('Kolor Wąż 1:','rgb',default=(100,100,255),onreturn=zmienKolorWaz1)
    menu.add.color_input('Kolor Wąż 2:','rgb',default=(200,100,255),onreturn=zmienKolorWaz2)
    menu.add.selector("Wybierz ilość jabłek",[('jedno',1),('dwa',2),('trzy',3),('cztery',4),('pięć',5)],onchange=zmienJablka)
    menu.add.selector("Rozmiar ekranu",[('440x440',440),('560x560',560),('800x800',800)], onchange=zmienRozdzielczosc)
    #menu.add.button('Zapisz kolor Wąż 1')
    menu.mainloop(oknoMenu)

main()