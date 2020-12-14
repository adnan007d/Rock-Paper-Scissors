#!/usr/bin/python3
from PyQt5.QtWidgets import  QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import random


class Game(QMainWindow):
    
    def __init__(self):
        super(Game,self).__init__()
        self.image = {
            "rock":"Image/Rock.png",
            "paper":"Image/Paper.png",
            "scissors":"Image/Scissors.png"
        }
        self.C_Points = 0;
        self.P_Points = 0;
        self.initUi()
        
        
    def initUi(self):
        loadUi("RPS.ui",self)
        self.setPoints()
        self.Rock.clicked.connect(lambda: self.set("rock"))
        self.Paper.clicked.connect(lambda: self.set("paper"))
        self.Scissors.clicked.connect(lambda: self.set("scissors"))
        self.Reset.clicked.connect(self.reset)
        self.Exit.clicked.connect(lambda: self.close())
        
    def set(self,pl_choice):
        self.PlayerResult.setText("")
        self.ComputerResult.setText("")
        self.disableButton(True)
        pic = QPixmap(self.image[pl_choice])
        self.PlayerLabel.setPixmap(pic)
        comp_choice = random.choice(list(self.image.keys()))
        pic = QPixmap(self.image[comp_choice])
        self.ComputerLabel.setPixmap(pic)

        self.declareWinner(pl_choice,comp_choice)
        
        
    def disableButton(self,value):
        self.Rock.setDisabled(value)
        self.Paper.setDisabled(value)
        self.Scissors.setDisabled(value)
        
        
    def declareWinner(self, pl_choice, comp_choice):
        self.checker = {
            "rock scissors": True,
            "paper rock": True,
            "scissors paper": True,
        }
        if pl_choice == comp_choice:
            self.PlayerResult.setText("Draw")
            self.ComputerResult.setText("Draw")
        elif self.checker.get(pl_choice + " " + comp_choice, False):
            self.PlayerResult.setText("Winner")
            self.P_Points += 1
        else:
            self.ComputerResult.setText("Winner")
            self.C_Points += 1
            
        self.setPoints()
        self.disableButton(False)
    
    
    def setPoints(self):
        self.ComputerPoints.setText(str(self.C_Points))
        self.PlayerPoints.setText(str(self.P_Points))
        
    
    def reset(self):
        self.ComputerLabel.clear()
        self.PlayerLabel.clear()
        self.PlayerResult.setText("")
        self.ComputerResult.setText("")
        self.C_Points = self.P_Points = 0
        self.setPoints()

if __name__ == '__main__':
    print("Run game.py")