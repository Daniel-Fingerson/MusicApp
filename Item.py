#!/usr/bin/env python
#Written by Daniel Fingerson, 6/23/2020

#DF; this is the object that makes the view in each row 

import sys
from PyQt5 import * #QtCore, QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenu, QAbstractButton, QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QHBoxLayout, QSizePolicy, QStyleOptionButton, QStyle, QVBoxLayout, QStackedLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize  
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from buttonImage import ImgButton

#eventually, populate with notes (pass it list received from database upon intialization of notes)

class Item(QWidget):
   
    def __init__(self, pos, parent = None):
        super(Item, self).__init__(parent)
        self.button = ImgButton(QPixmap('images/addGraph.png'))
        self.button.clicked.connect(self.Action)

        if pos == 0:
            self.button.hide()

        self.xpos = 330
        self.ypos = 0
        self.staff = QLabel(self)
        #image needs to be redrawn every time
        self.oldPos = [[30,10],[130,10],[230,50]]
        self.initWidget(pos)
        
        

    def initWidget(self, pos):
        #title = QLabel(title)
        #date = QLabel(date)
        #TODO if images work like this, make titleBox a Z stack and see if images will overlay (overlya each staff with list of notes)
        #should make note its own file/ class (since it will track position, height, noteType)
        titleBox = QVBoxLayout()
        #staff = QLabel(self)
        staffImage = QImage('images/test.png')
        #staff.setPixmap(staffImage)


        #later, should probably use the paint/ tranlate mthod in a for loop to draw staffs over eachother so there is no offset like there is currently 
        if pos == 0:
            #starting one would probably have different widgets

            #image = (QImage("test.png").setOffset(QPoint(200,200)))
            #image.setOffset(QPoint(200,200))
    
    
            overlay = QImage("images/treble.png").scaled(150,150)
            #should probably change this so that QPoint is tied to the exact position of the give staff image object
            #overlay.setOffset(QPoint(100,100))
            
            '''
            if overlay.size() > image.size():
            
                overlay = overlay.scaled(image.size(), Qt.KeepAspectRatio)
            '''
            #use translate method on painter to physically move it (input is QPoint; also can give it x and y coordinate)
            painter = QPainter()
            painter.begin(staffImage)
            painter.drawImage(-30, 10, overlay) 
            painter.end()

            
            self.staff.setPixmap(QPixmap.fromImage(staffImage))
            self.staff.move(0,-100)
            self.staff.show()
            
            cleff = QLabel(self)
            beginning = QHBoxLayout()
            cleffImage = overlay
            #cleff.setPixmap(cleffImage)
            #cleff.setParent(staff)
            #cleff.show()
            beginning.addWidget(cleff)
            titleBox.addLayout(beginning)
            #cleff.move(20,20)
        else:
            #TODO make an array of note/images (eventually make note its own class/ file, so height and position can be set)
            overlay1 = QImage("images/quarter.png").scaled(100,100)
            overlay2 = QImage("images/juntosSame.png").scaled(100,100)
            painter = QPainter()
            painter.begin(staffImage)

            painter.drawImage(30, 0, overlay1) 
            painter.drawImage(130, 0, overlay2) 
            painter.drawImage(230, 0, overlay1) 
            painter.drawImage(330, 0, overlay2) 
            #self.oldPos.append([530,10])


            painter.end()
            self.staff.setPixmap(QPixmap.fromImage(staffImage))
            #self.staff.show()
            #include buttons here 
            
    
        

        


        titleBox.addWidget(self.staff)
        titleBox.addWidget(self.button)
        #titleBox.addWidget(date)
        self.setLayout(titleBox)

    def Action(self):
        staffImage = QImage('images/test.png')
        print("hello world")
        overlay1 = QImage("images/quarter.png").scaled(100,100)
        overlay2 = QImage("images/juntosSame.png").scaled(100,100)
        painter = QPainter()
        painter.begin(staffImage)

        for i in range(len(self.oldPos)):
            if i == 1:
                painter.drawImage(self.oldPos[i][0], self.oldPos[i][1], overlay2) 
            else:

                painter.drawImage(self.oldPos[i][0], self.oldPos[i][1], overlay1) 

        painter.drawImage(self.xpos, self.ypos, overlay1) 

        self.oldPos.append([self.xpos,self.ypos])



        self.xpos += 100
        self.ypos +=20
        


        painter.end()
        self.staff.setPixmap(QPixmap.fromImage(staffImage))
        self.staff.show()