import math

width = 5
board = [" "," "," ",
         " "," "," ",
         " "," "," "]

jeux = int(input("Choisi le mode solo en appuyant sur 0 ou en multijoueur en appuyant sur 1 : "))

def afficher_plateau():
    print('|' + '-' * (width) + '|'+ '-' * (width) + '|'+ '-' * (width) + '|')
    print('|' + ' ' * (width-3) + board[6] *(width-4)+ ' ' * (width-3) + '|'+ ' ' * (width-3) + board[7] *(width-4)+ ' ' * (width-3)+'|'+ ' ' * (width-3) + board[8] *(width-4)+ ' ' * (width-3)+ '|')
    print('|' + '-' * (width) + '|'+ '-' * (width) + '|'+ '-' * (width) + '|')
    print('|' + ' ' * (width-3) + board[3] *(width-4)+ ' ' * (width-3) + '|'+ ' ' * (width-3) + board[4] *(width-4)+ ' ' * (width-3)+'|'+ ' ' * (width-3) + board[5] *(width-4)+ ' ' * (width-3)+ '|')
    print('|' + '-' * (width) + '|'+ '-' * (width) + '|'+ '-' * (width) + '|')
    print('|' + ' ' * (width-3) + board[0] *(width-4)+ ' ' * (width-3) + '|'+ ' ' * (width-3) + board[1] *(width-4)+ ' ' * (width-3)+'|'+ ' ' * (width-3) + board[2] *(width-4)+ ' ' * (width-3)+ '|')
    print('|' + '-' * (width) + '|'+ '-' * (width) + '|'+ '-' * (width) + '|')

def verifier_victoire(signe):
    combinaisons = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)] 
    for combinaison in combinaisons:
        if board[combinaison[0]] == board[combinaison[1]] == board[combinaison[2]] == signe:
            return True
    return False

# Algorithme Minimax
def minimax(board, profondeur, is_maximizing, signe_ia, signe_joueur):
    if verifier_victoire(signe_ia):
        return 1
    elif verifier_victoire(signe_joueur):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        meilleur_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = signe_ia
                score = minimax(board, profondeur + 1, False, signe_ia, signe_joueur)
                board[i] = " "
                meilleur_score = max(score, meilleur_score)
        return meilleur_score
    else:
        meilleur_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = signe_joueur
                score = minimax(board, profondeur + 1, True, signe_ia, signe_joueur)
                board[i] = " "
                meilleur_score = min(score, meilleur_score)
        return meilleur_score

def meilleur_coup(board, signe_ia, signe_joueur):
    meilleur_score = -math.inf
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

def ia_avec_minimax(board, signe_ia, signe_joueur):
    coup = meilleur_coup(board, signe_ia, signe_joueur)
    board[coup] = signe_ia
    afficher_plateau()
    if verifier_victoire(signe_ia):
        return(f"L'IA a gagné!")
    if " " not in board:
        return("Match nul!")
    return None

# Mode Solo
if jeux == 0:
    joueur1 = input("Choisi un pseudo banger pour le joueur: ")
    joueur2 = "L'IA"
    signe_joueur = input("Choisi ton signe (X ou O) : ").lower()
    if signe_joueur =="o":
        signe_ia ='x'
    elif signe_joueur == "x":
        signe_ia = 'o'

    tour = 0
    while True:
        afficher_plateau()
        if tour % 2 == 0:
            joueur = joueur1
            signe = signe_joueur
            case = int(input(f"{joueur}, choisis une case (1-9) : ")) - 1
            if 0 <= case <= 8 and board[case] == " ":
                board[case] = signe
            else:
                print("Case invalide, réessayez.")
                continue
        else:
            print(f"{joueur2} joue...")
            result = ia_avec_minimax(board, signe_ia, signe_joueur)
            if result:
                print(result)
                break
        
        if verifier_victoire(signe):
            afficher_plateau()
            print(f"{joueur} a gagné!")
            break
        if " " not in board:
            afficher_plateau()
            print("Match nul!")
            break
        tour += 1

# Mode Multijoueur
elif jeux == 1:
    joueur1 = input("Choisi un pseudo banger pour le joueur 1 : ")
    joueur2 = input("Choisi un pseudo rocambolesque pour le joueur 2 : ")
    signe_joueur1 = input(f"{joueur1}, choisi ton signe (X ou O) : ").lower()
    if signe_joueur1 =="o":
        signe_joueur2 ='x'
    elif signe_joueur1 == "x":
        signe_joueur2 = 'o'
    
    tour = 0
    while True:
        afficher_plateau()
        if tour % 2 == 0:
            joueur = joueur1
            signe = signe_joueur1
        else:
            joueur = joueur2
            signe = signe_joueur2

        case = int(input(f"{joueur}, choisis une case (1-9) : ")) - 1
        if 0 <= case <= 8 and board[case] == " ":
            board[case] = signe
        else:
            print("Case invalide, réessayez.")
            continue

        if verifier_victoire(signe):
            afficher_plateau()
            print(f"{joueur} a gagné!")
            break
        if " " not in board:
            afficher_plateau()
            print("Match nul!")
            break
        tour += 1
else:
    print("Choisi un chiffre entre 0 et 1")
