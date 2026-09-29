from kivymd.app import MDApp
from screens.base import NexaScreen


class AdminScreen(NexaScreen):
    def save_status(self):
        MDApp.get_running_app().toast("Configurações locais prontas para integração com usuários e permissões.")
