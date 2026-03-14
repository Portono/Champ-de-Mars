import pygame
from Menu import boucle_menu

def afficher_menu_pause():
    en_pause = True
    while en_pause:
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                   pygame.quit()
                   exit()
       result = boucle_menu(pause=True)
       if result:
             return result  # Quitter le menu pause

