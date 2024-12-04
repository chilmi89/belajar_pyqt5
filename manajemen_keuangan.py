import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
import mysql.connector

# Koneksi Database
def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="manajemen_keuangan",
        )
        if db_connection.is_connected():
            print("Koneksi ke database berhasil")
        return db_connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Halaman Login
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_connection = connect_to_database()
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Header
        header = Label(
            text="LOGIN",
            font_size=24,
            bold=True,
            size_hint=(1, 0.2),
            color=(1, 1, 1, 1),
        )
        layout.add_widget(header)

        # Username
        self.username_input = TextInput(
            hint_text="Username",
            multiline=False,
            size_hint=(1, 0.2),
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
        )
        layout.add_widget(self.username_input)

        # Password
        self.password_input = TextInput(
            hint_text="Password",
            multiline=False,
            password=True,
            size_hint=(1, 0.2),
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
        )
        layout.add_widget(self.password_input)

        # Login Button
        login_button = Button(
            text="Log In",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.4, 0.8, 1),
            on_press=self.login,
        )
        layout.add_widget(login_button)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        if not username or not password:
            self.show_popup("Login Gagal", "Username atau password tidak boleh kosong!")
            return

        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                self.show_popup("Login Berhasil", f"Selamat datang, {result[1]}!")
                self.manager.current = "home"  # Berpindah ke HomeScreen
            else:
                self.show_popup("Login Gagal", "Username atau password salah!")

        except mysql.connector.Error as err:
            self.show_popup("Error", f"Terjadi kesalahan: {err}")

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4),
        )
        popup.open()


# Halaman Utama
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        layout.add_widget(
            Label(
                text="Selamat Datang di Aplikasi Manajemen Keuangan!",
                font_size=18,
                size_hint=(1, 0.2),
            )
        )
        self.add_widget(layout)


# Aplikasi Utama
class FinanceApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        return sm


if __name__ == "__main__":
    FinanceApp().run()
