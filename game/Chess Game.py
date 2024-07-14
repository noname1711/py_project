class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'white'
        self.game_over = False

    def initialize_board(self):
        # Create an empty chess board
        board = []
        for _ in range(8):
            row = [' '] * 8
            board.append(row)

        # Set up the initial positions of the pieces
        board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        board[1] = ['p'] * 8
        board[6] = ['P'] * 8
        board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

        return board

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_move(self, start_pos, end_pos):
        # Check if the start and end positions are within the board
        if not self.is_valid_position(start_pos) or not self.is_valid_position(end_pos):
            return False

        # Check if the piece at the start position belongs to the current player
        piece = self.board[start_pos[0]][start_pos[1]]
        if piece.islower() and self.current_player == 'white':
            return False
        if piece.isupper() and self.current_player == 'black':
            return False

        # TODO: Implement the validation logic for specific chess rules

        return True

    def is_valid_position(self, pos):
        row, col = pos
        return 0 <= row < 8 and 0 <= col < 8

    def make_move(self, start_pos, end_pos):
        piece = self.board[start_pos[0]][start_pos[1]]
        self.board[start_pos[0]][start_pos[1]] = ' '
        self.board[end_pos[0]][end_pos[1]] = piece

    def switch_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'

    def play(self):
        while not self.game_over:
            self.print_board()
            start_pos = input("Enter the start position (e.g., 'e2'): ")
            end_pos = input("Enter the end position (e.g., 'e4'): ")

            start_row, start_col = ord(start_pos[1]) - ord('1'), ord(start_pos[0]) - ord('a')
            end_row, end_col = ord(end_pos[1]) - ord('1'), ord(end_pos[0]) - ord('a')

            if not self.is_valid_move((start_row, start_col), (end_row, end_col)):
                print("Invalid move. Please try again.")
                continue

            self.make_move((start_row, start_col), (end_row, end_col))
            self.switch_player()

            # TODO: Check for checkmate and stalemate conditions


        self.print_board()
        print("Game over!")

# Start the chess game
game = ChessGame()
game.play()
