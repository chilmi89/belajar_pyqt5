from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel

app = QApplication([])
window = QWidget()

label = QLabel(parent=window)
label.setText('Hello im achmad chilmi')

label.move(200, 10)
button = QPushButton("Hello", parent=window)


button.setText("button 1")
window.show()

app.exec_()
