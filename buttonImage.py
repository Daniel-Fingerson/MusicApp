#!/usr/bin/env python
#Written by Daniel Fingerson, 6/23/2020
import sys
from PyQt5.QtGui import *



import sys
from PyQt5 import * #QtCore, QtGui
from PyQt5 import QtCore, QtWidgets


#!/usr/bin/env python
#TODO: COMBINE THIS WITH THE LOGIC OF BETTER.PY
#THIS IS THE MOST RECENT/ URGENT TO DO!!

#process most likely will be me adding the logic from better in here with each widget

#ALSO REMEMBER TO MAKE A FILE EARLY ON THAT IMPLEMENTS BEING THE IMAGE; (right now it is betterCustom)
#need to code in some sort of feedback with it (visual/ action)
#either way will want to have a seperate file at some point that is an image button

#will probably have a different file for each polygon button, or have a dictionary of polygons



import sys
from PyQt5.QtGui import *



import sys
from PyQt5 import * #QtCore, QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QAbstractButton, QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QHBoxLayout, QSizePolicy, QStyleOptionButton, QStyle
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class ImgButton(QPushButton):
    size = 100
    x = (3**0.5 / 2)
    

    

    def __init__(self, pixmap, parent=None):
        QPushButton.__init__(self)
        self.setMinimumSize(ImgButton.size + 10, ImgButton.size + 10)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.pixmap = pixmap
        
        self.setFlat(True)
        #self.setIcon(QIcon('test.png'))
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    '''
    def sizeHint(self):
        return self.pixmap.size()
    '''

    

    

        

