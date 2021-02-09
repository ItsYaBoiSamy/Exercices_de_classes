import random


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

    def attaquer(self, cible):
        attack_num = random.randint(1, 20)
        if attack_num > cible.Classe_armure:
            if attack_num == 20:
                cible.subir_dommage(random.randint(1, 8))
            cible.subir_dommage(1, 6)

    def subir_dommage(self, dommage):
        self.pv -= dommage

class Hero(NPC):
    def __init__(self):
        super().__init__()
        self.race = "Héros"
        self.espece = "humanoïde"

    def attaquer(self, cible):
        attack_num = random.randint(1, 20)
        if attack_num > cible.Classe_armure:
            if attack_num == 20:
                cible.subir_dommage(random.randint(1, 8))
            cible.subir_dommage(1, 6)

    def subir_dommage(self, dommage):
        self.pv -= dommage

hampter = NPC()

k = Kobold()
hampter = Hero()
k.attaquer(hampter)
hampter.afficher_caracteristiques()

