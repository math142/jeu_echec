import easygui
from interface_damier import FenetrePartie
import mysql.connector
from tkinter import N, Tk,Button,Entry,Label,ttk,Listbox
from typing import Text

class StartPoint(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(150,150)
        self.creerNouveauCompte = Button(self,text="Nouveau Compte",command=self.nouveau_compte)
        self.creerNouveauCompte.grid(row=0,column=0)
        self.connecter_compte = Button(self,text="Connexion",command=self.connexion)
        self.connecter_compte.grid(row=1,column=0)
    def nouveau_compte(self):
        NouveauCompte()
    def connexion(self):
        Connexion()
class NouveauCompte(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(150,150)
        self.LabeladresseCourrielle = Label(self,text="Adresse Courriel")
        self.LabeladresseCourrielle.grid(row=0,column=0)
        self.TextAdresseCourielle = Entry(self)
        self.TextAdresseCourielle.grid(row=0,column=1)
        self.mdp = Label(self,text="Mot de passe")
        self.mdp.grid(row=1,column=0)
        self.mdpText = Entry(self,show='*')
        self.mdpText.grid(row=1,column=1)
        self.mdptwo = Label(self,text="Veuillez répéter le mot de passe")
        self.mdptwo.grid(row=2,column=0)
        self.mdptwotext = Entry(self,show='*')
        self.mdptwotext.grid(row=2,column=1)
        self.nickname = Label(self,text="Veuillez rentrer un pseudonyme")
        self.nickname.grid(row=3,column=0)
        self.nicknameText = Entry(self)
        self.nicknameText.grid(row=3,column=1)

        self.buttonCreer = Button(self,text="Créer",command=self.creer)
        self.buttonCreer.grid(row=4,column=0)
        self.buttonAnnuler = Button(self,text="Annuler",command=self.annuler)
        self.buttonAnnuler.grid(row=4,column=1)
    def check_adresse(self,db,adresse):
        cursor = db.cursor()
        result = None
        query = """select email from user where email = %s """, (adresse,)
        cursor.execute(*query)
        result = cursor.fetchall()
        if result == None or len(result) == 0:
            return True
        else:
            return False
    def check_nickname(self,db,nickname):
        cursor = db.cursor()
        result = None
        query = """select * from user where nickname = %s""", (nickname,)
        cursor.execute(*query)
        result = cursor.fetchall()
        if result == None or len(result) == 0:
            return True
        else:
            return False   
    def compare(self,password1,password2):
        if password1 == password2:
            return True
        return False
   
    def connexion_bd(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="fernweh",
            password="F3rnweh$",
            database="jeux_echec",
            auth_plugin='mysql_native_password')
        return mydb
    
    def creer(self):
        password = self.mdpText.get()
        password2 = self.mdptwotext.get()
        adresse = self.TextAdresseCourielle.get()
        nickname = self.nicknameText.get()
        if self.compare(password,password2):
            print("ok")
        else:
            print("Mot de passe différent")
        db = self.connexion_bd()
        if self.check_adresse(db,adresse) and self.check_nickname(db,nickname):
            cursor = db.cursor()
            cursor.execute("insert into user (email,mdp,nickname) values (%s,%s,%s)",(adresse,password,nickname))
            db.commit()
            easygui.msgbox("Votre compte a été crée",title="Information")
            Connexion()
            self.destroy()

    def annuler(self):
        self.destroy()
class Connexion(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(150,150)
        self.email = Label(self,text="Adresse Courriel")
        self.email.grid(row=0,column=0)
        self.email_text = Entry(self)
        self.email_text.grid(row=0,column=1)
        self.mdp = Label(self,text="Mot de passe")
        self.mdp.grid(row=1,column=0)
        self.mdp_Text = Entry(self,show='*')
        self.mdp_Text.grid(row=1,column=1)
        self.connecter = Button(self,text="Connecter",command=self.connect)
        self.connecter.grid(row=2,column=0)
        self.annuler = Button(self,text="Annuler",command=self.cancel)
        self.annuler.grid(row=2,column=1)
    def connect(self):
        db = self.connexion_bd()
        email = self.email_text.get()
        password = self.mdp_Text.get()
        if self.connexion(db,email,password):
            pass
    def cancel(self):
        self.destroy()
    def connexion_bd(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="fernweh",
            password="F3rnweh$",
            database="jeux_echec")
        return mydb
    def connexion(self,db,email,mdp):
        cursor = db.cursor()
        cursor.execute("select * from user where email = %s",(email,))
        info = cursor.fetchall()
        if len(info) == 0:
            print("Votre compte est inexistant")
            NouveauCompte()
        else:
            FenetrePartie()
            self.destroy()

if __name__ == '__main__':
    # Point d'entrée principal du jeu
    fenetre = StartPoint()
    fenetre.mainloop()