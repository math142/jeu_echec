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

    def __repr__(self):
        """Méthode spéciale indiquant à Python comment représenter une instance de Position par une chaîne de
        caractères. Notamment utilisé pour imprimer une position à l'écran.

        """
        return '({}, {})'.format(self.ligne, self.colonne)

    def __hash__(self):
        """Méthode spéciale indiquant à Python comment "hasher" une Position. Cette méthode est nécessaire si on veut
        utiliser une classe que nous avons définie nous mêmes comme clé d'un dictionnaire.
        Les étudiants(es) curieux(ses) peuvent consulter wikipédia pour en savoir plus:
            https://fr.wikipedia.org/wiki/Fonction_de_hachage

        """
        return hash(str(self))

