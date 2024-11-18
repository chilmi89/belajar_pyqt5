
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel , QDesktopWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Hello, I am Achmad Chilmi', self)
        self.label.move(200 , 0 )

        self.button = QPushButton('Button 1', self)
        self.button.move(10, 40)
        
        
        # setting windows tiltle 
        self.setWindowTitle('Belajar Class Window')
        
        # setting geometry
        self.setGeometry(0,0, 500, 500)
        
        
        # cek frame Window
        size_frame = self.frameGeometry()
        
        # cek dan setting layout windows ke center
        size_dekstop = QDesktopWidget().availableGeometry().center()
        
        # setting to center
        size_frame.moveCenter(size_dekstop)
        
        self.move(size_frame.topLeft())
        
        
        self.setFixedSize(500, 500)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
