import tkinter as tk
from tkinter import messagebox
import random

# Initialisation du plateau et des joueurs
board = [" " for _ in range(9)]
current_player = "X"
jeux = None
joueur1 = ""
joueur2 = ""
difficulte = "Facile"  # Par défaut, la difficulté est "Facile"
signe_joueur1 = "X"  # Par défaut, joueur 1 est "X"
signe_joueur2 = "O"  # Par défaut, joueur 2 (ou IA) est "O"

# Fonction pour vérifier la victoire
def verifier_victoire(signe):
    combinaisons = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]
    for combinaison in combinaisons:
        if board[combinaison[0]] == board[combinaison[1]] == board[combinaison[2]] == signe:
            return True
    return False

# Fonction Minimax pour l'IA (difficile)
def minimax(board, profondeur, is_maximizing, signe_ia, signe_joueur):
    if verifier_victoire(signe_ia):
        return 1
    elif verifier_victoire(signe_joueur):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        meilleur_score = -999999
        for i in range(9):
            if board[i] == " ":
                board[i] = signe_ia
                score = minimax(board, profondeur + 1, False, signe_ia, signe_joueur)
                board[i] = " "
                meilleur_score = max(score, meilleur_score)
        return meilleur_score
    else:
        meilleur_score = 999999
        for i in range(9):
            if board[i] == " ":
                board[i] = signe_joueur
                score = minimax(board, profondeur + 1, True, signe_ia, signe_joueur)
                board[i] = " "
                meilleur_score = min(score, meilleur_score)
        return meilleur_score

# Fonction pour déterminer le meilleur coup de l'IA
def meilleur_coup(board, signe_ia, signe_joueur):
    meilleur_score = -999999
    coup = None
    for i in range(9):
        if board[i] == " ":
            board[i] = signe_ia
            score = minimax(board, 0, False, signe_ia, signe_joueur)
            board[i] = " "
            if score > meilleur_score:
                meilleur_score = score
                coup = i
    return coup

# Fonction pour le coup aléatoire (facile)
def coup_aleatoire():
    coups_possibles = [i for i in range(9) if board[i] == " "]
    return random.choice(coups_possibles) if coups_possibles else None

# Fonction pour le jeu de l'IA dans Tkinter
def ia_joue():
    signe_ia = signe_joueur2  # L'IA prend le signe du joueur 2
    if difficulte == "Facile":
        coup = coup_aleatoire()
    else:  # Mode difficile
        coup = meilleur_coup(board, signe_ia, signe_joueur1)
    if coup is not None:
        on_button_click(coup)

# Fonction pour réinitialiser le jeu
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = signe_joueur1  # Réinitialiser le joueur courant
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
            messagebox.showinfo("Fin de la partie", f"{joueur1 if current_player == signe_joueur1 else joueur2} a gagné!")
            reset_game()
            return

        if " " not in board:
            messagebox.showinfo("Fin de la partie", "Match nul!")
            reset_game()
            return

        current_player = signe_joueur2 if current_player == signe_joueur1 else signe_joueur1
        update_status()

        if jeux == 0 and current_player == signe_joueur2:  # Si c'est le tour de l'IA
            root.after(500, ia_joue)

# Fonction pour mettre à jour le statut
def update_status():
    status_label.config(text=f"Tour de : {joueur1 if current_player == signe_joueur1 else joueur2}")

# Fonction pour démarrer le jeu
def start_game():
    global jeux, joueur1, joueur2, difficulte, signe_joueur1, signe_joueur2, current_player

    # Déterminer le mode de jeu
    jeux = mode_var.get()

    # Récupérer le nom du joueur 1
    joueur1 = joueur1_entry.get() or "Joueur 1"

    # Récupérer le nom du joueur 2
    if jeux == 1:  # Mode Multijoueur
        joueur2 = joueur2_entry.get() or "Joueur 2"
    else:  # Mode Solo
        joueur2 = "L'IA"

    # Récupérer la difficulté si en mode Solo
    if jeux == 0:
        difficulte = difficulte_var.get()
    
    # Récupérer le signe choisi pour le joueur 1
    signe_joueur1 = signe_var.get()  
    # Déterminer automatiquement le signe de l'autre joueur
    signe_joueur2 = "O" if signe_joueur1 == "X" else "X"
    
    # Assurer que le joueur 1 commence toujours
    current_player = signe_joueur1
    
    # Masquer le cadre de configuration et afficher le cadre de jeu
    setup_frame.pack_forget()
    game_frame.pack()
    status_frame.pack(fill=tk.X)
    update_status()

