from tkinter import Tk,Canvas
from turtle import width
from position import Position

class CanvasEchequier(Canvas):

    def __init__(self,parent,echequier,n_pixels_par_case=60):
        self.echequier = echequier
        self.couleur = '#FFFFFF'
        self.n_pixels_par_case = n_pixels_par_case

        largeur = self.echequier.n_lignes * n_pixels_par_case
        hauteur = self.echequier.n_colonnes * n_pixels_par_case

        super().__init__(parent,width=largeur,height=hauteur)

        self.bind('<Configure>',self.redimensionner)

    def dessiner_cases(self,couleur):
        
        for i in range(self.echequier.n_lignes):
            for j in range(self.echequier.n_colonnes):
                debut_ligne = i * self.n_pixels_par_case 
                fin_ligne = debut_ligne + self.n_pixels_par_case
                debut_colonne = j * self.n_pixels_par_case
                fin_colonne = debut_colonne + self.n_pixels_par_case

                # On détermine la couleur.
                if (i + j) % 2 == 0:
                    self.couleur = couleur
                else:
                    self.couleur = '#006400'

                # On dessine le rectangle. On utilise l'attribut "tags" pour être en mesure de récupérer les éléments
                # par la suite.
                self.create_rectangle(debut_colonne, debut_ligne, fin_colonne, fin_ligne, fill=self.couleur, tags='case')
    def dessiner_pieces(self):
        """Méthode qui dessine les pièces sur le canvas"""

        # Pour tout paire position, pièce:
        for position, piece in self.echequier.cases.items():
          
            # On dessine la pièce dans le canvas, au centre de la case. On utilise l'attribut "tags" pour être en
            # mesure de récupérer les éléments dans le canvas.
            quotient_x = 30
            quotient_y = 30
            coordonnee_y = (position.ligne * self.n_pixels_par_case + self.n_pixels_par_case) - quotient_y
            coordonnee_x = (position.colonne * self.n_pixels_par_case ) + quotient_x

            # On utilise des caractères unicodes représentant des pièces
            if piece.est_blanche() and piece.est_pion():
                icone = "♙"
            elif piece.est_blanche() and piece.est_dame():
                icone = "♕"
            elif piece.est_fou() and piece.est_blanche():
                icone = "♗"
            elif piece.est_blanche() and piece.est_cavalier():
                icone = "♘"
            elif piece.est_roi() and piece.est_blanche():
                icone = "♔"
            elif piece.est_tour() and piece.est_blanche():
                icone = "♖"
            elif piece.est_noire() and piece.est_pion():
                icone = "♟"
            elif piece.est_noire() and piece.est_cavalier():
                icone = "♞"
            elif piece.est_noire() and piece.est_fou():
                icone = "♝"
            elif piece.est_noire() and piece.est_tour():
                icone = "♜"
            elif piece.est_noire() and piece.est_roi():
                icone = "♚"
            elif piece.est_noire() and piece.est_dame():
                icone =  "♛"
            
         
            

            police_de_caractere = ('Deja Vu', self.n_pixels_par_case//2)
            self.create_text(coordonnee_x, coordonnee_y, text=icone, font=police_de_caractere, tags='piece')
    def redimensionner(self, event):
        """Méthode qui est est appellé automatiquement lorsque le canvas est redimensionné.

        Args:
            event (tkinter.Event): Objet décrivant l'évènement qui a causé l'appel de la méthode.

        """
        # Nous recevons dans le "event" la nouvelle dimension dans les attributs width et height. On veut un échequier
        # carré, alors on ne conserve que la plus petite de ces deux valeurs.
        nouvelle_taille = min(event.width, event.height)

        # Calcul de la nouvelle dimension des cases.
        self.n_pixels_par_case = nouvelle_taille // self.echequier.n_lignes

        self.actualiser()

    def actualiser(self):
        """Méthode qui redésinne le canvas (mets à jour l'affichage de l'échequier).
        """
        # On supprime les anciennes cases et on ajoute les nouvelles.
        self.delete('case')
        self.dessiner_cases(self.couleur)

        # On supprime les anciennes pièces et on ajoute les nouvelles.
        self.delete('piece')
        self.dessiner_pieces()
        