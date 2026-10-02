from kivy.properties import StringProperty
from screens.base import NexaScreen


class AiScreen(NexaScreen):
    response=StringProperty("Pergunte ao NEXA sobre seus dados, faturamento ou divergências.")

    def ask(self):
        message=self.ids.ai_message.text.strip()
        if not message:
            self.response="Digite uma pergunta primeiro."
            return
        result=self.manager.get_screen("home").app.ai.ask(message) if hasattr(self.manager.get_screen("home"),"app") else None
        if result is None:
            from kivymd.app import MDApp
            result=MDApp.get_running_app().ai.ask(message)
        self.response=result["message"]+"\n\n"+str(result["data"])
