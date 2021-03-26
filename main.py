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

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for cercle in self.liste_cercles:
            if analyseCollision(x, y, cercle.centre_x, cercle.centre_y, cercle.rayon):
                if button == arcade.MOUSE_BUTTON_LEFT:
                    self.liste_cercles.remove(cercle)
                if button == arcade.MOUSE_BUTTON_RIGHT:
                    cercle.color = random.choice(COLORS)


def analyseCollision(mouseX, mouseY, circleX, circleY, circleRadius):
    if (mouseX - circleX) ** 2 + (mouseY - circleY) ** 2 > circleRadius ** 2:
        return False
    else:
        return True

def main():
    epileptic_circles = MyGame()
    epileptic_circles.setup()
    arcade.run()


main()