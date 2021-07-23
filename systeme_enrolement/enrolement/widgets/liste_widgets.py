import sys
import os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap


FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/liste.ui"))

class Listes(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boutons()


    def boutons(self):
        pass