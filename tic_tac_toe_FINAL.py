from stddraw import *
import color
setXscale(0, 3.0)
setYscale(-0.5, 3.0)

def find_row(my):
    """takes the Y coordinate of the mouse and returns a value for the row"""
    if my >= 0.0 and my <= 1.0:
        row = 0
    elif my > 1 and my <=2.0:
        row = 1
    elif my > 2.0 and my <= 3.0:
        row = 2
    else:
        row = -1
    return row

def find_column(mx):
    """takes the x coordinate and returns a value for the column"""
    if mx >= 0.0 and mx <= 1.0:
        column = 0
    elif mx >= 1 and mx <= 2.0:
        column = 1
    else:
        column = 2
    return column

def win_condition(moves_arr, find_row, find_column,mx,my):
    """checks the conditions for winning a game"""
    row = find_row(mx)
    column = find_column(my)
    for i in range(len(moves_arr)):
        for j in range(len(moves_arr)):
            if moves_arr[0][0] == moves_arr[0][1] == moves_arr[0][2] != 0: #top horizontal
                return True
            elif moves_arr[1][0] == moves_arr[1][1] == moves_arr[1][2] != 0: #middle horizontal
                return True
            elif moves_arr[2][0] == moves_arr[2][1]== moves_arr[2][2] != 0: #bottom horizontal
                return True
            elif moves_arr[2][0] == moves_arr[1][0] == moves_arr[0][0] != 0: #left vertical
                return True
            elif moves_arr[2][1] == moves_arr[1][1] == moves_arr[0][1] != 0: # middle vertical
                return True
            elif moves_arr[0][2] == moves_arr[1][2] == moves_arr[2][2] != 0:# right vertical
                return True
            elif moves_arr[0][0] == moves_arr[1][1] == moves_arr[2][2] != 0: #diagonal
                return True
            elif moves_arr[0][2] == moves_arr[1][1] == moves_arr[2][0] != 0: # diagonal
                return True
            else:
                return False

def draw_prev_turns(moves_arr):
    """draws all of the previous turns that have taken place so far in the game"""
    setPenRadius(0.02)
    setPenColor(BLACK)
    line_1 = line(0.0, 1.0, 3.0, 1.0)
    line_2 = line(0.0, 2.0, 3.0, 2.0)
    line_3 = line(1.0, 0.0, 1.0, 3.0)
    line_4 = line(2.0, 0.0, 2.0, 3.0)
    for i in range(len(moves_arr)):
        for j in range(len(moves_arr)):
            if moves_arr[i][j] != 0:
                row = i
                column = j
                if moves_arr[i][j] =='X':
                    setFontSize(100)
                    setFontFamily("Lucida")
                    setPenColor(BOOK_BLUE)
                    text(0.5 + column, 0.5 +row, str(moves_arr[i][j]))
                elif moves_arr[i][j] == 'O':
                    setFontSize(100)
                    setFontFamily("Lucida")
                    setPenColor(RED)
                    text(0.5 + column, 0.5 +row, str(moves_arr[i][j]))

def cont_play(mouse_x, mouse_y):
    """goes back to welcome window and asks the player if they want to play another game or exit"""
    if mouse_y >= 1.0 and mouse_y <= 1.5:
        if mouse_x >= 0.25 and mouse_x <= 1.25:
            return True
        elif mouse_x >= 1.75 and mouse_x <= 2.75:
            return False

def whose_turn(turn):
    """Writes the statement for who's turn it is"""
    a = "It is X's turn"
    b = "It is O's turn"
    setPenColor(BLACK)
    setFontFamily("Lucida")
    setFontSize(30)
    turn_text = text(1.5, -0.1, '')
    if turn%2 == 0:
        turn_text = text(1.5, -0.1, str(a))
    else:
        turn_text = text(1.5, -0.1, str(b))
    return turn_text
    
