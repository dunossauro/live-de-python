from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication()

font = QFont()
font.setPixelSize(90)

label = QLabel('Deixa um like!')
label.setFont(font)
label.show()

app.exec()
