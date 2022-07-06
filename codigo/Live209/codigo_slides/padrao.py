from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QPushButton,
)


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        font = QFont()
        font.setPixelSize(40)

        base_widget = QWidget()
        base_widget.setFont(font)
        layout = QVBoxLayout()

        widgets = [
            QLabel('Texto!'),
            QLineEdit(),
            QPushButton('Clique!')
        ]

        for w in widgets:
            layout.addWidget(w)

        base_widget.setLayout(layout)

        self.setCentralWidget(base_widget)


app = QApplication()
window = AppWindow()
window.show()
app.exec()
