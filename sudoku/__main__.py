import requests
import numpy as np
import pygame
import sys

resp = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")

sudoku_grille = np.array(resp.json()['board'])
grille = sudoku_grille.copy()
print(grille)


# écran :
height = 1280
width = 720
longueur = 660  # taille du sudoku
ecart = longueur / 11
icon = None  # mettre un icon ici "./assets/images/sudoku_icon.png" et le récupérer
bg_color = (245, 245, 245)  # couleur de fond
black = (0, 0, 0)
bleu = (100, 100, 200)


def game():
    flag = 0
    case = None
    pygame.init()  # initializing pygame.
    window = pygame.display.set_mode((height, width))  # taille de la fenêtre
    pygame.display.set_caption("Sudoku")  # setting the caption (Tittle, icontitle=icon)
    window.fill(bg_color)  # remplissage du fond de la fenêtre
    Board_font = pygame.font.SysFont('Arial', 30)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, black, (ecart + ecart * i, ecart), (ecart + ecart * i, longueur - ecart), 4)
            pygame.draw.line(window, black, (ecart, ecart + ecart * i), (longueur - ecart, ecart + ecart * i), 4)
        else:
            pygame.draw.line(window, black, (ecart + ecart * i, ecart), (ecart + ecart * i, longueur - ecart), 2)
            pygame.draw.line(window, black, (ecart, ecart + ecart * i), (longueur - ecart, ecart + ecart * i), 2)

    def affichage():
        for x in range(0, len(grille[0])):
            for y in range(0, len(grille[0])):

                # if it is a number between 1 to 9
                if 0 < grille[x][y] < 10:
                    if grille[x][y] == sudoku_grille[x][y]:
                        number_color = black
                    else: number_color = bleu
                    # rendering the text
                    val = Board_font.render(str(grille[x][y]), True, number_color)
                    # blitting the text on the board
                    window.blit(val, ((y + 1) * ecart + ecart // 2.5, (x + 1) * ecart + ecart // 5))
    affichage()
    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                position_x, position_y = pygame.mouse.get_pos()
                case = int(position_y // ecart)-1, int(position_x // ecart)-1
                print(case)

            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_1 or pygame.K_KP1):
                    value = 1
                    grille[case] = value
                    flag = 1
                if event.key == (pygame.K_2 or pygame.K_KP2):
                    value = 2
                    grille[case] = value
                    flag = 1
                if event.key == (pygame.K_3 or pygame.K_KP3):
                    value = 3
                    grille[case] = value
                    flag = 1
                if event.key == (pygame.K_4 or pygame.K_KP4):
                    value = 4
                    grille[case] = value
                    flag = 1
                if event.key == (pygame.K_5 or pygame.K_KP5):
                    value = 5
                    grille[case] = value
                    flag = 1
                if event.key == (pygame.K_6 or pygame.K_KP6):
                    value = 6
                    grille[case] = value
                    flag = 1
                if event.key == (pygame.K_7 or pygame.K_KP7):
                    value = 7
                    grille[case] = value
                    flag = 1
                if event.key == (pygame.K_8 or pygame.K_KP8):
                    value = 8
                    grille[case] = value
                    flag = 1
                if event.key == (pygame.K_9 or pygame.K_KP9):
                    value = 9
                    grille[case] = value
                    flag = 1
                if flag == 1:
                    affichage()
                    flag = 0
        pygame.display.update()


if __name__ == "__main__":
    game()
