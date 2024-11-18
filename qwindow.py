from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel

app = QApplication([])
# window = QWidget()
windows = QMainWindow()

label = QLabel(parent=windows)
label.setText('Hello im achmad chilmi')

label.move(200, 10)
button = QPushButton("Hello", parent=windows)


button.setText("button 1")
windows.show()

app.exec_()
