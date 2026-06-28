"""
Dashboard Page
Astro Research Lab
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout

from app.ui.widgets.dashboard import Dashboard


class DashboardPage(QWidget):
    """
    Wrapper page for the Dashboard widget.
    """

    def __init__(self):
        super().__init__()

        self.dashboard = Dashboard()

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.dashboard)

        self.setLayout(layout)