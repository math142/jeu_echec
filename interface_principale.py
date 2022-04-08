from tkinter import Tk,Button
from interface_damier import FenetrePartie
class InteracePrincipale(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(150,150)
        self.waitforplayer = Button(self,text="Attendre pour autres joueurs",command=self.attendre_joueur)
        self.waitforplayer.grid(column=0,row=0)
        self.jouer_contre_ordi = Button(self,text="Jouer contre l'ordinateur")
        self.jouer_contre_ordi.grid(column = 0, row = 1)
    def attendre_joueur(self):
        FenetrePartie()

