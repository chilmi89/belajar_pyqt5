# cara import pyqt5
# from PyQt5 import QtCore, QtGui, QtWidgets



# cara kedua import pyqt5 cara paling efektif
from PyQt5.QtWidgets import QApplication , QPushButton


# cara ketiga import pyqt5

# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *



app = QApplication([])
button = QPushButton("Hello")
button.show()
app.exec_()