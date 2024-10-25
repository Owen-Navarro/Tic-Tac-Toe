import tkinter as tk
from tkinter import messagebox
import random

# Initialisation du plateau
board = [" " for _ in range(9)]

# Fonction pour vérifier la victoire
def verifier_victoire(signe):
    combinaisons = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)] 
    for combinaison in combinaisons:
        if board[combinaison[0]] == board[combinaison[1]] == board[combinaison[2]] == signe:
            return True
    return False

# Fonction pour réinitialiser le jeu
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)

# Fonction pour gérer un clic sur un bouton
def on_button_click(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        
        if verifier_victoire(current_player):
            messagebox.showinfo("Fin de la partie", f"{current_player} a gagné!")
            reset_game()
            return

        if " " not in board:
            messagebox.showinfo("Fin de la partie", "Match nul!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"
        
        if jeux == 0 and current_player == "O":
            ia_play()

# Fonction pour le jeu de l'IA
def ia_play():
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        move = random.choice(empty_cells)
        on_button_click(move)

# Configuration de l'interface Tkinter
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
current_player = "X"

for i in range(9):
    button = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

jeux = int(input("Choisi le mode solo en appuyant sur 0 ou en multijoueur en appuyant sur 1 : "))
if jeux == 0:
    joueur1 = input("Choisi un pseudo banger pour le joueur: ")
    joueur2 = "L'IA"
else:
    joueur1 = input("Choisi un pseudo banger pour le joueur 1 : ")
    joueur2 = input("Choisi un pseudo rocambolesque pour le joueur 2 : ")

root.mainloop()
