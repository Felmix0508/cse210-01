def main():
    player = players_turn("")
    blackboard = create_board()
    while not (winner_player(blackboard) or loser_player(blackboard)):
        display_game(blackboard)
        players_move(player,blackboard)
        player = players_turn(player)
    display_game(blackboard)

def create_board():
    blackboard = []
    for square in range(9):
        blackboard.append(square + 1)
    return blackboard

def display_game(blackboard):
    print()
    print(f"{blackboard[0]}|{blackboard[1]}|{blackboard[2]}")
    print('_____')
    print(f"{blackboard[3]}|{blackboard[4]}|{blackboard[5]}")
    print('_____')
    print(f"{blackboard[6]}|{blackboard[7]}|{blackboard[8]}")
    print()


def loser_player(blackboard):
    for square in range(9):
        if blackboard[square] != "x" and blackboard[square] != "o":
            return False
    return True

def winner_player(blackboard):
    return(blackboard[0] == blackboard[1] == blackboard[2] or
           blackboard[3] == blackboard[4] == blackboard[5] or
           blackboard[6] == blackboard[7] == blackboard[8] or
           blackboard[0] == blackboard[3] == blackboard[6] or
           blackboard[1] == blackboard[4] == blackboard[7] or
           blackboard[2] == blackboard[5] == blackboard[8] or
           blackboard[0] == blackboard[4] == blackboard[8] or
           blackboard[2] == blackboard[4] == blackboard[6])
    
def players_move(player,blackboard):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    blackboard[square - 1] = player
    
def players_turn(move):
    if move == "" or move == "o":
        return "x"
    elif move == "x":
        return "o"
    
if __name__ == "__main__":
    main()