import requests
import numpy as np
import pygame
import sys

resp = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")

sudoku_grille = np.array(resp.json()['board'])
grille = sudoku_grille.copy()
solution_grille = grille.copy()  # il faut récupéer la solution


def enlever(nombre, valeur):
    a = nombre
    b = 0
    for i in range(9):
        b += a % 10 * 2 ** i
        a //= 10
    b -= (2 ** (valeur - 1))
    return bin(b)


def mettre(valeur):
    return bin(2 ** (valeur - 1))


matpos = 111111111 * np.ones((9, 9))

for i, j in range(9):
    x = sudoku_grille[i, j]
    if x != 0:
        matpos[i, j] = mettre(x)


def check_pos(position_x, position_y):
    for j in range(9):
        if position_x != j:
            matpos[position_y, position_x] = enlever([position_y, position_x], grille[position_y, j])
    for k in range(9):
        if position_y != k:
            matpos[position_y, position_x] = enlever([position_y, position_x], grille[k, position_x])


print(matpos)
