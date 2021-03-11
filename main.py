import arcade
import random

ScreenWidth = 1920
ScreenHeight = 1080

class MakeGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_rectangle_filled(ScreenWidth/3 - 25, ScreenHeight/2 + 50, 100, 100, (arcade.color.DIM_GRAY))
        arcade.finish_render()

    def build_TicTacToe_grid(self, grid_pos_x, grid_pos_y, square_size, bar_width, grid_color):
        

def main():
    TicTacToe = MakeGame(ScreenWidth, ScreenHeight, "Test game")
    arcade.run()

main()
