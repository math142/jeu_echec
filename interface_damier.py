import numpy as np
from pickle import NONE
from tkinter import END, N, NS, S, Frame, Listbox, Tk,Label, simpledialog, ttk
from typing import List
from canvasEchequier import CanvasEchequier
from partie import Partie
from position import Position
from piece import Piece

class FenetrePartie(Tk):
    def __init__(self):
        super().__init__()
        self.liste_position = []
        self.partie = Partie()
        self.frameJeux = Frame(self)
        self.frameJeux.grid(row=0,column=0)
        self.canvasEchequier = CanvasEchequier(self.frameJeux,self.partie.echequier,60)
        self.canvasEchequier.grid(column=0, row=0)
        self.canvasEchequier.bind('<Button-1>',self.selectionner)
        self.liste_coup =  Listbox(self.frameJeux)
        self.liste_coup.grid(row=0,column=1,sticky=NS)
        self.couleur_joueur = self.partie.couleur_joueur_courant
        self.messages = Label(self.frameJeux)
        self.messages.grid()
        self.peut_changer_couleur = True
        self.title("Jeu d'echeque")
        self.nbr_Coup = 1
        self.position =Position(0,0)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.pos_algebrique = []
       
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
            type_piece_source = self.canvasEchequier.echequier.recuperer_piece_a_position(position_source)
            type_piece_cible = self.canvasEchequier.echequier.recuperer_piece_a_position(position_cible)

            self.partie.echequier.twice = True
            self.coup_precedent = []
            resultat_deplacement = self.canvasEchequier.echequier.deplacer(position_source,position_cible)
            if resultat_deplacement == "erreur":
                self.messages['foreground'] = 'red'
                self.messages['text'] = "Une erreur s'est produite lors du déplacement."
                self.liste_position = []
                return
            self.coup_precedent.append(position_source)
            self.coup_precedent.append(position_cible)
            
            if type_piece_cible is not None:
                if self.partie.couleur_joueur_courant == 'blanc':
                    position_algebrique = self.position.conversion_en_algebrique(position_source,position_cible,type_piece_source.type_piece,type_piece_cible.type_piece,resultat_deplacement,
                    self.canvasEchequier.echequier.est_en_echec('noir','echec',Position(0,0)))
                else:
                    position_algebrique = self.position.conversion_en_algebrique(position_source,position_cible,type_piece_source.type_piece,type_piece_cible.type_piece,resultat_deplacement,
                    self.canvasEchequier.echequier.est_en_echec('blanc','echec',Position(0,0)))
            else:
                type_piece_cible = type_piece_source
                if self.partie.couleur_joueur_courant == 'blanc':
                    position_algebrique = self.position.conversion_en_algebrique(position_source,position_cible,type_piece_source.type_piece,type_piece_cible.type_piece,resultat_deplacement,
                    self.canvasEchequier.echequier.est_en_echec('noir','echec',Position(0,0)))
                else:
                    position_algebrique = self.position.conversion_en_algebrique(position_source,position_cible,type_piece_source.type_piece,type_piece_cible.type_piece,resultat_deplacement,
                    self.canvasEchequier.echequier.est_en_echec('noir','echec',Position(0,0)))

            if len(self.pos_algebrique) == 0:
                self.pos_algebrique.append("{0}.{1}".format(self.nbr_Coup,position_algebrique))
            else:
                self.liste_coup.delete(self.nbr_Coup - 1)
                self.pos_algebrique.append(position_algebrique)
            self.liste_coup.insert(END,self.pos_algebrique)
            if self.partie.echequier.est_pat(self.partie.couleur_joueur_courant,'echec',Position(0,0)):
                self.messages['foreground'] = 'red'
                self.messages['text'] = "Pat"
            if resultat_deplacement == 'Last':
                piece = self.nouvelle_piece()
                self.partie.echequier.creation_nouvelle_piece(self.partie.couleur_joueur_courant,piece,self.coup_precedent[1])
            if self.partie.echequier.joueur_est_en_echec == True and (self.partie.echequier.est_en_echec(self.partie.couleur_joueur_courant,'echec',Position(0,0))):
                piece_originale = self.partie.echequier.recuperer_piece_a_position(self.coup_precedent[1])
                self.partie.echequier.cases[self.coup_precedent[0]] = piece_originale
                del self.partie.echequier.cases[self.coup_precedent[1]]
                self.coup_precedent.clear()
                self.peut_changer_couleur = False
            else:
                self.partie.echequier.echec = False
                self.peut_changer_couleur = True

            if self.peut_changer_couleur == True:
                if self.partie.couleur_joueur_courant == 'blanc':
                    self.partie.couleur_joueur_courant = 'noir'
                    
                else:
                    self.partie.couleur_joueur_courant = 'blanc'
                    self.pos_algebrique.clear()
                    self.nbr_Coup+=1
                if self.canvasEchequier.echequier.est_echec_math(self.partie.couleur_joueur_courant):
                    self.messages['foreground'] = 'red'
                    self.messages['text'] = 'echec et math'
                if self.canvasEchequier.echequier.est_en_echec(self.partie.couleur_joueur_courant,'echec',Position(0,0)):
                        self.messages['foreground'] = 'red'
                        self.messages['text'] = 'echec'
                        self.partie.echequier.joueur_est_en_echec = True        
                self.partie.echequier.twice = False
                self.partie.echequier.echec = True
                if self.partie.echequier.est_echec_math(self.partie.couleur_joueur_courant):
                    self.messages['foreground'] = 'red'
                    self.messages['text'] = 'Echec et Math'
                    if self.partie.couleur_joueur_courant == 'blanc':
                        self.partie_gagne('noir')
                    else:
                        self.partie_gagne('blanc')
                        
                        

        except AttributeError:
            self.messages['foreground'] = 'red'
            self.messages['text'] = "Deplacement impossible"
    

    def partie_gagne(self,joueur):
        msg = '{0} a gagné la partie'.format(joueur)
        label = ttk.Label(self,text=msg)
        label.grid(row=0,column=0,pady=50)    
    def  nouvelle_piece(self):
        piece = simpledialog.askstring(title="Nouvelle Piece",prompt="Choissisez une piece")
        return piece
