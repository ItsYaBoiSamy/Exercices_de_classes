import arcade
import random
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BABY_PINK, arcade.color.FRENCH_MAUVE,
          arcade.color.JELLY_BEAN, arcade.color.PURPLE_MOUNTAIN_MAJESTY,
          arcade.color.ANTI_FLASH_WHITE]


@dataclass
class Cercle:
    centre_x: int
    centre_y: int
    rayon: int
    color: (int,  int,  int)

    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice arcade #1")
        self.liste_cercles = []

    def setup(self):
        for i in range(20):
            self.liste_cercles.append(Cercle(random.randint(0 + 50, SCREEN_WIDTH - 50), random.randint(0 + 50, SCREEN_HEIGHT - 50), random.randint(20, 50), random.choice(COLORS)))

    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()
        arcade.finish_render()


def main():
    epileptic_circles = MyGame()
    epileptic_circles.setup()
    arcade.run()


main()