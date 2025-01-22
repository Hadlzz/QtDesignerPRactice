import sys, time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QTextBrowser, QComboBox, QListWidget, QProgressBar, QMessageBox, QDialogButtonBox
from PyQt5 import uic
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main', self)
