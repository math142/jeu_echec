class Piece:
    def __init__(self,couleur,type_piece):
        self.couleur = couleur
        self.type_piece = type_piece
    def est_pion(self):
        return self.type_piece == "pion"
    def est_dame(self):
        return self.type_piece == "Dame"
    def est_fou(self):
        return self.type_piece == "fou"
    def est_cavalier(self):
        return self.type_piece == "cavalier"
    def est_tour(self):
        return self.type_piece == "Tour"
    def est_roi(self):
        return self.type_piece == "roi"
    def est_blanche(self):
        return self.couleur == "blanc"
    def est_noire(self):
        return self.couleur == "noir"
    def __eq__(self, other):
        """Méthode spéciale indiquant à Python comment vérifier si deux pièces sont égales. On compare simplement
        la couleur et le type de l'objet actuel (self) et de l'autre objet (other).

        """
        return self.couleur == other.couleur and self.type_de_piece == other.type_de_piece

