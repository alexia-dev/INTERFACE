from pathlib import Path

from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import BooleanProperty, ListProperty
from kivymd.uix.snackbar import Snackbar

from core.api_client import ApiClient
from core.database import Database
from core.session import Session
from repositories.appointments import AppointmentRepository
from repositories.billing import BillingRepository
from screens.admin import AdminScreen
from screens.bill import BillScreen
from screens.central import CentralScreen
from screens.home import HomeScreen
from screens.instrua import InstruaScreen
from screens.login import LoginScreen


class NEXA(MDApp):
    logged_in = BooleanProperty(False)
    bg_color = ListProperty([0.035, 0.018, 0.075, 1])
    surface_color = ListProperty([0.055, 0.025, 0.11, 0.98])
    card_color = ListProperty([0.08, 0.04, 0.16, 0.92])
    text_color = ListProperty([0.98, 0.94, 1, 1])
    muted_color = ListProperty([0.72, 0.65, 0.80, 1])
    is_dark = True
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        self.title = "NEXA"
        Window.softinput_mode = "resize"

        # The local DB remains a cache/compatibility layer for now.
        self.database = Database(Path(self.user_data_dir) / "nexa.db")
        self.appointments = AppointmentRepository(self.database)
        self.billing = BillingRepository(self.database)

        self.api = ApiClient()
        self.session = Session()

        root_dir = Path(__file__).resolve().parent
        for filename in (
            "theme.kv",
            "home.kv",
            "instrua.kv",
            "bill.kv",
            "admin.kv",
            "central.kv",
            "login.kv",
        ):
            Builder.load_file(str(root_dir / "ui" / filename))

        root = Builder.load_file(str(root_dir / "ui" / "app.kv"))
        self._build_screens(root)
        return root

    @staticmethod
    def _build_screens(root):
        screen_manager = root.ids.screen_manager
        screens = (
            (HomeScreen, "home"),
            (InstruaScreen, "instrua"),
            (BillScreen, "bill"),
            (AdminScreen, "admin"),
            (CentralScreen, "central"),
        )
        for screen_class, name in screens:
            screen_manager.add_widget(screen_class(name=name))
        screen_manager.add_widget(LoginScreen(name="login"))

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.theme_cls.theme_style = "Dark" if self.is_dark else "Light"
        if self.is_dark:
            self.bg_color = [0.035, 0.018, 0.075, 1]
            self.surface_color = [0.055, 0.025, 0.11, 0.98]
            self.card_color = [0.08, 0.04, 0.16, 0.92]
            self.text_color = [0.98, 0.94, 1, 1]
            self.muted_color = [0.72, 0.65, 0.80, 1]
        else:
            self.bg_color = [0.97, 0.95, 0.99, 1]
            self.surface_color = [1, 1, 1, 0.98]
            self.card_color = [1, 1, 1, 1]
            self.text_color = [0.16, 0.08, 0.22, 1]
            self.muted_color = [0.38, 0.31, 0.45, 1]

    def configure_api(self, base_url: str) -> None:
        self.api.configure(base_url)

    def apply_login(self, auth_response: dict) -> None:
        self.session.apply_auth_response(auth_response)

    def logout(self) -> None:
        self.api.clear_session()
        self.session.clear()
        self.go_home()

    def open_menu(self):
        self.root.ids.nav.set_state("open")

    def close_menu(self):
        self.root.ids.nav.set_state("close")

    def show_app_shell(self):
        self.root.ids.screen_manager.current = "home"

    def go_home(self):
        self.close_menu()
        self.root.ids.screen_manager.current = "home"

    def open_module(self, module):
        routes = {
            "Instrua": "instrua",
            "Nexa Bill": "bill",
            "Nexa Admin": "admin",
            "Central": "central",
        }
        self.close_menu()
        self.root.ids.screen_manager.current = routes.get(module, "home")

    def show_help(self):
        self.toast("Use o menu para acessar os módulos do NEXA.")

    def toast(self, message):
        Snackbar(text=message).open()


if __name__ == "__main__":
    NEXA().run()
