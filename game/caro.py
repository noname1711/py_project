import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("4x4 Tic Tac Toe")
        self.window.resizable(0, 0)
        self.board = [['' for _ in range(4)] for _ in range(4)]
        self.player_turn = 'X'

        self.buttons = [[tk.Button(self.window, text='', command=lambda row=i, col=j: self.click(row, col), height=2, width=5, 
                                   font=('Helvetica', '20'), bg='white') for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, row, col):
        if self.board[row][col] == '' and self.check_winner() is None:
            self.board[row][col] = self.player_turn
            self.buttons[row][col]['text'] = self.player_turn

            if self.player_turn == 'X':
                self.buttons[row][col]['fg'] = 'red' 
            else:
                self.buttons[row][col]['fg'] = 'blue' 

            self.buttons[row][col]['disabledforeground'] = 'black'
            self.buttons[row][col]['bg'] = 'lightgrey'
            self.player_turn = 'O' if self.player_turn == 'X' else 'X'

        winner = self.check_winner()
        if winner is not None:
            messagebox.showinfo("Game Over", f"'{winner}' has won!")
            self.window.destroy()

    def check_winner(self):
        for i in range(4):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] != '':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.board[3][i] != '':
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] != '':
            return self.board[0][0]
        if self.board[0][3] == self.board[1][2] == self.board[2][1] == self.board[3][0] != '':
            return self.board[0][3]

        if '' not in self.board[0] and '' not in self.board[1] and '' not in self.board[2] and '' not in self.board[3]:
            return 'No one'

        return None

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()