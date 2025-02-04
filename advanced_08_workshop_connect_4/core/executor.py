from advanced_08_workshop_connect_4.constants import CONNECT_WINNER_COUNT, direction_mapper
from advanced_08_workshop_connect_4.core.validation import validate_column_choice, is_valid_position


def obtain_position(player_num, available_spots):
    while True:
        data = input(f"Player {player_num}, please select a column: ")
        column = validate_column_choice(player_num, data, available_spots)
        if not column:
            continue
        column_index = column - 1
        return available_spots[column_index], column_index
        # TODO optimise
        # for row_index in range(ROWS - 1, -1, -1):
        #     if board[row_index][column_index] == 0:
        #         return row_index, column_index



def check_direction_count(
    current_row_index,
    current_col_index,
    row_index_movement,
    col_index_movement,
    board,
    current_player_num,
    sign,
):
    count = 0

    for index in range(1, CONNECT_WINNER_COUNT):
        next_row_index = eval(f"{current_row_index} {sign} {row_index_movement}*{index}")
        next_col_index = eval(f"{current_col_index} {sign} {col_index_movement} * {index}")

        if not is_valid_position(next_row_index, next_col_index):
            return count
        if board[next_row_index][next_col_index] == current_player_num:
            count += 1
        else:
            return count
    return count


def is_winner(current_wor_index, current_col_index, board, current_player_num):

    for direction, movement in direction_mapper.items():
        total_count = 1

        row_index_movement, col_index_movement = movement

        total_count += check_direction_count(
            current_wor_index,
            current_col_index,
            row_index_movement,
            col_index_movement,
            board,
            current_player_num,
            "+"
        )
        if direction != "down":
            total_count += check_direction_count(
                current_wor_index,
                current_col_index,
                row_index_movement,
                col_index_movement,
                board,
                current_player_num,
                "-"
            )
        if total_count >= CONNECT_WINNER_COUNT:
            return True
    return False