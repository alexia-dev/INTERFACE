from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem, ILeftBody
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.pickers import MDDatePicker
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from datetime import datetime
import pandas as pd
import os

Window.size = (900, 600)

# Classe para checkbox no menu
class LeftCheckbox(ILeftBody, MDCheckbox):
    pass

KV = '''
<DrawerItem>:
    LeftCheckbox:
        active: root.active
        size_hint: None, None
        size: "24dp", "24dp"

MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: [0.9, 0.95, 1, 1]  # Fundo azul claro
    
    MDTopAppBar:
        title: "SISTEMA DE RELATÓRIOS"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [["text-long", lambda x: app.change_font_size(1)], ["text-short", lambda x: app.change_font_size(-1)]]
        md_bg_color: [0.1, 0.4, 0.8, 1]  # Azul médio
        elevation: 0
        specific_text_color: [1, 1, 1, 1]  # Texto branco
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: '40dp'
        spacing: '20dp'
        
        MDLabel:
            text: "SISTEMA DE GESTÃO DE RELATÓRIOS"
            halign: "center"
            bold: True
            font_style: "H5"
            size_hint_y: None
            height: self.texture_size[1]
            theme_text_color: "Primary"
            font_size: app.font_size + 2  # Tamanho de fonte ajustável
        
        MDLabel:
            text: "Selecione o tipo de relatório e as datas desejadas"
            halign: "center"
            font_style: "H6"
            size_hint_y: None
            height: self.texture_size[1]
            theme_text_color: "Secondary"
            font_size: app.font_size
        
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: '20dp'
            size_hint_y: None
            height: "50dp"
            padding: '20dp'
            
            MDLabel:
                text: "Data Início:"
                size_hint_x: None
                width: "100dp"
                halign: "right"
                font_size: app.font_size
            
            MDTextField:
                id: start_date
                hint_text: "DD/MM/AAAA"
                text: app.start_date
                size_hint_x: 0.4
                font_size: app.font_size
                on_focus: if self.focus: app.show_date_picker("start")
            
            MDLabel:
                text: "Data Fim:"
                size_hint_x: None
                width: "100dp"
                halign: "right"
                font_size: app.font_size
            
            MDTextField:
                id: end_date
                hint_text: "DD/MM/AAAA"
                text: app.end_date
                size_hint_x: 0.4
                font_size: app.font_size
                on_focus: if self.focus: app.show_date_picker("end")
        
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '10dp'
            padding: '20dp'
            size_hint_y: None
            height: "150dp"
            
            MDLabel:
                text: "Tipo de Relatório:"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
                font_size: app.font_size
            
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: '20dp'
                
                MDRaisedButton:
                    text: "Financeiro"
                    on_release: app.select_report_type("financeiro")
                    md_bg_color: [0.1, 0.5, 0.9, 1] if app.report_type == "financeiro" else [0.7, 0.8, 0.9, 1]
                    theme_text_color: "Custom"
                    text_color: [1, 1, 1, 1]
                    font_size: app.font_size
                
                MDRaisedButton:
                    text: "Comercial"
                    on_release: app.select_report_type("comercial")
                    md_bg_color: [0.1, 0.5, 0.9, 1] if app.report_type == "comercial" else [0.7, 0.8, 0.9, 1]
                    theme_text_color: "Custom"
                    text_color: [1, 1, 1, 1]
                    font_size: app.font_size
                
                MDRaisedButton:
                    text: "Cobrança"
                    on_release: app.select_report_type("cobranca")
                    md_bg_color: [0.1, 0.5, 0.9, 1] if app.report_type == "cobranca" else [0.7, 0.8, 0.9, 1]
                    theme_text_color: "Custom"
                    text_color: [1, 1, 1, 1]
                    font_size: app.font_size
        
        MDRaisedButton:
            text: "GERAR RELATÓRIO"
            icon: "file-excel"
            size_hint: None, None
            size: "300dp", "50dp"
            pos_hint: {"center_x": 0.5}
            md_bg_color: [0.1, 0.4, 0.8, 1]
            theme_text_color: "Custom"
            text_color: [1, 1, 1, 1]
            font_size: app.font_size
            on_release: app.generate_report()
    
    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 0, 0, 0)  # Bordas retas
        elevation: 0  # Sem sombra
        md_bg_color: [1, 1, 1, 0.9]  # Fundo branco com transparência
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '20dp'
            adaptive_height: True
            
            MDLabel:
                text: "SISTEMA DE RELATÓRIOS"
                font_style: "H4"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Primary"
                font_size: app.font_size + 4
            
            MDLabel:
                text: "SISTEMA DE GESTÃO DE DOCUMENTOS"
                font_style: "Caption"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Secondary"
                font_size: app.font_size
            
            ScrollView:
                MDList:
                    id: menu_list
                    padding: 0
                    spacing: '10dp'
'''

