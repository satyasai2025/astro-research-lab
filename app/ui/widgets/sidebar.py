"""
Modern Sidebar
Astro Research Lab
"""

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
)

from app.ui.themes.theme import Theme


class Sidebar(QFrame):

    page_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.buttons = {}

        self.setObjectName("Sidebar")

        self.build_ui()

    def build_ui(self):

        self.setFixedWidth(Theme.SIDEBAR_WIDTH)

        self.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Expanding,
        )

        self.setStyleSheet(f"""
            QFrame#Sidebar {{
                background:{Theme.SURFACE};
                border-right:1px solid {Theme.BORDER};
            }}
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            Theme.LG,
            Theme.LG,
            Theme.LG,
            Theme.LG,
        )

        layout.setSpacing(12)

        # --------------------------------------
        # Logo
        # --------------------------------------

        logo = QLabel("✨")

        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logo.setStyleSheet("""
            font-size:40px;
            background:transparent;
        """)

        layout.addWidget(logo)

        title = QLabel("Astro\nResearch Lab")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet(f"""
            QLabel {{
                font-size:{Theme.H2}px;
                font-weight:700;
                color:{Theme.TEXT};
                background:transparent;
            }}
        """)

        layout.addWidget(title)

        layout.addSpacing(25)

        # --------------------------------------
        # Navigation
        # --------------------------------------

        pages = [
            ("🏠 Dashboard", "dashboard"),
            ("👤 Horoscopes", "horoscope"),
            ("🪐 Charts", "charts"),
            ("📈 Dashas", "dashas"),
            ("🌍 Transits", "transits"),
            ("🔬 Research", "research"),
            ("📚 Events", "events"),
            ("📊 Analytics", "analytics"),
            ("📄 Reports", "reports"),
            ("⚙ Settings", "settings"),
        ]

        for text, page in pages:

            button = QPushButton(text)

            button.setCursor(Qt.PointingHandCursor)

            button.setMinimumHeight(48)

            button.setStyleSheet(f"""
                QPushButton {{
                    background:transparent;
                    color:{Theme.TEXT};
                    text-align:left;
                    padding-left:20px;
                    border-radius:12px;
                    font-size:15px;
                    font-weight:600;
                }}

                QPushButton:hover {{
                    background:{Theme.PRIMARY};
                }}

                QPushButton:pressed {{
                    background:{Theme.SECONDARY};
                }}
            """)

            button.clicked.connect(
                lambda checked=False, p=page: self.page_selected.emit(p)
            )

            self.buttons[page] = button

            layout.addWidget(button)

        layout.addStretch()

        version = QLabel("Astro Research Lab\nv0.0.1")

        version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        version.setStyleSheet(f"""
            QLabel {{
                color:{Theme.TEXT_SECONDARY};
                font-size:{Theme.SMALL}px;
                background:transparent;
            }}
        """)

        layout.addWidget(version)

    def highlight(self, page_name: str):

        for page, button in self.buttons.items():

            if page == page_name:

                button.setStyleSheet(f"""
                    QPushButton {{
                        background:{Theme.PRIMARY};
                        color:white;
                        text-align:left;
                        padding-left:20px;
                        border-radius:12px;
                        font-size:15px;
                        font-weight:700;
                    }}
                """)

            else:

                button.setStyleSheet(f"""
                    QPushButton {{
                        background:transparent;
                        color:{Theme.TEXT};
                        text-align:left;
                        padding-left:20px;
                        border-radius:12px;
                        font-size:15px;
                        font-weight:600;
                    }}

                    QPushButton:hover {{
                        background:{Theme.PRIMARY};
                    }}
                """)