import requests
import numpy as np
import pygame
import sys
#aaaaaaaaaaaaaaaaaaaaaaa
resp = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")

grille = np.array(resp.json()['board'])

print(grille)

# écran :
height = 1280
width = 720
longueur = 660  # taille du sudoku
long_case = longueur/11
icon = None  # mettre un icon ici "./assets/images/sudoku_icon.png" et le récupérer
bg_color = (245, 245, 245)  # couleur de fond
black = (0, 0, 0)


def game():
    pygame.init()  # initializing pygame.
    window = pygame.display.set_mode((height, width))  # taille de la fenêtre
    pygame.display.set_caption("Sudoku")  # setting the caption (Tittle, icontitle=icon)
    window.fill(bg_color)  # remplissage du fond de la fenêtre
    Board_font = pygame.font.SysFont('Arial', 30)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, black, (long_case + long_case * i, long_case), (long_case + long_case * i, longueur - long_case), 4)
            pygame.draw.line(window, black, (long_case, long_case + long_case * i), (longueur - long_case, long_case + long_case * i), 4)
        else:
            pygame.draw.line(window, black, (long_case + long_case * i, long_case), (long_case + long_case * i, longueur - long_case), 2)
            pygame.draw.line(window, black, (long_case, long_case + long_case * i), (longueur - long_case, long_case + long_case * i), 2)

    for x in range(0, len(grille[0])):
        for y in range(0, len(grille[0])):

            # if it is a number between 1 to 9
            if 0 < grille[x][y] < 10:
                # rendering the text
                val = Board_font.render(str(grille[x][y]), True, (100, 100, 200))
                # blitting the text on the board
                window.blit(val, ((y + 1) * long_case + long_case//2.5, (x + 1) * long_case + long_case//5))

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    game()
