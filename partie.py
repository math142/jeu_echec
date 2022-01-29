
from echequier import Echequier
from position import Position

class Partie:

    def __init__(self):
        self.echequier = Echequier()
        self.position_selectionnee = None
        self.couleur_joueur_courant = 'blanc' 
    def position_source_valide(self,position_source):
        piece_source = self.echequier.recuperer_piece_a_position(position_source)
        
        if piece_source is None:
            return False, "Position source invalide:aucune pièce à cet endroit"
        if not piece_source.couleur == self.couleur_joueur_courant:
            return False,"Position source invalide, mauvais choix de couleur"
        return True, ""
    def position_cible_valide(self,position_cible):
        if self.echequier.piece_peut_se_deplacer_vers(self.position_source_selectionnee,position_cible):
            return True,""
        return False, "Position cible invalide"
    def verification_positions_deplacement(self,position_source_clic,position_cible_clic):
        position_source = position_source_clic
        position_valide,message = self.position_source_valide(position_source)
        if not position_valide:
            print("Erreur: {}.\n".format(message))
        else:
            self.position_source_selectionnee = position_source
        
        position_cible = position_cible_clic
        position_valide, message = self.position_cible_valide(position_cible)
        if not position_valide:
            print(message + "\n")
            self.position_source_selectionnee = None
        else:
            position_valide = True
            return position_source, position_cible
    if __name__ == "__main__":

        pass