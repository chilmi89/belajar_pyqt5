
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel , QGridLayout , QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")
        # pengaturan  koordinat  paramter seperti kolol 0,1 dengan rowq dan kolom 
        layout.addWidget(btn1 , 0 , 0)
        layout.addWidget(btn2 , 0 , 1)
        layout.addWidget(btn3 , 1 , 0)
        layout.addWidget(btn4   , 1 , 1)
        self.setLayout(layout)
        

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

