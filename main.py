from datetime import datetime
from pathlib import Path

from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

Window.size = (1000, 680)

KV = '''
MDScreen:
    md_bg_color: 0.96, 0.96, 0.98, 1

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "NEXA"
            left_action_items: [["menu", lambda x: app.open_menu()]]
            right_action_items: [["help-circle-outline", lambda x: app.show_help()]]
            md_bg_color: 0.24, 0.18, 0.45, 1
            specific_text_color: 1, 1, 1, 1
            elevation: 1

        MDBoxLayout:
            padding: "28dp"
            spacing: "18dp"
            orientation: "vertical"

            MDLabel:
                text: "NEXA — Plataforma de Gestão para Clínicas"
                font_style: "H5"
                bold: True
                theme_text_color: "Primary"
                halign: "center"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "Um ecossistema modular para atendimento, faturamento e gestão."
                theme_text_color: "Secondary"
                halign: "center"
                size_hint_y: None
                height: self.texture_size[1]

            MDGridLayout:
                cols: 2
                spacing: "16dp"
                size_hint_y: None
                height: "150dp"

                MDCard:
                    radius: [12, 12, 12, 12]
                    elevation: 1
                    padding: "16dp"
                    orientation: "vertical"
                    MDLabel:
                        text: "🩺 INSTRUA"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Agenda, pacientes, confirmações e instruções."
                        theme_text_color: "Secondary"
                    MDRaisedButton:
                        text: "ABRIR INSTRUA"
                        on_release: app.open_module("Instrua")

                MDCard:
                    radius: [12, 12, 12, 12]
                    elevation: 1
                    padding: "16dp"
                    orientation: "vertical"
                    MDLabel:
                        text: "💰 NEXA BILL"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Faturamento, lotes, guias e protocolos."
                        theme_text_color: "Secondary"
                    MDRaisedButton:
                        text: "ABRIR FATURAMENTO"
                        on_release: app.open_module("Nexa Bill")

                MDCard:
                    radius: [12, 12, 12, 12]
                    elevation: 1
                    padding: "16dp"
                    orientation: "vertical"
                    MDLabel:
                        text: "📊 NEXA ADMIN"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Gestão, relatórios e administração."
                        theme_text_color: "Secondary"
                    MDRaisedButton:
                        text: "ABRIR GESTÃO"
                        on_release: app.open_module("Nexa Admin")

                MDCard:
                    radius: [12, 12, 12, 12]
                    elevation: 1
                    padding: "16dp"
                    orientation: "vertical"
                    MDLabel:
                        text: "🔍 CENTRAL"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Pesquisa e visão unificada dos dados."
                        theme_text_color: "Secondary"
                    MDRaisedButton:
                        text: "PESQUISAR"
                        on_release: app.open_module("Central")

            MDCard:
                radius: [12, 12, 12, 12]
                elevation: 1
                padding: "16dp"
                orientation: "vertical"
                size_hint_y: None
                height: "150dp"

                MDLabel:
                    text: "VISÃO DA PLATAFORMA"
                    bold: True
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDBoxLayout:
                    spacing: "12dp"
                    MDLabel:
                        text: "Produto\nNEXA"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Módulo clínico\nInstrua"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Módulo de faturamento\nNexa Bill"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Módulo administrativo\nNexa Admin"
                        halign: "center"
                        theme_text_color: "Secondary"

    MDNavigationDrawer:
        id: nav
        radius: [0, 0, 0, 0]
        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"
            spacing: "8dp"
            MDLabel:
                text: "NEXA"
                font_style: "H4"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "Plataforma de gestão para clínicas"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]
            OneLineListItem:
                text: "Instrua"
                on_release: app.open_module("Instrua")
            OneLineListItem:
                text: "Nexa Bill"
                on_release: app.open_module("Nexa Bill")
            OneLineListItem:
                text: "Nexa Admin"
                on_release: app.open_module("Nexa Admin")
            OneLineListItem:
                text: "Central"
                on_release: app.open_module("Central")
            OneLineListItem:
                text: "Ajuda"
                on_release: app.show_help()
'''

class NEXA(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        self.title = "NEXA"
        return Builder.load_string(KV)

    def close_menu(self):
        self.root.ids.nav.set_state("close")

    def open_menu(self):
        self.root.ids.nav.set_state("open")

    def open_module(self, module):
        self.close_menu()
        print(f"{module} — módulo selecionado.")

    def show_help(self):
        self.close_menu()
        print("NEXA: escolha Instrua, Nexa Bill, Nexa Admin ou Central.")

if __name__ == "__main__":
    NEXA().run()
