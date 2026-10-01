from kivy.properties import StringProperty
from kivymd.app import MDApp

from screens.base import NexaScreen


class LoginScreen(NexaScreen):
    email = StringProperty("")
    password = StringProperty("")

    def login(self):
        email = self.ids.email_input.text.strip()
        password = self.ids.password_input.text
        if not email or not password:
            self.ids.login_status.text = "Informe e-mail e senha para entrar na demo local."
            return
        app = MDApp.get_running_app()
        app.logged_in = True
        app.show_app_shell()
