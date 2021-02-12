import random
from dataclasses import dataclass
from enum import Enum

def quantite_stats():
    nums = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    nums.sort()
    return nums[1] + nums[2] + nums[3]

class NPC:
    def __init__(self):
        self.Force = quantite_stats()
        self.Agilité = quantite_stats()
        self.Constitution = quantite_stats()
        self.Intelligence = quantite_stats()
        self.Sagesse = quantite_stats()
        self.Charisme = quantite_stats()
        self.Classe_armure = random.randint(1, 12)
        self.nom = ""
        self.race = ""
        self.espece = ""
        self.pv = random.randint(1, 20)
        self.profession = ""
        self.alignement = 0

    @staticmethod
    def attaquer(cible):
        attack_num = random.randint(1, 20)
        if attack_num > cible.Classe_armure:
            if attack_num == 20:
                cible.subir_dommage(random.randint(1, 8))
            cible.subir_dommage(1, 6)

    def verify_alive(self):
        if self.pv <= 0:
            return False
        else:
            return True


    def afficher_caracteristiques(self):
        print(f"Force: {self.Force}\n"
              f"Agilité: {self.Agilité}\n"
              f"Constitution: {self.Constitution}\n"
              f"Intelligence: {self.Intelligence}\n"
              f"Sagesse: {self.Sagesse}\n"
              f"Charisme: {self.Charisme}\n"
              f"Classe_armure: {self.Classe_armure}\n"
              f"nom: {self.nom}\n"
              f"race: {self.race}\n"
              f"espece: {self.espece}\n"
              f"pv: {self.pv}\n"
              f"profession: {self.profession}\n")


class Kobold(NPC):
    def __init__(self):
        super().__init__()
        self.race = "kobold"
        self.espece = "humanoïde"

    def subir_dommage(self, dommage):
        self.pv -= dommage

class Hero(NPC):
    def __init__(self):
        super().__init__()
        self.race = "Héros"
        self.espece = "humanoïde"

    def subir_dommage(self, dommage):
        self.pv -= dommage

@dataclass
class item:
    quantite: int
    nom: str


class backpack:
    def __init__(self):
        self.items = []

    def ajouter_item(self, nom):
        pass

class alignement(Enum):
    undefined = 0
    Lawful_good = 1
    Lawful_neutral = 2
    Lawful_evil = 3
    Neutral_good = 4
    True_neutral = 5
    Neutral_evil = 6
    Chaotic_good = 7
    Chaotic_neutral = 8
    Chaotic_evil = 9

k = Kobold()
hampter = Hero()
k.attaquer(hampter)
hampter.afficher_caracteristiques()
