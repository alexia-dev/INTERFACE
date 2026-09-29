from screens.base import NexaScreen


class HomeScreen(NexaScreen):
    """Home/Central shell for the NEXA application ecosystem."""

    def open_app(self, app_id: str) -> None:
        self.dispatch("on_open_app", app_id)

    def on_open_app(self, app_id: str) -> None:
        """Hook for future app launcher integrations."""
        return None
