from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide6.QtCore import Qt
import random

class OmaAkkuna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 400, 300)
        self.alusta_UI()

    def alusta_UI(self):
        self.setWindowTitle("Noppapeli")

        self.bLabel = QLabel("Noppapeli", self)
        self.bLabel.setGeometry(150, 30, 100, 20)
        self.bLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.num = QLabel("--", self)
        self.num.setGeometry(150, 116, 100, 20)
        self.num.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Pyöräytä noppaa", self)
        self.button.setGeometry(125, 200, 150, 50)
        self.button.clicked.connect(self.diceRolled)

    def diceRolled(self):
        diceNum = str(random.randint(1,6))
        self.num.setText(diceNum)



def main():
    app = QApplication()#Luodaan sovellus olio
    akkuna = OmaAkkuna()#Luodaan akkuna olio
    akkuna.show() #Näytetään akkuna
    app.exec() #Jäädään odottamaan käyttäjän toimia

if __name__ == "__main__":
    main()