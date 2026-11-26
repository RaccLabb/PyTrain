from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import random

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 400, 400)
        self.setStyleSheet("background-color: white; color: darkred")
        self.money = 200
        self.setUI()

    def setUI(self):
        self.header = QLabel("Hedelmäpeli 🎄Christmast Edition🎄", self)
        self.header.setGeometry(0, 50, 400, 50)
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.header.setFont(QFont("Calibri", 18))

        self.icons = QLabel("🎄🔔🎅", self)
        self.icons.setGeometry(0, 150, 400, 100)
        self.icons.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.icons.setFont(QFont("Calibri", 32))
    
        self.button = QPushButton("Pelaa", self)
        self.button.setGeometry(50, 300, 80, 60)
        self.button.setStyleSheet("background-color: green; color: white")
        self.button.clicked.connect(self.playGame)
        self.button.setFont(QFont("Calibri", 18))

        self.moneyText = QLabel(f"{self.money}snt", self)
        self.moneyText.setGeometry(130, 300, 200, 60)
        self.moneyText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.moneyText.setFont(QFont("Calibri", 18))


    def playGame(self):
        if self.money > 0:
            self.money -= 20
            listOfIconlists = [["🎄","🔔","🎅"], ["🎄","🔔","🎅"], ["🎄","🔔","🎅"]]
            chosenPossibility = []
            for iconList in listOfIconlists:
                icon = random.choice(iconList)
                chosenPossibility.append(icon)

            self.icons.setText(f"|{chosenPossibility[0]} {chosenPossibility[1]} {chosenPossibility[2]}|")
            self.money = self.money + checkTheWin(chosenPossibility)
            if self.money < 0:
                self.money = 0
            self.moneyText.setText(f"{self.money} snt voitit {checkTheWin(chosenPossibility)} snt")
        else:
            self.header.setText("GAME OVER!")

def checkTheWin(chosenIcons):
    #Valitaan oikea palkinto
    if chosenIcons.count("🔔") == 2:
        moneyWon = 10
    elif chosenIcons.count("🔔") == 3 or chosenIcons.count("🧹") == 2:
        moneyWon = 20
    elif chosenIcons.count("🎅") == 3 or chosenIcons.count("🫟") == 2:
        moneyWon = 100
    elif chosenIcons.count("🎄") == 3 or chosenIcons.count("🧛") == 2:
        moneyWon = 300
    else: 
        moneyWon = 0
    return moneyWon


def main():
    app = QApplication()
    _window = Window()
    _window.show()
    app.exec()

if __name__=="__main__":
    main()