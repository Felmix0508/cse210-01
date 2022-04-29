print("Tic Tac Toe The Game by Felix S. Guzmán")
def main():
    player = next_player("")
    board = create_board()
    while not (The_winner(board) or The_loser(board)):
        display_game(board)
        player_turn(player, board)
        player = next_player(player)
    display_game(board)
    print("Great game. Please Come back!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_game(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def The_loser(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def The_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def player_turn(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(move):
    if move == "" or move == "o":
        return "x"
    elif move == "x":
        return "o"
       
if __name__ == "__main__":
    main()