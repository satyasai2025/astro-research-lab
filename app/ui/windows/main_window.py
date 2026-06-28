"""
Main Window
Astro Research Lab
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QStatusBar,
    QWidget,
)

from app.config.settings import (
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
    MINIMUM_WIDTH,
    MINIMUM_HEIGHT,
)

from app.ui.navigation.page_manager import PageManager
from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.horoscope_page import HoroscopePage
from app.ui.themes.theme import Theme
from app.ui.widgets.sidebar import Sidebar


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.sidebar = None
        self.stack = None
        self.page_manager = None

        self.initialize_window()

        self.build_ui()

    # ----------------------------------------------------

    def initialize_window(self):

        self.setWindowTitle(WINDOW_TITLE)

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

        self.setMinimumSize(
            MINIMUM_WIDTH,
            MINIMUM_HEIGHT,
        )

        self.setStyleSheet(
            Theme.stylesheet()
        )

    # ----------------------------------------------------

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.setSpacing(0)

        central.setLayout(layout)

        # ---------------- Sidebar ----------------

        self.sidebar = Sidebar()

        layout.addWidget(self.sidebar)

        # ---------------- Pages ----------------

        self.stack = QStackedWidget()

        layout.addWidget(
            self.stack,
            1,
        )

        self.page_manager = PageManager(
            self.stack
        )

        self.page_manager.register_page(
            "dashboard",
            DashboardPage(),
        )

        self.page_manager.register_page(
            "horoscope",
            HoroscopePage(),
        )

        self.page_manager.show_page(
            "dashboard"
        )

        self.sidebar.highlight(
            "dashboard"
        )

        self.sidebar.page_selected.connect(
            self.change_page
        )

        self.build_statusbar()

    # ----------------------------------------------------

    def change_page(
        self,
        page_name: str,
    ):

        if self.page_manager.contains(
            page_name
        ):

            self.page_manager.show_page(
                page_name
            )

            self.sidebar.highlight(
                page_name
            )

    # ----------------------------------------------------

    def build_statusbar(self):

        status = QStatusBar()

        self.setStatusBar(
            status
        )

        label = QLabel(
            "Ready"
        )

        label.setAlignment(
            Qt.AlignmentFlag.AlignLeft
        )

        status.addPermanentWidget(
            label
        )