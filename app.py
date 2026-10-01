from pathlib import Path

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ListProperty
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

from core.database import Database
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
    bg_color = ListProperty([0.031, 0.012, 0.06, 1])
    surface_color = ListProperty([0.05, 0.018, 0.09, 0.96])
    card_color = ListProperty([0.13, 0.06, 0.20, 0.88])
    text_color = ListProperty([0.98, 0.96, 1, 1])
    muted_color = ListProperty([0.72, 0.65, 0.78, 1])
    is_dark = True
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        self.title = "NEXA"
        Window.softinput_mode = "resize"

        self.database = Database(Path(self.user_data_dir) / "nexa.db")
        self.appointments = AppointmentRepository(self.database)
        self.billing = BillingRepository(self.database)

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
        screen_manager.current = "login"

    def show_app_shell(self):
        self.logged_in = True
        self.root.ids.screen_manager.current = "home"

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.theme_cls.theme_style = "Dark" if self.is_dark else "Light"
        if self.is_dark:
            self.bg_color = [0.031, 0.012, 0.06, 1]
            self.surface_color = [0.05, 0.018, 0.09, 0.96]
            self.card_color = [0.13, 0.06, 0.20, 0.88]
            self.text_color = [0.98, 0.96, 1, 1]
            self.muted_color = [0.72, 0.65, 0.78, 1]
        else:
            self.bg_color = [0.96, 0.94, 0.98, 1]
            self.surface_color = [1, 1, 1, 0.96]
            self.card_color = [1, 1, 1, 0.96]
            self.text_color = [0.16, 0.08, 0.22, 1]
            self.muted_color = [0.38, 0.31, 0.45, 1]

    def open_menu(self):
        self.root.ids.nav.set_state("open")

    def close_menu(self):
        self.root.ids.nav.set_state("close")

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
