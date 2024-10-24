width = 5
board = [" "] * 9
jeux = int(input("Choisi le mode solo en appuyant sur 0 ou en multijoueur en appuyant sur 1 : "))
def afficher_plateau():
    print('|' + '-' * (width) + '|' + '-' * (width) + '|' + '-' * (width) + '|')
    for row in range(0, 9, 3):
        print('|' + ' ' * (width//2) + board[row] + ' ' * (width//2) + '|' + 
            ' ' * (width//2) + board[row+1] + ' ' * (width//2) + '|' + 
            ' ' * (width//2) + board[row+2] + ' ' * (width//2) + '|')
        print('|' + '-' * (width) + '|' + '-' * (width) + '|' + '-' * (width) + '|')
                
def verifier_victoire(signe):
    combinaisons = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)] 
    for combinaison in combinaisons:
        if board[combinaison[0]] == board[combinaison[1]] == board[combinaison[2]] == signe:
            return True
    return False

if jeux == 0 :

    joueur1 = input("Choisi un pseudo banger pour le joueur: ")
    joueur2 = "L'IA"

    def ia(board,signe):
        tour = 0
        while True:
            afficher_plateau()
            if tour % 2 == 0:
                joueur = joueur1 
            else:
                joueur = joueur2
            if signe == "x":
                signe = "o"
            elif signe == "o":
                signe ="x"

            case = int(input(f"{joueur} choisi la case (1-9) : ")) - 1 
            
            if 0 <= case <= 8 and board[case] == " ":
                board[case] = signe
            
        
                if verifier_victoire(signe):
                    afficher_plateau()
                    return(f"{joueur} a gagné!")

                if " " not in board:
                    afficher_plateau()
                    return("Match nul!")
                tour += 1
            else:
                print("Case invalide, réessayez.")
    print(ia(board,input("Choisi le signe du bot (X ou O) : ")))

elif jeux == 1 :

    joueur1 = input("Choisi un pseudo banger pour le joueur 1 : ")
    joueur2 = input("Choisi un pseudo rocambolesque pour le joueur 2 : ")

    def multi(board,signe_joueur1):
        if signe_joueur1 == "x":
            signe_joueur2 = "o"
        elif signe_joueur1 == "o" :
            signe_joueur2 = "x"
        tour = 0
        while True:
            afficher_plateau()
            if tour % 2 == 0:
                joueur = joueur1
                signe = signe_joueur1
            else:
                joueur = joueur2
                signe = signe_joueur2
    
            case = int(input(f"{joueur} choisi la case (1-9) : ")) - 1 
            
            if 0 <= case <= 8 and board[case] == " ":
                board[case] = signe
        
                if verifier_victoire(signe):
                    afficher_plateau()
                    return(f"{joueur} a gagné!")

                if " " not in board:
                    afficher_plateau()
                    return("Match nul!")
                tour += 1
            else:
                print("Case invalide, réessayez.")
    print(multi(board,input(f"{joueur1} choisi ton signe (X ou O) : ")))
else :
    print("Choisi un chiffre entre 0 et 1")