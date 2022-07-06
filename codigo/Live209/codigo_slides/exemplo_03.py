from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QPushButton

app = QApplication()

font = QFont()
font.setPixelSize(90)

label = QLabel('Deixa um like!')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)

botao = QPushButton('Botão!')
botao.setFont(font)
botao.show()

label.show()

app.exec()