# Fonction pour afficher les options en fonction du mode de jeu choisi
def show_options():
    global joueur1_entry, joueur2_entry, difficulte_var, signe_var

    # Réinitialiser le cadre de configuration
    for widget in setup_frame.winfo_children():
        widget.destroy()

    # Choix du mode de jeu
    if mode_var.get() == 0:  # Mode Solo
        tk.Label(setup_frame, text="Mode Solo", font=("Arial", 18)).pack(pady=10)
        tk.Label(setup_frame, text="Nom du Joueur 1:", font=("Arial", 14)).pack()
        joueur1_entry = tk.Entry(setup_frame, font=("Arial", 14))
        joueur1_entry.pack()
        
        # Choix de la difficulté
        difficulte_var = tk.StringVar(value="Facile")
        tk.Label(setup_frame, text="Choisissez la difficulté:", font=("Arial", 14)).pack()
        tk.Radiobutton(setup_frame, text="Facile", variable=difficulte_var, value="Facile", font=("Arial", 14)).pack()
        tk.Radiobutton(setup_frame, text="Difficile", variable=difficulte_var, value="Difficile", font=("Arial", 14)).pack()
        
    else:  # Mode Multijoueur
        tk.Label(setup_frame, text="Mode Multijoueur", font=("Arial", 18)).pack(pady=10)
        tk.Label(setup_frame, text="Nom du Joueur 1:", font=("Arial", 14)).pack()
        joueur1_entry = tk.Entry(setup_frame, font=("Arial", 14))
        joueur1_entry.pack()
        
        tk.Label(setup_frame, text="Nom du Joueur 2:", font=("Arial", 14)).pack()
        joueur2_entry = tk.Entry(setup_frame, font=("Arial", 14))
        joueur2_entry.pack()

    # Choix du signe pour le joueur 1
    signe_var = tk.StringVar(value="X")  # Par défaut, joueur 1 est "X"
    tk.Label(setup_frame, text="Choisissez le signe du Joueur 1:", font=("Arial", 14)).pack()
    tk.Radiobutton(setup_frame, text="X", variable=signe_var, value="X", font=("Arial", 14)).pack()
    tk.Radiobutton(setup_frame, text="O", variable=signe_var, value="O", font=("Arial", 14)).pack()

    # Bouton pour démarrer le jeu
    tk.Button(setup_frame, text="Démarrer le jeu", font=("Arial", 16), command=start_game).pack(pady=20)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu de Tic Tac Toe")
root.geometry("600x700")  # Taille de la fenêtre

# Variable pour le mode de jeu
mode_var = tk.IntVar(value=0)

# Cadre de configuration
setup_frame = tk.Frame(root)
setup_frame.pack(pady=20)

# Boutons pour choisir le mode de jeu
tk.Label(setup_frame, text="Choisissez le mode de jeu:", font=("Arial", 20)).pack(pady=10)
tk.Button(setup_frame, text="Mode Solo", font=("Arial", 16), width=10, command=lambda: (mode_var.set(0), show_options())).pack(pady=10)
tk.Button(setup_frame, text="Mode Multijoueur", font=("Arial", 16), width=15, command=lambda: (mode_var.set(1), show_options())).pack(pady=10)

# Cadre de jeu
game_frame = tk.Frame(root)

# Création des boutons du plateau
buttons = []
for i in range(9):
    button = tk.Button(game_frame, text=" ", font=("Arial", 48), width=5, height=2,
                       command=lambda index=i: on_button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Frame de statut
status_frame = tk.Frame(root)
status_label = tk.Label(status_frame, text="", font=("Arial", 16))
status_label.pack()

# Lancer l'application
root.mainloop()