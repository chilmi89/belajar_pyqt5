# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        
        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.mainLayout.addWidget(self.titleLabel)
        
        # Form frame
        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QGridLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        
        # Label and Input for "Nama"
        self.labelNama = QtWidgets.QLabel(self.formFrame)
        font.setPointSize(16)
        self.labelNama.setFont(font)
        self.labelNama.setObjectName("labelNama")
        self.formLayout.addWidget(self.labelNama, 0, 0)
        
        self.lineEditNama = QtWidgets.QLineEdit(self.formFrame)
        self.lineEditNama.setPlaceholderText("Masukkan nama")
        self.lineEditNama.setObjectName("lineEditNama")
        self.formLayout.addWidget(self.lineEditNama, 0, 1)
        
        # Label and Input for "Kelas"
        self.labelKelas = QtWidgets.QLabel(self.formFrame)
        self.labelKelas.setFont(font)
        self.labelKelas.setObjectName("labelKelas")
        self.formLayout.addWidget(self.labelKelas, 1, 0)
        
        self.lineEditKelas = QtWidgets.QLineEdit(self.formFrame)
        self.lineEditKelas.setPlaceholderText("Masukkan kelas")
        self.lineEditKelas.setObjectName("lineEditKelas")
        self.formLayout.addWidget(self.lineEditKelas, 1, 1)
        
        # Label and Input for "NPM"
        self.labelNPM = QtWidgets.QLabel(self.formFrame)
        self.labelNPM.setFont(font)
        self.labelNPM.setObjectName("labelNPM")
        self.formLayout.addWidget(self.labelNPM, 2, 0)
        
        self.lineEditNPM = QtWidgets.QLineEdit(self.formFrame)
        self.lineEditNPM.setPlaceholderText("Masukkan NPM")
        self.lineEditNPM.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEditNPM.setObjectName("lineEditNPM")
        self.formLayout.addWidget(self.lineEditNPM, 2, 1)
        
        self.mainLayout.addWidget(self.formFrame)
        
        # Buttons
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        
        self.pushButtonSignUp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")
        self.buttonLayout.addWidget(self.pushButtonSignUp)
        
        self.pushButtonSignIn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSignIn.setObjectName("pushButtonSignIn")
        self.buttonLayout.addWidget(self.pushButtonSignIn)
        
        self.mainLayout.addLayout(self.buttonLayout)
        
        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menu bar and status bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.titleLabel.setText(_translate("MainWindow", "Login"))
        self.labelNama.setText(_translate("MainWindow", "Nama"))
        self.labelKelas.setText(_translate("MainWindow", "Kelas"))
        self.labelNPM.setText(_translate("MainWindow", "NPM"))
        self.pushButtonSignUp.setText(_translate("MainWindow", "SIGN UP"))
        self.pushButtonSignIn.setText(_translate("MainWindow", "SIGN IN"))


