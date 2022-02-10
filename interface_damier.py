
from tkinter import Tk,Label
from canvasEchequier import CanvasEchequier
from partie import Partie
from position import Position
from piece import Piece

class FenetrePartie(Tk):
    def __init__(self):
        super().__init__()
        self.liste_position = []
        self.partie = Partie()
        self.canvasEchequier = CanvasEchequier(self,self.partie.echequier,60)
        self.canvasEchequier.grid(column=0, row=0)
        self.canvasEchequier.bind('<Button-1>',self.selectionner)
        self.couleur_joueur = self.partie.couleur_joueur_courant
        self.messages = Label(self)
        self.messages.grid()

        self.title("Jeu d'echeque")

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
    def selectionner(self, event):


    # On trouve le numéro de ligne/colonne en divisant les positions en y/x par le nombre de pixels par case.
        ligne = event.y // self.canvasEchequier.n_pixels_par_case 
        colonne = event.x // self.canvasEchequier.n_pixels_par_case 
        position = Position(ligne, colonne)
        self.liste_position.append(position)
        piece = self.partie.echequier.recuperer_piece_a_position(self.liste_position[0])
        if piece is None:
            self.messages['foreground'] = 'red'
            self.messages['text'] = 'Erreur: Aucune pièce à cet endroit.'
        elif piece is not None and len(self.liste_position) == 1:
            self.messages['foreground'] = 'black'
            self.messages['text'] = 'Pièce sélectionnée à la position {}.'.format(position)
        else:
            self.messages['foreground'] = 'black'
            self.messages['text'] = 'Déplacement effectué'

        if len(self.liste_position) == 2:
            self.tour()
            self.canvasEchequier.actualiser()
            self.liste_position = []
    def tour(self):
        try:
            position_source,position_cible = self.partie.verification_positions_deplacement(self.liste_position[0],self.liste_position[1])
            resultat_deplacement = self.canvasEchequier.echequier.deplacer(position_source,position_cible)
            if resultat_deplacement == "erreur":
                self.messages['foreground'] = 'red'
                self.messages['text'] = "Une erreur s'est produite lors du déplacement."
                self.liste_position = []
                return

            if self.partie.couleur_joueur_courant == 'blanc':
                self.partie.couleur_joueur_courant = 'noir'
            else:
                self.partie.couleur_joueur_courant = 'blanc'
        except TypeError:
            self.messages['foreground'] = 'red'
            self.messages['text'] = "Deplacement impossible"
        except AttributeError:
            self.messages['foreground'] = 'red'
            self.messages['text'] = "Deplacement impossible"
       
if __name__ == '__main__':
    # Point d'entrée principal du jeu
    fenetre = FenetrePartie()
    fenetre.mainloop()