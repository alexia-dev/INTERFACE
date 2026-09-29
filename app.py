from pathlib import Path

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp

from core.database import Database
from repositories.appointments import AppointmentRepository
from repositories.billing import BillingRepository
from screens.admin import AdminScreen
from screens.bill import BillScreen
from screens.central import CentralScreen
from screens.home import HomeScreen
from screens.instrua import InstruaScreen


class NEXA(MDApp):
    database = ObjectProperty(None)
    appointments = ObjectProperty(None)
    billing = ObjectProperty(None)

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        self.title = "NEXA"

        # Keep the Android keyboard from covering the active form field.
        Window.softinput_mode = "resize"

        # Kivy provides a writable per-app directory on each target platform.
        self.database = Database(Path(self.user_data_dir) / "nexa.db")
        self.appointments = AppointmentRepository(self.database)
        self.billing = BillingRepository(self.database)

        root = Path(__file__).resolve().parent
        for filename in (
            "theme.kv",
            "app.kv",
            "home.kv",
            "instrua.kv",
            "bill.kv",
            "admin.kv",
            "central.kv",
        ):
            Builder.load_file(str(root / "ui" / filename))

        screen_manager = self._build_screens()
        self._configure_mobile_window()
        return screen_manager

    def _build_screens(self):
        screen_manager = self.root.ids.screen_manager
        screens = (
            (HomeScreen, "home"),
            (InstruaScreen, "instrua"),
            (BillScreen, "bill"),
            (AdminScreen, "admin"),
            (CentralScreen, "central"),
        )
        for screen_class, name in screens:
            screen_manager.add_widget(screen_class(name=name))
        return self.root

    def _configure_mobile_window(self):
        # Portrait is the primary Android layout; desktop remains resizable.
        if Window.width < 700:
            Window.fullscreen = False

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
        try:
            from kivymd.uix.snackbar import Snackbar
            Snackbar(text=message).open()
        except Exception:
            print(message)


if __name__ == "__main__":
    NEXA().run()