def welcome_window():
    setPenColor(BLACK)
    setPenRadius()
    setFontFamily("Serif")
    setFontSize(30)
    setPenColor(GREEN)
    play_button = filledRectangle(0.25, 1.0, 1.0, 0.5)
    setPenColor(RED)
    exit_button = filledRectangle(1.75, 1.0, 1.0, 0.5)
    setPenColor(BLACK)
    play_text = text(0.75, 1.25, "Play")
    exit_text= text(2.25, 1.25, "Exit" )
    welcome_text_1 = text(1.5, 0.0, "Welcome to Tic-Tac-Toe")
    welcome_text_2 = text(1.5, -0.25, "Click 'Play' to continue")

def X_wins(moves_arr):
    """execute when it is X's turn and the win condition is satisfied"""
    clear()
    draw_prev_turns(moves_arr)
    setFontSize(30)
    setPenColor(BOOK_BLUE)
    text(1.5, -0.1, "X wins!")
    show(2000.0)
    clear()
    main()

def O_wins(moves_arr):
    """execute when it is O's turn and the win condition is satisfied"""
    clear()
    draw_prev_turns(moves_arr)
    setFontSize(30)
    setPenColor(RED)
    text(1.5, -0.1, "O wins!")
    show(2000.0)
    clear()
    main()

def player_turn(moves_arr, sign, row, column):
    """Executes players turns and updates the array for moves"""
    if sign == 'X':
        setFontSize(100)
        setFontFamily("Lucida")
        setPenColor(BOOK_BLUE)
        text(0.5 + column, 0.5 +row, str(sign))
        moves_arr[row][column] = sign
    elif sign == 'O':
        setFontSize(100)
        setFontFamily("Lucida")
        setPenColor(RED)
        text(0.5 + column, 0.5 +row, str(sign))
        moves_arr[row][column] = sign


def draw_case(moves_arr):
    """execute when the game is over and its a draw"""
    clear()
    draw_prev_turns(moves_arr)
    setFontSize(30)
    setPenColor(VIOLET)
    text(1.5, -0.1, "It's a draw")
    show(2000.0)
    clear()
    main()

def empty_cell_error(moves_arr):
    clear()
    draw_prev_turns(moves_arr)
    setPenColor(BLACK)
    setFontSize(30)
    error= text(1.5, -0.1, "Please select an empty cell")
    return error

def play_tic_tac_toe():
    """Playing a turn of tic-tac-toe until someone wins or its a draw"""
    turn = 0
    moves_arr = [[0,0,0],[0,0,0], [0,0,0]]
    while turn <= 9:
        clear()
        draw_prev_turns(moves_arr)
        mouse_clicked = mousePressed()
        who = whose_turn(turn)
        if mouse_clicked:
            mx = mouseX()
            my = mouseY()
            column = find_column(mx)
            row = find_row(my)
            if turn%2 == 0 and row >= 0:
                sign = "X"
                if moves_arr[row][column] == 0:
                    player_turn(moves_arr, sign, row, column)
                    turn+=1
                    win = win_condition(moves_arr, find_row, find_column,mx,my)
                    if win == True:
                        X_wins(moves_arr)
                    elif turn == 9:
                        draw_case(moves_arr)
                elif moves_arr[row][column] != 0:
                    empty_cell_error(moves_arr)
                    show(2000.0)
            elif turn% 2 != 0 and row >= 0:
                sign = "O"
                if moves_arr[row][column] == 0:
                    player_turn(moves_arr, sign, row, column)
                    turn+=1
                    win = win_condition(moves_arr,find_row, find_column,mx,my)
                    if win == True:
                        O_wins(moves_arr)
                    elif turn == 9:
                        draw_case(moves_arr)
                elif moves_arr[row][column] != 0:
                    empty_cell_error(moves_arr)
                    show(2000.0)   
        show(0.5)
    moves_arr = [[0,0,0],[0,0,0], [0,0,0]]

def main():
    while True:
        mouse_clicked = mousePressed()
        welcome_window()
        if mouse_clicked:
            mouse_x = mouseX()
            mouse_y = mouseY()
            play_again = cont_play(mouse_x, mouse_y)
            if play_again == True:
                clear()
                play_tic_tac_toe()
            elif play_again == False:
                exit()
        show(0.5)
main()  