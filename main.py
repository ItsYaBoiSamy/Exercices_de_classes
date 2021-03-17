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
    rayon: int
    centre_x: int
    centre_y: int
    color: (int,  int,  int)

    def draw(self):
        pass


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice arcade #1")
        self.liste_cercles = []

    def setup(self):
        for i in range(20):
            rayon = random.randint(10, 20)
            centre_x = random.randint(0 + 20, SCREEN_WIDTH - 20)
            centre_y = random.randint(0 + 20, SCREEN_HEIGHT - 20)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.liste_cercles.append(Cercle(rayon, centre_x, centre_y, color))

    def on_draw(self):
        arcade.start_render()
        for i in self.liste_cercles:
            arcade.draw_circle_filled(self.liste_cercles[i].centre_x,
            self.liste_cercles[i].centre_y, self.liste_cercles[i].rayon,
            self.liste_cercles[i].color)


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()