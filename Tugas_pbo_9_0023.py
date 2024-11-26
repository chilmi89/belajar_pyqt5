from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_window(object):

        def __init__(self):
                self.db_connection = None
                self.connect_to_database()

        def connect_to_database(self):
                
                try:
                        self.db_connection = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="",
                                database="management_data"
                        )
                        if self.db_connection.is_connected():
                                print("Koneksi ke database berhasil")
                except mysql.connector.Error as err:
                        print(f"Error: {err}")
                        self.db_connection = None

        def setupUi(self, window):
                window.setObjectName("window")
                window.resize(441, 388)
                window.setStyleSheet("#window{background-color: #cbcbcb;}")
                self.centralwidget = QtWidgets.QWidget(window)
                self.centralwidget.setStyleSheet("#centralwidget{background-color: black;}")
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setObjectName("verticalLayout")
                self.frame_2 = QtWidgets.QFrame(self.centralwidget)
                self.frame_2.setStyleSheet("#frame_2{border: 1px solid black;}")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
                self.frame_2.setObjectName("frame_2")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.frame = QtWidgets.QFrame(self.frame_2)
                self.frame.setEnabled(True)
                self.frame.setStyleSheet("#frame{border: 1px solid black;}")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
                self.frame.setObjectName("frame")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(20, 70, 81, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("#label {background-color: blue;color:white;border-radius: 10px;font-size: 12px;}")
                self.label.setLineWidth(5)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.form = QtWidgets.QLineEdit(self.frame)
                self.form.setGeometry(QtCore.QRect(110, 70, 291, 31))
                self.form.setStyleSheet("#form{border-radius:10px;font-size:15px;}")
                self.form.setText("")
                self.form.setFrame(True)
                self.form.setAlignment(QtCore.Qt.AlignCenter)
                self.form.setPlaceholderText("Masukkan Nama ")
                self.form.setObjectName("form")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(20, 110, 81, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("#label_2 {background-color: blue;color:white;border-radius: 10px;font-size: 12px;}")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.form_2 = QtWidgets.QLineEdit(self.frame)
                self.form_2.setGeometry(QtCore.QRect(110, 110, 291, 31))
                self.form_2.setStyleSheet("#form_2{border-radius:10px;font-size:15px;}")
                self.form_2.setText("")
                self.form_2.setAlignment(QtCore.Qt.AlignCenter)
                self.form_2.setObjectName("form_2")
                self.button1 = QtWidgets.QPushButton(self.frame)
                self.button1.setGeometry(QtCore.QRect(40, 160, 341, 29))
                self.button1.setEnabled(True)
                font = QtGui.QFont()
                font.setPointSize(13)
                self.button1.setFont(font)
                self.button1.setStyleSheet("#button1{background-color: blue;border-radius: 5px;color:white;}")
                self.button1.setObjectName("button1")
                self.button2 = QtWidgets.QPushButton(self.frame)
                self.button2.setGeometry(QtCore.QRect(40, 200, 341, 29))
                self.button2.setEnabled(True)
                font = QtGui.QFont()
                font.setPointSize(13)
                self.button2.setFont(font)
                self.button2.setStyleSheet("#button2{background-color: blue;border-radius: 5px;color:white;}")
                self.button2.setObjectName("button2")
                self.button3 = QtWidgets.QPushButton(self.frame)
                self.button3.setGeometry(QtCore.QRect(40, 240, 341, 29))
                self.button3.setEnabled(True)
                font = QtGui.QFont()
                font.setPointSize(13)
                self.button3.setFont(font)
                self.button3.setStyleSheet("#button3{background-color: blue;border-radius: 5px;color:white;}")
                self.button3.setObjectName("button3")
                self.button4 = QtWidgets.QPushButton(self.frame)
                self.button4.setGeometry(QtCore.QRect(40, 280, 341, 29))
                self.button4.setEnabled(True)
                font = QtGui.QFont()
                font.setPointSize(13)
                self.button4.setFont(font)
                self.button4.setStyleSheet("#button4{background-color: blue;border-radius: 5px;color:white;}")
                self.button4.setObjectName("button4")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(110, 10, 181, 31))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("#label_3{color:white;background-color: blue;border-radius: 5px;}")
                self.label_3.setObjectName("label_3")
                self.verticalLayout_2.addWidget(self.frame)
                self.verticalLayout.addWidget(self.frame_2)
                window.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(window)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
                self.menubar.setObjectName("menubar")
                window.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(window)
                self.statusbar.setObjectName("statusbar")
                window.setStatusBar(self.statusbar)

                self.retranslateUi(window)
                QtCore.QMetaObject.connectSlotsByName(window)
                
                
                
                # button fungsi
                self.button1.clicked.connect(self.create_data)  
                self.button2.clicked.connect(self.update_data)  
                self.button3.clicked.connect(self.delete_data)  
                self.button4.clicked.connect(self.search_data)  


        def retranslateUi(self, window):
                _translate = QtCore.QCoreApplication.translate
                window.setWindowTitle(_translate("window", "MainWindow"))
                self.label.setText(_translate("window", "Nama"))
                self.label_2.setText(_translate("window", "Alamat "))
                self.form_2.setPlaceholderText(_translate("window", "Masukkan Alamat"))
                self.button1.setText(_translate("window", "Tambah"))
                self.button2.setText(_translate("window", "Edit"))
                self.button3.setText(_translate("window", "Hapus"))
                self.button4.setText(_translate("window", "Cari"))
                self.label_3.setText(_translate("window", "    Management Data"))
                
        def reset_form(self):
                """Mereset form input menjadi kosong."""
                self.form.clear()
                self.form_2.clear()
        def create_data(self):
                nama = self.form.text()
                alamat = self.form_2.text()

                if nama and alamat:  
                        try:
                                cursor = self.db_connection.cursor()
                                query = "INSERT INTO biodata (nama, alamat) VALUES (%s, %s)"
                                cursor.execute(query, (nama, alamat))
                                self.db_connection.commit()
                                print("Data berhasil ditambahkan.")
                                
                                self.reset_form()
                        except mysql.connector.Error as err:
                                print(f"Error: {err}")
                        finally:
                                cursor.close()
                else:
                        print("Nama dan Alamat tidak boleh kosong.")

        def update_data(self):
                nama = self.form.text()
                alamat = self.form_2.text()

                if nama and alamat:  
                        try:
                                cursor = self.db_connection.cursor()
                                query = "UPDATE biodata SET alamat = %s WHERE nama = %s"
                                cursor.execute(query, (alamat, nama))
                                self.db_connection.commit()
                                if cursor.rowcount > 0:
                                        print("Data berhasil diperbarui.")
                                        self.reset_form()
                                else:
                                        print("Data tidak ditemukan.")
                        except mysql.connector.Error as err:
                                print(f"Error: {err}")
                        finally:
                                cursor.close()
                else:
                        print("Nama dan Alamat tidak boleh kosong.")

        def delete_data(self):
                """Fungsi untuk menghapus data dari database."""
                nama = self.form.text()

                if nama:  
                        try:
                                cursor = self.db_connection.cursor()
                                query = "DELETE FROM biodata WHERE nama = %s"
                                cursor.execute(query, (nama,))
                                self.db_connection.commit()sdasdasdasdasd
                                if cursor.rowcount > 0:
                                        print("Data berhasil dihapus.")
                                        self.reset_form()
                                else:
                                        print("Data tidak ditemukan.")
                        except mysql.connector.Error as err:
                                print(f"Error: {err}")
                        finally:
                                cursor.close()
                else:
                        print("Nama tidak boleh kosong.")

        def search_data(self):
                """Fungsi untuk mencari data di database."""
                nama = self.form.text()

                if nama:  
                        try:
                                cursor = self.db_connection.cursor()
                                query = "SELECT * FROM biodata WHERE nama = %s"
                                cursor.execute(query, (nama,))
                                result = cursor.fetchone()
                                if result:
                                        print("Data ditemukan:", result)
                                        self.form_2.setText(result[1])
                                        self.reset_form()
                                else:
                                        print("Data tidak ditemukan.")
                        except mysql.connector.Error as err:
                                print(f"Error: {err}")
                        finally:
                                cursor.close()
                else:
                        print("Nama tidak boleh kosong.")



if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        ui = Ui_window()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec_())

