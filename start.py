import pygame
import pygame_menu
import lekcja1

def wlaczGre():
    lekcja1.main()
def zmienKolorWaz1():
    lekcja1.kolorWaz1()
def main():
    pygame.init()
    oknoMenu=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Wąż")
    menu=pygame_menu.Menu("Gra Snake 3TieG",500,500,theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("Włącz grę",wlaczGre,background_color=(0,0,255))
    menu.add.color_input('Kolor Wąż 1:','rgb')
    menu.add.button('Zapisz kolor Wąż 1')
    menu.mainloop(oknoMenu)

main()