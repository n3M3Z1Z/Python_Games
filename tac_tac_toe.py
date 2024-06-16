# Define the print board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Initialize a 3x3 board with empty spaces
def main():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

# Print the initial board
    print("Tic-Tac-Toe Board:")
    print_board(board)

if __name__ == "__main__":
    main()
