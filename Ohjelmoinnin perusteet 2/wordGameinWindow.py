from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout
)

from Sanakysely import Sanakysely


class OmaAkkuna(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sanakysely")

        self.sanakysely = Sanakysely()

        keskiwidget = QWidget()
        self.setCentralWidget(keskiwidget)

        paa_layout = QVBoxLayout()

        self.lblSana = QLabel()
        self.txbVastaus = QLineEdit()

        self.lblOikeat = QLabel("Oikeat: 0")
        self.lblVaarat = QLabel("Väärät: 0")
        self.lblNumero = QLabel("Sana nro: 0")

        self.btnUusi = QPushButton("Uusi peli")

        paa_layout.addWidget(QLabel("Sana suomeksi"))
        paa_layout.addWidget(self.lblSana)

        paa_layout.addWidget(QLabel("Sana ruotsiksi"))
        paa_layout.addWidget(self.txbVastaus)

        tilasto_layout = QHBoxLayout()
        tilasto_layout.addWidget(self.lblNumero)
        tilasto_layout.addWidget(self.lblOikeat)
        tilasto_layout.addWidget(self.lblVaarat)

        paa_layout.addLayout(tilasto_layout)
        paa_layout.addWidget(self.btnUusi)

        keskiwidget.setLayout(paa_layout)

        self.btnUusi.clicked.connect(self.uusi_peli)
        self.txbVastaus.returnPressed.connect(self.tarkista_vastaus)

        self.uusi_peli()

    def uusi_peli(self):
        self.sanakysely.nollaa()

        self.lblOikeat.setText("Oikeat: 0")
        self.lblVaarat.setText("Väärät: 0")

        sana = self.sanakysely.seuraavaSana()
        self.lblSana.setText(sana)
        self.lblNumero.setText(
            f"Sana nro: {self.sanakysely.sananro}"
        )

        self.txbVastaus.clear()

    def tarkista_vastaus(self):
        vastaus = self.txbVastaus.text()

        self.sanakysely.tarkista(vastaus)

        self.lblOikeat.setText(
            f"Oikeat: {self.sanakysely.oikeat}"
        )

        self.lblVaarat.setText(
            f"Väärät: {self.sanakysely.vaarat}"
        )

        sana = self.sanakysely.seuraavaSana()
        self.lblSana.setText(sana)

        self.lblNumero.setText(
            f"Sana nro: {self.sanakysely.sananro}"
        )

        self.txbVastaus.clear()


def main():
    app = QApplication()
    ikkuna = OmaAkkuna()
    ikkuna.show()
    app.exec()


main()