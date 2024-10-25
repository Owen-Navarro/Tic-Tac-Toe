import random
width = 5
board = [" "," "," ",
         " "," "," ",
         " "," "," "]

game = int(input("Choisi le mode solo en appuyant sur 0 ou en multijoueur en appuyant sur 1 : "))

def display_board():
    print('|' + '-' * (width) + '|'+ '-' * (width) + '|'+ '-' * (width) + '|')
    print('|' + ' ' * (width-3) + board[6] *(width-4)+ ' ' * (width-3) + '|'+ ' ' * (width-3) + board[7] *(width-4)+ ' ' * (width-3)+'|'+ ' ' * (width-3) + board[8] *(width-4)+ ' ' * (width-3)+ '|')
    print('|' + '-' * (width) + '|'+ '-' * (width) + '|'+ '-' * (width) + '|')
    print('|' + ' ' * (width-3) + board[3] *(width-4)+ ' ' * (width-3) + '|'+ ' ' * (width-3) + board[4] *(width-4)+ ' ' * (width-3)+'|'+ ' ' * (width-3) + board[5] *(width-4)+ ' ' * (width-3)+ '|')
    print('|' + '-' * (width) + '|'+ '-' * (width) + '|'+ '-' * (width) + '|')
    print('|' + ' ' * (width-3) + board[0] *(width-4)+ ' ' * (width-3) + '|'+ ' ' * (width-3) + board[1] *(width-4)+ ' ' * (width-3)+'|'+ ' ' * (width-3) + board[2] *(width-4)+ ' ' * (width-3)+ '|')
    print('|' + '-' * (width) + '|'+ '-' * (width) + '|'+ '-' * (width) + '|')

def victory_check(sign):
    combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)] 
    for combination in combination:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == sign:
            return True
    return False

def minimax(board, depth, is_maximizing, ia_sign, player_sign):
    if victory_check(ia_sign):
        return 1
    elif victory_check(player_sign):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = ia_sign
                score = minimax(board, depth + 1, False, ia_sign, player_sign)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = player_sign
                score = minimax(board, depth + 1, True, ia_sign, player_sign)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board, ia_sign, player_sign):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = ia_sign
            score = minimax(board, 0, False, ia_sign, player_sign)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def minimax_ia(board, ia_sign, player_sign):
    move = best_move(board, ia_sign, player_sign)
    board[move] = ia_sign
    if victory_check(ia_sign):
        return(f"L'IA a gagné!")
    if " " not in board:
        return("Match nul!")
    return None

# Solo mode
if game == 0:
    difficulty = int(input("Choisir la difficulté facile (0) ou difficile (1) : "))
    player1 = input("Choisi un pseudo banger pour le joueur: ")
    player2 = "L'IA"
    player_sign = input("Choisi ton signe (X ou O) : ").lower()
    ia_sign = 'o' if player_sign == "x" else 'x'

    round = 0
    while True:
        display_board()
        if round % 2 == 0:
            player = player1
            sign = player_sign
            box = int(input(f"{player}, choisis une case (1-9) : ")) - 1
            if 0 <= box <= 8 and board[box] == " ":
                board[box] = sign
            else:
                print("Case invalide, réessayez.")
                continue
        else:
            print(f"{player2} joue...")
            if difficulty == 1:
                result = minimax_ia(board, ia_sign, player_sign)
                if result:
                    display_board()
                    print(result)
                    break
            elif difficulty == 0:
                empty_positions = [i for i, x in enumerate(board) if x == " "]
                box = random.choice(empty_positions)
                board [box] = ia_sign
                print(f"L'IA a choisi la case {box + 1}")           

                if victory_check(ia_sign):
                    display_board()
                    print("L'IA a gagné!")
                    break

        if victory_check(sign):
            display_board()
            print(f"{player} a gagné!")
            break
        if " " not in board:
            display_board()
            print("Match nul!")
            break
        
        round += 1

# Multiplayer mode
elif game == 1:
    player1 = input("Choisi un pseudo banger pour le joueur 1 : ")
    player2 = input("Choisi un pseudo rocambolesque pour le joueur 2 : ")
    player1_sign = input(f"{player1}, choisis ton signe (X ou O) : ").lower()
    if player1_sign =="o":
        player2_sign ='x'
    elif player1_sign == "x":
        player2_sign = 'o'

    round = 0
    while True:
        display_board()
        if round % 2 == 0:
            player = player1
            sign = player1_sign
        else:
            player = player2
            sign = player2_sign

        box = int(input(f"{player}, choisis une case (1-9) : ")) - 1
        if 0 <= box <= 8 and board[box] == " ":
            board[box] = sign
        else:
            print("Case invalide, réessayez.")
            continue

        if victory_check(sign):
            display_board()
            print(f"{player} a gagné!")
            break

        if " " not in board:
            display_board()
            print("Match nul!")
            break
        round += 1
else:
    print("Choisi un chiffre entre 0 et 1")
