#!/usr/bin/env python
#Written by Daniel Fingerson, 6/23/2020

from ItemsList import ItemsList
from Item import Item




import sys
from PyQt5 import * #QtCore, QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenu, QAbstractButton, QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QHBoxLayout, QSizePolicy, QStyleOptionButton, QStyle, QScrollArea
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class MainApp(QApplication):
    def __init__(self, args):
        super(MainApp, self).__init__(args)
        self.addWidgets()

    def addWidgets(self):
        self.window = MainWindow()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        #self.statusBar().showMessage("ok")
        self.resize(2000, 400)
        self.setWindowTitle("Music staffs")
        staffs=[]
        for x in range(0, 20):
            staffs.append(Item(x))
        self.setCentralWidget(ItemsList(staffs))
       

if __name__ == "__main__":
    app = MainApp(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    app.exec_()