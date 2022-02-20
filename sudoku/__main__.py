import requests
import numpy as np
import pygame
import sys
from solution import Solver

level = 'easy'
resp = requests.get("https://sugoku.herokuapp.com/board?difficulty=" + level)

sudoku_grille = np.array(resp.json()['board'])
grille = sudoku_grille.copy()
solution_grille = np.array(Solver().solve(grille.copy()))

# écran :
height, width = 1280, 720
longueur = 660  # taille du sudoku
ecart = longueur / 11
icon = pygame.image.load("../assets/images/icon.jpg")
bg_color = (240, 240, 240)  # couleur de fond
black = (0, 0, 0)
bleu = (100, 100, 200)
red = (200, 50, 50)


def game():
    flag = 0
    case = 0, 0
    position_x, position_y = 0, 0
    pygame.init()  # initializing pygame.
    window = pygame.display.set_mode((height, width))  # taille de la fenêtre
    pygame.display.set_caption("Sudoku")
    pygame.display.set_icon(icon)
    window.fill(bg_color)  # remplissage du fond de la fenêtre
    Board_font = pygame.font.SysFont('Arial', 30)

    def drawlines():
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(window, black, (ecart + ecart * i, ecart), (ecart + ecart * i, longueur - ecart), 4)
                pygame.draw.line(window, black, (ecart, ecart + ecart * i), (longueur - ecart, ecart + ecart * i), 4)
            else:
                pygame.draw.line(window, black, (ecart + ecart * i, ecart), (ecart + ecart * i, longueur - ecart), 2)
                pygame.draw.line(window, black, (ecart, ecart + ecart * i), (longueur - ecart, ecart + ecart * i), 2)

    def affichage():
        window.fill(bg_color)
        drawlines()
        highlightbox(position_x, position_y)
        for x in range(0, len(grille[0])):
            for y in range(0, len(grille[0])):
                # if it is a number between 1 and 9
                if 0 < grille[x][y] < 10:
                    if grille[x][y] == sudoku_grille[x][y]:
                        number_color = black
                    else:
                        number_color = bleu
                    # rendering the text
                    val = Board_font.render(str(grille[x][y]), True, number_color)
                    # blitting the text on the board
                    window.blit(val, ((y + 1) * ecart + ecart // 2.5, (x + 1) * ecart + ecart // 5))

    def highlightbox(pos_x, pos_y):
        pos_x = (pos_x + 1) * ecart
        pos_y = (pos_y + 1) * ecart
        if 1 * ecart <= pos_x <= 9 * ecart and 1 * ecart <= pos_y <= 9 * ecart:
            for k in range(2):
                pygame.draw.line(window, red, (pos_x + k * ecart, pos_y), (pos_x + k * ecart, pos_y + ecart), 7)
                pygame.draw.line(window, red, (pos_x, pos_y + k * ecart), (pos_x + ecart, pos_y + k * ecart), 7)

    affichage()
    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                position_x = int(mouse_x // ecart) - 1
                position_y = int(mouse_y // ecart) - 1
                case = position_y, position_x
                affichage()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    position_x = (position_x - 1) % 9
                    case = position_y, position_x
                    flag = 1
                if event.key == pygame.K_RIGHT:
                    position_x = (position_x + 1) % 9
                    flag = 1
                    case = position_y, position_x
                if event.key == pygame.K_UP:
                    position_y = (position_y - 1) % 9
                    flag = 1
                    case = position_y, position_x
                if event.key == pygame.K_DOWN:
                    position_y = (position_y + 1) % 9
                    flag = 1
                    case = position_y, position_x
                if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and sudoku_grille[case] == 0:
                    value = 1
                    grille[case] = value
                    flag = 1
                if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and sudoku_grille[case] == 0:
                    value = 2
                    grille[case] = value
                    flag = 1
                if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and sudoku_grille[case] == 0:
                    value = 3
                    grille[case] = value
                    flag = 1
                if (event.key == pygame.K_4 or event.key == pygame.K_KP4) and sudoku_grille[case] == 0:
                    value = 4
                    grille[case] = value
                    flag = 1
                if (event.key == pygame.K_5 or event.key == pygame.K_KP5) and sudoku_grille[case] == 0:
                    value = 5
                    grille[case] = value
                    flag = 1
                if (event.key == pygame.K_6 or event.key == pygame.K_KP6) and sudoku_grille[case] == 0:
                    value = 6
                    grille[case] = value
                    flag = 1
                if (event.key == pygame.K_7 or event.key == pygame.K_KP7) and sudoku_grille[case] == 0:
                    value = 7
                    grille[case] = value
                    flag = 1
                if (event.key == pygame.K_8 or event.key == pygame.K_KP8) and sudoku_grille[case] == 0:
                    value = 8
                    grille[case] = value
                    flag = 1
                if (event.key == pygame.K_9 or event.key == pygame.K_KP9) and sudoku_grille[case] == 0:
                    value = 9
                    grille[case] = value
                    flag = 1

                if (event.key == pygame.K_BACKSPACE or event.key == pygame.K_0 or event.key == pygame.K_KP0) and \
                        sudoku_grille[case] == 0:
                    value = 0
                    grille[case] = value
                    flag = 1

                if flag == 1:
                    affichage()
                    flag = 0
        pygame.display.update()
        if np.all(grille == solution_grille):
            running = False


if __name__ == "__main__":
    game()
