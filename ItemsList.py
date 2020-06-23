#!/usr/bin/env python

#Written by Daniel Fingerson, 6/23/2020


#THIS FILE CREATES AND POPULATES THE LIST OF ITEM OBJECTS

#https://stackoverflow.com/questions/25187444/pyqt-qlistwidget-custom-items
#TODO MAKE THIS A Qlist Widget rather then scroll
import sys
from PyQt5 import * #QtCore, QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenu, QAbstractButton, QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QHBoxLayout, QSizePolicy, QStyleOptionButton, QStyle, QVBoxLayout, QScrollArea
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class ItemsList(QWidget):
    def __init__(self, items, parent=None):
        super(ItemsList, self).__init__(parent)
        self.initWidget(items)

    def initWidget(self, items):
	    listBox = QVBoxLayout(self)
	    self.setLayout(listBox)

	    scroll = QScrollArea(self)
	    listBox.addWidget(scroll)
	    scroll.setWidgetResizable(True)
	    scrollContent = QWidget(scroll)

	    scrollLayout = QHBoxLayout(scrollContent)
	    scrollContent.setLayout(scrollLayout)
	    for item in items:
	        scrollLayout.addWidget(item)
	    scroll.setWidget(scrollContent)