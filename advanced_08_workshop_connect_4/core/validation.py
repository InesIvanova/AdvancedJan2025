from advanced_08_workshop_connect_4.constants import ROWS, COLUMNS
from advanced_08_workshop_connect_4.exceptions import FullColumnError, InvalidColumnNumber


def validate_column_choice(player_num, column_choice, available_spots):
    try:
        column = int(column_choice)
        if column < 1 or column > 7:
            raise InvalidColumnNumber
        available_row = available_spots[column-1]
        if available_row < 0:
            raise FullColumnError
        return column
    except ValueError:
        print(f"Player {player_num}, please enter a valid number")
    except InvalidColumnNumber:
        print(f"Player {player_num}, please enter a number between 1-7")
    except FullColumnError:
        print(f"Please select a columн with available spots")


def is_valid_position(row, col):
    return 0 <= row < ROWS and 0 <= col < COLUMNS