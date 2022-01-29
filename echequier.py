from turtle import position
from piece import Piece
from position import Position

class Echequier:
    def __init__(self):
        self.n_lignes = 8
        self.n_colonnes = 8

        self.cases = {
            Position(7,7):Piece("blanc","Tour"),
            Position(6,7):Piece("blanc","pion"),
            Position(7,6):Piece("blanc","cavalier"),
            Position(6,6):Piece("blanc","pion"),
            Position(7,5):Piece("blanc","fou"),
            Position(6,5):Piece("blanc","pion"),
            Position(7,3):Piece("blanc","Dame"),
            Position(6,4):Piece("blanc","pion"),
            Position(7,4):Piece("blanc","roi"),
            Position(6,3):Piece("blanc","pion"),
            Position(7,2):Piece("blanc","fou"),
            Position(6,2):Piece("blanc","pion"),
            Position(7,1):Piece("blanc","cavalier"),
            Position(6,1):Piece("blanc","pion"),
            Position(7,0):Piece("blanc","Tour"),
            Position(6,0):Piece("blanc","pion"),
            Position(1,7):Piece("noir","pion"),
            Position(0,7):Piece("noir","Tour"),
            Position(1,6):Piece("noir","pion"),
            Position(0,6):Piece("noir","cavalier"),
            Position(1,5):Piece("noir","pion"),
            Position(0,5):Piece("noir","fou"),
            Position(1,4):Piece("noir","pion"),
            Position(0,4):Piece("noir","Dame"),
            Position(1,3):Piece("noir","pion"),
            Position(0,3):Piece("noir","roi"),
            Position(1,2):Piece("noir","pion"),
            Position(0,2):Piece("noir","fou"),
            Position(1,1):Piece("noir","pion"),
            Position(0,1):Piece("noir","cavalier"),
            Position(1,0):Piece("noir","pion"),
            Position(0,0):Piece("noir","Tour")
        }
    def recuperer_piece_a_position(self, position):
    
        if position not in self.cases:
            return None

        return self.cases[position]
    def position_est_dans_echequier(self,position):
        
        return 0 <= position.ligne < self.n_lignes and 0 <= position.colonne < self.n_colonnes
    def piece_entre_source_cible(self,position_source,position_cible):
        positions = []
        if position_source.colonne == position_cible.colonne:
            nbrLigne = abs(position_cible.ligne - position_source.ligne)
            for i in range(nbrLigne):
                if position_source.ligne > position_cible.ligne:
                    positions.append(Position(position_cible.colonne,position_cible.ligne + i))
                else:
                    positions.append(Position(position_cible.colonne,position_cible.ligne - i))
        elif position_source.ligne == position_cible.ligne:
            nbrColonne = abs(position_cible.colonne - position_source.colonne)
            for i in range(len(nbrColonne)):
                if position_source.colonne > position_cible.colonne:
                    positions.append(Position(position_cible.colonne + i,position_cible.ligne)) 
                else:
                     positions.append(Position(position_cible.colonne - i,position_cible.ligne)) 
        else:
            if (position_cible.ligne - position_source.ligne > 0) and (position_cible.colonne -position_source.colonne > 0):
                nbrLigne = abs(position_cible.ligne - position_source.ligne)
                for i in range(nbrLigne):
                    positions.append(Position(position_cible.colonne - i,position_cible.ligne - i))
            elif (position_cible.ligne - position_source.ligne < 0) and (position_cible.colonne -position_source.colonne < 0):
                nbrLigne = abs(position_cible.ligne - position_source.ligne)
                for i in range(nbrLigne):
                    positions.append(Position(position_cible.colonne + i,position_cible.ligne + i))
            elif (position_cible.ligne - position_source.ligne < 0) and (position_cible.colonne -position_source.colonne > 0):
                nbrLigne = abs(position_cible.ligne - position_source.ligne)
                for i in range(nbrLigne):
                    positions.append(Position(position_cible.colonne - i,position_cible.ligne - i))
            else:
                nbrLigne = abs(position_cible.ligne - position_source.ligne)
                for i in range(nbrLigne):
                    positions.append(Position(position_cible.colonne - i,position_cible.ligne + i))
        return positions

    def piece_peut_se_deplacer_vers(self,position_source,position_cible):
        if(not self.position_est_dans_echequier(position_source)) or (not self.position_est_dans_echequier(position_cible)):
            return False
        
        # a changer pour gerer les prises de piece(piece_cible peut etre None si tu veux prendre)
       
        piece_source = self.recuperer_piece_a_position(position_source)
        piece_cible = self.recuperer_piece_a_position(position_cible)
        positions = []
        if not piece_source.est_cavalier():
            positions = self.piece_entre_source_cible(position_source,position_cible)
       
        if piece_source is None or piece_cible is not None:
            return False
        if piece_source.est_pion() and  piece_source.est_blanche() and (position_cible in position_source.avancement_pion_blanc() or position_cible in position_source.avancement_pion_premier_blanc()):
            return True
        if piece_source.est_pion() and  piece_source.est_noire() and (position_cible in position_source.avancement_pion_noir() or position_cible in position_source.avancement_pion_premier_noir()):
            return True
        if (piece_source.est_cavalier()) and (position_cible in position_source.deplacement_cavalier()):
            return True
        if (piece_source.est_fou() and position_cible in position_source.positions_diagonales()):
            return True
        if piece_source.est_tour() and (position_cible in position_source.avancement() or position_cible in position_source.mouvement_lateral()):
            return True
        if piece_source.est_dame() and (position_cible in position_source.positions_diagonales()\
        or position_cible in position_source.avancement() or position_cible in position_source.mouvement_lateral()):
            return True
        if piece_source.est_roi() and (position_cible in position_source.deplacement_roi()):
            return True
        
        return False
    def deplacer(self,position_source,position_cible):
        if self.piece_peut_se_deplacer_vers(position_source,position_cible):
            resultat = 'ok'
            piece = self.recuperer_piece_a_position(position_source)
            self.cases[position_cible] = piece
            del self.cases[position_source]
        else:
            return 'erreur'
        
        return resultat