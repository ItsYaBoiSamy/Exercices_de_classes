"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import arcade
import random


SCREEN_WIDTH = 1680
SCREEN_HEIGHT = 850
SCREEN_TITLE = "Projet TP1"
COLORS = [arcade.color.BLUE, arcade.color.PURPLE,
          arcade.color.GREEN, arcade.color.RED,
          arcade.color.YELLOW, arcade.color.ORANGE,
          arcade.color.WHITE, arcade.color.DIM_GRAY,
          arcade.color.PALE_BLUE, arcade.color.PINK,
          arcade.color.BROWN]

#Cette fonction génère un nombre aléatoire entre les bornes désignées, le nombre 0 est exclu des possibilitées aléatoires
def random_without_zero(num1, num2):
    random_result = 0
    while random_result == 0:
        random_result = random.randint(num1, num2)
    return random_result

#Cette classe permet la création de cercles, elle est appelée chaque fois que le joueur pèse sur le bouton gauche de la souris
class Cercle ():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rayon = random.randint(10, 30)
        self.couleur = random.choice(COLORS)
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)

    #Cette méthode gère le rendering du cercle, elle est appelée à chaque frame
    def draw_cercle (self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rayon, self.couleur)

    #Cette méthode gère les ajustements dans la position du cercle, elle est appelée à chaque frame
    def update_cercle (self):
        if self.pos_x + self.rayon >= SCREEN_WIDTH or self.pos_x - self.rayon <= 0:
            self.speed_x *= -1
        if self.pos_y + self.rayon >= SCREEN_WIDTH or self.pos_y - self.rayon <= 0:
            self.speed_y *= -1
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

#Cette classe permet la création de rectangles, elle est appelée chaque fois que le joueur pèse sur le bouton droit de la souris
class Rect ():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.largeur = random.randint(20, 60)
        self.hauteur = random.randint(20, 60)
        self.couleur = random.choice(COLORS)
        self.speed_x = random_without_zero(-3, 3)
        self.speed_y = random_without_zero(-3, 3)

    # Cette méthode gère le rendering du rectangle, elle est appelée à chaque frame
    def draw_rect (self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.largeur, self.hauteur, self.couleur)

    # Cette méthode gère les ajustements dans la position du rectangle, elle est appelée à chaque frame
    def update_rect (self):
        if self.pos_x + self.largeur >= SCREEN_WIDTH or self.pos_x <= 0:
            self.speed_x *= -1
        if self.pos_y + self.hauteur >= SCREEN_HEIGHT or self.pos_y <= 0:
            self.speed_y *= -1
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

class MyGame(arcade.Window):
    """
    La classe principale de l'application

    NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    #Cette méthode initialise les listes de cercles et de rectangles, elle est appelée une fois quand le jeu est débuté
    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        self.liste_cercles = []
        self.liste_rectangles = []
        self.rapid_fire = False

    #Cette méthode s'occupe du rendering
    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw_cercle()

        for rect in self.liste_rectangles:
            rect.draw_rect()

    #Cette méthode s'occupe des ajustements de position des formes, elle est appelée à chaque frame
    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        for cercle in self.liste_cercles:
            cercle.update_cercle()

        for rect in self.liste_rectangles:
            rect.update_rect()

    #Cette méthode crée une forme dépendemment du bonton de la souris pesé, le bouton droit crée un cercle tandis que le bouton gauche crée un rectangle
    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager clique un bouton de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été cliqué
            - button: le bouton de la souris appuyé
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.liste_cercles.append(Cercle(x, y))
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.liste_rectangles.append(Rect(x, y))


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()