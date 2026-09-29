from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

Window.size = (1000, 680)

KV = '''
#:import dp kivy.metrics.dp

MDScreen:
    md_bg_color: 0.988, 0.973, 1, 1

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "NEXA"
            left_action_items: [["menu", lambda x: app.open_menu()]]
            right_action_items: [["help-circle-outline", lambda x: app.show_help()]]
            md_bg_color: 0.388, 0.055, 0.831, 1
            specific_text_color: 1, 1, 1, 1
            elevation: 0

        MDBoxLayout:
            orientation: "vertical"
            padding: dp(28)
            spacing: dp(18)

            MDLabel:
                text: "NEXA — Plataforma de Gestão para Clínicas"
                font_size: "24sp"
                bold: True
                theme_text_color: "Primary"
                halign: "left"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "Um ecossistema modular para atendimento, faturamento e gestão."
                theme_text_color: "Secondary"
                halign: "left"
                size_hint_y: None
                height: self.texture_size[1]

            MDGridLayout:
                cols: 2
                spacing: dp(16)
                size_hint_y: None
                height: dp(260)

                MDCard:
                    radius: [16, 16, 16, 16]
                    elevation: 0
                    padding: dp(18)
                    md_bg_color: 1, 1, 1, 1
                    orientation: "vertical"
                    MDLabel:
                        text: "INSTRUA"
                        bold: True
                        font_size: "18sp"
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Agenda, pacientes, confirmações e instruções."
                        theme_text_color: "Secondary"
                    Widget:
                    MDRaisedButton:
                        text: "ABRIR INSTRUA"
                        md_bg_color: 0.388, 0.055, 0.831, 1
                        on_release: app.open_module("Instrua")

                MDCard:
                    radius: [16, 16, 16, 16]
                    elevation: 0
                    padding: dp(18)
                    md_bg_color: 1, 1, 1, 1
                    orientation: "vertical"
                    MDLabel:
                        text: "NEXA BILL"
                        bold: True
                        font_size: "18sp"
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Faturamento, lotes, guias e protocolos."
                        theme_text_color: "Secondary"
                    Widget:
                    MDRaisedButton:
                        text: "ABRIR FATURAMENTO"
                        md_bg_color: 0.388, 0.055, 0.831, 1
                        on_release: app.open_module("Nexa Bill")

                MDCard:
                    radius: [16, 16, 16, 16]
                    elevation: 0
                    padding: dp(18)
                    md_bg_color: 1, 1, 1, 1
                    orientation: "vertical"
                    MDLabel:
                        text: "NEXA ADMIN"
                        bold: True
                        font_size: "18sp"
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Gestão, relatórios e administração."
                        theme_text_color: "Secondary"
                    Widget:
                    MDRaisedButton:
                        text: "ABRIR GESTÃO"
                        md_bg_color: 0.388, 0.055, 0.831, 1
                        on_release: app.open_module("Nexa Admin")

                MDCard:
                    radius: [16, 16, 16, 16]
                    elevation: 0
                    padding: dp(18)
                    md_bg_color: 1, 1, 1, 1
                    orientation: "vertical"
                    MDLabel:
                        text: "CENTRAL"
                        bold: True
                        font_size: "18sp"
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Pesquisa e visão unificada dos dados."
                        theme_text_color: "Secondary"
                    Widget:
                    MDRaisedButton:
                        text: "PESQUISAR"
                        md_bg_color: 0.388, 0.055, 0.831, 1
                        on_release: app.open_module("Central")

            MDCard:
                radius: [16, 16, 16, 16]
                elevation: 0
                padding: dp(20)
                md_bg_color: 1, 1, 1, 1
                orientation: "vertical"
                size_hint_y: 1

                MDLabel:
                    text: "VISÃO DA PLATAFORMA"
                    bold: True
                    font_size: "18sp"
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDBoxLayout:
                    spacing: dp(12)
                    padding: dp(8), dp(12)

                    MDLabel:
                        text: "NEXA\\nPlataforma"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Instrua\\nClínico"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Nexa Bill\\nFaturamento"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Nexa Admin\\nGestão"
                        halign: "center"
                        theme_text_color: "Secondary"

    MDNavigationDrawer:
        id: nav
        radius: [0, 0, 0, 0]
        md_bg_color: 0.988, 0.973, 1, 1

        MDBoxLayout:
            orientation: "vertical"
            padding: dp(22)
            spacing: dp(8)

            MDLabel:
                text: "NEXA"
                font_size: "28sp"
                bold: True
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "Plataforma de gestão para clínicas"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]

            Widget:
                size_hint_y: None
                height: dp(10)

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
