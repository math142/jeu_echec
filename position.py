from selectors import EpollSelector


class Position:
    def __init__(self,ligne,colonne):
        self.ligne = int(ligne)
        self.colonne = int(colonne)
    
    
    def __eq__(self, other):
        """Méthode spéciale indiquant à Python comment vérifier si deux positions sont égales. On compare simplement
        la ligne et la colonne de l'objet actuel et de l'autre objet.

        """
        return self.ligne == other.ligne and self.colonne == other.colonne
    def positions_diagonales(self):
        return [Position(self.ligne + 1,self.colonne + 1),Position(self.ligne + 2,self.colonne + 2),Position(self.ligne + 3,self.colonne + 3),Position(self.ligne + 4,self.colonne + 4),
        Position(self.ligne + 5,self.colonne + 5),Position(self.ligne + 6,self.colonne + 6),Position(self.ligne + 7,self.colonne + 7),Position(self.ligne - 1,self.colonne - 1),Position(self.ligne - 1,self.colonne + 1),
        Position(self.ligne +1,self.colonne - 1 ),Position(self.ligne - 2,self.colonne + 2),Position(self.ligne + 2,self.colonne - 2),Position(self.ligne - 2,self.colonne - 2),Position(self.ligne -3,self.colonne - 3),
        Position(self.ligne + 3,self.colonne - 3),Position(self.ligne - 3,self.colonne + 3),Position(self.ligne - 4,self.colonne -4),Position(self.ligne + 4,self.colonne - 4),Position(self.ligne - 4,self.colonne + 4),
        Position(self.ligne - 5,self.colonne - 5),Position(self.ligne + 5,self.colonne - 5),Position(self.ligne - 5,self.colonne + 5),Position(self.ligne - 6,self.colonne - 6),Position(self.ligne + 6,self.colonne -6),
        Position(self.ligne - 6,self.colonne + 6),Position(self.ligne - 7,self.colonne - 7),Position(self.ligne + 7,self.colonne -7),Position(self.ligne -7,self.colonne + 7)]
    def avancement_pion_blanc(self):
        return [Position(self.ligne - 1,self.colonne + 0)]
    def avancement_pion_premier_blanc(self):
        return [Position(self.ligne - 2,self.colonne + 0)]
    def avancement_pion_noir(self):
        return [Position(self.ligne + 1,self.colonne + 0)]
    def avancement_pion_premier_noir(self):
        return [Position(self.ligne + 2,self.colonne + 0)]
    def prise_pion_blanc(self):
        return [Position(self.ligne - 1,self.colonne - 1),Position(self.ligne - 1,self.colonne + 1)]
    def prise_pion_noir(self):
        return [Position(self.ligne + 1,self.colonne - 1),Position(self.ligne +1,self.colonne +1)]
    def avancement(self):
         return [Position(self.ligne + 1,self.colonne + 0),Position(self.ligne + 2,self.colonne + 0),Position(self.ligne + 3,self.colonne + 0),Position(self.ligne + 4,self.colonne + 0),Position(self.ligne + 5,self.colonne + 0),
         Position(self.ligne + 6,self.colonne + 0),Position(self.ligne + 7,self.colonne + 0),Position(self.ligne - 1,self.colonne + 0),Position(self.ligne - 2,self.colonne + 0),Position(self.ligne -3,self.colonne + 0),
         Position(self.ligne - 4,self.colonne + 0),Position(self.ligne - 5,self.colonne + 0),Position(self.ligne - 6,self.colonne + 0),Position(self.ligne - 7,self.colonne + 0)]
    def mouvement_lateral(self):
        return [Position(self.ligne + 0,self.colonne + 1),Position(self.ligne + 0,self.colonne + 2),Position(self.ligne + 0,self.colonne + 3),Position(self.ligne + 0,self.colonne + 4),Position(self.ligne + 0,self.colonne + 5),
         Position(self.ligne + 0,self.colonne + 6),Position(self.ligne + 0,self.colonne + 7),Position(self.ligne - 0,self.colonne - 1),Position(self.ligne - 0,self.colonne - 2),Position(self.ligne - 0,self.colonne - 3),
         Position(self.ligne - 0,self.colonne -4),Position(self.ligne - 0,self.colonne - 5),Position(self.ligne - 0,self.colonne -6),Position(self.ligne - 0,self.colonne - 7)]
    def deplacement_roi(self):
        return [Position(self.ligne + 0,self.colonne + 1),Position(self.ligne +1,self.colonne - 1 ),Position(self.ligne + 1,self.colonne + 0),Position(self.ligne - 1,self.colonne - 1),Position(self.ligne + 1,self.colonne + 1),
        Position(self.ligne + 0,self.colonne - 1),Position(self.ligne -1,self.colonne + 0)]
    def deplacement_cavalier(self):
        return [Position(self.ligne + 2,self.colonne + 1),Position(self.ligne +2,self.colonne - 1 ),Position(self.ligne -2,self.colonne + 1),Position(self.ligne - 2,self.colonne - 1),Position(self.ligne -2,self.colonne + 1),
        Position(self.ligne + 1,self.colonne + 2),Position(self.ligne +1,self.colonne - 2 ),Position(self.ligne -1,self.colonne + 2),Position(self.ligne -1,self.colonne - 2 )]
    def grand_roque_blanc(self):
        return [Position(self.ligne,self.colonne - 2)]
    def grand_roque_noir(self):
        return [Position(self.ligne,self.colonne - 2)]
    def petit_roque_blanc(self):
        return [Position(self.ligne,self.colonne + 2)]
    def petit_roque_noir(self):
        return [Position(self.ligne,self.colonne + 2)]
    def conversion(self,pos):
        colonne = ['a','b','c','d','e','f','g','h']
        ligne = [8,7,6,5,4,3,2,1]
        for i in range(len(ligne)):
            lettre = ligne[pos.ligne]
            number = colonne[pos.colonne]
        algebrique = number + str(lettre)
        return algebrique
    def lettre_piece(self,type_piece):
        if type_piece == 'Dame':
            letter = 'D'
        elif type_piece == 'roi':
            letter = 'R'
        elif type_piece == 'Tour':
            letter = 'T'
        elif type_piece == 'fou':
            letter = 'C'
        elif type_piece == 'cavalier':
            letter = 'C'
        else:
            letter = ''
        return letter
    def conversion_en_algebrique(self,position_source,position_cible,type_piece_source,type_piece_cible,resultat,est_en_echec):
        
        letter_source = self.lettre_piece(type_piece_source)
        letter_cible = self.lettre_piece(type_piece_cible)
        if resultat == 'prise':
            raw_pos_source =  self.conversion(position_source)
            raw_pos_cible = self.conversion(position_cible)
            position_algebrique = letter_source + raw_pos_source + 'X' + letter_cible + raw_pos_cible
        elif est_en_echec == True:
            raw_pos_cible = self.conversion(position_cible)
            position_algebrique = letter_source + raw_pos_cible + '+'
        else:

            raw_pos_cible = self.conversion(position_cible)
            position_algebrique = letter_source + raw_pos_cible
        return position_algebrique
    def __repr__(self):
        """Méthode spéciale indiquant à Python comment représenter une instance de Position par une chaîne de
        caractères. Notamment utilisé pour imprimer une position à l'écran.

        """
        return '({}, {})'.format(self.ligne, self.colonne)

    def __hash__(self):
        
        return hash(str(self))

