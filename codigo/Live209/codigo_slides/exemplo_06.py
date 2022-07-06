from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QLabel, QPushButton, QWidget, QVBoxLayout,
    QMainWindow
)

app = QApplication()
window = QMainWindow()
base = QWidget()
layout = QVBoxLayout()

font = QFont()
font.setPixelSize(90)

label = QLabel('Deixa um like!')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)

botao = QPushButton('Botão!')
botao.setFont(font)

layout.addWidget(label)
layout.addWidget(botao)

base.setLayout(layout)
window.setCentralWidget(base)

window.show()

app.exec()
