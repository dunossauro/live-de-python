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

        label = QLabel('Deixa um like!')
        label.setAlignment(Qt.AlignCenter)

        botao = QPushButton('Botão!')

        layout.addWidget(label)
        layout.addWidget(botao)

        base.setLayout(layout)
        self.setCentralWidget(base)

        action = QAction('Ação', self)
        menu = self.menuBar()
        menu_geral = menu.addMenu('Menu')
        menu_geral.addAction(action)


app = QApplication()

window = Window()
window.show()

app.exec()
