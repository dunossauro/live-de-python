from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def callback():
    print(window.email_input.text())
    print('Callback Login!')

app = QApplication()

loder = QUiLoader()
window = loder.load('login.ui')

window.login_button.clicked.connect(callback)

window.show()

app.exec()
