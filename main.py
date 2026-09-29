from datetime import datetime

from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

Window.size = (1000, 680)

KV = '''
#:import dp kivy.metrics.dp

MDScreenManager:
    id: screens

    MDScreen:
        name: "home"
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
            MDScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    padding: dp(28)
                    spacing: dp(18)
                    size_hint_y: None
                    height: self.minimum_height
                    MDLabel:
                        text: "NEXA — Plataforma de Gestão para Clínicas"
                        font_size: "24sp"
                        bold: True
                        theme_text_color: "Primary"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Um ecossistema modular para atendimento, faturamento e gestão."
                        theme_text_color: "Secondary"
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
                                text: "ABRIR CENTRAL"
                                md_bg_color: 0.388, 0.055, 0.831, 1
                                on_release: app.open_module("Central")
                    MDCard:
                        radius: [16, 16, 16, 16]
                        elevation: 0
                        padding: dp(20)
                        md_bg_color: 1, 1, 1, 1
                        orientation: "vertical"
                        size_hint_y: None
                        height: dp(150)
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

    MDScreen:
        name: "instrua"
        md_bg_color: 0.988, 0.973, 1, 1
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "NEXA / INSTRUA"
                left_action_items: [["arrow-left", lambda x: app.go_home()]]
                md_bg_color: 0.388, 0.055, 0.831, 1
                specific_text_color: 1, 1, 1, 1
            MDScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    padding: dp(24)
                    spacing: dp(14)
                    size_hint_y: None
                    height: self.minimum_height
                    MDLabel:
                        text: "Agenda e atendimento"
                        font_size: "22sp"
                        bold: True
                        theme_text_color: "Primary"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDCard:
                        radius: [16, 16, 16, 16]
                        elevation: 0
                        padding: dp(16)
                        orientation: "vertical"
                        size_hint_y: None
                        height: dp(190)
                        md_bg_color: 1, 1, 1, 1
                        MDTextField:
                            id: patient_input
                            hint_text: "Nome do paciente"
                            mode: "rectangle"
                        MDTextField:
                            id: appointment_input
                            hint_text: "Consulta / procedimento"
                            mode: "rectangle"
                        MDRaisedButton:
                            text: "AGENDAR"
                            md_bg_color: 0.388, 0.055, 0.831, 1
                            on_release: app.add_appointment()
                        MDLabel:
                            id: appointment_status
                            text: "Nenhum novo agendamento."
                            theme_text_color: "Secondary"
                    MDLabel:
                        text: "Próximos atendimentos"
                        bold: True
                        font_size: "18sp"
                        theme_text_color: "Primary"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDCard:
                        radius: [16, 16, 16, 16]
                        elevation: 0
                        padding: dp(16)
                        orientation: "vertical"
                        size_hint_y: None
                        height: dp(170)
                        md_bg_color: 1, 1, 1, 1
                        MDLabel:
                            text: "09:00  •  Maria Silva  •  Consulta"
                        MDLabel:
                            text: "10:30  •  João Santos  •  Retorno"
                        MDLabel:
                            text: "14:00  •  Ana Souza  •  Exame"

    MDScreen:
        name: "bill"
        md_bg_color: 0.988, 0.973, 1, 1
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "NEXA / NEXA BILL"
                left_action_items: [["arrow-left", lambda x: app.go_home()]]
                md_bg_color: 0.388, 0.055, 0.831, 1
                specific_text_color: 1, 1, 1, 1
            MDScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    padding: dp(24)
                    spacing: dp(14)
                    size_hint_y: None
                    height: self.minimum_height
                    MDLabel:
                        text: "Faturamento"
                        font_size: "22sp"
                        bold: True
                        theme_text_color: "Primary"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDCard:
                        radius: [16, 16, 16, 16]
                        elevation: 0
                        padding: dp(16)
                        orientation: "vertical"
                        size_hint_y: None
                        height: dp(190)
                        md_bg_color: 1, 1, 1, 1
                        MDTextField:
                            id: bill_patient
                            hint_text: "Paciente / atendimento"
                            mode: "rectangle"
                        MDTextField:
                            id: bill_value
                            hint_text: "Valor (ex.: 350,00)"
                            mode: "rectangle"
                        MDRaisedButton:
                            text: "LANÇAR FATURAMENTO"
                            md_bg_color: 0.388, 0.055, 0.831, 1
                            on_release: app.add_bill()
                        MDLabel:
                            id: bill_status
                            text: "Nenhum lançamento nesta sessão."
                            theme_text_color: "Secondary"
                    MDLabel:
                        text: "Lançamentos recentes"
                        bold: True
                        font_size: "18sp"
                        theme_text_color: "Primary"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDCard:
                        radius: [16, 16, 16, 16]
                        elevation: 0
                        padding: dp(16)
                        orientation: "vertical"
                        size_hint_y: None
                        height: dp(140)
                        md_bg_color: 1, 1, 1, 1
                        MDLabel:
                            text: "GUIA 0001  •  Maria Silva  •  R$ 350,00"
                        MDLabel:
                            text: "GUIA 0002  •  João Santos  •  R$ 180,00"

    MDScreen:
        name: "admin"
        md_bg_color: 0.988, 0.973, 1, 1
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "NEXA / NEXA ADMIN"
                left_action_items: [["arrow-left", lambda x: app.go_home()]]
                md_bg_color: 0.388, 0.055, 0.831, 1
                specific_text_color: 1, 1, 1, 1
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(24)
                spacing: dp(14)
                MDLabel:
                    text: "Administração"
                    font_size: "22sp"
                    bold: True
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDCard:
                    radius: [16, 16, 16, 16]
                    elevation: 0
                    padding: dp(16)
                    orientation: "vertical"
                    md_bg_color: 1, 1, 1, 1
                    MDLabel:
                        text: "USUÁRIOS E PERFIS"
                        bold: True
                        theme_text_color: "Primary"
                    MDLabel:
                        text: "Administradores  •  2"
                    MDLabel:
                        text: "Recepção  •  4"
                    MDLabel:
                        text: "Faturamento  •  2"
                    MDLabel:
                        text: "Clínico  •  6"
                    MDLabel:
                        text: "Auditoria: ativa"
                    MDRaisedButton:
                        text: "ATUALIZAR CONFIGURAÇÕES"
                        md_bg_color: 0.388, 0.055, 0.831, 1
                        on_release: app.show_admin_status()

    MDScreen:
        name: "central"
        md_bg_color: 0.988, 0.973, 1, 1
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "NEXA / CENTRAL"
                left_action_items: [["arrow-left", lambda x: app.go_home()]]
                md_bg_color: 0.388, 0.055, 0.831, 1
                specific_text_color: 1, 1, 1, 1
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(24)
                spacing: dp(14)
                MDLabel:
                    text: "Pesquisa unificada"
                    font_size: "22sp"
                    bold: True
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDTextField:
                    id: search_input
                    hint_text: "Pesquisar paciente, guia ou atendimento"
                    mode: "rectangle"
                MDRaisedButton:
                    text: "PESQUISAR"
                    md_bg_color: 0.388, 0.055, 0.831, 1
                    on_release: app.search_central()
                MDCard:
                    radius: [16, 16, 16, 16]
                    elevation: 0
                    padding: dp(16)
                    size_hint_y: None
                    height: dp(170)
                    md_bg_color: 1, 1, 1, 1
                    MDLabel:
                        id: search_result
                        text: "Digite algo para pesquisar nos dados da sessão."
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
                text: "Início"
                on_release: app.go_home()
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

    def go_home(self):
        self.close_menu()
        self.root.current = "home"

    def open_module(self, module):
        self.close_menu()
        routes = {"Instrua": "instrua", "Nexa Bill": "bill", "Nexa Admin": "admin", "Central": "central"}
        self.root.current = routes.get(module, "home")

    def add_appointment(self):
        screen = self.root.get_screen("instrua")
        patient = screen.ids.patient_input.text.strip()
        appointment = screen.ids.appointment_input.text.strip()
        if not patient or not appointment:
            screen.ids.appointment_status.text = "Preencha paciente e consulta."
            return
        now = datetime.now().strftime("%d/%m %H:%M")
        screen.ids.appointment_status.text = f"Agendado: {patient} • {appointment} • {now}"
        screen.ids.patient_input.text = ""
        screen.ids.appointment_input.text = ""

    def add_bill(self):
        screen = self.root.get_screen("bill")
        patient = screen.ids.bill_patient.text.strip()
        value = screen.ids.bill_value.text.strip()
        if not patient or not value:
            screen.ids.bill_status.text = "Preencha atendimento e valor."
            return
        screen.ids.bill_status.text = f"Lançamento criado: {patient} • R$ {value}"
        screen.ids.bill_patient.text = ""
        screen.ids.bill_value.text = ""

    def search_central(self):
        screen = self.root.get_screen("central")
        query = screen.ids.search_input.text.strip()
        screen.ids.search_result.text = (
            "Digite algo para pesquisar." if not query
            else f"Pesquisa por '{query}'\\n\\nResultado demonstrativo: Central pronta para integração com a base do NEXA."
        )

    def show_admin_status(self):
        print("NEXA Admin: configurações atualizadas nesta sessão.")

    def show_help(self):
        self.close_menu()
        self.root.current = "home"

if __name__ == "__main__":
    NEXA().run()
