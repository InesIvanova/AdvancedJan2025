class InvalidPositionNumber(Exception):
    pass


class PositionAlreadyTaken(Exception):
    pass


def obtain_valid_position(player_name, matrix, position_mapper):
    while True:
        try:
            selected_position = int(input(f"{player_name}, please select a spot: "))
            if selected_position < 1 or selected_position > 9:
                raise InvalidPositionNumber
            row, col = position_mapper[selected_position]
            # Alternative way to calculate row and col (with the given position without mapper)
            # if matrix[selected_position // 3 - 1][selected_position % 3 - 1] != " ":
            if matrix[row][col] != " ":
                raise PositionAlreadyTaken
            return selected_position
        except ValueError:
            print("Please enter a valid number")
        except InvalidPositionNumber:
            print("Please enter a number between 1-9")
        except PositionAlreadyTaken:
            print("Please select an empty position")


def print_board(matrix):
    for row in matrix:
        print(f"|  {'  |  '.join(row)}  |")

def is_winner(player_symbol, matrix):
    matrix_length = len(matrix)
    # Check for row winner
    for row in matrix:
        if all([el == player_symbol for el in row]):
            return True

    # Check for col winner
    for col_index in range(matrix_length):
        if all([matrix[row_index][col_index] == player_symbol for row_index in range(matrix_length)]):
            return True

    main_diagonal_winner = all([matrix[index][index] == player_symbol for index in range(matrix_length)])
    diagonal_winner = all([matrix[matrix_length - 1 - col_index][col_index] == player_symbol for col_index in range(matrix_length)])

    if main_diagonal_winner or diagonal_winner:
        return True

    return False

def play_turn(player_symbol, row, col, matrix, turns_count):
    matrix[row][col] = player_symbol

    if turns_count >= 5:
        return is_winner(player_symbol, matrix)
    print_board(matrix)


def save_game_result(winner_name):
    with open("result.txt") as file:
        lines = file.readlines()
    content = ""
    is_new = True
    for line in lines:
        name, score = line.split(",")
        score = score[:-1]
        if name.lower() == winner_name.lower():
            score = int(score) + 1
            is_new = False
        content += f"{name},{score}\n"
    if is_new:
        content += f"{winner_name},1\n"
    with open("result.txt", "w") as file:
        file.write(content)

def play():
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")

    symbol = input("Player 1 select your symbol - either X or O: ")
    while True:
        if symbol not in ["X", "O", "o", "x"]:
            symbol = input()
        else:
            break

    player1_symbol = symbol.upper()
    player2_symbol = "O" if player1_symbol == "X" else "X"

    position_matrix = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    for row in position_matrix:
        print(f"|  {'  |  '.join(row)}  |")

    print(f"{player1_name} starts first")

    position_mapper = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }
    matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    player_to_symbol = {
        player1_name: player1_symbol,
        player2_name: player2_symbol,
    }

    turns_count = 1
    while True:
        current_player_name = player2_name if turns_count % 2 == 0 else player1_name
        position = obtain_valid_position(current_player_name, matrix, position_mapper)
        row, col = position_mapper[position]
        player_symbol = player_to_symbol[current_player_name]
        winner = play_turn(player_symbol, row, col, matrix, turns_count)
        if winner:
            print_board(matrix)
            print(f"{current_player_name} is winner!")
            save_game_result(current_player_name)
            break
        turns_count += 1
        if turns_count == 10:
            print_board(matrix)
            print("No winner - game over")
            break


def show_stats():
    data = {}
    with open("result.txt") as file:
        for row in file.readlines():
            name, score = row.split(",")
            data[name] = int(score[:-1])
    sorted_data = sorted(data.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    for name, score in sorted_data:
        print(f"{name} -> {score}")


if __name__ == "__main__":
    command = input()
    while True:
        if command == "stats":
            show_stats()
            break
        elif command == "play":
            play()
            break
        elif command == "end":
            exit(0)
        else:
            print("Please select between: stats, play and end")
            command = input()
