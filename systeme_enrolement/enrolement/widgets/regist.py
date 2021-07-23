import sys
import os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap


FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/registration.ui"))


class Registers(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boutons()


    def boutons(self):
        self.btn_envoi_2.clicked.connect(self.enregistrement)
        self.btn_photo.clicked.connect(self.get_image_file)


    def enregistrement(self):
        nom = self.nom.text()
        prenom = self.prenom.text()
        dates = self.date.text()
        lieu = self.lieu.text()
        domicile = self.domicile.text()
        # genre = self.genre.text()
        nom_pere = self.nom_pere_2.text()
        nom_mere = self.nom_mere_2.text()
        pays = self.pays.text()
        
       
        if not nom or not prenom or not dates or not nom_pere or not domicile or not nom_mere or not pays or not lieu:
            QtWidgets.QMessageBox.warning(self, "Error", "Remplissez les champs vides svp")
        
        # else:
        #     db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database/data.db"))
        #     c = db.cursor()
        #     command = """ SELECT * FROM regist WHERE nom=? AND prenom=? """
        #     resultat = c.execute(command, (nom, prenom))
            
        #     if resultat.fetchone():
        #         QtWidgets.QMessageBox.warning(self, "Error", "Vous etes déja enrolé")
        else:
            QtWidgets.QMessageBox.information(self, "Success", "Message envoyé avec succès")
            # db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database/data.db"))
            # c = db.cursor()
            # valeur = (nom, prenom, dates, lieu, domicile, nom_mere, nom_pere, pays)
            # c.execute("""INSERT INTO contact (nom, prenom, date, lieu, domicile, nom_mere, nom_pere, pays) VALUES (?,?,?,?,?)""", valeur)
            # db.commit()
            self.nom.clear()
            self.prenom.clear()
            self.dates.clear()
            self.nom_pere_2.clear()
            self.nom_mere_2.clear()
            self.domicile.clear()
            self.pays.clear()
            self.lieu.clear()


 
    def get_image_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, 'Open Image File', r"C:\\Users\\Ouattara oba", "Image file(*.jpg *.jpeg *.gif)")
        self.photo_label.setPixmap(QPixmap(file_name))
        self.photo_label.setScaledContents(True)


# def search(self):
#     db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database/data.db"))
#     c = db.cursor()
#     noms = str(self.nom_filter_txt.text())
#     command = """ SELECT * FROM regist WHERE nom=? AND prenom=? """
#     resultat = c.execute(command, (noms))




# def list(self):
#     db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database/data.db"))
#     c = db.cursor()
#     command = """ SELECT * FROM regist WHERE nom=? AND prenom=? """
#     resultat = c.execute(command, (nom, prenom))
