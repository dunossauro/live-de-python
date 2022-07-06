from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (
    QApplication, QLabel, QPushButton, QWidget, QVBoxLayout,
    QMainWindow
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        base = QWidget()
        layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(90)
        base.setFont(font)

        self.label = QLabel('Deixa um like!')
        self.label.setAlignment(Qt.AlignCenter)

        botao = QPushButton('Botão!')
        botao.clicked.connect(self.sinal_de_exemplo)

        layout.addWidget(self.label)
        layout.addWidget(botao)

        base.setLayout(layout)
        self.setCentralWidget(base)

        action = QAction('Ação', self)
        action.triggered.connect(self.sinal_de_exemplo)
        menu = self.menuBar()
        menu_geral = menu.addMenu('Menu')
        menu_geral.addAction(action)

    def sinal_de_exemplo(self):
        self.label.setText('Cliquei')
        print('Apertei o botão!!!')


from qdarktheme import load_stylesheet

app = QApplication()
app.setStyleSheet(load_stylesheet())

window = Window()
window.show()

app.exec()
