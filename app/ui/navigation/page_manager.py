"""
Astro Research Lab
Page Manager
"""

from PySide6.QtWidgets import QStackedWidget, QWidget


class PageManager:
    """
    Manages all application pages.
    """

    def __init__(self, stack: QStackedWidget):

        self.stack = stack
        self.pages = {}

    def register_page(
        self,
        name: str,
        widget: QWidget,
    ):

        self.pages[name] = widget

        self.stack.addWidget(widget)

    def show_page(
        self,
        name: str,
    ):

        if name not in self.pages:
            return

        self.stack.setCurrentWidget(
            self.pages[name]
        )

    def contains(
        self,
        name: str,
    ) -> bool:

        return name in self.pages

    def get_page(
        self,
        name: str,
    ):

        return self.pages.get(name)