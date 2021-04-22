import arcade
import math

ScreenWidth = 1680
ScreenHeight = 850
X_image = arcade.load_texture("Sprites/X.png")
O_image = arcade.load_texture("Sprites/O.png")


class TicTacToe_game:
    def __init__(self, grid_x, grid_y, square_size, grid_color):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.square_size = square_size
        self.bar_width = self.square_size / 10
        self.grid_color = grid_color
        self.bar_length = self.square_size * 3 + self.bar_width * 2
        # Predefined relative coordinates for all of the tic tac toe squares
        self.winner = "no one"
        self.assigned_square_pos = [
            (self.grid_x - self.square_size - self.bar_width, self.grid_y - self.square_size - self.bar_width),
            (self.grid_x, self.grid_y - self.square_size - self.bar_width),
            (self.grid_x + self.square_size + self.bar_width, self.grid_y - self.square_size - self.bar_width),
            (self.grid_x - self.square_size - self.bar_width, self.grid_y),
            (self.grid_x, self.grid_y),
            (self.grid_x + self.square_size + self.bar_width, self.grid_y),
            (self.grid_x - self.square_size - self.bar_width, self.grid_y + self.square_size + self.bar_width),
            (self.grid_x, self.grid_y + self.square_size + self.bar_width),
            (self.grid_x + self.square_size + self.bar_width, self.grid_y + self.square_size + self.bar_width)]
        self.square_list = []
        for coordinate in self.assigned_square_pos:
            self.square_list.append(TicTacToe_square(coordinate[0], coordinate[1], self.square_size))
        self.turn = 'X'

    def draw_grid(self):
        arcade.draw_rectangle_filled(self.grid_x, self.grid_y + (self.bar_width + self.square_size) / 2,
                                     self.bar_length, self.bar_width, self.grid_color)
        arcade.draw_rectangle_filled(self.grid_x, self.grid_y - (self.bar_width + self.square_size) / 2,
                                     self.bar_length, self.bar_width, self.grid_color)
        arcade.draw_rectangle_filled(self.grid_x + (self.bar_width + self.square_size) / 2, self.grid_y, self.bar_width,
                                     self.bar_length, self.grid_color)
        arcade.draw_rectangle_filled(self.grid_x - (self.bar_width + self.square_size) / 2, self.grid_y, self.bar_width,
                                     self.bar_length, self.grid_color)
        for square in self.square_list:
            square.draw_square()
        if self.winner == "X":
            arcade.draw_text("X WINS", self.grid_x, self.grid_y + self.bar_length / 2 + 20, arcade.color.RED, 40,
                             width=200, align="center", anchor_x="center", anchor_y="center")
        elif self.winner == "O":
            arcade.draw_text("O WINS", self.grid_x, self.grid_y + self.bar_length / 2 + 20, arcade.color.BLUE, 40,
                             width=200, align="center", anchor_x="center", anchor_y="center")
        elif self.winner == "stalemate":
            arcade.draw_text("STALEMATE", self.grid_x, self.grid_y + self.bar_length / 2 + 20, arcade.color.DIM_GRAY, 40,
                             width=300, align="center", anchor_x="center", anchor_y="center")

    def mouse_position_verification_grid(self, mouse_x, mouse_y):
        if self.winner == "no one":
            for square in self.square_list:
                square.mouse_position_verification_square(mouse_x, mouse_y)

    def mouse_click_verification_grid(self, mouseButton):
        if self.winner == "no one":
            for square in self.square_list:
                self.turn = square.mouse_click_verification_square(mouseButton, self.turn)
            if (self.square_list[0].square_state == self.square_list[1].square_state and self.square_list[
                1].square_state == self.square_list[2].square_state and self.square_list[0].square_state == 2) or (
                    self.square_list[3].square_state == self.square_list[4].square_state and self.square_list[
                4].square_state == self.square_list[5].square_state and self.square_list[3].square_state == 2) or (
                    self.square_list[6].square_state == self.square_list[7].square_state and self.square_list[
                7].square_state == self.square_list[8].square_state and self.square_list[6].square_state == 2) or (
                    self.square_list[0].square_state == self.square_list[3].square_state and self.square_list[
                3].square_state == self.square_list[6].square_state and self.square_list[0].square_state == 2) or (
                    self.square_list[1].square_state == self.square_list[4].square_state and self.square_list[
                4].square_state == self.square_list[7].square_state and self.square_list[1].square_state == 2) or (
                    self.square_list[2].square_state == self.square_list[5].square_state and self.square_list[
                5].square_state == self.square_list[8].square_state and self.square_list[2].square_state == 2) or (
                    self.square_list[0].square_state == self.square_list[4].square_state and self.square_list[
                4].square_state == self.square_list[8].square_state and self.square_list[0].square_state == 2) or (
                    self.square_list[2].square_state == self.square_list[4].square_state and self.square_list[
                4].square_state == self.square_list[6].square_state and self.square_list[2].square_state == 2):
                self.winner = "X"

            elif (self.square_list[0].square_state == self.square_list[1].square_state and self.square_list[
                1].square_state == self.square_list[2].square_state and self.square_list[0].square_state == 3) or (
                    self.square_list[3].square_state == self.square_list[4].square_state and self.square_list[
                4].square_state == self.square_list[5].square_state and self.square_list[3].square_state == 3) or (
                    self.square_list[6].square_state == self.square_list[7].square_state and self.square_list[
                7].square_state == self.square_list[8].square_state and self.square_list[6].square_state == 3) or (
                    self.square_list[0].square_state == self.square_list[3].square_state and self.square_list[
                3].square_state == self.square_list[6].square_state and self.square_list[0].square_state == 3) or (
                    self.square_list[1].square_state == self.square_list[4].square_state and self.square_list[
                4].square_state == self.square_list[7].square_state and self.square_list[1].square_state == 3) or (
                    self.square_list[2].square_state == self.square_list[5].square_state and self.square_list[
                5].square_state == self.square_list[8].square_state and self.square_list[2].square_state == 3) or (
                    self.square_list[0].square_state == self.square_list[4].square_state and self.square_list[
                4].square_state == self.square_list[8].square_state and self.square_list[0].square_state == 3) or (
                    self.square_list[2].square_state == self.square_list[4].square_state and self.square_list[
                4].square_state == self.square_list[6].square_state and self.square_list[2].square_state == 3):
                self.winner = "O"

            elif (self.square_list[0].square_state == 2 or self.square_list[0].square_state == 3) and (
                    self.square_list[1].square_state == 2 or self.square_list[1].square_state == 3) and (
                    self.square_list[2].square_state == 2 or self.square_list[2].square_state == 3) and (
                    self.square_list[3].square_state == 2 or self.square_list[3].square_state == 3) and (
                    self.square_list[4].square_state == 2 or self.square_list[4].square_state == 3) and (
                    self.square_list[5].square_state == 2 or self.square_list[5].square_state == 3) and (
                    self.square_list[6].square_state == 2 or self.square_list[6].square_state == 3) and (
                    self.square_list[7].square_state == 2 or self.square_list[7].square_state == 3) and (
                    self.square_list[8].square_state == 2 or self.square_list[8].square_state == 3):
                self.winner = "stalemate"


