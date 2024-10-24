import tkinter as tk
from tkinter import messagebox
import random

# Initialisation du plateau
board = [" " for _ in range(9)]
current_player = "X"
jeux = None
joueur1 = ""
joueur2 = ""

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
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)
    update_status()

# Fonction pour gérer un clic sur un bouton
def on_button_click(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        
        if verifier_victoire(current_player):
            messagebox.showinfo("Fin de la partie", f"{joueur1 if current_player == 'X' else joueur2} a gagné!")
            reset_game()
            return

        if " " not in board:
            messagebox.showinfo("Fin de la partie", "Match nul!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"
        update_status()
        
        if jeux == 0 and current_player == "O":
            root.after(500, ia_play)  # Délai pour l'IA

# Fonction pour le jeu de l'IA
def ia_play():
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        move = random.choice(empty_cells)
        on_button_click(move)

# Fonction pour mettre à jour le statut
def update_status():
    status_label.config(text=f"Tour de : {joueur1 if current_player == 'X' else joueur2}")

# Configuration de l'interface Tkinter
root = tk.Tk()
root.title("Tic Tac Toe")

# Fonction pour démarrer le jeu
def start_game():
    global jeux, joueur1, joueur2
    jeux = mode_var.get()
    joueur1 = joueur1_entry.get() or "Joueur 1"
    joueur2 = joueur2_entry.get() or "Joueur 2" if jeux == 1 else "L'IA"
    setup_frame.pack_forget()
    game_frame.pack()
    status_frame.pack(fill=tk.X)
    update_status()

# Frame de configuration
setup_frame = tk.Frame(root)
setup_frame.pack(padx=10, pady=10)

mode_var = tk.IntVar(value=0)
tk.Radiobutton(setup_frame, text="Mode Solo", variable=mode_var, value=0).pack()
tk.Radiobutton(setup_frame, text="Mode Multijoueur", variable=mode_var, value=1).pack()

tk.Label(setup_frame, text="Nom du Joueur 1:").pack()
joueur1_entry = tk.Entry(setup_frame)
joueur1_entry.pack()

tk.Label(setup_frame, text="Nom du Joueur 2 (pour le multijoueur):").pack()
joueur2_entry = tk.Entry(setup_frame)
joueur2_entry.pack()

tk.Button(setup_frame, text="Commencer", command=start_game).pack(pady=10)

# Frame de jeu
game_frame = tk.Frame(root)
buttons = []

for i in range(9):
    button = tk.Button(game_frame, text=" ", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Frame de statut
status_frame = tk.Frame(root)
status_label = tk.Label(status_frame, text="", font=('Arial', 12))
status_label.pack(pady=5)

# Bouton pour recommencer
restart_button = tk.Button(status_frame, text="Recommencer", command=reset_game)
restart_button.pack(pady=5)

root.mainloop()