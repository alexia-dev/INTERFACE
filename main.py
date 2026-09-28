from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.list import OneLineListItem
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
from datetime import datetime
import os
import pandas as pd

Window.size = (1000, 680)

KV = '''
MDScreen:
    md_bg_color: 0.95, 0.97, 1, 1

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "SIFAC"
            left_action_items: [["menu", lambda x: app.open_menu()]]
            right_action_items: [["help-circle-outline", lambda x: app.show_help()]]
            md_bg_color: 0.12, 0.35, 0.65, 1
            specific_text_color: 1, 1, 1, 1
            elevation: 1

        MDBoxLayout:
            padding: "28dp"
            spacing: "18dp"
            orientation: "vertical"

            MDLabel:
                text: "SIFAC — Sistema de Faturamento e Relatórios"
                font_style: "H5"
                bold: True
                theme_text_color: "Primary"
                halign: "center"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "Controle simples de faturamentos, lotes e relatórios"
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
                        text: "📊 CONTROLE"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Acompanhe o faturamento por mês e ano."
                        theme_text_color: "Secondary"
                    MDRaisedButton:
                        text: "ABRIR CONTROLE"
                        on_release: app.show_control()

                MDCard:
                    radius: [12, 12, 12, 12]
                    elevation: 1
                    padding: "16dp"
                    orientation: "vertical"
                    MDLabel:
                        text: "➕ NOVO LOTE"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Cadastre um novo lote de faturamento."
                        theme_text_color: "Secondary"
                    MDRaisedButton:
                        text: "LANÇAR LOTE"
                        on_release: app.new_lot()

                MDCard:
                    radius: [12, 12, 12, 12]
                    elevation: 1
                    padding: "16dp"
                    orientation: "vertical"
                    MDLabel:
                        text: "🔎 PESQUISAR"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Consulte registros e pacientes."
                        theme_text_color: "Secondary"
                    MDRaisedButton:
                        text: "PESQUISAR"
                        on_release: app.search_records()

                MDCard:
                    radius: [12, 12, 12, 12]
                    elevation: 1
                    padding: "16dp"
                    orientation: "vertical"
                    MDLabel:
                        text: "📄 RELATÓRIOS"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Exporte dados para Excel."
                        theme_text_color: "Secondary"
                    MDRaisedButton:
                        text: "GERAR RELATÓRIO"
                        on_release: app.generate_report()

            MDCard:
                radius: [12, 12, 12, 12]
                elevation: 1
                padding: "16dp"
                orientation: "vertical"
                size_hint_y: None
                height: "160dp"

                MDLabel:
                    text: "VISÃO INICIAL"
                    bold: True
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDBoxLayout:
                    spacing: "12dp"
                    MDLabel:
                        text: "Ano\n2026"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Meses lançados\n06 a 09"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Guias registradas\n132"
                        halign: "center"
                        theme_text_color: "Secondary"
                    MDLabel:
                        text: "Faturamento\nR$ 46.756,73"
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
                text: "SIFAC"
                font_style: "H4"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "Menu principal"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]
            OneLineListItem:
                text: "Controle de faturamento"
                on_release: app.show_control()
            OneLineListItem:
                text: "Novo lote"
                on_release: app.new_lot()
            OneLineListItem:
                text: "Pesquisar"
                on_release: app.search_records()
            OneLineListItem:
                text: "Relatórios"
                on_release: app.generate_report()
            OneLineListItem:
                text: "Ajuda"
                on_release: app.show_help()
'''

class SIFAC(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.title = "SIFAC"
        return Builder.load_string(KV)

    def close_menu(self):
        self.root.ids.nav.set_state("close")

    def open_menu(self):
        self.root.ids.nav.set_state("open")

    def show_control(self):
        self.close_menu()
        print("Controle de faturamento — estrutura inicial pronta.")

    def new_lot(self):
        self.close_menu()
        print("Novo lote — formulário inicial pronto para evolução.")

    def search_records(self):
        self.close_menu()
        print("Pesquisa — estrutura inicial pronta para evolução.")

    def generate_report(self):
        self.close_menu()
        data = {
            "Sistema": ["SIFAC"],
            "Data de geração": [datetime.now().strftime("%d/%m/%Y %H:%M")],
            "Observação": ["Estrutura inicial do relatório."]
        }
        filename = f"sifac_relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        pd.DataFrame(data).to_excel(filename, index=False)
        print(f"Relatório criado: {os.path.abspath(filename)}")

    def show_help(self):
        self.close_menu()
        print("SIFAC: use Controle, Novo lote, Pesquisar ou Relatórios.")

if __name__ == "__main__":
    SIFAC().run()
