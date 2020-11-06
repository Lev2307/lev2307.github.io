from tkinter import *
#TODO: change import method, to fropm tkinter import module

# Constants
CANVAS_SIZE = 600
FIGURE_SIZE = CANVAS_SIZE / 3
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'white'
EMPTY = NONE

# players setup
X = 'player 1'
O = 'player 2'
FIRST_PLAYER = X

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    def build_grid(self):
        x = CANVAS_SIZE // RATIO
        y1 = 0
        y2 = CANVAS_SIZE
        for _ in range(2):
            self.canvas.create_line(x, y1, x, y2)
            self.canvas.create_line(y1, x, y2, x)
            x += CANVAS_SIZE // RATIO

    def render_cross(self, posX, posY):
        f_size = self.figure_size
        self.canvas.create_line(posX, posY, posX + f_size, posY + f_size, fill='red', width=5)
        self.canvas.create_line(posX, posY + f_size, posX + f_size, posY,  fill='red', width=5)

    def render_circle(self, posX, posY):
        """Magic number: 5, its a gap between edges and figure 
        Render 0 on field"""
        f_size = self.figure_size - 5
        self.canvas.create_oval(posX + 5, posY + 5, posX + f_size, posY + f_size, outline='blue', width=5)

    def winner(self, player=None):
        """Display end game text, depends on player attribute
        and shutdown the game"""
        center = CANVAS_SIZE // 2
        if player:
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center, center, text=text, fill='lightseagreen', font='Arial 50')
        self.canvas.unbind('<Button-1>')

    def click_event(self, event):
        """Get coordinates of the click, and proccess player/al move"""
        #player move
        x_coord = int(event.x // FIGURE_SIZE)
        y_coord = int(event.y // FIGURE_SIZE)
        self.make_move(x_coord, y_coord)

    def make_move(self, x, y):
        position = {0: 0, 1: 200, 2: 400}
        current_player = self.current_player
        if self.board[x][y] == EMPTY:
            self.update_board(x, y)
            self.change_player()

            if current_player == X:
                self.render_cross(position[x], position[y])
            elif current_player == O:
                self.render_circle(position[x], position[y])

    def update_board(self, x, y):
        current_player = self.current_player
        self.board[x][y] = current_player
        if self.check_win(self.board, current_player):
            self.winner(current_player)
        if self.check_draw(self.board):
            self.winner()

    def check_win(self, board, player):
        for r in board:
            if r.count(player) == 3:
                return True
        for x in range(len(board)):
            if board[0][x] == board[1][x] == board[2][x] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
            

    def check_draw(self, board):
        for row in board:
            if EMPTY in row:
                return False
                
        return True
    def change_player(self):
        if self.current_player == X:
            self.current_player = O
        else:
            self.current_player = X

game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid()


# Testing


game_v1.mainloop()                               