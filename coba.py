
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
import mysql.connector


class Ui_MainWindow(object):
    def __init__(self):
        self.db_connection = None
        self.connect_to_database()

    def connect_to_database(self):

        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="manajemen_keuangan",
            )
            if self.db_connection.is_connected():
                print("Koneksi ke database berhasil")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db_connection = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(418, 400))
        MainWindow.setStyleSheet(
            "#MainWindow{\n" "    background-color: rgba(0, 0, 0, 0.5);\n" "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "#centralwidget{\n"
            "    background-color: rgba(0, 0, 0, 0.5);\n"
            "      padding: 30px;\n"
            "      border-radius: 5px;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Header
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(350, 20))
        self.frame.setMaximumSize(QtCore.QSize(418, 50))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)

        # Form
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.frame_2.setObjectName("frame_2")

        # Username
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(29, 79, 244);")
        self.label_2.setText("Username")
        self.label_2.setObjectName("label_2")
        self.form1 = QtWidgets.QLineEdit(self.frame_2)
        self.form1.setGeometry(QtCore.QRect(30, 80, 331, 31))
        self.form1.setStyleSheet(
            "background-color: #1f2833; color: #fff; border-radius: 5px;"
        )
        self.form1.setAlignment(QtCore.Qt.AlignCenter)
        self.form1.setObjectName("form1")

        # Password
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 41))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(29, 79, 244);")
        self.label_3.setText("Password")
        self.label_3.setObjectName("label_3")
        self.form2 = QtWidgets.QLineEdit(self.frame_2)
        self.form2.setGeometry(QtCore.QRect(30, 160, 331, 31))
        self.form2.setStyleSheet(
            "background-color: #1f2833; color: #fff; border-radius: 5px;"
        )
        self.form2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.form2.setAlignment(QtCore.Qt.AlignCenter)
        self.form2.setObjectName("form2")

        # Button
        self.button1 = QtWidgets.QPushButton(self.frame_2)
        self.button1.setGeometry(QtCore.QRect(70, 230, 251, 41))
        font.setPointSize(12)
        self.button1.setFont(font)
        self.button1.setStyleSheet(
            "background-color: rgb(29, 79, 244); color:white; border-radius:15px;"
        )
        self.button1.setText("Log In")
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        # self.button1.clicked.connect(self.show_new_window)
        self.button1.clicked.connect(self.login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LOGIN"))

    def show_new_window(self):
        self.new_window = QtWidgets.QMainWindow()
        self.new_ui = Ui_new_window(self.db_connection)
        # self.new_ui = Ui_new_window(db_connection, login_window=self)
        self.new_ui.setupUi(self.new_window)
        self.new_window.show()

    def login(self):
        username = self.form1.text().strip()
        password = self.form2.text().strip()

        if not username or not password:
            QMessageBox.warning(
                None, "Login Gagal", "Username atau password tidak boleh kosong!"
            )
            return

        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                QMessageBox.information(
                    None, "Login Berhasil", f"Selamat datang, {result[1]}!"
                )
                # Ganti `result[1]` dengan nama kolom yang sesuai
                self.show_new_window()  # Jika login berhasil, buka window baru
            else:
                QMessageBox.warning(
                    None, "Login Gagal", "Username atau password salah!"
                )

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"Terjadi kesalahan: {err}")

    def show_failed_window(self):
        failed_window = QtWidgets.QMessageBox()
        failed_window.setWindowTitle("Login Gagal")
        failed_window.setText("Coba lagi. Username atau password salah!")
        failed_window.setIcon(QtWidgets.QMessageBox.Warning)
        failed_window.exec_()

    def reset_login_form(self):
        """Mereset field input username dan password."""
        self.form1.clear()  # Mengosongkan field username
        self.form2.clear()


