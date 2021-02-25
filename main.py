import arcade
import random

ScreenWidth = 500
ScreenHeight = 500

#color 0: green
#color 1: blue
#color 2: cyan
#color 3: yellow
#color 4: red
#color 5: purple
#color 6: white
#color 7: gray
#color 8: pink
#color 9: brown
#color 10: orange
#color 11:
#color 12:
#color 13:
#color 14:
#color 15:
#color 16:
#color 17:
#color 18:
#color 19:

colors = [arcade.color. ]

class MakeGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(10, 10, 10, (0, 235, 247))

def main():
    Test_game = MakeGame(ScreenWidth, ScreenHeight, "Test game")
    arcade.run()

main()
