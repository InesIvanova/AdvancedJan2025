from advanced_08_workshop_connect_4.constants import ROWS, COLUMNS
from advanced_08_workshop_connect_4.core.executor import obtain_position, is_winner
from advanced_08_workshop_connect_4.helpers import print_board


available_spots = {column_index: ROWS-1 for column_index in range(COLUMNS)}


turns = 1

matrix = []
for _ in range(ROWS):
    matrix.append([0 for _ in range(COLUMNS)])

print_board(matrix)
while True:
    player_num = 1 if turns % 2 != 0 else 2
    row_index, column_index = obtain_position(player_num, available_spots)
    matrix[row_index][column_index] = player_num
    available_spots[column_index] -= 1
    print_board(matrix)
    if turns >= 7:
        if is_winner(row_index, column_index, matrix, player_num):
            print(f"Player {player_num} you won!")
            break
    if ROWS * COLUMNS + 1 == turns:
        print("Board is full. No winner")
        break
    turns += 1