class Ui_new_window(object):
    def __init__(self, db_connection, login_window=None):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        self.login_window = login_window

    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)

        
        # Set central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: black;")

        # Header dashboard 
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.header.setStyleSheet("background-color: blue; color: white;")
        self.header.setObjectName("header")
        self.title = QtWidgets.QLabel(self.header)
        self.title.setGeometry(QtCore.QRect(380, 10, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setText("Dashboard Kas")
        self.title.setStyleSheet("color: white;")

        # element button tambah data
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(860, 70, 100, 30))
        self.add_button.setText("+ Add")
        self.add_button.setStyleSheet(
            "background-color: #28a745; color: white; border-radius: 5px;"
        )
        self.add_button.clicked.connect(self.open_add_window)

        # element search box 
        self.search_label = QtWidgets.QLabel(self.centralwidget)
        self.search_label.setGeometry(QtCore.QRect(20, 70, 50, 30))
        self.search_label.setText("Search:")
        self.search_label.setStyleSheet("font-size: 14px; color: white;")

        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(80, 70, 300, 30))
        self.search_input.setPlaceholderText("Search by ID, Type, or Description...")
        self.search_input.setStyleSheet(
            "border: 1px solid #ccc; border-radius: 5px; padding: 5px; color: white; background-color: black;"
        )

        # koneksi ke search input ke fungsi search
        self.search_input.textChanged.connect(self.search)

        # layout table dan elementnya
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 110, 960, 200))
        self.table.setStyleSheet(
            "background-color: black; color: #e0e0e0;"
        )  # Updated text color
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["ID", "tanggal_transaksi", "type", "jumlah", "deskripsi", "Actions"]
        )
        self.table.horizontalHeader().setStyleSheet(
            "::section { background-color: #333; color: white; }"
        )
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 250)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setItemDelegate(CenterDelegate())

        # Horizontal line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 320, 960, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # element label uang masuk
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        self.total_label.setGeometry(QtCore.QRect(20, 370, 120, 40))
        self.total_label.setText("Total Uang Masuk:")
        self.total_label.setStyleSheet("font-size: 14px; color: white;")

        # Deklarasikan total_input terlebih dahulu
        self.total_input = QtWidgets.QLineEdit(self.centralwidget)
        self.total_input.setGeometry(QtCore.QRect(150, 370, 200, 40))
        self.total_input.setReadOnly(True)  # Membuatnya hanya baca
        self.total_input.setStyleSheet(
            "border: 1px solid #ccc; border-radius: 5px; padding: 5px; color: white; background-color: black;"
        )

        # element label uang keluar
        self.total_keluar_label = QtWidgets.QLabel(self.centralwidget)
        self.total_keluar_label.setGeometry(QtCore.QRect(640, 370, 120, 40))
        self.total_keluar_label.setText("Total Uang Keluar:")
        self.total_keluar_label.setStyleSheet("font-size: 14px; color: white;")

        # Deklarasikan total_keluar_input terlebih dahulu
        self.total_keluar_input = QtWidgets.QLineEdit(self.centralwidget)
        self.total_keluar_input.setGeometry(QtCore.QRect(760, 370, 200, 40))
        self.total_keluar_input.setReadOnly(True)  # Membuatnya hanya baca
        self.total_keluar_input.setStyleSheet(
            "border: 1px solid #ccc; border-radius: 5px; padding: 5px; color: white; background-color: black;"
        )

        
        # Layout untuk tombol detail
        self.detail_button = QtWidgets.QPushButton("Detail", self.centralwidget)
        self.detail_button.setGeometry(QtCore.QRect(480, 370, 80, 40))  # Posisi di tengah
        self.detail_button.setStyleSheet(
            "background-color: #007bff; color: white; border-radius: 5px; font-size: 14px;"
        )
        self.detail_button.clicked.connect(self.show_detail)  # Menghubungkan ke fungsi detail


        # Logout button
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(900, 10, 80, 25))
        self.logout_button.setText("Logout")
        self.logout_button.setStyleSheet(
            "background-color: #dc3545; color: white; border-radius: 5px;"
        )
        self.logout_button.clicked.connect(self.logout)


        # layout pagination
        self.pagination_layout = QtWidgets.QHBoxLayout()
        self.pagination_widget = QtWidgets.QWidget(self.centralwidget)
        self.pagination_widget.setGeometry(QtCore.QRect(20, 320, 960, 40))
        self.pagination_widget.setLayout(self.pagination_layout)

        # element button prev
        self.prev_button = QtWidgets.QPushButton("Previous")
        self.prev_button.setEnabled(False)
        self.prev_button.clicked.connect(self.prev_page)
        self.prev_button.setFixedSize(70, 30)
        self.prev_button.setStyleSheet(
            "background-color: #17a2b8; color: white; border-radius: 5px; font-size: 14px;"
        )

        # element button next 
        self.next_button = QtWidgets.QPushButton("Next")
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.next_page)
        self.next_button.setFixedSize(70, 30)
        self.next_button.setStyleSheet(
            "background-color: #28a745; color: white; border-radius: 5px; font-size: 14px;"
        )

        self.pagination_layout.addWidget(self.prev_button)
        self.pagination_layout.addStretch()
        self.pagination_layout.addWidget(self.next_button)

        # Dummy Data

        # Inisialisasi variabel pagination
        self.current_page = 0  # Menambahkan variabel untuk halaman saat ini
        self.page_size = 5  # Menetapkan jumlah baris yang tampil per halaman
        self.all_data = []  # Menyimpan data yang diambil dari database
        self.populate_table()  # Memanggil fungsi untuk mengisi tabel
        self.update_pagination_buttons()  # Memperbarui tombol pagination

        self.calculate_totals()
        MainWindow.setCentralWidget(self.centralwidget)

    
    # fungsi menampilkan data dari databases ke tabel 
    def populate_table(self):
        if not self.cursor:
            print(
                "Cursor tidak tersedia. Pastikan koneksi database sudah diinisialisasi."
            )
            return

        # Hitung total baris
        count_query = "SELECT COUNT(*) FROM transactions"
        self.cursor.execute(count_query)
        total_rows = self.cursor.fetchone()[0]
        self.total_rows = total_rows

        # Query data untuk halaman saat ini
        offset = self.current_page * self.page_size
        query = "SELECT id, transaction_date, type, amount, description FROM transactions LIMIT %s OFFSET %s"
        self.cursor.execute(query, (self.page_size, offset))
        data = self.cursor.fetchall()

        # Perbarui tabel
        self.table.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, item in enumerate(row_data):
                self.table.setItem(row, col, QtWidgets.QTableWidgetItem(str(item)))
            self.add_action_buttons(row)

        self.update_pagination_buttons()

    # element tombol aksi edit dan hapus
    def add_action_buttons(self, row):
        edit_button = QtWidgets.QPushButton("Edit")
        edit_button.setFixedSize(40, 20)  # Ukuran tombol lebih kecil
        edit_button.setStyleSheet(
            "background-color: #007bff; color: white; border-radius: 5px;"
        )
        edit_button.clicked.connect(lambda checked, row=row: self.edit_row(row))
        edit_button.clicked.connect(lambda: self.edit_row(row))

        # Delete button
        delete_button = QtWidgets.QPushButton("Delete")
        delete_button.setFixedSize(40, 20)  # Ukuran tombol lebih kecil
        delete_button.setStyleSheet(
            "background-color: #dc3545; color: white; border-radius: 5px;"
        )
        delete_button.clicked.connect(lambda checked, row=row: self.delete_row(row))

        # Add buttons to the last column
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        button_layout.setContentsMargins(0, 0, 0, 0)  # Hilangkan margin di layout#-
        button_layout.setSpacing(10)  # Jarak antar tombol#-
        button_layout.setAlignment(
            QtCore.Qt.AlignCenter
        )  # Posisikan tombol di tengah#-
        button_layout.setContentsMargins(0, 0, 0, 0)  # +
        button_layout.setSpacing(10)  # +
        button_layout.setAlignment(QtCore.Qt.AlignCenter)  # +

        button_widget = QtWidgets.QWidget()
        button_widget.setLayout(button_layout)
        self.table.setCellWidget(row, 5, button_widget)
    
    def open_add_window(self):
        # Callback untuk memperbarui tabel
        def refresh_table():
            self.populate_table()  # Memuat ulang data ke tabel
            self.calculate_totals()  # Jika ada hitungan ulang total

        # Buka UI_AddWidget dengan callback
        self.add_window = UI_addWidget(db_connection=self.db_connection, refresh_callback=refresh_table)
        self.add_window.show()

        
    
    # fungsi edit 
    def edit_row(self, row):
        # Ambil data dari baris yang dipilih
        row_data = []
        for col in range(self.table.columnCount() - 1):  # Tidak termasuk kolom "Actions"
            item = self.table.item(row, col)
            row_data.append(item.text() if item else "")

        # Callback untuk memperbarui tabel dan hitung ulang total
        def refresh_table():
            self.populate_table()  # Memperbarui data di tabel
            self.calculate_totals()  # Menghitung ulang total

        # Buka form edit dan teruskan callback
        self.edit_window = UI_EditWidget(
            self.db_connection, transaction_data=row_data, populate_table_callback=refresh_table
        )
        self.edit_window.show()


    def delete_row(self, row):
        # Ambil ID transaksi dari baris yang dipilih
        item = self.table.item(row, 0)  # Asumsi kolom pertama adalah ID
        transaction_id = item.text() if item else None

        if transaction_id:
            # Callback untuk refresh tabel
            def refresh_table():
                self.populate_table()  # Memuat ulang data ke tabel
                self.calculate_totals()  # Jika ada hitungan ulang total

            # Buka UI_DeleteWidget dengan callback
            self.delete_widget = UI_DeleteWidget(
                db_connection=self.db_connection,
                transaction_id=transaction_id,
                refresh_callback=refresh_table,
            )
            self.delete_widget.show()
        else:
            # Jika ID tidak ditemukan
            warning_msg = QtWidgets.QMessageBox(self.main_window)
            warning_msg.setWindowTitle("Peringatan")
            warning_msg.setText("Transaksi tidak ditemukan. Pilih baris yang valid.")
            warning_msg.setIcon(QtWidgets.QMessageBox.Warning)
            warning_msg.setStyleSheet("background-color: black; color: white;")
            warning_msg.exec_()
        # +
    # +
    

    # fungsi search 
    def search(self, search_text):
    # Bersihkan tabel sebelum menampilkan data
        self.table.setRowCount(0)

        if not search_text.strip():
            # Reset pagination ke halaman pertama saat kotak pencarian kosong
            self.current_page = 0
            self.update_table_with_pagination()
        else:
            # Query untuk pencarian
            query = """
            SELECT id, transaction_date, type, amount, description
            FROM transactions
            WHERE id LIKE %s OR transaction_date LIKE %s OR type LIKE %s 
            OR amount LIKE %s OR description LIKE %s
            """
            search_term = f"%{search_text}%"
            self.cursor.execute(query, (search_term, search_term, search_term, search_term, search_term))

            results = self.cursor.fetchall()

            # Tetapkan jumlah kolom di tabel sesuai dengan hasil query
            

            # Tampilkan hasil di tabel tanpa pagination
            for row_number, row_data in enumerate(results):
                self.table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                # Tambahkan tombol aksi (Edit/Delete) ke setiap baris
                self.add_action_buttons(row_number)

            # Nonaktifkan tombol pagination karena semua data sudah ditampilkan
            self.prev_button.setEnabled(False)
            self.next_button.setEnabled(False)
    
    # fungsi update tabel setelah paginasi
    def update_table_with_pagination(self):
        # Query untuk mengambil data berdasarkan pagination
        query = """
        SELECT id, transaction_date, type, amount, description
        FROM transactions
        LIMIT %s OFFSET %s
        """
        self.cursor.execute(query, (self.page_size, self.current_page * self.page_size))

        # Ambil hasil dari query
        results = self.cursor.fetchall()

        # Bersihkan tabel sebelum menampilkan data
        self.table.setRowCount(0)

        # Tampilkan hasil di tabel
        for row_number, row_data in enumerate(results):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            # Tambahkan tombol aksi (Edit/Delete) ke setiap baris
            self.add_action_buttons(row_number)

        # Update tombol pagination
        self.update_pagination_buttons()
    
    # fungsi update tombol setelah pagination
    def update_pagination_buttons(self):
    # Total data yang sesuai dengan pencarian
        total_results_query = """
        SELECT COUNT(*) 
        FROM transactions
        WHERE id LIKE %s OR transaction_date LIKE %s OR type LIKE %s 
            OR amount LIKE %s OR description LIKE %s
        """
        search_term = f"%{self.search_input.text()}%"
        self.cursor.execute(total_results_query, (search_term, search_term, search_term, search_term, search_term))
        total_results = self.cursor.fetchone()[0]

        # Hitung total halaman
        total_pages = (total_results // self.page_size) + (1 if total_results % self.page_size else 0)

        # Perbarui tombol "Previous"
        self.prev_button.setEnabled(self.current_page > 0)

        # Perbarui tombol "Next"
        self.next_button.setEnabled(self.current_page < total_pages - 1)

    # fungsi button prev
    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.populate_table()
    # fungsi button next page
    def next_page(self):
        if (self.current_page + 1) * self.page_size < self.total_rows:
            self.current_page += 1
            self.populate_table()
    
    
    
    def calculate_totals(self):
        try:
            # Query untuk menghitung total Income (Uang Masuk)
            query_income = "SELECT SUM(amount) FROM transactions WHERE type = 'income'"
            self.cursor.execute(query_income)
            total_income = self.cursor.fetchone()[0] or 0  # Jika hasil None, ganti dengan 0

            # Query untuk menghitung total Expense (Uang Keluar)
            query_expense = "SELECT SUM(amount) FROM transactions WHERE type = 'expense'"
            self.cursor.execute(query_expense)
            total_expense = self.cursor.fetchone()[0] or 0  # Jika hasil None, ganti dengan 0

            # Perbarui nilai di input field
            self.total_input.setText(f"Rp {total_income:,.2f}")  # Format angka dengan koma dan dua desimal
            self.total_keluar_input.setText(f"Rp {total_expense:,.2f}")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Terjadi kesalahan saat menghitung total: {str(e)}")

    # fungsi logout
    def logout(self):
        
        if self.db_connection and self.db_connection.is_connected():
            self.db_connection.close()
            print("Koneksi database ditutup.")

        # Tutup window dashboard
        self.main_window.close()

        # Tampilkan window login
        if self.login_window:
            self.login_window.ui.reset_login_form()
            self.login_window.show()

    def show_detail(self):
        self.detail_window = QtWidgets.QMainWindow()
        self.ui_detail = UI_Detail(self.db_connection)
        self.ui_detail.setupUi(self.detail_window)
        self.detail_window.show()
class CenterDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class UI_addWidget(QtWidgets.QWidget):
    def __init__(self, db_connection , refresh_callback=None, parent=None):
        super(UI_addWidget, self).__init__(parent)

        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        
        self.refresh_callback = refresh_callback 
        self.setWindowTitle("tambahkan Transaksi")
        
        self.setGeometry(100, 100, 400, 250)

        # Layout
        self.layout = QtWidgets.QFormLayout(self)

        # Create form fields
        self.id_input = QtWidgets.QLineEdit(self)
        self.date_input = QtWidgets.QLineEdit(self)
        self.type_input = QtWidgets.QLineEdit(self)
        self.amount_input = QtWidgets.QLineEdit(self)
        self.description_input = QtWidgets.QLineEdit(self)

        self.layout.addRow("ID:", self.id_input)
        self.layout.addRow("Tanggal Transaksi:", self.date_input)
        self.layout.addRow("Type:", self.type_input)
        self.layout.addRow("Nominal", self.amount_input)
        self.layout.addRow("Deskripsi:", self.description_input)

        # Submit button
        self.submit_button = QtWidgets.QPushButton("Tambah", self)
        self.submit_button.clicked.connect(self.submit_form)
        self.layout.addWidget(self.submit_button)

        # Style
        self.setStyleSheet("background-color: #000; color: #fff;")
        input_style = (
            "background-color: #000; color: white; border: 1px solid #fff; "
            "padding: 5px; border-radius: 5px;"
        )
        self.id_input.setStyleSheet(input_style)
        self.date_input.setStyleSheet(input_style)
        self.type_input.setStyleSheet(input_style)
        self.amount_input.setStyleSheet(input_style)
        self.description_input.setStyleSheet(input_style)
        button_style = (
            "background-color: rgb(29, 79, 244); color: #fff; padding: 10px; "
            "border: none; border-radius: 5px;"
        )
        self.submit_button.setStyleSheet(button_style)

        # Center the window
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        width = self.width()
        height = self.height()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.move(x, y)
        # self.calculate_totals()

    def submit_form(self):
        # Collect form data
        id_value = self.id_input.text()
        date_value = self.date_input.text()
        type_value = self.type_input.text()
        amount_value = self.amount_input.text()
        description_value = self.description_input.text()

        
        # Validation
        if not all([date_value, type_value, amount_value, description_value]):
            error_msg = QtWidgets.QMessageBox(self)
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.setWindowTitle("Error")
            error_msg.setText("Semua kolom harus diisi!")
            error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error_msg.show()
            QtCore.QTimer.singleShot(1000, error_msg.close)
            return

        try:
            # Handle form submission (insert into the database)
            query = """INSERT INTO transactions (transaction_date, type, amount, description)
                    VALUES (%s, %s, %s, %s)"""
            self.cursor.execute(
                query, (date_value, type_value, amount_value, description_value)
            )
            self.db_connection.commit()

            # Pesan sukses
            success_msg = QtWidgets.QMessageBox(self)
            success_msg.setIcon(QtWidgets.QMessageBox.Information)
            success_msg.setWindowTitle("Success")
            success_msg.setText("Data berhasil ditambahkan.")
            success_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            success_msg.show()

            # Panggil refresh_callback untuk memperbarui tabel
            if self.refresh_callback:
                self.refresh_callback()

            # Tutup form setelah 1 detik
            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            error_msg = QtWidgets.QMessageBox(self)
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.setWindowTitle("Error")
            error_msg.setText(f"Terjadi kesalahan: {str(e)}")
            error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error_msg.show()

    def show_detail(self):
        # Fungsi ini akan menampilkan detail tambahan ketika tombol "Detail" diklik
        detail_message = QtWidgets.QMessageBox()
        detail_message.setWindowTitle("Detail Transaksi")
        detail_message.setText("Fungsi ini dapat diisi dengan detail laporan transaksi.")
        detail_message.setIcon(QtWidgets.QMessageBox.Information)
        detail_message.exec_()

class UI_EditWidget(QtWidgets.QWidget):
    def __init__(self, db_connection, transaction_data=None, populate_table_callback=None, parent=None):
        super(UI_EditWidget, self).__init__(parent)

        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        self.transaction_data = transaction_data
        self.populate_table_callback = populate_table_callback   # Data awal transaksi yang akan diedit
        
        
        self.setWindowTitle("Edit Transaction")
        
        self.setGeometry(100, 100, 400, 250)

        # Layout
        self.layout = QtWidgets.QFormLayout(self)

        # Create form fields
        self.id_input = QtWidgets.QLineEdit(self)
        self.id_input.setReadOnly(True)  # ID tidak bisa diubah
        self.date_input = QtWidgets.QLineEdit(self)
        self.type_input = QtWidgets.QLineEdit(self)
        self.amount_input = QtWidgets.QLineEdit(self)
        self.description_input = QtWidgets.QLineEdit(self)

        self.layout.addRow("ID:", self.id_input)
        self.layout.addRow("Tanggal Transaksi:", self.date_input)
        self.layout.addRow("Type:", self.type_input)
        self.layout.addRow("Amount:", self.amount_input)
        self.layout.addRow("Description:", self.description_input)

        # Submit button
        self.submit_button = QtWidgets.QPushButton("Update", self)
        self.submit_button.clicked.connect(self.submit_form)
        self.layout.addWidget(self.submit_button)

        # Style
        self.setStyleSheet("background-color: #000; color: #fff;")
        input_style = (
            "background-color: #000; color: white; border: 1px solid #fff; "
            "padding: 5px; border-radius: 5px;"
        )
        self.id_input.setStyleSheet(input_style)
        self.date_input.setStyleSheet(input_style)
        self.type_input.setStyleSheet(input_style)
        self.amount_input.setStyleSheet(input_style)
        self.description_input.setStyleSheet(input_style)
        button_style = (
            "background-color: rgb(29, 79, 244); color: #fff; padding: 5px; "
            "border: none; border-radius: 5px;"
        )
        self.submit_button.setStyleSheet(button_style)
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        width = self.width()
        height = self.height()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.move(x, y)

        # Isi data awal ke form
        if self.transaction_data:
            self.id_input.setText(str(self.transaction_data[0]))
            self.date_input.setText(self.transaction_data[1])
            self.type_input.setText(self.transaction_data[2])
            self.amount_input.setText(str(self.transaction_data[3]))
            self.description_input.setText(self.transaction_data[4])


    
        # Validation
    def submit_form(self):
    # Mengambil data dari form
        id_value = self.id_input.text()
        date_value = self.date_input.text()
        type_value = self.type_input.text()
        amount_value = self.amount_input.text()
        description_value = self.description_input.text()

        # Validasi data
        if not all([id_value, date_value, type_value, amount_value, description_value]):
            error_msg = QtWidgets.QMessageBox(self)
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.setWindowTitle("Error")
            error_msg.setText("Semua kolom harus diisi!")
            error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error_msg.show()
            QtCore.QTimer.singleShot(1000, error_msg.close)
            return

        # Konfirmasi update
        confirm = QtWidgets.QMessageBox(self)
        confirm.setWindowTitle("Konfirmasi Update")
        confirm.setText(f"Apakah Anda yakin ingin memperbarui transaksi dengan ID {id_value}?")
        confirm.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        confirm.setDefaultButton(QtWidgets.QMessageBox.No)
        response = confirm.exec_()

        if response == QtWidgets.QMessageBox.Yes:
            # Update data di database
            query = """
            UPDATE transactions
            SET transaction_date = %s, type = %s, amount = %s, description = %s
            WHERE id = %s
            """
            self.cursor.execute(
                query, (date_value, type_value, amount_value, description_value, id_value)
            )
            self.db_connection.commit()

            # Panggil callback untuk memperbarui tabel
            if self.populate_table_callback:
                self.populate_table_callback()

            # Tampilkan pesan sukses
            success_msg = QtWidgets.QMessageBox(self)
            success_msg.setIcon(QtWidgets.QMessageBox.Information)
            success_msg.setWindowTitle("Success")
            success_msg.setText("Data berhasil diperbarui.")
            success_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            success_msg.show()

            # Tutup form setelah 1 detik
            QtCore.QTimer.singleShot(1000, self.close)


        

class UI_DeleteWidget(QtWidgets.QWidget):
    def __init__(self, db_connection, transaction_id=None, refresh_callback=None, parent=None):
        super(UI_DeleteWidget, self).__init__(parent)

        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        self.transaction_id = transaction_id  # ID transaksi yang akan dihapus
        self.refresh_callback = refresh_callback  # Callback untuk refresh tabel

        self.setWindowTitle("Delete Transaction")
        self.setGeometry(100, 100, 400, 200)

        # Layout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Label konfirmasi
        self.label = QtWidgets.QLabel(self)
        self.label.setText(f"Apakah Anda ingin menghapus data dengan ID transaksi {self.transaction_id}?")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Tombol
        self.button_layout = QtWidgets.QHBoxLayout()
        self.yes_button = QtWidgets.QPushButton("Yes", self)
        self.no_button = QtWidgets.QPushButton("No", self)

        yes_button_style = "background-color: green; color: white; padding: 10px ; border-radius: 10px ;"
        no_button_style = "background-color: red; color: white; padding: 10px ; border-radius: 10px ;"
        self.yes_button.setStyleSheet(yes_button_style)
        self.no_button.setStyleSheet(no_button_style)

        self.yes_button.clicked.connect(self.delete_data)
        self.no_button.clicked.connect(self.close)

        self.button_layout.addWidget(self.yes_button)
        self.button_layout.addWidget(self.no_button)
        
        self.layout.addLayout(self.button_layout)

        # Style
        self.setStyleSheet("background-color: #000; color: #fff;")
        label_style = "font-size: 14px; color: #fff;"
        self.label.setStyleSheet(label_style)
        
        
        # set geomatry layout
        
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        width = self.width()
        height = self.height()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.move(x, y)

    def delete_data(self):
        try:
            # Hapus data dari database
            query = "DELETE FROM transactions WHERE id = %s"
            self.cursor.execute(query, (self.transaction_id,))
            self.db_connection.commit()

            # Pesan sukses
            success_msg = QtWidgets.QMessageBox(self)
            success_msg.setIcon(QtWidgets.QMessageBox.Information)
            success_msg.setWindowTitle("Sukses")
            success_msg.setText("Data berhasil dihapus.")
            success_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            success_msg.exec_()

            # Panggil callback untuk refresh tabel
            if self.refresh_callback:
                self.refresh_callback()

            # Tutup form setelah selesai
            self.close()
        except Exception as e:
            # Tangani kesalahan saat penghapusan
            error_msg = QtWidgets.QMessageBox(self)
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.setWindowTitle("Kesalahan")
            error_msg.setText(f"Gagal menghapus data: {str(e)}")
            error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error_msg.exec_()

        


class UI_Detail:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()

    def setupUi(self, DetailWindow):
        DetailWindow.setObjectName("DetailWindow")
        DetailWindow.resize(600, 500)

        # Set background color to white
        DetailWindow.setStyleSheet("background-color: black;")

        self.centralwidget = QtWidgets.QWidget(DetailWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(200, 10, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setText("Detail Transaksi")
        # Change text color to white
        self.title.setStyleSheet("color: white;")

        
        # Table Income
        self.income_table = QtWidgets.QTableWidget(self.centralwidget)
        self.income_table.setGeometry(QtCore.QRect(20, 50, 260, 200))
        self.income_table.setColumnCount(2)
        self.income_table.setHorizontalHeaderLabels(["Income", "Tanggal"])
        self.income_table.horizontalHeader().setStretchLastSection(True)
        self.income_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.income_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.income_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        # Set style for header, data, and scrollbar
        self.income_table.setStyleSheet("""
                QHeaderView::section { 
                    background-color: #333; 
                    color: white; 
                    font-weight: bold; 
                    padding: 4px;
                    border: none;
                    text-align: center;
                }
                QTableWidget::item { 
                    color: white; 
                    background-color: #000;  
                }
                QTableWidget { 
                    background-color: #000; 
                    border: none;
                }
                QTableWidget::item:selected { 
                    background-color: #444;  
                    color: white;
                }
                QScrollBar:vertical {
                    background: #333; 
                    width: 10px; 
                }
                QScrollBar::handle:vertical {
                    background: #555; 
                    min-height: 20px;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    background: none;
                }
            """)

        # Table Expense
        self.expense_table = QtWidgets.QTableWidget(self.centralwidget)
        self.expense_table.setGeometry(QtCore.QRect(320, 50, 260, 200))
        self.expense_table.setColumnCount(2)
        self.expense_table.setHorizontalHeaderLabels(["Expense", "Tanggal"])
        self.expense_table.horizontalHeader().setStretchLastSection(True)
        self.expense_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.expense_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.expense_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        # Set style for header, data, and scrollbar
        # Set style for header, data, and scrollbar
        self.expense_table.setStyleSheet("""
            QHeaderView::section { 
                background-color: #333; 
                color: white; 
                font-weight: bold; 
                padding: 4px;
                border: none;
                text-align: center;
            }
            QTableWidget::item { 
                color: white; 
                background-color: #000;  
            }
            QTableWidget { 
                background-color: #000;  
                border: none;
            }
            QTableWidget::item:selected { 
                background-color: #444;  
                color: white;
            }
            QScrollBar:vertical {
                background: #333; 
                width: 10px; 
            }
            QScrollBar::handle:vertical {
                background: #555; 
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
        """)
        
        # Label and Input for Total Income
        self.income_label = QtWidgets.QLabel(self.centralwidget)
        self.income_label.setGeometry(QtCore.QRect(20, 270, 150, 30))
        font.setPointSize(12)
        self.income_label.setFont(font)
        self.income_label.setText("Total Income:")
        self.income_label.setAlignment(QtCore.Qt.AlignCenter)
        # Style with white text, black background, white border, and rounded corners
        self.income_label.setStyleSheet("""
            color: white; 
            background-color: black; 
            border: 1px solid white; 
            border-radius: 10px; 
            padding: 5px;
        """)

        self.income_input = QtWidgets.QLineEdit(self.centralwidget)
        self.income_input.setGeometry(QtCore.QRect(180, 270, 150, 30))
        self.income_input.setReadOnly(True)
        # Style the input with black background, white border, and rounded corners
        self.income_input.setStyleSheet("""
            background-color: black; 
            color: white; 
            border: 1px solid white; 
            border-radius: 10px; 
            padding: 5px;
        """)

        # Label and Input for Total Expense
        self.expense_label = QtWidgets.QLabel(self.centralwidget)
        self.expense_label.setGeometry(QtCore.QRect(20, 310, 150, 30))
        self.expense_label.setFont(font)
        self.expense_label.setText("Total Expense:")
        self.expense_label.setAlignment(QtCore.Qt.AlignCenter)
        # Style with white text, black background, white border, and rounded corners
        self.expense_label.setStyleSheet("""
            color: white; 
            background-color: black; 
            border: 1px solid white; 
            border-radius: 10px; 
            padding: 5px;
        """)

        self.expense_input = QtWidgets.QLineEdit(self.centralwidget)
        self.expense_input.setGeometry(QtCore.QRect(180, 310, 150, 30))
        self.expense_input.setReadOnly(True)
        # Style the input with black background, white border, and rounded corners
        self.expense_input.setStyleSheet("""
            background-color: black; 
            color: white; 
            border: 1px solid white; 
            border-radius: 10px; 
            padding: 5px;
        """)

        # Label and Input for Total Balance
        self.balance_label = QtWidgets.QLabel(self.centralwidget)
        self.balance_label.setGeometry(QtCore.QRect(20, 350, 150, 30))
        self.balance_label.setFont(font)
        self.balance_label.setText("Total Uang")
        self.balance_label.setAlignment(QtCore.Qt.AlignCenter)
        # Style with white text, black background, white border, and rounded corners
        self.balance_label.setStyleSheet("""
            color: white; 
            background-color: black; 
            border: 1px solid white; 
            border-radius: 10px; 
            padding: 5px;
        """)

        self.balance_input = QtWidgets.QLineEdit(self.centralwidget)
        self.balance_input.setGeometry(QtCore.QRect(180, 350, 150, 30))
        self.balance_input.setReadOnly(True)
        # Style the input with black background, white border, and rounded corners
        self.balance_input.setStyleSheet("""
            background-color: black; 
            color: white; 
            border: 1px solid white; 
            border-radius: 10px; 
            padding: 5px;
        """)

        # Label for Profit/Loss Status
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(20, 390, 560, 40))
        font.setPointSize(14)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        # Style the label with white text, black background, white border, and rounded corners
        self.status_label.setStyleSheet("""
            color: white; 
            background-color: black; 
            border: 1px solid white; 
            border-radius: 10px; 
            padding: 5px;
        """)


        # Populate tables and calculate profit/loss
        self.populate_tables()
        self.calculate_profit_loss()

        DetailWindow.setCentralWidget(self.centralwidget)

    def populate_tables(self):
        # Fetch Income data from database
        query_income = "SELECT amount, transaction_date FROM transactions WHERE type = 'income'"
        self.cursor.execute(query_income)
        income_data = self.cursor.fetchall()
        self.income_table.setRowCount(len(income_data))

        for row_index, row_data in enumerate(income_data):
            amount = str(row_data[0])
            transaction_date = row_data[1].strftime("%Y-%m-%d")
            self.income_table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(amount))
            self.income_table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(transaction_date))

        # Fetch Expense data from database
        query_expense = "SELECT amount, transaction_date FROM transactions WHERE type = 'expense'"
        self.cursor.execute(query_expense)
        expense_data = self.cursor.fetchall()
        self.expense_table.setRowCount(len(expense_data))

        for row_index, row_data in enumerate(expense_data):
            amount = str(row_data[0])
            transaction_date = row_data[1].strftime("%Y-%m-%d")
            self.expense_table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(amount))
            self.expense_table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(transaction_date))

    def calculate_profit_loss(self):
        # Fetch and calculate total income
        query_total_income = "SELECT SUM(amount) FROM transactions WHERE type = 'income'"
        self.cursor.execute(query_total_income)
        total_income = self.cursor.fetchone()[0] or 0

        # Fetch and calculate total expense
        query_total_expense = "SELECT SUM(amount) FROM transactions WHERE type = 'expense'"
        self.cursor.execute(query_total_expense)
        total_expense = self.cursor.fetchone()[0] or 0

        # Calculate total balance
        total_balance = total_income - total_expense

        # Update inputs and status
        self.income_input.setText(f"Rp {total_income:,}")
        self.expense_input.setText(f"Rp {total_expense:,}")
        self.balance_input.setText(f"Rp {total_balance:,}")

        # Update status label
        if total_balance > 0:
            self.status_label.setText("Status: Anda sedang LABA!")
            self.status_label.setStyleSheet("color: green; border: 1px solid green; border-radius: 10px;")
        elif total_balance < 0:
            self.status_label.setText("Status: Anda sedang RUGI!")
            self.status_label.setStyleSheet("color: red; border: 1px solid red; border-radius: 10px;")
        else:
            self.status_label.setText("Status: Tidak ada Laba atau Rugi (NOL).")
            self.status_label.setStyleSheet("color: black; border: 1px solid black; border-radius: 10px;")


 

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
