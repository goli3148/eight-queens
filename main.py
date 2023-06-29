board_size = 8
row_next = 0
row_indexed_col = [-1 for i in range(board_size)]

FIND_ALL_ANSWERES = True
ANSWERES = []

def chess_board():
    global board_size
    # 0 empty and allowed signal
    # 1 inserted quuen
    board = [[0 for i in range(board_size)] for i in range(board_size)]
    return board


def collision_detecter(board, row, col):
    global row_indexed_col
    # coloumn collision detecter
    for i in range(0, row):
        if col == row_indexed_col[i]:
            return True
    # go back reverse row
    for i in range(1, row+1):
        if col-i >= 0:
            if board[row-i][col-i] == 1:
                return True
        if col+i < board_size:
            if board[row-i][col+i] == 1:
                return True
    return False

def insert(board):
    global board_size
    global row_next
    global row_indexed_col
    global FIND_ALL_ANSWERES
    
    if row_next == board_size:
        print(f"solution number: {len(ANSWERES)+1}")
        print_board(board)
        
        if not FIND_ALL_ANSWERES:
            exit()
        else:
            ANSWERES.append(board)
            row_next -= 1
            board[row_next][row_indexed_col[row_next]]=0
            row_indexed_col[row_next] = -1
            row_next -= 1
            board[row_next][row_indexed_col[row_next]]=0
            return board
    
    for j in range(row_indexed_col[row_next]+1, board_size):
        if not collision_detecter(board, row_next, j):
            board[row_next][j] = 1
            row_indexed_col[row_next] = j
            row_next += 1
            return board
    row_indexed_col[row_next]=-1
    row_next -= 1
    if row_next < 0:
        print("FAILED: ")
        print_board(board)
        exit()
    board[row_next][row_indexed_col[row_next]]=0
    return board
   


def print_board(board):
    global board_size
    for i in range(board_size):
        print(board[i])
    print("\n---------------------------")
        
def solve():
    board = chess_board()
    while True:
        board = insert(board)
        

solve()
            