class DrawerItem(OneLineAvatarIconListItem):
    active = BooleanProperty(False)

class SistemaRelatorios(MDApp):
    report_type = StringProperty("financeiro")
    start_date = StringProperty("")
    end_date = StringProperty("")
    font_size = NumericProperty(16)  # Tamanho base da fonte
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Definir datas padrão (primeiro e último dia do mês atual)
        today = datetime.today()
        self.start_date = f"01/{today.month:02d}/{today.year}"
        self.end_date = f"{today.day:02d}/{today.month:02d}/{today.year}"
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
    
    def on_start(self):
        menu_items = [
            {"text": "Financeiro", "active": False},
            {"text": "Comercial", "active": False},
            {"text": "Cobrança", "active": False},
            {"text": "Histórico", "active": True},
            {"text": "Ajuda", "active": False}
        ]
        
        for item in menu_items:
            list_item = DrawerItem(text=item["text"])
            list_item.active = item["active"]
            list_item.bind(on_release=self.select_menu_item)
            self.root.ids.menu_list.add_widget(list_item)
    
    def select_menu_item(self, instance):
        # Desmarca todos os itens
        for item in self.root.ids.menu_list.children:
            if hasattr(item, 'active'):
                item.active = False
                
        # Marca o item selecionado
        instance.active = True
        self.root.ids.nav_drawer.set_state("close")
        
        # Define o tipo de relatório baseado na seleção
        if "Financeiro" in instance.text:
            self.select_report_type("financeiro")
        elif "Comercial" in instance.text:
            self.select_report_type("comercial")
        elif "Cobrança" in instance.text:
            self.select_report_type("cobranca")
        elif "Histórico" in instance.text:
            self.show_report_history()
        elif "Ajuda" in instance.text:
            self.help()
    
    def select_report_type(self, report_type):
        self.report_type = report_type
        print(f"Tipo de relatório selecionado: {report_type.capitalize()}")
    
    def show_date_picker(self, field):
        """Abre o date picker para o campo especificado"""
        current_date = self.start_date if field == "start" else self.end_date
        try:
            day, month, year = map(int, current_date.split('/'))
            date_obj = datetime(year, month, day)
        except:
            date_obj = datetime.now()
        
        picker = MDDatePicker(
            year=date_obj.year,
            month=date_obj.month,
            day=date_obj.day,
            on_save=lambda instance, value, date_range: self.set_date(field, value)
        )
        picker.open()
    
    def set_date(self, field, date):
        """Define a data no campo apropriado"""
        formatted_date = date.strftime("%d/%m/%Y")
        if field == "start":
            self.start_date = formatted_date
        else:
            self.end_date = formatted_date
    
    def generate_report(self):
        if not self.report_type:
            print("Selecione um tipo de relatório antes de gerar")
            return
            
        start = self.root.ids.start_date.text
        end = self.root.ids.end_date.text
        
        print(f"Gerando relatório {self.report_type.upper()}...")
        print(f"Período: {start} a {end}")
        
        # Criar um DataFrame de exemplo (substituir por dados reais)
        data = {
            'Item': ['Vendas', 'Custos', 'Lucro'],
            'Valor': [150000, 85000, 65000]
        }
        df = pd.DataFrame(data)
        
        # Gerar o arquivo Excel
        filename = f"relatorio_{self.report_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        df.to_excel(filename, index=False)
        
        print(f"Relatório gerado com sucesso! Salvo como {filename}")
        
        # Mostrar mensagem de sucesso
        from kivymd.uix.dialog import MDDialog
        dialog = MDDialog(
            title="Relatório Gerado",
            text=f"Relatório {self.report_type.capitalize()} salvo como {filename}",
            buttons=[
                MDRaisedButton(
                    text="Abrir Pasta",
                    on_release=lambda _: self.open_folder(filename)
                ),
                MDFlatButton(
                    text="OK",
                    on_release=lambda _: dialog.dismiss()
                )
            ]
        )
        dialog.open()
    
    def open_folder(self, filename):
        """Abre a pasta onde o arquivo foi salvo"""
        try:
            folder = os.path.dirname(os.path.abspath(filename))
            os.startfile(folder)  # Funciona no Windows
        except:
            print(f"Pasta não encontrada: {folder}")
    
    def change_font_size(self, delta):
        """Altera o tamanho da fonte"""
        self.font_size = max(12, min(24, self.font_size + delta))
        print(f"Tamanho da fonte alterado para: {self.font_size}")
    
    def show_report_history(self):
        print("Mostrando histórico de relatórios...")
    
    def help(self):
        print("Abrindo ajuda...")
    
    def exit_app(self):
        print("Saindo do aplicativo...")
        self.stop()

if __name__ == "__main__":
    SistemaRelatorios().run()