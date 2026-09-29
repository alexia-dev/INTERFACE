from pathlib import Path

from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
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


class NEXA(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
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
