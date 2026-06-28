"""
Modern Dashboard
Astro Research Lab
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
)

from app.ui.themes.theme import Theme


class Dashboard(QFrame):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding,
        )

        self.setStyleSheet(f"""
            QFrame {{
                background:{Theme.BACKGROUND};
            }}
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            Theme.XL,
            Theme.XL,
            Theme.XL,
            Theme.XL,
        )

        layout.setSpacing(Theme.LG)

        # ---------------------------------------------------
        # Header
        # ---------------------------------------------------

        title = QLabel("Dashboard")

        title.setStyleSheet(f"""
            QLabel {{
                font-size:{Theme.H1}px;
                font-weight:700;
                color:{Theme.TEXT};
                background:transparent;
            }}
        """)

        subtitle = QLabel(
            "Professional Astrology Research Platform"
        )

        subtitle.setStyleSheet(f"""
            QLabel {{
                color:{Theme.TEXT_SECONDARY};
                font-size:{Theme.BODY}px;
                background:transparent;
            }}
        """)

        layout.addWidget(title)

        layout.addWidget(subtitle)

        # ---------------------------------------------------
        # Statistics
        # ---------------------------------------------------

        grid = QGridLayout()

        grid.setHorizontalSpacing(20)

        grid.setVerticalSpacing(20)

        stats = [

            ("👤", "Horoscopes", "0"),

            ("📚", "Events", "0"),

            ("🪐", "Research", "0"),

            ("📈", "Reports", "0"),

        ]

        row = 0

        col = 0

        for icon, title, value in stats:

            card = self.create_card(
                icon,
                title,
                value,
            )

            grid.addWidget(card, row, col)

            col += 1

            if col == 2:

                col = 0

                row += 1

        layout.addLayout(grid)

        layout.addStretch()

    # -------------------------------------------------------

    def create_card(
        self,
        icon,
        title,
        value,
    ):

        card = QFrame()

        card.setMinimumHeight(170)

        card.setStyleSheet(f"""
            QFrame {{
                background:{Theme.CARD};
                border:1px solid {Theme.BORDER};
                border-radius:18px;
            }}

            QFrame:hover {{
                border:2px solid {Theme.PRIMARY};
            }}
        """)

        layout = QVBoxLayout(card)

        layout.setContentsMargins(20, 20, 20, 20)

        icon_label = QLabel(icon)

        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon_label.setStyleSheet("""
            font-size:38px;
            background:transparent;
        """)

        title_label = QLabel(title)

        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label.setStyleSheet(f"""
            QLabel {{
                font-size:16px;
                color:{Theme.TEXT_SECONDARY};
                background:transparent;
            }}
        """)

        value_label = QLabel(value)

        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        value_label.setStyleSheet(f"""
            QLabel {{
                font-size:34px;
                font-weight:700;
                color:{Theme.PRIMARY};
                background:transparent;
            }}
        """)

        layout.addWidget(icon_label)

        layout.addWidget(title_label)

        layout.addStretch()

        layout.addWidget(value_label)

        return card