class TicTacToe_square:
    def __init__(self, square_x, square_y, square_size):
        # State 0 is neutral, nothing is happening in that situation
        # State 1 is the state where the mouse is hovering over the square, the square is a light shade of gray
        # State 2 is X
        # State 3 is O
        self.square_size = square_size
        self.square_state = 0
        self.square_x = square_x
        self.square_y = square_y

    def mouse_position_verification_square(self, mouse_x, mouse_y):
        if -1 * self.square_size / 2 < mouse_x - self.square_x < self.square_size / 2 \
                and -1 * self.square_size / 2 < mouse_y - self.square_y < self.square_size / 2 \
                and (self.square_state == 0 or self.square_state == 1):
            self.square_state = 1
        elif self.square_state == 1:
            self.square_state = 0

    def mouse_click_verification_square(self, mouseButton, turn):
        if self.square_state == 1 and mouseButton == arcade.MOUSE_BUTTON_LEFT:
            if turn == 'X':
                self.square_state = 2
                return 'O'
            else:
                self.square_state = 3
                return 'X'
        else:
            return turn

    def draw_square(self):
        if self.square_state == 1:
            arcade.draw_rectangle_filled(self.square_x, self.square_y, self.square_size, self.square_size,
                                         arcade.color.GAINSBORO)
        elif self.square_state == 2:
            arcade.draw_texture_rectangle(self.square_x, self.square_y, self.square_size - 30, self.square_size - 30,
                                          X_image)
        elif self.square_state == 3:
            arcade.draw_texture_rectangle(self.square_x, self.square_y, self.square_size - 30, self.square_size - 30,
                                          O_image)


class MakeGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.grid_list = []

    def setup(self):
        self.grid_list.append(TicTacToe_game(ScreenWidth / 4, ScreenHeight / 4, 100, arcade.color.BLACK))
        self.grid_list.append(TicTacToe_game(ScreenWidth / 2, ScreenHeight / 4, 100, arcade.color.BLACK))
        self.grid_list.append(TicTacToe_game(ScreenWidth * 3 / 4, ScreenHeight / 4, 100, arcade.color.BLACK))
        self.grid_list.append(TicTacToe_game(ScreenWidth / 4, ScreenHeight * 3 / 4, 100, arcade.color.BLACK))
        self.grid_list.append(TicTacToe_game(ScreenWidth / 2, ScreenHeight * 3 / 4, 100, arcade.color.BLACK))
        self.grid_list.append(TicTacToe_game(ScreenWidth * 3 / 4, ScreenHeight * 3 / 4, 100, arcade.color.BLACK))

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        for grid in self.grid_list:
            grid.draw_grid()
        arcade.finish_render()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for grid in self.grid_list:
            grid.mouse_position_verification_grid(x, y)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        for grid in self.grid_list:
            grid.mouse_click_verification_grid(button)


def main():
    TicTacToe = MakeGame(ScreenWidth, ScreenHeight, "Tic Tac Toe")
    TicTacToe.setup()
    arcade.run()


main()
