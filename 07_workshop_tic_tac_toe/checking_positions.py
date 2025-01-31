winning_combinations = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
]


def check_winner(board, player):
    for combo in winning_combinations:
        if board[combo[0] - 1] == board[combo[1] - 1] == board[combo[2] - 1] == player:
            return True
    return False


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def play_game():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    current_player = 'X'
    moves = 0

    print("Добре дошли в морски шах!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Играч {current_player}, изберете позиция (1-9): "))
            if move < 1 or move > 9:
                print("Моля, изберете валидна позиция (1-9).")
                continue
            if board[move - 1] in ['X', 'O']:
                print("Тази позиция е вече заета. Изберете друга.")
                continue
        except ValueError:
            print("Моля, въведете валидно число (1-9).")
            continue

        board[move - 1] = current_player
        moves += 1
        print_board(board)

        if check_winner(board, current_player) and moves >= 5:
            print(f"Играч {current_player} спечели!")
            break

        if moves == 9:
            print("Играта завърши наравно!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


play_game()