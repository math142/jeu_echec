from matplotlib.pyplot import pie
from piece import Piece
from position import Position

class Echequier:
    def __init__(self):
        self.n_lignes = 8
        self.n_colonnes = 8
        self.twice = False
        self.echec = True
        self.joueur_est_en_echec = False
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
            Position(0,4):Piece("noir","roi"),
            Position(1,3):Piece("noir","pion"),
            Position(0,3):Piece("noir","Dame"),
            Position(1,2):Piece("noir","pion"),
            Position(0,2):Piece("noir","fou"),
            Position(1,1):Piece("noir","pion"),
            Position(0,1):Piece("noir","cavalier"),
            Position(1,0):Piece("noir","pion"),
            Position(0,0):Piece("noir","Tour")
        }
        self.piece_non_bougee = {
            Position(7,7):Piece("blanc","Tour"),
            Position(6,7):Piece("blanc","pion"),
            Position(6,6):Piece("blanc","pion"),
            Position(6,5):Piece("blanc","pion"),
            Position(6,4):Piece("blanc","pion"),
            Position(7,4):Piece("blanc","roi"),
            Position(6,3):Piece("blanc","pion"),
            Position(6,2):Piece("blanc","pion"),
            Position(7,0):Piece("blanc","Tour"),
            Position(6,0):Piece("blanc","pion"),
            Position(1,7):Piece("noir","pion"),
            Position(0,7):Piece("noir","Tour"),
            Position(1,6):Piece("noir","pion"),
            Position(1,5):Piece("noir","pion"),
            Position(1,4):Piece("noir","pion"),
            Position(0,4):Piece("noir","roi"),
            Position(1,3):Piece("noir","pion"),
            Position(1,2):Piece("noir","pion"),
            Position(1,1):Piece("noir","pion"),
            Position(1,1):Piece("noir","pion"),
            Position(1,0):Piece("noir","pion")
        }
    def recuperer_piece_a_position(self, position):
    
        if position not in self.cases:
            return None

        return self.cases[position]
    def position_est_dans_echequier(self,position):
        
        return 0 <= position.ligne < self.n_lignes and 0 <= position.colonne < self.n_colonnes
    def piece_entre_source_cible(self,position_source,position_cible):
        positions = []
        if position_cible.colonne == position_source.colonne:
            nbrLigne = abs(position_cible.ligne - position_source.ligne)
            for i in range(1,nbrLigne):
                if position_source.ligne > position_cible.ligne:
                   
                    positions.append(Position(position_source.ligne - i,position_source.colonne))
                else:
                    positions.append(Position(position_source.ligne + i,position_cible.colonne))
        elif position_cible.ligne == position_source.ligne:
            nbrColonne = abs(position_cible.colonne - position_source.colonne)
            for i in range(1,nbrColonne):
                if position_source.colonne > position_cible.colonne:
                    positions.append(Position(position_source.ligne,position_source.colonne - i)) 
                else:
                     positions.append(Position(position_source.ligne,position_source.colonne + i)) 
        else:
            if (position_cible.ligne - position_source.ligne > 0) and (position_cible.colonne -position_source.colonne > 0):
                nbrLigne = abs(position_cible.ligne - position_source.ligne)
                for i in range(1,nbrLigne):
                    positions.append(Position(position_source.ligne + i,position_source.colonne + i))
            elif (position_cible.ligne - position_source.ligne < 0) and (position_cible.colonne -position_source.colonne < 0):
                nbrLigne = abs(position_cible.ligne - position_source.ligne)
                for i in range(1,nbrLigne):
                    positions.append(Position(position_source.ligne - i,position_source.colonne - i))
            elif (position_cible.ligne - position_source.ligne < 0) and (position_cible.colonne -position_source.colonne > 0):
                nbrLigne = abs(position_cible.ligne - position_source.ligne)
                for i in range(1,nbrLigne):
                    positions.append(Position(position_source.ligne - i,position_source.colonne + i))
            else:
                nbrLigne = abs(position_cible.ligne - position_source.ligne)
                for i in range(1,nbrLigne):
                    positions.append(Position(position_source.ligne + i,position_source.colonne - i))
        return positions
    def piece_a_position(self,positions_dict,position_cible):
        for i in range(len(positions_dict)):
            for key in self.cases:
                if positions_dict[i] == key and key != position_cible:
                    return False
        return True

    def piece_peut_se_deplacer_vers(self,position_source,position_cible):
        if(not self.position_est_dans_echequier(position_source)) or (not self.position_est_dans_echequier(position_cible)):
            return False
        
        # a changer pour gerer les prises de piece(piece_cible peut etre None si tu veux prendre)
       
        piece_source = self.recuperer_piece_a_position(position_source)
        piece_cible = self.recuperer_piece_a_position(position_cible)
        positions = []
        if not piece_source.est_cavalier():
            positions = self.piece_entre_source_cible(position_source,position_cible)
        
        if self.deplacement_autorise(position_source,position_cible):
            return True

        return False
    def deplacer(self,position_source,position_cible):
        piece_source = self.recuperer_piece_a_position(position_source)
        piece_cible = self.recuperer_piece_a_position(position_cible)
        if (position_cible in self.cases):
            if (piece_cible.couleur != piece_source.couleur):
                resultat = 'prise'
                piece = self.recuperer_piece_a_position(position_source)
                self.cases[position_cible] = piece
                if position_source in self.piece_non_bougee:
                    
                    del self.piece_non_bougee[position_source]
                del self.cases[position_source]
                return resultat
            else:
                return 'erreur'
        elif self.piece_peut_se_deplacer_vers(position_source,position_cible):
            resultat = 'ok'
            if position_source in self.piece_non_bougee:
                
                del self.piece_non_bougee[position_source]
            piece = self.recuperer_piece_a_position(position_source)
            self.cases[position_cible] = piece
            del self.cases[position_source]
            if piece.est_pion() and (piece.couleur == 'blanc' and position_cible.ligne == 0 or piece.couleur == 'noir' and position_cible.ligne == 7):
                return 'Last'
        else:
            return 'erreur'
        return resultat
    def deplacement_autorise(self,position_source,position_cible):
        piece_source = self.recuperer_piece_a_position(position_source)
        piece_cible = self.recuperer_piece_a_position(position_cible)
        positions = self.piece_entre_source_cible(position_source,position_cible)
        if piece_source is None:
                return False
        if piece_source.est_pion() and  piece_source.est_blanche() and self.piece_a_position(positions,position_cible):
            if position_source in self.piece_non_bougee and (position_cible in position_source.avancement_pion_premier_blanc()):
                return True
            elif position_cible in position_source.avancement_pion_blanc()\
            or (position_cible in position_source.prise_pion_blanc() and position_cible in self.cases and self.piece_couleur_diff(position_source,position_cible)):
                return True
        if piece_source.est_pion() and  piece_source.est_noire() and  self.piece_a_position(positions,position_cible):
            if position_source in self.piece_non_bougee and position_cible in position_source.avancement_pion_premier_noir(): 
                return True
            elif(position_cible in position_source.avancement_pion_noir() \
            or (position_cible in position_source.prise_pion_noir() and position_cible in self.cases and self.piece_couleur_diff(position_source,position_cible))):
                return True
        if (piece_source.est_cavalier()) and (position_cible in position_source.deplacement_cavalier()):
            return True
        if (piece_source.est_fou() and position_cible in position_source.positions_diagonales())  and self.piece_a_position(positions,position_cible):
            return True
        if (piece_source.est_tour()) and (position_cible in position_source.avancement() or position_cible in position_source.mouvement_lateral())  and self.piece_a_position(positions,position_cible):
            return True
        if (piece_source.est_dame()) and (position_cible in position_source.positions_diagonales()\
        or position_cible in position_source.avancement() or position_cible in position_source.mouvement_lateral()) and self.piece_a_position(positions,position_cible):
            return True
        if piece_source.est_roi() and (position_cible in position_source.deplacement_roi()) and self.piece_a_position(positions,position_cible):
            return True
        if self.peut_roquer(position_source,position_cible) and piece_source.type_piece == 'roi' and self.echec == True:
            return True
        return False
    def position_occupe(self,positions,position_tour):
        for i in range(len(positions)):
            if positions[i] in self.cases and positions[i] != position_tour:
                return False
        return True
    def positions_en_echecs(self,positions,position_tour):
        try:
            piece_tour = self.recuperer_piece_a_position(position_tour)
            for i in self.cases.keys():
                for y in range(len(positions)):
                    if self.cases[i].couleur != piece_tour.couleur and positions[y] != position_tour:
                        resultat =self.deplacer(i,positions[y])
                        if resultat == 'prise':
                            return False
        except KeyError:
            pass       
        return True
    def peut_roquer(self,position_source,position_cible):
        if self.twice == True and (position_cible.colonne == 6 or position_cible.colonne == 2):
            return True
        piece_source = self.recuperer_piece_a_position(position_source)
        if piece_source.type_piece != "roi":
            return False
        if position_source in self.piece_non_bougee:
            position_tour_blanche_g = Position(7,0)
            positions_1 = self.piece_entre_source_cible(position_source,position_tour_blanche_g)
            position_tour_noir_g = Position(0,0)
            positions_2 = self.piece_entre_source_cible(position_source,position_tour_noir_g)
            position_tour_noir_d = Position(0,7)
            positions_3 = self.piece_entre_source_cible(position_source,position_tour_noir_d)
            position_tour_blanche_d = Position(7,7)
            positions_4 = self.piece_entre_source_cible(position_source,position_tour_blanche_d)
            #Il faut s'assurer que les psitions dans la liste sont libres et ne sont pas égales à la position de la tour
            if position_cible in position_source.grand_roque_blanc() and piece_source.couleur == "blanc" and self.position_occupe(positions_1,position_tour_blanche_g)\
            and self.positions_en_echecs(positions_1,position_tour_blanche_g):
                try:
                    del self.cases[position_tour_blanche_g]
                    self.cases[Position(7,3)] = Piece("blanc","Tour")
                    return True
                except KeyError:
                    pass
            elif position_cible in position_source.grand_roque_noir()  and piece_source.couleur == "noir" and self.position_occupe(positions_2,position_tour_noir_g):
                try:
                    del self.cases[position_tour_noir_g]
                    self.cases[Position(0,3)] = Piece("noir","Tour")
                    return True
                except KeyError:
                    pass
            elif position_cible in position_source.petit_roque_blanc() and piece_source.couleur == "blanc" and self.position_occupe(positions_4,position_tour_blanche_d):
                try:
                    del self.cases[position_tour_blanche_d]
                    self.cases[Position(7,5)] = Piece("blanc","Tour")

                    return True
                except KeyError:
                    pass
            elif position_cible in position_source.petit_roque_noir()  and piece_source.couleur == "noir" and  self.position_occupe(positions_3,position_tour_noir_d):
                try:
                    del self.cases[position_tour_noir_d]
                    self.cases[Position(0,5)] = Piece("noir","Tour")
                    return True
                except KeyError:
                    pass
            return False
    def piece_couleur_diff(self,position_source,position_cible):
        piece_source = self.recuperer_piece_a_position(position_source)
        piece_cible = self.recuperer_piece_a_position(position_cible)
        if piece_source.couleur != piece_cible.couleur:
            return True
        else:
            return False
    def position_roi_joueur(self,joueur_courant):
        for item,value in self.cases.items():
            if value.couleur == joueur_courant and value.type_piece == 'roi':
                position_roi = item
        return position_roi
    def est_en_echec(self,joueur_courant,appelation,position_roi):
        if appelation == 'echec':
            position_roi = self.position_roi_joueur(joueur_courant)
        for item,value in self.cases.items():
            if value.couleur != joueur_courant and self.piece_peut_se_deplacer_vers(item,position_roi):
                pos = self.piece_entre_source_cible(item,position_roi)
                if len(pos) == 0:
                    return True
                for i in range(len(pos)):
                    
                    if pos[i] in self.cases and pos[i] != item:
                        return False
                return True
            else:
                pass
        return False
    def deplacement_roi(self,position_roi):
        return [Position(position_roi.ligne+1,position_roi.colonne),Position(position_roi.ligne-1,position_roi.colonne-1),Position(position_roi.ligne+1,position_roi.colonne+1),Position(position_roi.ligne,position_roi.colonne+1),
        Position(position_roi.ligne -1,position_roi.colonne+1),Position(position_roi.ligne -1,position_roi.colonne),Position(position_roi.ligne - 1, position_roi.colonne - 1),Position(position_roi.ligne -1,position_roi.colonne)]
    def est_echec_math(self,joueur_courant):
        #Creer une fonction qui simule avec tous les deplacements possibles du roi s'il sera en echec ou non
    
       position_roi = self.position_roi_joueur(joueur_courant)
       positions_possibles = self.deplacement_roi(position_roi)
       for i in range(len(positions_possibles)):
           if self.position_est_dans_echequier(positions_possibles[i]) == False:
               pass
           if self.piece_peut_se_deplacer_vers(position_roi,positions_possibles[i]) and (self.est_en_echec(joueur_courant,'mat',positions_possibles[i])) == False:
               return False
       return True
       
    def creation_nouvelle_piece(self,joueur_courant,piece,position_cible):
        self.cases[position_cible] = Piece(joueur_courant,piece)