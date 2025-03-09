# Lab 6: Connect Four

def initialize_board(num_rows, num_cols): # creates a 2D list
    initial = []
    for row in range(num_rows):
        sublist = []
        for i in range(num_cols):
            sublist.append('-')
        initial.append(sublist)
    return initial

def print_board(board): # iterates through initialized board to print it
    for li in board:
        for item in li:
            print(item, '', end='')
        print()

def insert_chip(board, col, chip_type):
    for i in range(user_rows):
        if board[i][col] == '-':
            board[i][col] = chip_type
            return i
    print('Cannot insert chip there. Please try another column.')

def check_if_winner(board, row, col, chip_type):
    check_col_counter = 0
    check_row_counter = 0
    for i in range(user_cols):
        if board[row][i] == chip_type:
            check_col_counter += 1
            if check_col_counter == 4:
                return True
        else: check_col_counter = 0
    for i in range(user_rows):
        if board[i][col] == chip_type:
            check_row_counter += 1
            if check_row_counter == 4:
                return True
        else: check_row_counter = 0
    return False

if __name__ == "__main__":
    draw_counter = 0
    user_rows = int(input('What would you like the height of the board to be? '))
    user_cols = int(input('What would you like the length of the board to be? '))
    initial = initialize_board(user_rows,user_cols)
    print_board(initial)
    print('\nPlayer 1: x')
    print('Player 2: o')
    while True:
        while True:
            p1_choice = int(input('\nPlayer 1: Which column would you like to choose? '))
            if p1_choice >= user_cols:
                print('Invalid selection. Please try again.')
                continue
            break
        draw_counter += 1
        inserted_row1 = insert_chip(initial, p1_choice, 'x')
        print_board(initial[::-1])
        winner1 = check_if_winner(initial, inserted_row1, p1_choice, 'x')
        if winner1:
            print('\nPlayer 1 won the game!')
            break
        if draw_counter == (user_rows * user_cols):
            print('\nDraw. Nobody wins.')
            break

        while True:
            p2_choice = int(input('\nPlayer 2: Which column would you like to choose? '))
            if p2_choice >= user_cols:
                print('Invalid selection. Please try again.')
                continue
            break
        draw_counter += 1
        inserted_row2 = insert_chip(initial, p2_choice, 'o')
        print_board(initial[::-1])
        winner2 = check_if_winner(initial, inserted_row2, p2_choice, 'o')
        if winner2:
            print('\nPlayer 2 won the game!')
            break
        if draw_counter == (user_rows * user_cols):
            print('\nDraw. Nobody wins.')
            break