ROWS = 6
COLUMNS = 7
CONNECT_WINNER_COUNT = 4

direction_mapper = {
    "up": (-1, 0),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
}

class InvalidColumnNumber(Exception):
    pass


class FullColumnError(Exception):
    pass


def validate_column_choice(player_num, column_choice, board):
    try:
        column = int(column_choice)
        if column < 1 or column > 7:
            raise InvalidColumnNumber
        return column
    except ValueError:
        print(f"Player {player_num}, please enter a valid number")
    except InvalidColumnNumber:
        print(f"Player {player_num}, please enter a number between 1-7")


def obtain_position(player_num, board):
    while True:
        data = input(f"Player {player_num}, please select a column: ")
        column = validate_column_choice(player_num, data, board)
        if not column:
            continue
        available_row_index = None
        column_index = column - 1
        for row_index in range(ROWS-1, -1, -1):
            if board[row_index][column_index] == 0:
                available_row_index = row_index
                return available_row_index, column_index
        if not available_row_index:
            print(f"Please select a colunm with available spots")
            continue

def is_valid_position(row, col):
    return 0<=row< ROWS and 0<=col<COLUMNS


def check_direction_count(current_row_index, current_col_index, row_index_movement, col_index_movement, board, current_player_num):
    count = 0

    for index in range(1, CONNECT_WINNER_COUNT):
        # TODO multiple better than + or -
        next_row_index = current_row_index + row_index_movement * index
        next_col_index = current_col_index + col_index_movement * index
        if not is_valid_position(next_row_index, next_col_index):
            return count
        if board[next_row_index][next_col_index] == current_player_num:
            count += 1
    return count


def is_winner(current_wor_index, current_col_index, board, current_player_num):
    for direction, movement in direction_mapper.items():
        row_index_movement, col_index_movement = movement

        count_direction = check_direction_count(current_wor_index, current_col_index, row_index_movement, col_index_movement, board, current_player_num)
        # TODO
        # opposite_count_direction = check_opposite_direction_count()

        # TODO
        # if count_direction + opposite_count_direction ==??



def print_board(board):
    for row in board:
        print(row)


turns = 1

matrix = []
for _ in range(ROWS):
    matrix.append([0 for _ in range(COLUMNS)])

print_board(matrix)
while True:
    player_num = 1 if turns % 2 != 0 else 2
    row_index, column_index = obtain_position(player_num, matrix)
    matrix[row_index][column_index] = player_num
    if turns >= 7 and is_winner(row_index, column_index, matrix, player_num):
        break
    if ROWS*COLUMNS + 1 == turns:
        print("Board is full. No winner")
        break
    turns += 1
    print_board(matrix)

