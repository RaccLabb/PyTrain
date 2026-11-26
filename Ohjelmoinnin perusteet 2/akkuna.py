from PySide6.QtWidgets import  QApplication, QMainWindow

class OmaAkkuna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 600, 400)

def main():
    sovellus = QApplication()
    akkuna = OmaAkkuna()
    akkuna.show()
    sovellus.exec()

if __name__=="__main__":
    main()