from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QLabel, QPushButton, QWidget, QVBoxLayout
)

app = QApplication()

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

base.show()

app.exec()
