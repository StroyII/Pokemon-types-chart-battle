class Joueur():
    def __init__(self,nom="Joueur"):
        self.nom = nom
        self.score = 0

    def augmenter_score(self):
        self.score += 1