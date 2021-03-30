import arcade
import random
from dataclasses import dataclass

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

COLORS = [arcade.color.BLUE, arcade.color.PURPLE,
          arcade.color.GREEN, arcade.color.RED,
          arcade.color.YELLOW, arcade.color.ORANGE,
          arcade.color.WHITE, arcade.color.BLACK,
          arcade.color.DIM_GRAY, arcade.color.PALE_BLUE,
          arcade.color.PINK, arcade.color.BROWN]


@dataclass
class Cercle:
    centre_x: int
    centre_y: int
    rayon: int
    color: (int,  int,  int)
    speed_x: float
    speed_y: float

    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)

    def update(self):
        if self.centre_x <= 0 + self.rayon or self.centre_x >= SCREEN_WIDTH - self.rayon:
            self.speed_x *= -1
        if self.centre_y <= 0 + self.rayon or self.centre_y >= SCREEN_HEIGHT - self.rayon:
            self.speed_y *= -1
        self.centre_x += self.speed_x
        self.centre_y += self.speed_y


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice arcade #1")
        self.liste_cercles = []

    def setup(self):
        for i in range(2000):
            self.liste_cercles.append(Cercle(random.randint(0 + 50, SCREEN_WIDTH - 50), random.randint(0 + 50, SCREEN_HEIGHT - 50), random.randint(20, 50), random.choice(COLORS), random.randint(-5, 5), random.randint(-5, 5)))

    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        for cercle in self.liste_cercles:
            cercle.update()

def main():
    epileptic_circles = MyGame()
    epileptic_circles.setup()
    arcade.run()


main()